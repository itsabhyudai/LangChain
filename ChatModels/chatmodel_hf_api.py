from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation",
    temperature=0.5,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Tell me a slogan for a coffee shop")

print(result.content)

