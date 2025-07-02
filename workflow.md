```mermaid
graph TD
    A[PDF Extractor Agent] --> B[Classifier Agent]
    B --> C[Output Formatter Agent]



---

### ✅ Explanation

- **A: PDF Extractor Agent**
  - Reads a PDF file and splits it into text sections

- **B: Classifier Agent**
  - Classifies each section into categories like "Legal", "Technical", or "Financial" using an LLM

- **C: Output Formatter Agent**
  - Aggregates the classified sections into a clean JSON structure grouped by category

---

Let me know if you'd like:
- This exported as an image
- The diagram extended with logging or error-handling agents
- A more advanced version for Assignment 3 (Validator & Approval Gate)

I'm happy to help build that too!
