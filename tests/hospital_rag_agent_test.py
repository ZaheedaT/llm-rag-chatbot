import dotenv
import os, sys
dotenv.load_dotenv()

# Get the current directory of the script (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to other_directory
module_dir = os.path.join(current_dir, "../app/src/agents")

# Add the constructed path to sys.path
if module_dir not in sys.path:
    sys.path.append(module_dir)

from hospital_rag_agent import hospital_rag_agent_executor

responses = [hospital_rag_agent_executor.invoke(
    {"input": "What is the wait time at Wallace-Hamilton?"}
) ,hospital_rag_agent_executor.invoke(
    {"input": "Which hospital has the shortest wait time?"}
), hospital_rag_agent_executor.invoke(
    {
        "input": (
            "What have patients said about their "
            "quality of rest during their stay?"
        )
    }
), hospital_rag_agent_executor.invoke(
    {
        "input": (
            "Which physician has treated the "
            "most patients covered by Cigna?"
        )
    }
),
    # In this example, you ask the agent to show you reviews written by patient 7674.
    # Your agent invokes Experiences and doesn’t find the answer you’re looking for.
    # While it may be possible to find the answer using semantic vector search,
    # you can get an exact answer by generating a Cypher query to
    # look up reviews corresponding to patient ID 7674.

    hospital_rag_agent_executor.invoke(
    {"input": "Show me reviews written by patient 7674."}
), hospital_rag_agent_executor.invoke(
    {
        "input": (
            "Query the graph database to show me "
            "the reviews written by patient 7674"
        )
    }
)
]


print(*responses.get("output"))