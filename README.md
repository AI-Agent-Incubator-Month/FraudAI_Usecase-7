# FraudAI_Usecase-7


## Overview
Welcome to our project submission for the Agentic AI Incubation! This repository presents our intelligent credit card fraud detection system. The project leverages agentic AI to enhance fraud analysis through explainable LLM-based decision-making and domain-specific rule evaluation.

## Explanation
Our project is centered around LangChain agents integrated with Azure OpenAI to perform intelligent fraud analysis. We use a Zero-Shot ReAct Agent that evaluates credit card transactions and determines whether they are fraudulent, while providing a clear explanation for its decision.
The system includes the following key components:   

**LLM-Powered Agent**
A LangChain agent powered by Azure OpenAI's GPT model that analyzes transaction data using natural language prompts. It returns a fraud prediction along with a human-readable explanation.  

**Custom Tool**: FraudAnalysisTool
A tool provided to the agent that simulates fraud analysis logic and can be extended to interact with real analytics functions or databases.  

**Alert Generator**
If a transaction is marked as fraudulent, the system automatically creates a text-based alert containing transaction details and the reason for the flag.  

**Summary Report Generator**
After processing a batch of transactions, the system compiles a report showing the total number of analyzed and fraudulent transactions, including reasons for each.  

**Streamlit Interface**
A user interface where users can upload CSV files, run the analysis, view predictions, download results, and read AI-generated reports.

## Intent
The primary intent of our project is to detect fraudulent credit card transactions using AI agents. We aim to provide simple, explainable results that help financial institutions identify and understand suspicious activity.

## Use Case
**Public Sector :
Fraud Detection and Prevention Specialist**
 
Our solution is designed to help financial institutions, analysts, and fraud detection teams analyze credit card transactions for fraudulent activity. It can be applied in scenarios such as:  
- **Scenario 1**: Detecting fraud in real-time during credit card transactions.
- **Scenario 2**: Analyzing batches of transactions to identify suspicious behavior.
- **Scenario 3**: Generating alerts and reports to support investigation and compliance teams.


## Contributors
This project was developed by a dedicated team of contributors:
- **Anuj Khaddar**: Designed and implemented the rule-based detection logic.
- **Arti Bhandari**: Focused on integrating the AI agent using LangChain and Azure OpenAI, ensuring intelligent and explainable fraud analysis.
- **Momin Mariyam**: Managed the processing flow, coordinating how transactions are evaluated and results are structured.
- **Sakshi Kothawale**: Developed the interactive web interface, enabling users to upload data, view predictions, and download reports.
- **Shaksham Khandelwal**: Worked on alert generation, report creation, and ensuring clear, user-friendly output of fraud detection results.
- **Wasim Ahmed**: Mentor

## Images
## Flowchart
![alt text](<images/flowchart.png>)
  
## Screenshots
![alt text](<images/image1.png>)    

![alt text](<images/image3.jpg>)    

![alt text](<images/image2.png>)

![alt text](<images/image4.png>)

## Implementation


The system consists of the following components:   
- **langchain_agent.py**  
Uses AzureChatOpenAI via LangChain to instantiate a Zero-Shot ReAct agent. The agent is fed transaction data and returns a binary classification along with a detailed explanation.  
- **rules.py**  
Encodes multiple rule-based logic checks (e.g., high transaction distance, low account balance, abnormal authentication) that automatically classify transactions.  
- **main.py**  
Loads sample credit card transaction data (credit.csv), processes it through the agent and rules engine, and saves outputs such as alerts and reports.  
- **streamlit_app.py**  
Interactive dashboard for end-users. Allows CSV uploads, configures row selection, runs the agent analysis, displays results in a table, and generates downloadable alerts and summary reports.  
- **Environment Variables**  
Uses .env for secure access to Azure OpenAI services (deployment name, endpoint, API key, version).  
All AI calls are routed through Azure OpenAI, using a gpt-4o. Tools and responses are handled through LangChain’s agent system for flexibility and extensibility.

## Additional Information
### Future Plans
- Replace the current AI agent with a trained ML model for better accuracy.
- Add real-time transaction monitoring and anomaly detection.
- Improve the UI with user authentication and enhanced reporting.

-We have shared a sample .env file and dataset to experiment and verify.

