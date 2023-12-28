from openai import OpenAI
import os

client = OpenAI(
    api_key="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"
)

def fine_tune_model(file_path):
    # Upload the file
    with open(file_path, "rb") as file_data:
        upload_response = client.files.create(
        file=file_data,
        purpose='fine-tune'
    )
    
    file_id = upload_response.id
    print(f"File uploaded successfully. ID: {file_id}")

# Usage
fine_tune_model("train_gpt_datasets.jsonl")