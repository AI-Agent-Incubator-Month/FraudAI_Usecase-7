import streamlit as st
import pandas as pd
from langchain_agent import create_langchain_agent, generate_alert, generate_report
from rules import rule_based_detection
import os

# Set up Streamlit page
st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detection System")

st.markdown("Upload a CSV to analyze credit card transactions for potential fraud using AI + rules.")

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload your credit card transaction CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Uploaded Data Preview")
    st.dataframe(df.head(10), use_container_width=True)

    top_n = st.slider("Select number of rows to analyze", min_value=1, max_value=len(df), value=5)

    if st.button("🚀 Analyze Transactions"):
        with st.spinner("Analyzing with AI Agent..."):

            os.makedirs("alerts", exist_ok=True)
            os.makedirs("reports", exist_ok=True)

            agent = create_langchain_agent()
            sample = df.head(top_n).to_dict(orient="records")
            results = []

            for txn in sample:
                prompt = (
                    f"Here is a credit card transaction:\n{txn}\n\n"
                    f"Based on the features, decide if this transaction is 'Fraudulent' or 'Non-Fraudulent'. "
                    f"Also explain your reasoning clearly."
                )
                try:
                    response = agent.run(prompt)
                    prediction = "Fraudulent" if "fraudulent" in response.lower() else "Non-Fraudulent"
                    reason = response.strip()
                except Exception as e:
                    prediction = "Error"
                    reason = str(e)

                txn_result = {
                    "Transaction_ID": txn.get("Transaction_ID", "N/A"),
                    "User_ID": txn.get("User_ID", "N/A"),
                    "Transaction_Amount": txn.get("Transaction_Amount", "N/A"),
                    "Prediction": prediction,
                    "Reason": reason
                }
                results.append(txn_result)

                # Save alert if fraudulent
                if prediction == "Fraudulent":
                    alert_msg = generate_alert(txn_result)
                    with open(f"alerts/alert_{txn_result['Transaction_ID']}.txt", "w", encoding="utf-8") as f:
                        f.write(alert_msg)

            results_df = pd.DataFrame(results)

        st.success("✅ Analysis Complete!")

        st.subheader("📈 Prediction Results")
        st.dataframe(results_df, use_container_width=True)

        # Download prediction CSV
        csv = results_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Predictions CSV", data=csv, file_name="fraud_predictions.csv", mime="text/csv")

        # Generate and show report
        report_text = generate_report(results)
        with open("reports/fraud_summary_report.txt", "w", encoding="utf-8") as f:
            f.write(report_text)

        st.subheader("📄 Fraud Summary Report")
        st.text_area("Summary Report", report_text, height=250)

        st.download_button(
            label="📄 Download Report",
            data=report_text,
            file_name="fraud_summary_report.txt",
            mime="text/plain"
        )
