from openai import OpenAI

client = OpenAI(
    api_key="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"
)

def start_finetuning_job(file_id, model="gpt-3.5-turbo"):
    try:
        job = client.fine_tuning.jobs.create(
            training_file=file_id,
            model="gpt-3.5-turbo",
            hyperparameters={
                "n_epochs":2
            },
            # validation_file = "valid.jsonl",
            # suffix = "ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel"
            
        )
        # job = client.fine_tunes.create(training_file=file_id, model=model)
        print(f"Fine-tuning job created successfully: {job}")
        return job
    except Exception as e:
        print(f"Failed to create fine-tuning job. Error: {e}")
        return None

start_finetuning_job("file-1wnK3fboxdUQN9WLmqF0Jzpu")