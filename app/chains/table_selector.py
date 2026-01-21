from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

TABLE_SELECTION_PROMPT = PromptTemplate(
    input_variables=["question", "tables"],
    template="""
You are a database expert.

Available tables:
{tables}

Based on the user's question, return a comma-separated list of tables
that are required to answer the question.

User question:
{question}

Only return table names. No explanations.
"""
)

llm = ChatOpenAI(
  model="gpt-4o-mini",
  api_key=os.getenv("OPENAI_API_KEY")
  )

def select_tables(question: str, available_tables: list[str]) -> list[str]:
  prompt = TABLE_SELECTION_PROMPT.format(
    question=question,
    tables=", ".join(available_tables)
  )

  response = llm.invoke(prompt).content
  return [t.strip() for t in response.split(",")]