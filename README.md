# 🌙 Dreamscape RAG

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about the fictional fantasy world of **Dreamscape** and receive answers grounded in a custom knowledge base.

The project combines semantic retrieval, FAISS vector search, embeddings, a local LLM, FastAPI, and a Streamlit frontend.

---

## ✨ Features

* 🔎 Semantic document retrieval using embeddings
* 🧠 FAISS vector database for fast similarity search
* 📚 Custom Dreamscape knowledge base
* 🤖 Local LLM generation using Ollama and Llama 3
* 🛡️ Grounded responses based only on retrieved context
* 🚫 Prevents unsupported answers when information is not available
* ⚡ FastAPI backend API
* 🎨 Streamlit interactive frontend
* 🧪 Automated API tests using pytest
* 📖 Complete RAG pipeline demonstrated in a Jupyter notebook

---

## 🏰 Dreamscape Knowledge Base

The application currently contains six knowledge-base documents:

```text
data/documents/
├── world_guide.txt
├── characters.txt
├── magic_system.txt
├── locations.txt
├── history.txt
└── creatures.txt
```

The knowledge base covers topics such as:

* The Kingdom of Lunaris
* Luna Vale
* Kael Raven
* The Moon Crystal
* Moon Magic
* The Eclipse War
* The Moonlit Mountains
* Moonwolves
* Ember Dragons
* The five realms of Dreamscape

---

## 🧩 RAG Pipeline

The application follows these main steps:

```text
User Question
      ↓
Streamlit Frontend
      ↓
FastAPI Backend
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Top Relevant Chunks
      ↓
Grounded Prompt
      ↓
Llama 3 via Ollama
      ↓
Final Answer + Sources
```

### 1. Document Loading

The six Dreamscape text documents are loaded from the knowledge-base directory.

### 2. Chunking

The documents are divided into meaningful text chunks to make retrieval more effective.

### 3. Embeddings

The project uses:

```text
all-MiniLM-L6-v2
```

to convert text into numerical vectors.

The resulting embeddings have:

```text
384 dimensions
```

### 4. Vector Store

FAISS is used to store and search the document embeddings.

The final vector store contains:

```text
10 vectors
10 metadata entries
384 dimensions
```

### 5. Retrieval

When a user asks a question, the system searches the FAISS index and retrieves the most relevant knowledge-base chunks.

### 6. Generation

The retrieved information is passed to the local:

```text
Llama 3
```

model through Ollama.

The generation prompt instructs the model to answer using only the retrieved Dreamscape context.

If the knowledge base does not contain enough information, the application responds that it does not have enough information rather than inventing an answer.

---

## 🛠️ Technologies

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Main programming language |
| FAISS                 | Vector similarity search  |
| Sentence Transformers | Text embeddings           |
| all-MiniLM-L6-v2      | Embedding model           |
| Ollama                | Local LLM runtime         |
| Llama 3               | Text generation           |
| FastAPI               | Backend API               |
| Streamlit             | Frontend interface        |
| Pydantic              | Data validation           |
| Pytest                | Automated testing         |
| Jupyter Notebook      | RAG experimentation       |

---

## 📁 Project Structure

```text
Dreamscape/
│
├── backend/
│   └── app/
│       ├── api/
│       │   └── routes/
│       │       └── query.py
│       ├── core/
│       │   └── config.py
│       ├── schemas/
│       │   └── query.py
│       ├── services/
│       │   ├── generation.py
│       │   └── retrieval.py
│       ├── utils/
│       │   └── logging_config.py
│       └── main.py
│
├── data/
│   ├── documents/
│   │   ├── world_guide.txt
│   │   ├── characters.txt
│   │   ├── magic_system.txt
│   │   ├── locations.txt
│   │   ├── history.txt
│   │   └── creatures.txt
│   │
│   └── vector_store/
│       ├── dreamscape.index
│       ├── metadata.json
│       └── config.json
│
├── frontend/
│   ├── app.py
│   ├── api_client.py
│   ├── style.css
│   ├── .env.example
│   └── .env
│
├── notebooks/
│   └── rag_pipeline.ipynb
│
├── tests/
│   ├── conftest.py
│   └── test_query.py
│
├── .gitignore
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/AryamRashad20/Dreamscape-RAG.git
cd Dreamscape-RAG
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Make sure Ollama is installed and the Llama 3 model is available:

```powershell
ollama pull llama3:latest
```

---

## 🔐 Environment Configuration

Create:

```text
frontend/.env
```

with:

```env
API_URL=http://127.0.0.1:8000/api/query
```

The `.env` file is intentionally ignored by Git.

A safe example configuration is provided in:

```text
frontend/.env.example
```

---

## ▶️ Running the Application

### Start the Backend

From the project root:

```powershell
uvicorn backend.app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Start the Frontend

Open a second PowerShell terminal:

```powershell
cd F:\college\dreamscape\frontend
streamlit run app.py
```

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open that URL in your browser.

---

## 💬 Example Questions

Try questions such as:

```text
Who is Luna Vale?
```

```text
What is the Moon Crystal?
```

```text
What happened during the Eclipse War?
```

```text
What types of magic exist in Dreamscape?
```

```text
Where are the Moonlit Mountains?
```

```text
What creatures live in Dreamscape?
```

You can also test an unsupported question such as:

```text
What is Crystal Lake?
```

The system should avoid inventing information and explain that the information is not available in the Dreamscape knowledge base.

---

## 🧪 Testing

Run the automated tests from the project root:

```powershell
pytest
```

The project currently includes tests for the query API.

Expected result:

```text
2 passed
```

---

## 📓 RAG Notebook

The complete RAG development process is documented in:

```text
notebooks/rag_pipeline.ipynb
```

The notebook demonstrates:

* Document loading
* Text chunking
* Embedding generation
* FAISS indexing
* Vector retrieval
* Retrieval evaluation
* Local LLM generation
* Grounded question answering

---

## 🎯 Project Goal

The goal of Dreamscape RAG is to demonstrate how a Retrieval-Augmented Generation system can combine a custom knowledge base with semantic search and a language model.

Instead of relying entirely on the language model's pretrained knowledge, the system retrieves relevant information from the Dreamscape knowledge base and uses that information to generate grounded responses.

---

## 👩‍💻 Author

**Aryam Rashad**

Dreamscape RAG — AI / RAG Coursework Project
