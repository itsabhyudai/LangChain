from langchain_ollama import ChatOllama
from typing import Optional, Literal
from pydantic import BaseModel, Field


# Local Ollama Model
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5
)

# schema
class Review(BaseModel):

    key_themes : list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary : str = Field(description="A brief summary of the review")
    sentiment : Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros : Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons : Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" The Samsung Galaxy S24 is a compact flagship smartphone that delivers strong performance, excellent cameras, and long software support. Its premium design and bright AMOLED display make it a great choice for everyday use, gaming, and photography.

Pros
Excellent AMOLED display with vibrant colors and smooth 120Hz refresh rate
Powerful performance for gaming and multitasking
Great camera quality, especially in daylight and portrait shots
Premium and compact design that feels comfortable in hand
Long battery life with fast charging support
Samsung promises several years of Android updates

Cons
Charging speed is slower compared to some competitors
No charger included in the box
Slight heating during heavy gaming sessions
Price is on the higher side for casual users
Final Verdict

The Samsung Galaxy S24 is a reliable premium smartphone with balanced features, strong cameras, and excellent software support. It is ideal for users who want a compact flagship experience without major compromises. """)

print(result)
print(result.summary)
print(result.sentiment)

