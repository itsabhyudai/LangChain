from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from langchain.output_parsers import StructuredOutputParser, ResponseSchema   # langchain.output_parsers not in use!!!

# Local Ollama Model
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5
)

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="give 3 facts about {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt = template.invoke({"topic":"black hole"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

# ~~~~~~~~~~~~~~~using chains~~~~~~~~~~~~~~~~~~~~
chain = template | model | parser

result = chain.invoke({"topic":"black hole"})

print(result)
