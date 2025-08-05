import json
import pandas as pd
from backend.nl2sql_feature import nl_to_sql
from utils.schema_tables import get_db_schema
from utils.connection import get_db_connection


# Load schema from database
schema = get_db_schema('company.db')
# Get connection
conn = get_db_connection('company.db')

with open('evalution_sets.json', 'r') as f:
    evalution_data = json.load(f)
        
# Initialise total, correct, and mismatches count
total = len(evalution_data)
correct = 0


# Normalize Dataframe
def normalize_df(df):
    """Standardizes DataFrame: lower column names, sort, reset index"""
    df.columns = [col.lower() for col in df.columns]
    return df.sort_values(by=df.columns.tolist()).reset_index(drop=True)


# Evaluation loop
for i, entry in enumerate(evalution_data, 1):
    question = entry['question']
    expected_sql = entry['expected_sql']
    
    # Execute queries
    try:
        result_sql = nl_to_sql(question, schema)
        df_result = pd.read_sql(result_sql, conn)
        df_expected = pd.read_sql(expected_sql, conn)
        
        # Normalize results for fair comparison
        df_result_norm = normalize_df(df_result)
        df_expected_norm = normalize_df(df_expected)
        
        if df_result_norm.values.tolist() == df_expected_norm.values.tolist():
            correct += 1
            print(f'[{i}/{total}] ✅ Correct: {question}')
        else:
           print(f'[{i}/{total}] ❌ incorrect: {question}')
           print("Expected:\n", df_expected_norm)
           print("Got:\n", df_result_norm)
           print("-" * 50)

            
    except Exception as e:
        print(f"[{i}/{total}] ❌ Error for question: {question}")
        print("Error:", e)
        print("-" * 50)

# Get the final report
accuracy = (correct / total) * 100
print(f'\n Accuracy: {correct}/{total} = {accuracy:.2f}%\n')
