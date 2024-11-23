"""Vector search indexes were released as a public beta in Neo4j 5.11.
They allow you to run semantic queries directly on your graph.
This is really convenient for your chatbot because you can store review
embeddings in the same place as your structured hospital system data.

In LangChain, you can use Neo4jVector to create review embeddings and
the retriever needed for your chain. Here’s the code to create the reviews chain:"""

import os
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

HOSPITAL_QA_MODEL = os.getenv("HOSPITAL_QA_MODEL")

neo4j_vector_index = Neo4jVector.from_existing_graph(
    embedding=OpenAIEmbeddings(),
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="reviews",
    node_label="Review",
    text_node_properties=[
        "physician_name",
        "patient_name",
        "text",
        "hospital_name",
    ],
    embedding_node_property="embedding",
)

# Create the prompt template below
review_template = """Your job is to use patient
reviews to answer questions about their experience at a hospital. Use
the following context to answer questions. Be as detailed as possible, but
don't make up any information that's not from the context. If you don't know
an answer, say you don't know.
{context}
"""

review_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["context"], template=review_template)
)

review_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["question"], template="{question}")
)
messages = [review_system_prompt, review_human_prompt]

review_prompt = ChatPromptTemplate(
    input_variables=["context", "question"], messages=messages
)

# Create Vector Chain using a Neo4j vector index retriever that returns 12 review embeddings
# from a similarity search
reviews_vector_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model=HOSPITAL_QA_MODEL, temperature=0),
    chain_type="stuff", # tells chain to pass all 12 reviews to the prompt/ "stuffs" a prompt. Others are for batches: "map_reduce", "refine", "map-rerank"
    retriever=neo4j_vector_index.as_retriever(k=12),
)
reviews_vector_chain.combine_documents_chain.llm_chain.prompt = review_prompt