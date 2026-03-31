# AI DDR Report Generator

## Overview
This project is an AI-based system that converts inspection and thermal reports into a structured Detailed Diagnostic Report (DDR).

The system processes raw PDF documents, extracts relevant information, and generates a client-ready report with proper structure and clarity.

---

## Features
- Extracts text from inspection and thermal PDFs
- Extracts and includes images from reports
- Combines multiple data sources logically
- Detects conflicts between reports
- Handles missing information (marks as "Not Available")
- Generates structured DDR output
- Produces a clean HTML report

---

## Workflow
1. Input: Inspection Report + Thermal Report (PDF)
2. Text & Image Extraction (PyMuPDF)
3. Conflict Detection Logic
4. Data Structuring
5. DDR Report Generation
6. HTML Report Output

---

## Output Structure
The generated DDR includes:
1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

---

## Tech Stack
- Python
- PyMuPDF (PDF processing)
- HTML/CSS (report generation)
- Optional: Gemini API (for AI-based reasoning)

---

## Reliability Design
The system includes fallback logic to ensure report generation even if external AI APIs are unavailable or rate-limited.

---

## Limitations
- Conflict detection is rule-based
- Image mapping is not context-aware
- Depends on input data quality

---

## Future Improvements
- Integrate advanced AI reasoning (Gemini / LLM)
- Improve image-to-section mapping
- Add web UI for file uploads
- Export reports as PDF

---

## How to Run
1. Install dependencies:
   pip install pymupdf python-dotenv

2. Add input files:
   input/inspection.pdf
   input/thermal.pdf

3. Run:
   python main.py

4. Output:
   outputs/report.html"# AI-DDR-report-generator" 
