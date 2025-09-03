from openai import OpenAI
from utils.prompting import system_prompt
import os
# For development purpose.
import streamlit as st

# Creates an OpenAI client to call OpenAI API using API KEY.
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

# Creates function to call OpenAI API with a prompt.
def call_openai(user_prompt, schema, model='gpt-4o'):
    """
    Calls OpenAI API to generate SQL from a natural language query using the provided schema.
    
    Args:
        user_question (str): Natural language input.
        schema_tables (str): Database schema.
        model (str): OpenAI model to use (default = gpt-4o).
    """
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        top_p=1,
        messages=[
            {
                'role': 'system',
                'content': system_prompt(schema)

            },
            {
                'role': 'user',
                'content': user_prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()


# Creates function to generate SQL Query for users.
def nl_to_sql(query, schema_table):
    """_summary_
    Converts natural language query to SQL using OpenAI.

    Args:
        query (string): Takes a natural language query.
        table (string): Takes a table schema.
    
    Returns:
        str: SQL query.
    """
    user_prompt = (
        f"Convert the following natural language question to an SQL query ONLY.\n"
        f"Use ONLY the tables and columns provided below.\n"
        f"Question : {query}\n"
        f"Table : {schema_table}\n"
        f"SQL Query :"
    )
    sql_query = call_openai(user_prompt, schema_table)
    sql_query = clean_sql_response(sql_query)
    return sql_query



# Creates function to clean SQL query responses.
def clean_sql_response(sql_str):
    """Remove markdown code fences if present.

    Args:
        sql_str (string): Takes an sql string to clean up.
    """
    sql_text = sql_str.strip()
    if sql_text.startswith("```sql"):
        sql_text = sql_text[6:]
    if sql_text.startswith("```"):
        sql_text = sql_text[3:]
    if sql_text.endswith("```"):
        sql_text = sql_text[:-3]
    return sql_text.strip()