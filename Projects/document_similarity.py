from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding =  HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Artificial Intelligence is transforming many industries.",
    "Machine learning helps computers learn from data.",
    "Neural networks are inspired by the human brain.",
    "AI-powered chatbots are becoming increasingly popular.",
    "Deep learning models require large amounts of training data."
]

query = "Tell me about deep learning"

doc_embeddings = embedding.embed_documents(docs)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print("similarity score is: ", score)

