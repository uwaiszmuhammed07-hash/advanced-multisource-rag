# 🤖 Advanced Multi-Source RAG System

> An AI-powered Retrieval-Augmented Generation (RAG) system that can answer questions from PDFs, CSV files, and websites — built with Python, Streamlit, and Groq API.

---

## 🌐 Live Demo
**[🚀 Try the live app → https://advanced-multisource-rag.onrender.com](https://advanced-multisource-rag.onrender.com)**

---

## 📌 What Is This Project?

An **Advanced Multi-Source RAG System** that allows users to upload and query multiple data sources:

- 📄 PDFs  
- 📊 CSV files  
- 🌐 Websites  

The system retrieves relevant information and generates intelligent answers using an LLM (Groq API).

---

## 🎬 How It Works
```text
Upload PDF / CSV / Enter URL → Data Processing → Retrieval → LLM → Final Answer
```
## 🧠 Core Components
| Component         | Role                       | Output         |
| ----------------- | -------------------------- | -------------- |
| 📥 Data Ingestion | Load PDF, CSV, Web content | Raw text       |
| 🧹 Processing     | Clean and structure data   | Processed text |
| 🔍 Retrieval      | Find relevant chunks       | Context        |
| 🤖 LLM (Groq)     | Generate answer            | Final response |

,,,


🚀 Getting Started
```
1. Clone the repository
git clone https://github.com/uwaiszmuhammed07-hash/advanced-multisource-rag.git
cd advanced-multisource-rag
```
2. Create virtual environment
python -m venv venv
source venv/bin/activate

```
3. Install dependencies
pip install -r requirements.txt
```
4. Add your API key

Create a .env file:
GROQ_API_KEY=your_groq_api_key_here
```
5. Run the app
streamlit run app.py

```
## 🛠️ Tech Stack
| Technology    | Purpose            |
| ------------- | ------------------ |
| Python 3.10   | Core language      |
| Streamlit     | Interactive web UI |
| Groq API      | LLM inference      |
| Pandas        | CSV processing     |
| BeautifulSoup | Web scraping       |
| PyPDF         | PDF processing     |
```
## 📁 Project Structure
advanced-multisource-rag/
├── .env
├── requirements.txt
├── app.py
├── start.sh
├── README.md
├── src/
│   ├── loaders/
│   │   ├── pdf_loader.py
│   │   ├── csv_loader.py
│   │   └── web_loader.py
│   ├── processing/
│   │   ├── cleaner.py
│   │   └── chunker.py
│   ├── retrieval/
│   │   └── vector_retriever.py
│   └── llm/
│       └── response_generator.py
└── data/
```
## ✨ Key Features
✅ Multi-source data ingestion
✅ PDF, CSV, and website support
✅ Intelligent retrieval system
✅ AI-powered answer generation
✅ Live deployed app on Render
✅ Clean and interactive Streamlit UI

## 💡 Use Cases
📚 Students — Ask questions from notes and PDFs
📊 Data Analysts — Query CSV datasets
🌐 Researchers — Extract insights from websites
👨‍💻 Developers — Learn and build RAG applications

##👨‍💻 Built By

Uwais Muhammed KP — 2026


