import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite-preview-09-2025",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def decompose_node(state):
    prompt = f"""Break this research query into 3 simple sub-questions:
    Query: {state['query']}
    Return only a numbered list, nothing else."""
    response = llm.invoke(prompt)
    lines = response.content.strip().split("\n")
    sub_questions = [l.split(". ", 1)[-1] for l in lines if l.strip()]
    return {"sub_questions": sub_questions}

def search_node(state):
    answers = []
    for question in state["sub_questions"]:
        prompt = f"Answer this concisely in 2-3 sentences: {question}"
        response = llm.invoke(prompt)
        answers.append(response.content.strip())
    return {"answers": answers}

def synthesize_node(state):
    qa_pairs = "\n".join([
        f"Q: {q}\nA: {a}"
        for q, a in zip(state["sub_questions"], state["answers"])
    ])
    prompt = f"""Based on these Q&A pairs, write a clear and concise research report:
    {qa_pairs}
    Keep it under 200 words."""
    response = llm.invoke(prompt)
    return {"final_report": response.content.strip()}
