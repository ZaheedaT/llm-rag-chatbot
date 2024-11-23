from pydantic import BaseModel

class HospitalQueryInput(BaseModel):
    """ A function used to verify that the POST request body includes a text field,
    representing the query your chatbot responds to"""
    text: str

class HospitalQueryOutput(BaseModel):
    """ A function that verifies the response body sent back to the user includes input, output,
    and intermediate_step fields."""

    input: str
    output: str
    intermediate_steps: list[str]