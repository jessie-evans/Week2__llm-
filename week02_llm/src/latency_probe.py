import os
import time
from huggingface_hub import InferenceClient
import requests # For Together AI API

def measure_hf_latency(prompt: str, model: str, hf_token: str):
    """
    Measures the latency of a text generation call to Hugging Face Inference API.
    """
    if not hf_token:
        print("Hugging Face token (HF_TOKEN) not set. Skipping HF probe.")
        return

    print(f"\n--- Hugging Face Inference API ({model}) ---")
    client = InferenceClient(model=model, token=hf_token)

    start_time = time.time()
    try:
        # For chat-tuned models like Zephyr, use chat_completion
        # If you were using a simple text-generation model, you'd use client.text_generation
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        response_obj = client.chat_completion(
            messages=messages,
            max_tokens=50, # Use max_tokens for chat_completion
            do_sample=False
        )
        end_time = time.time()
        latency = end_time - start_time
        
        generated_text = ""
        if response_obj and response_obj.choices and response_obj.choices[0] and response_obj.choices[0].message:
            generated_text = response_obj.choices[0].message.content

        print(f"Prompt: '{prompt}'")
        print(f"Response (first 100 chars): '{generated_text[:100]}...'")
        print(f"Latency: {latency:.2f} seconds")
    except Exception as e:
        end_time = time.time()
        latency = end_time - start_time # Still measure time to error out
        print(f"Error during Hugging Face call: {e}")
        print(f"Time to error: {latency:.2f} seconds")


def measure_together_latency(prompt: str, model: str, together_api_key: str):
    """
    Measures the latency of a text generation call to Together AI API.
    Together AI's API is OpenAI-compatible.
    """
    if not together_api_key:
        print("Together AI API key (TOGETHER_API_KEY) not set. Skipping Together AI probe.")
        return

    print(f"\n--- Together AI API ({model}) ---")
    
    url = "https://api.together.xyz/v1/completions" # Or /chat/completions for chat models
    headers = {
        "Authorization": f"Bearer {together_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 50, # Limit response length
        "temperature": 0.0 # Keep it deterministic for latency testing
    }

    start_time = time.time()
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60) # Add timeout
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        json_response = response.json()
        end_time = time.time()
        latency = end_time - start_time

        generated_text = json_response.get("choices", [{}])[0].get("text", "No response text")
        print(f"Prompt: '{prompt}'")
        print(f"Response (first 100 chars): '{generated_text[:100]}...'")
        print(f"Latency: {latency:.2f} seconds")

    except requests.exceptions.Timeout:
        end_time = time.time()
        latency = end_time - start_time
        print(f"Error: Together AI API call timed out after {latency:.2f} seconds.")
    except requests.exceptions.RequestException as e:
        end_time = time.time()
        latency = end_time - start_time
        print(f"Error during Together AI call: {e}")
        print(f"Time to error: {latency:.2f} seconds")
    except Exception as e:
        end_time = time.time()
        latency = end_time - start_time
        print(f"An unexpected error occurred with Together AI: {e}")
        print(f"Time to error: {latency:.2f} seconds")


if __name__ == "__main__":
    COMMON_PROMPT = "Explain the concept of quantum entanglement in simple terms."

    # Hugging Face Model (choose an accessible one, e.g., Zephyr-7B-beta)
    HF_MODEL = "HuggingFaceH4/zephyr-7b-beta" # A good choice for HF Inference API

    # Together AI Model (choose a free-tier compatible one, e.g., Mistral-7B-Instruct-v0.2)
    TOGETHER_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

    # Get API Keys from environment variables
    hf_token = os.getenv("HF_TOKEN")
    together_api_key = os.getenv("TOGETHER_API_KEY")

    print("--- Running Latency Probes ---")
    measure_hf_latency(COMMON_PROMPT, HF_MODEL, hf_token)
    measure_together_latency(COMMON_PROMPT, TOGETHER_MODEL, together_api_key)
    print("\n--- Latency Probes Complete ---")
