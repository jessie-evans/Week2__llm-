from transformers import AutoTokenizer
import sys

if len(sys.argv) < 2:
    print("Usage: python token_counter.py <filepath>")
    sys.exit(1)

filepath = sys.argv[1]

# Choose a tokenizer (e.g., Llama 2 or Mistral)
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        prompt_text = f.read()

    tokens = tokenizer.encode(prompt_text)
    print(f"Text: '{prompt_text.strip()}'")
    print(f"Token count: {len(tokens)}")

except FileNotFoundError:
    print(f"Error: File '{filepath}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")