# 📄 PDF Section Classifier using LangGraph and Ollama

This project implements a multi-step agent workflow to **extract sections from a PDF** and classify each section into one of three categories: **Legal**, **Technical**, or **Financial**. It uses [LangGraph](https://github.com/langgraph-ai/langgraph) to build the agent pipeline and [Ollama](https://ollama.com) to run the LLM locally (e.g., `mistral`).

---

## 🚀 Features

- ✅ Automatically extracts text from PDF documents
- 🧠 Classifies sections using a local LLM (`mistral`) via Ollama
- 🔄 Modular agent-based flow with LangGraph
- 📦 Outputs categorized text into a structured JSON file

---

## 🧠 How It Works

1. **Extractor Agent** – Parses the PDF and extracts meaningful text sections.
2. **Classifier Agent** – Sends each section to a local LLM to classify it as `Legal`, `Technical`, or `Financial`.
3. **Formatter Agent** – Organizes the classified results and saves them to a JSON file.

---

## 📁 Project Structure
.
├── main.py # Main script with the LangGraph pipeline
├── output/
│ └── result.json # Classified output (generated after run)
├── sample.pdf # Your input PDF file (optional)
└── README.md # Project documentation
---

## 🔧 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- LangGraph, LangChain, and PyMuPDF

---

## 📦 Installation:
# 1. Clone the repository
git clone https://github.com/yourusername/pdf-section-classifier.git
cd pdf-section-classifier

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# Update the file path in main.py:
doc = fitz.open("C:\\path\\to\\your\\document.pdf")

# Run the script:
python main.py

# The result will be saved to:
output/result.json





