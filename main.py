import json
from pathlib import Path
import fitz  # PyMuPDF
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, END

# Categories
CATEGORIES = ["Legal", "Technical", "Financial"]

# Load PDF and split by heading-like sections (basic heuristic)
def extract_sections_from_pdf(path):
    doc = fitz.open("C:\\Users\\HP\\OneDrive\\Desktop\\AI_Internship_Interview_QA_Nayan_Agrawal.pdf")
    sections = []
    for page in doc:
        text = page.get_text()
        for para in text.split("\n\n"):
            if len(para.strip()) > 50:
                sections.append(para.strip())
    return sections

# Agent 1: Extractor
def pdf_extractor_agent(state):
    sections = extract_sections_from_pdf("C:\\Users\\HP\\OneDrive\\Desktop\\AI_Internship_Interview_QA_Nayan_Agrawal.pdf")
    return {"sections": sections}

# Agent 2: Classifier
def classifier_agent(state):
    llm = ChatOllama(model="mistral")
    classified = []
    for section in state["sections"]:
        prompt = f"""Classify this section into one of these categories: {CATEGORIES}.

Section:
\"\"\"
{section}
\"\"\"

Return only the category label."""
        label = llm.invoke(prompt).content.strip()
        classified.append({"section": section, "category": label})
    return {"classified": classified}

# Agent 3: Formatter
def output_formatter_agent(state):
    result = {}
    for item in state["classified"]:
        label = item["category"]
        result.setdefault(label, []).append(item["section"])
    return {"result": result}

# Build LangGraph workflow
graph = StateGraph(dict)
graph.add_node("extractor", RunnableLambda(pdf_extractor_agent))
graph.add_node("classifier", RunnableLambda(classifier_agent))
graph.add_node("formatter", RunnableLambda(output_formatter_agent))

graph.set_entry_point("extractor")
graph.add_edge("extractor", "classifier")
graph.add_edge("classifier", "formatter")
graph.set_finish_point("formatter")
graph.add_edge("formatter", END)

app = graph.compile()
output = app.invoke({})

# Save output
Path("output").mkdir(exist_ok=True)
with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(output["result"], f, indent=4)


print("✅ Classification complete. See output/result.json")
