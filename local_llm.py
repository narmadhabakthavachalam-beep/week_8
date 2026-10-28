
import pandas as pd
import ollama
import os

os.makedirs("data", exist_ok=True)

df = pd.read_csv("data/prompts.csv")

responses = []

for prompt in df["prompt"]:
    print("Prompt:", prompt)

    result = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )

    answer = result["response"]
    print("Response:", answer)
    print("-" * 50)

    responses.append({
        "prompt": prompt,
        "response": answer
    })

output = pd.DataFrame(responses)
output.to_csv("data/llm_responses.csv", index=False)

print("All responses saved successfully!")
