from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=10)
# temperature is a parameter that controls the randomness of a language model's output
# lower values (0 to 0.3) - more deterministic and predictable
# higher values (0.7 - 1.5) - more random and creative


result = model.invoke("what is the capital of india")

# print(result)
print(result.content)

