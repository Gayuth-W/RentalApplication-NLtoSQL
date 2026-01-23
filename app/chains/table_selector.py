from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

TABLE_SELECTION_PROMPT = PromptTemplate(
    input_variables=["question", "tables", "examples"],
    template="""
You are a database expert.

Available tables:
{tables}

Few-shot examples:
{examples}

User question:
{question}

Return a comma-separated list of tables required to answer the question. Only the table names.
"""
)

llm = ChatOpenAI(
  model="gpt-4o-mini",
  api_key=os.getenv("OPENAI_API_KEY")
  )

def select_tables(question: str, available_tables: dict, examples: list) -> list[str]:
  prompt = TABLE_SELECTION_PROMPT.format(
      question=question,
      tables=", ".join([f"{t}: {available_tables[t]}" for t in available_tables]),
      examples="\n".join([f"Q: {ex['question']}\nSQL: {ex['sql']}" for ex in examples])
  )

  response = llm.invoke(prompt).content
  return [t.strip() for t in response.split(",")]

  
def generate_sql(question: str, tables_used: list[str], tables_desc: dict, examples: list[dict]) -> str:
    tables_str = "\n".join([f"{t}: {tables_desc[t]}" for t in tables_used])
    examples_str = "\n".join([f"Q: {e['question']}\nSQL: {e['sql']}" for e in examples])

    prompt = f"""
You are an expert SQL developer.

Tables available:
{tables_str}

Few-shot examples:
{examples_str}

User question:
{question}

Return ONLY the SQL query. Do not include explanations or extra text.
"""
    response = llm.invoke(prompt).content
    sql_only = response.strip().replace("```sql", "").replace("```", "").strip()
    return sql_only
  