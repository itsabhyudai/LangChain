# LangChain Models

Hands-on LangChain examples covering chat models, legacy LLM usage, embeddings, prompt templates, and structured output.

The repository is organized as small, focused demos for different providers and workflows:

- OpenAI
- Hugging Face API and local pipelines
- Anthropic
- Google Gemini
- Ollama for local structured output

## Folder Overview

| Folder | Purpose | Key Files |
| --- | --- | --- |
| `ChatModels/` | Chat model examples across providers | `chatmodel_openai.py`, `chatmodel_google.py`, `chatmodel_anthropic.py`, `chatmodel_hf_api.py`, `chatmodel_hf_local.py` |
| `LLMs/` | Basic non-chat LLM invocation example | `llm_demo.py` |
| `EmbeddedModels/` | Embedding generation for single queries and document lists | `embedding_openai_query.py`, `embedding_openai_docs.py`, `embedding_hf_local.py`, `embedding_hf_local_docs.py` |
| `Prompts/` | PromptTemplate and ChatPromptTemplate demos, plus a small Streamlit UI | `prompt_generator.py`, `prompt_ui.py`, `chat_prompt_template.py`, `message_placeholder.py`, `messages.py` |
| `StructuredOutput/` | Typed output with `Pydantic`, `TypedDict`, and JSON schema | `pydantic_demo.py`, `with_pydantic.py`, `with_typeddict.py`, `with_json.py`, `json_schema.json` |
| `Projects/` | Small applied examples built on embeddings/chat models | `chatbot.py`, `document_similarity.py` |

## What Each Section Demonstrates

### `ChatModels/`

Examples of invoking chat-capable models through LangChain wrappers:

- `chatmodel_openai.py`: OpenAI chat invocation using `ChatOpenAI`
- `chatmodel_google.py`: Gemini via `ChatGoogleGenerativeAI`
- `chatmodel_anthropic.py`: Claude via `ChatAnthropic`
- `chatmodel_hf_api.py`: Hugging Face hosted inference using `HuggingFaceEndpoint`
- `chatmodel_hf_local.py`: local Hugging Face pipeline using `HuggingFacePipeline`

### `LLMs/`

- `llm_demo.py`: basic `OpenAI` completion-style invocation using `gpt-3.5-turbo-instruct`

### `EmbeddedModels/`

Examples of generating embeddings for:

- a single query
- multiple documents
- local Hugging Face embedding models
- OpenAI embedding models

### `Prompts/`

Prompt engineering and reusable template examples:

- `chat_prompt_template.py`: parameterized chat prompts
- `messages.py`: direct use of `SystemMessage`, `HumanMessage`, and `AIMessage`
- `message_placeholder.py`: inserting chat history with `MessagesPlaceholder`
- `prompt_generator.py`: creates and saves a reusable prompt template into `template.json`
- `prompt_ui.py`: Streamlit app that loads `template.json` and runs a summarization flow

### `StructuredOutput/`

Examples of schema-constrained outputs:

- `pydantic_demo.py`: Pydantic basics such as validation, defaults, optional fields, and JSON export
- `with_pydantic.py`: structured output with a Pydantic schema
- `with_typeddict.py`: structured output with `TypedDict`
- `with_json.py`: structured output using a JSON schema dictionary
- `typeddict.py`: simple `TypedDict` syntax demo
- `json_schema.json`: basic schema example file

### `Projects/`

Mini practical demos:

- `chatbot.py`: command-line chatbot with chat history
- `document_similarity.py`: semantic similarity search using embeddings and cosine similarity

## Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root and add only the keys you need for the examples you want to run:

```env
OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
```

## Running Examples

From the project root:

```powershell
python ChatModels\chatmodel_openai.py
python LLMs\llm_demo.py
python EmbeddedModels\embedding_hf_local.py
python Projects\document_similarity.py
python StructuredOutput\with_pydantic.py
```

To run the Streamlit app:

```powershell
streamlit run Prompts\prompt_ui.py
```

## Notes

- `StructuredOutput\with_pydantic.py` and `StructuredOutput\with_json.py` use `ChatOllama`, so Ollama must be installed locally and the model `qwen2.5:1.5b` should be available.
- Several Hugging Face examples use hosted inference endpoints and require a Hugging Face token.
- `Prompts\prompt_ui.py` expects `template.json` to exist. If needed, generate it first by running `python Prompts\prompt_generator.py`.
- The repository currently includes a local `venv/` folder. It is usually better to keep that untracked and recreate it per machine.
- Some imports used in the examples, such as `streamlit` and `langchain-ollama`, are not listed in `requirements.txt` yet. Install them separately if you plan to run those scripts.

## Suggested Learning Order

1. Start with `LLMs/llm_demo.py` and `ChatModels/chatmodel_openai.py`
2. Move to `Prompts/` to understand prompt construction
3. Explore `EmbeddedModels/` for vector generation
4. Finish with `StructuredOutput/` and `Projects/` for practical workflows
