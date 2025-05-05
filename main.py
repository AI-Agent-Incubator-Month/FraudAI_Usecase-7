
import pandas as pd
import os
from langchain_agent import create_langchain_agent, generate_alert, generate_report
from rules import rule_based_detection

# Create necessary directories
os.makedirs("alerts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Load data
data = pd.read_csv("credit.csv")
top_n = 10
sample = data.head(top_n).to_dict(orient="records")

agent = create_langchain_agent()

results = []

for i, txn in enumerate(sample):
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
        "Fraud_Label": txn.get("Fraud_Label", "N/A"),
        "Prediction": prediction,
        "Reason": reason
    }

    results.append(txn_result)

    # Save alert if fraudulent
    if prediction == "Fraudulent":
        alert_msg = generate_alert(txn_result)
        with open(f"alerts/alert_{txn_result['Transaction_ID']}.txt", "w", encoding="utf-8") as f:
            f.write(alert_msg)

    print(f"\n Transaction ID: {txn_result['Transaction_ID']}")
    print(f" Prediction: {prediction}")
    print(f" Reason:\n{reason}")

# Save predictions CSV
pd.DataFrame(results).to_csv("fraud_predictions_with_explanations.csv", index=False)
print("\n✅ Saved predictions to 'fraud_predictions_with_explanations.csv'")

# Save summary report
report_text = generate_report(results)
with open("reports/fraud_summary_report.txt", "w", encoding="utf-8") as f:
    f.write(report_text)

print("📄 Summary report saved in 'reports/fraud_summary_report.txt'")

