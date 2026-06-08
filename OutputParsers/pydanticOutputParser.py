from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Local Ollama Model
model = ChatOllama(
    model="llama3.1:8b",
    temperature=0.5
)

class Person(BaseModel):

    name : str = Field(description="name of the person")
    age  : int = Field(gt=18, description="age of the person")
    city : str = Field(description="name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="generate the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt = template.invoke({"place":"indian"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)


# ~~~~~~~~~~~~~using chains~~~~~~~~~~~~~~~
chain = template | model | parser

final_result = chain.invoke({"place":"indian"})

print(final_result)

