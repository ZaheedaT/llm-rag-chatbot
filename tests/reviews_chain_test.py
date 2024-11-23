"""In this example, notice how specific patient and hospital names are mentioned
in the response. This happens because you embedded hospital and patient names
along with the review text, so the LLM can use this information to answer questions."""
import dotenv
import sys
import os
dotenv.load_dotenv()

# Get the current directory of the script (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to other_directory
module_dir = os.path.join(current_dir, "../app/src/chains")

# Add the constructed path to sys.path
if module_dir not in sys.path:
    sys.path.append(module_dir)

from hospital_review_chain import (
    reviews_vector_chain
)


query= """Have patients ever mentioned or commented on the cost of medical visits? 
Be specific, directly from reviews"""

response = reviews_vector_chain.invoke(query)

print(response.get("result"))