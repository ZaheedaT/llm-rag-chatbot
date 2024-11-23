## LLM RAG Chat Bot for Hospitals

### A large hospital system has stakeholders who want answers to ad-hoc questions about patients, visits, physicians, hospitals, and insurance payers

The stakeholders want to create an internal chatbot, similar to ChatGPT, designed to answer questions using a company’s data. The chatbot should handle queries such as:
  *"How long is the current wait time at XYZ hospital?"
  *" Which hospital has the lowest wait time?"
  *"Where are patients voicing concerns about billing or insurance problems?"

To achieve this, the chatbot must identify the type of question being asked and determine the appropriate data source to retrieve the information from.

## Modules used:
To fulfill our task we utilize 
  * LangChain Agent : Decides which tool (if any) must be called and what input mst be given to it based on a user's query. The agent takes the tool's output and decides what response to give the user.
  * Neo4j AuraDB
  * LangChain Neo4j Cypher Chain (Agent Tool)
  * LangChain Neo4j Reviews Vector Chain (Agent Tol)
  * Wait Times Function (Agent Tool)

## Data
All of the data in this app a used synthetically generated, and much of it was derived from a popular [health care dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) on Kaggle. This data specifically comes from https://realpython.com/ 

To store our CSV tabular data, this app uses a Graph Database rather than a Relational Database.
Graph Database benefits:
Simple data representation, handles cpmlex relationships efficiently, flexible to changes, faster performance than relational dbs, they allow pattern matching queries for data with numerous complex relationships, graph databases offer simplicity and flexibility, making them easier to design and query than relational databases
