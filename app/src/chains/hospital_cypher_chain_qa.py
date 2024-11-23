
#Next, you define the prompt template for the question-answer component of your chain.
# This template tells the LLM to use the Cypher query results to generate a
# nicely-formatted answer to the user’s query
import os,sys
from langchain_community.graphs import Neo4jGraph
from langchain.prompts import (
    PromptTemplate)

from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, "../chains")
if module_dir not in sys.path:
    sys.path.append(module_dir)

from hospital_cypher_chain import (HOSPITAL_CYPHER_MODEL, HOSPITAL_QA_MODEL, cypher_generation_prompt)

# ...


qa_generation_template = """You are an assistant that takes the results
from a Neo4j Cypher query and forms a human-readable response. The
query results section contains the results of a Cypher query that was
generated based on a user's natural language question. The provided
information is authoritative, you must never doubt it or try to use
your internal knowledge to correct it. Make the answer sound like a
response to the question.

Query Results:
{context}

Question:
{question}

If the provided information is empty, say you don't know the answer.
Empty information looks like this: []

If the information is not empty, you must provide an answer using the
results. If the question involves a time duration, assume the query
results are in units of days unless otherwise specified.

When names are provided in the query results, such as hospital names,
beware  of any names that have commas or other punctuation in them.
For instance, 'Jones, Brown and Murray' is a single hospital name,
not multiple hospitals. Make sure you return any list of names in
a way that isn't ambiguous and allows someone to tell what the full
names are.

Never say you don't have the right information if there is data in
the query results. Always use the data in the query results.

Helpful Answer:
"""

qa_generation_prompt = PromptTemplate(
    input_variables=["context", "question"], template=qa_generation_template
)

def qa_generation(question):
        graph= Neo4jGraph(
                url=os.getenv("NEO4J_URI"),
                username=os.getenv("NEO4J_USERNAME"),
                password=os.getenv("NEO4J_PASSWORD"),
        )
        graph.refresh_schema()

        # The last step in creating your Cypher chain is to instantiate a GraphCypherQAChain object:
        # qa_prompt: The prompt template for responding to questions/queries.
        # cypher_prompt: The prompt template for generating Cypher queries.
        try:
            hospital_cypher_chain = GraphCypherQAChain.from_llm(
            cypher_llm=ChatOpenAI(model=HOSPITAL_CYPHER_MODEL, temperature=0),
            qa_llm=ChatOpenAI(model=HOSPITAL_QA_MODEL, temperature=0),
            graph=graph,
            verbose=True,
            qa_prompt=qa_generation_prompt,
            cypher_prompt=cypher_generation_prompt,
            validate_cypher=True,
            top_k=100,
            allow_dangerous_requests='True')
            result= hospital_cypher_chain.invoke(question)
        finally:
            # Explicitly close the Neo4jGraph connection if it has a close method
            if hasattr(graph, 'close'):
                graph.close()

        return result


