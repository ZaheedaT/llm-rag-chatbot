import os, sys
import dotenv
dotenv.load_dotenv()


# Get the current directory of the script (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to other_directory
module_dir = os.path.join(current_dir, "../app/src/chains")

# Add the constructed path to sys.path
if module_dir not in sys.path:
    sys.path.append(module_dir)


from hospital_cypher_chain_qa import (
qa_generation
)

question = """What is the average visit duration for
emergency visits in North Carolina?"""
response = qa_generation(question)

question_2 = """Which state had the largest percent increase
           in Medicaid visits from 2022 to 2023?"""
response_2 = qa_generation(question_2)

print(response.get("result"))
print("2nd Query", response_2.get("result"))

