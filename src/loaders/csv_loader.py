import pandas as pd

def load_csv(file_path: str):
    df = pd.read_csv(file_path)
    documents = []

    for i, row in df.iterrows():
        row_text = " | ".join([f"{col}: {row[col]}" for col in df.columns])
        documents.append({
            "text": row_text,
            "source": file_path,
            "row": i,
            "type": "csv"
        })

    return documents