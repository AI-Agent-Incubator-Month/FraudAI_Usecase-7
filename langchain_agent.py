
from langchain_community.chat_models import AzureChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os

load_dotenv()

# Azure OpenAI LLM
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0.3,
)


# LangChain Agent using the LLM
def create_langchain_agent():
    tools = [
        Tool(
            name="FraudAnalysisTool",
            func=lambda x: f"Agent response: {x}",
            description="Analyzes fraud using LangChain."
        )
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent

# Simple alert message generator
def generate_alert(transaction):
    return (
        f"🚨 ALERT: Fraudulent Transaction Detected!\n"
        f"Transaction ID: {transaction.get('Transaction_ID', 'N/A')}\n"
        f"User ID: {transaction.get('User_ID', 'N/A')}\n"
        f"Amount: ₹{transaction.get('Transaction_Amount', 'N/A')}\n"
        f"Reason: {transaction.get('Reason', 'N/A')}\n"
    )

# Simple report generator
def generate_report(transactions):
    lines = ["📊 Fraud Summary Report\n", "=" * 25 + "\n"]
    lines.append(f"Total Transactions Analyzed: {len(transactions)}\n")
    frauds = [txn for txn in transactions if txn["Prediction"] == "Fraudulent"]
    lines.append(f"Fraudulent Transactions: {len(frauds)}\n\n")

    for txn in frauds:
        lines.append(f"Transaction ID: {txn['Transaction_ID']}, User ID: {txn['User_ID']}, Amount: ₹{txn['Transaction_Amount']}\n")
        lines.append(f"Reason: {txn['Reason']}\n\n")

    return "".join(lines)
