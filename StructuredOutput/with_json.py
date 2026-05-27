from langchain_ollama import ChatOllama


# Local Ollama Model
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.5
)

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}
    

structured_model = model.with_structured_output(json_schema)

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

The Samsung Galaxy S24 is a reliable premium smartphone with balanced features, strong cameras, and excellent software support. It is ideal for users who want a compact flagship experience without major compromises. Review by Abhi.""")

print(result)

