# from langchain.chains import LLMChain
# from app.prompts.sql_prompt import SQL_PROMPT
# from app.utils.sql_cleaner import clean_sql
from app.db.database import engine
from sqlalchemy import text
from app.chains.table_selector import select_tables, generate_sql
from app.examples.few_shot_examples import FEW_SHOT_EXAMPLES as examples

def run_nl2sql(question: str, session_id: str | None = None):
    # 1. Select tables-done
    # 2. Generate SQL-done
    # 3. Clean SQL
    # 4. Execute SQL-done
    # 5. Generate natural language answer-done
  
  TABLES = {
      "listing": "Listing table with columns: listing_id, title, location, price, bedrooms, bathrooms, seller_id",
      "seller": "Seller table with columns: seller_id, owner_fname, owner_lname, phone, email",
      "listing_image": "Listing images table with columns: listing_id, url, alt_text"
  }
    
  tables_used = select_tables(question, TABLES, examples)

  sql = generate_sql(question, tables_used, TABLES, examples)

  with engine.connect() as conn:
      result = conn.execute(text(sql))
      rows = [dict(row._mapping) for row in result]

  answer = f"I found {len(rows)} results that match your descrption."
  return {
      "sql": sql,
      "rows": rows,
      "tables_used": tables_used,
      "answer": answer
  }