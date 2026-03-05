from typing import TypedDict, List

class ResearchState(TypedDict):
    query: str
    sub_questions: List[str]
    answers: List[str]
    final_report: str