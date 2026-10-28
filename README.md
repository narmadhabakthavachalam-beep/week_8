
# Local LLM Inference

## Objective
To run a Large Language Model locally using Ollama.

## Model Used
Llama 3.2

## Tools Used
- Python
- Ollama
- Pandas

## Project Workflow
1. Read prompts from prompts.csv.
2. Send each prompt to the Llama 3.2 model.
3. Generate responses locally.
4. Save the responses in llm_responses.csv.

## How to Run
1. Install Ollama and download the Llama 3.2 model.
2. Install dependencies using:
   pip install -r requirements.txt
3. Run the program:
   python local_llm.py

## Output
The generated responses are saved in data/llm_responses.csv.
