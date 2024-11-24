## LLM RAG Chat Bot for Hospitals

### A large hospital system has stakeholders who want answers to ad-hoc questions about patients, visits, physicians, hospitals, and insurance payers

The stakeholders want to create an internal chatbot, similar to ChatGPT, designed to answer questions using a company’s data. The chatbot should handle queries such as:
  * "How long is the current wait time at XYZ hospital?"
  * " Which hospital has the lowest wait time?"
  * "Where are patients voicing concerns about billing or insurance problems?" and sp on

To achieve this, the chatbot must identify the type of question being asked and determine the appropriate data source to retrieve the information from.

## Methods used:
To fulfill our task we utilize 
  * LangChain Agent : Decides which tool (if any) must be called and what input must be given to it based on a user's query. The agent takes the tool's output and decides what response to give the user.
  * Neo4j AuraDB (Graph Database)
  * LangChain Neo4j Cypher Chain (Agent Tool)
  * LangChain Neo4j Reviews Vector Chain (Agent Tool)
  * Wait Times Function (Agent Tool)

## Model Deployment
We serve the LangChain Agent using FastAPI and using Streamlit to easily create a UI frontend. 
We then deploy the App using Docker containers that are orchestrated with Docker Compose.

## Data
The Hospital System Data is stored in CSV files, namely:
`hospitals.csv`,`patients.csv` ,`payers.csv`, `physicians.csv` , `reviews.csv` , `visits.csv`

All of the data in this app a used synthetically generated, and much of it was derived from a popular [health care dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) on Kaggle. This data specifically, comes from https://realpython.com

To store our CSV tabular data, this app uses a Graph Database rather than a Relational Database.

#### Graph Database benefits:

Simple data representation, handles cpmlex relationships efficiently, flexible to changes, faster performance than relational dbs, they allow pattern matching queries for data with numerous complex relationships, graph databases offer simplicity and flexibility, making them easier to design and query than relational databases

# Future updates:
A memory feature will be added, to allow the Chatbot to recall past interactions that users have had with it. This will improve user experience and improve the Apps efficiency 

#### Credits:
This app was inspired by Real Python's LLM RAG Chatbot Tutorial
