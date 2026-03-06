# LangGraph Research Agent

An agentic research assistant built with LangGraph and Google Gemini.
Autonomously decomposes queries, answers sub-questions, and synthesizes structured reports via a FastAPI REST endpoint.

## Tech Stack
- LangGraph + LangChain
- Google Gemini (via ChatGoogleGenerativeAI)
- FastAPI + Uvicorn
- Python

## Run Locally
pip install -r requirements.txt
uvicorn main:app --reload

## API
POST /research
{"query": "Your research question here"}
