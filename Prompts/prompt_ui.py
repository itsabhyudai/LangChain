from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation",
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)

st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name",
    ["Attention is all you need",
     "BERT: Pre-training of Deep Bidirectional Transformers",
     "GPT-3: Language Models are Few-Shot Learners",
     "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style",["Beginner-friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 Paragraph)", "Medium (3-4 Paragraph)", "Large (Detailed Explanation)"])



#template
# template = PromptTemplate(
#     template=""" Please summarize the research paper titled "{paper_input}" with the following specifications:
#     Explanation Style: {style_input}
#     Explanation Length: {length_input}

#     1. Mathematical Details:
#     - include relevant mathematical equations if present in the paper.
#     - explain the mathematical concepts using simple, intuitive code snippets where applicable.

#     2. Analogies:
#     - use relatable analogies to simplify complex ideas.

#     If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
#     Ensure the summary is clear, accurate, and aligned with provided style and length. """,

#     input_variables=["paper_input", "style_input", "length_input"]
# )


template = load_prompt("template.json")



if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result.content)

