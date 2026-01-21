# from langchain.chains import LLMChain
# from app.prompts.sql_prompt import SQL_PROMPT
# from app.utils.sql_cleaner import clean_sql
from app.db.database import engine
from sqlalchemy import text
from app.db.database import engine

def run_nl2sql(question: str, session_id: str | None = None):
    # 1. Select tables
    # 2. Generate SQL
    # 3. Clean SQL
    # 4. Execute SQL
    # 5. Generate natural language answer
    
  sql= "SELECT * FROM listing LIMIT 5;"
  
  
  with engine.connect() as conn:
      result = conn.execute(text(sql))
      rows = [dict(row._mapping) for row in result]
      
      
  answer= "Pipeline connected successfully."

  return {
    "sql": sql,
    "rows": rows,
    "answer": answer
  }