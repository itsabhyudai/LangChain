from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import JsonOutputParser

# Local Ollama Model
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)


# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
# print(type(final_result))

# print(final_result["name"])


# ~~~~~~~~~~~~~~~~~~~~~~using chains~~~~~~~~~~~~~~~~~~~~~~~~~~~~
chain = template | model | parser

result = chain.invoke({})

print(result)

