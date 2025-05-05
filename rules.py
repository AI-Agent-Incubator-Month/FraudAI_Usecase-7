
def rule_based_detection(transaction):
    # Rule 1: High Risk and Previous Fraudulent Activity
    if transaction["Risk_Score"] > 0.7 and transaction["Previous_Fraudulent_Activity"] == 1:
        return "Fraudulent"
    
    # Rule 2: Mobile Device and High Transaction Distance
    if transaction["Device_Type"] == "Mobile" and transaction["Transaction_Distance"] > 1000:
        return "Fraudulent"
    
    # Rule 3: Failed Transactions and Low Account Balance
    if transaction["Failed_Transaction_Count_7d"] > 3 and transaction["Account_Balance"] < 10000:
        return "Fraudulent"
    
    # Rule 4: High Risk and Unusual Authentication Method
    if transaction["Risk_Score"] > 0.5 and transaction["Authentication_Method"] not in ["PIN", "OTP"]:
        return "Fraudulent"
    
    # Rule 5: Transaction Type - ATM or Online with Low Balance
    if transaction["Transaction_Type"] in ["ATM Withdrawal", "Online"] and transaction["Account_Balance"] < 10000:
        return "Fraudulent"
    
    return "Non-Fraudulent"

