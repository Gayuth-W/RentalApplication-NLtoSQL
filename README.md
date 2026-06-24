# 🏠 RentalApp NL2SQL Engine

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain)](https://www.langchain.com/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Ollama](https://img.shields.io/badge/Ollama-black?style=for-the-badge&logo=ollama)](https://ollama.com/)

An AI-powered Natural Language to SQL (NL2SQL) engine designed for the **Rental Application** ecosystem. This service allows users to query rental databases using plain English, abstracting away the complexity of SQL joins and filters.

---

## Overview

The **RentalApp NL2SQL Engine** bridges the gap between non-technical users and complex rental data. By leveraging local Large Language Models (via Ollama) and Few-Shot learning techniques, it translates natural language questions into precise, executable SQL queries against a MySQL database.

**Example:**
> *"Show me all listings in Colombo under 50,000 LKR with at least 2 bedrooms"* 
> ⮕ `SELECT * FROM listing WHERE location='Colombo' AND price < 50000 AND bedrooms >= 2;`

---

## Key Features

- **Intelligent Table Selection**: Dynamically identifies which tables (listings, sellers, images, etc.) are needed to answer a specific query to minimize token usage and improve accuracy.
- **Few-Shot Learning**: Uses curated examples to guide the LLM in generating optimal SQL syntax for the specific rental schema.
- **Local LLM Integration**: Privacy-first approach using **Gemma 3** via **Ollama**, ensuring data never leaves your infrastructure.
- **Multi-Table Joins**: Automatically handles complex relationships between listings, sellers, and images.
- **High Performance**: Built on **FastAPI** for asynchronous request handling and **SQLAlchemy** for robust database interaction.

---

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Orchestration**: [LangChain](https://www.langchain.com/)
- **Database**: [MySQL](https://www.mysql.com/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **LLM Engine**: [Ollama](https://ollama.com/) (Model: `gemma3:1b`)
- **Language**: Python 3.10+

- [frontend](https://github.com/Gayuth-W/RentalApplication-frontend)
- [Backend](https://github.com/Gayuth-W/RentalApplication-backend)
- [chatbot](https://github.com/Gayuth-W/RentalApplication-NLtoSQL)

---

## Setup Instructions

### 1. Prerequisites
- Python 3.10 or higher
- MySQL Server installed and running
- [Ollama](https://ollama.com/) installed

### 2. Database Configuration
Create a database named `rental_db` and ensure you have the following tables (or run your migration scripts):
- `listing`
- `seller`
- `listing_image`

### 3. Ollama Setup
Pull the required model:
```bash
ollama pull gemma3:1b
```

### 4. Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd renting-app-nltosql

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 5. Environment Variables
Create a `.env` file in the root directory (or update `app/db/database.py`):
```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=rental_db
OPENAI_API_KEY=your_key_if_using_openai  # Optional
```

### 6. Running the App
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

---

## Usage

### API Endpoints

#### `POST /api/chat`
The main endpoint for NL2SQL queries.

**Request Body:**
```json
{
  "question": "Show me all listings in Malabe with images",
  "session_id": "optional-uuid"
}
```

**Response:**
```json
{
  "sql": "SELECT l.title, l.location, l.price, li.url FROM listing l LEFT JOIN listing_image li ON l.listing_id = li.listing_id WHERE l.location='Malabe';",
  "rows": [...],
  "tables_used": ["listing", "listing_image"],
  "answer": "I found 5 results that match your description."
}
```

---

## Project Structure

```text
renting-app-nltosql/
├── app/
│   ├── api/          # FastAPI routes
│   ├── chains/       # LangChain logic (SQL generation & table selection)
│   ├── db/           # Database configuration & session management
│   ├── examples/     # Few-shot training examples for the LLM
│   ├── prompts/      # LLM prompt templates
│   ├── schemas/      # Pydantic models for API validation
│   ├── utils/        # Helper functions (SQL cleaning, etc.)
│   └── main.py       # Application entry point
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

---

## Future Improvements

- [ ] **Semantic Search Integration**: Combine SQL filtering with vector search for better "vibe-based" queries.
- [ ] **Query History**: Maintain a session-based history for follow-up questions (e.g., "Now filter by price").
- [ ] **Explainability**: Add a feature to explain *why* certain results were returned in natural language.
- [ ] **Multi-DB Support**: Support for PostgreSQL and SQLite.

---

## Author

**Gayuth**
- [GitHub](https://github.com/Gayuth-W)
- [LinkedIn](https://linkedin.com/in/yourprofile)

---

> *"Making data accessible, one query at a time."*
