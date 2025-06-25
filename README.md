LLM Fundamentals Internship - Week 02 Projects

This repository contains the completed mini-projects for Week 02 of the LLM Fundamentals Internship, covering core concepts such as tokenization, LLM API latency, temperature control in text generation, and a basic Retrieval Augmented Generation (RAG) system. An optional Streamlit dashboard for the latency probe is also included.

Project Structure

Your project directory should generally look like this:

week02_llm/
├── .venv/                      # Python Virtual Environment
├── src/
│   ├── token_counter.py        # Mini-Project A: Token counter script
│   ├── latency_probe.py        # Mini-Project B: Latency probe script
│ 
├── notebooks/                  # Folder for Jupyter Notebooks
│   └── temp_sweep.ipynb        # Mini-Project C: Jupyter Notebook for Temperature Playground
├── output/                     # Folder for screenshots and output logs (
│   ├── Output_Mini_Project_A.png # Mini-Project A screenshot/output
│   ├── Output_Mini_Project_B.png # Mini-Project B screenshot/output 
│   ├── Temp_sweep_takeaway.txt # Mini-Project C takeaways
│   
├── prompt.txt                  # Mini-Project A: Sample prompt
├── prompt_medium.txt           # Mini-Project A: Medium prompt (ensure this exists if used)
├── prompt_long.txt             # Mini-Project A: Long prompt (ensure this exists if used)
└── README.md                   # This file


---

## Setup Instructions

Follow these steps to set up your environment and install necessary dependencies.

1.  **Navigate to your Project Directory:**
    Open your terminal (e.g., PowerShell on Windows, or your preferred terminal on Linux/macOS) and navigate to the `week02_llm` directory.

    ```bash
    cd C:\Users\jessi\week02_llm
    ```
    (Replace `C:\Users\jessi\week02_llm` with your actual path).

2.  **Create a Python Virtual Environment (if you haven't already):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```
    You should see `(.venv)` at the beginning of your terminal prompt, indicating the environment is active.

4.  **Install Core Python Libraries:**
    Install all required packages for the mini-projects.

    ```bash
    pip install huggingface_hub transformers requests sentence-transformers rich notebook streamlit scikit-learn
    ```
    * `huggingface_hub` and `transformers`: For interacting with Hugging Face models and tokenizers.
    * `requests`: For making HTTP requests to APIs (like Together AI).
    * `sentence-transformers`: For creating text embeddings (RAG system).
    * `rich`: For enhanced console output (RAG system).
    * `notebook`: To run Jupyter Notebooks (Temperature Playground).
    * `streamlit`: For building the optional dashboard.
    * `scikit-learn`: For `cosine_similarity` in the RAG system.

5.  **Set Up API Keys (Hugging Face & Together AI):**
    You will need API keys from Hugging Face and Together AI for the projects.

    * **Hugging Face Token (`HF_TOKEN`):**
        1.  Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
        2.  Generate a new "read" token and copy it.
        3.  **Set it as an environment variable in your *current* terminal session:**
            * **Windows (PowerShell):**
                ```powershell
                $env:HF_TOKEN="hf_YOUR_ACTUAL_HF_TOKEN_HERE"
                ```
            * **Linux/macOS:**
                ```bash
                export HF_TOKEN="hf_YOUR_ACTUAL_HF_TOKEN_HERE"
                ```
            (Replace `hf_YOUR_ACTUAL_HF_TOKEN_HERE` with your copied token).
        4.  **Important:** For the Mistral model on Hugging Face (used in some projects), ensure you've accepted its terms on its Hugging Face model page ([https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)) while logged in.

    * **Together AI API Key (`TOGETHER_API_KEY`):**
        1.  Go to [https://www.together.ai/](https://www.together.ai/).
        2.  Sign up/Log in and navigate to your API Keys section.
        3.  Generate a new API key (starts with `sk-` or `ak_`) and copy it.
        4.  **Set it as an environment variable in your *current* terminal session:**
            * **Windows (PowerShell):**
                ```powershell
                $env:TOGETHER_API_KEY="sk_YOUR_ACTUAL_TOGETHER_API_KEY_HERE"
                ```
            * **Linux/macOS:**
                ```bash
                export TOGETHER_API_KEY="sk_YOUR_ACTUAL_TOGETHER_API_KEY_HERE"
                ```
            (Replace `sk_YOUR_ACTUAL_TOGETHER_API_KEY_HERE` with your copied key).

---

## Mini-Project Run Steps

-> Ensure your virtual environment is activated and API keys are set in your terminal before running any commands. All commands below should be executed from the `week02_llm` project root directory.
Mini-Project Run Steps

-> Ensure your virtual environment is activated and API keys are set in your terminal before running any commands. All commands below should be executed from the week02_llm project root directory.

1. Mini-Project A: Token Counter (token_counter.py)
    Objective: Count tokens for a given text using a pre-trained LLM tokenizer (Mistral).
    Files:
        -- src/token_counter.py
    prompt.txt
    prompt_medium.txt (if created)
    prompt_long.txt (if created)

Run Command:
    
    -- python src/token_counter.py prompt.txt

# You can also try with:
# python src/token_counter.py prompt_medium.txt
# python src/token_counter.py prompt_long.txt


Expected Output/Deliverables:

    The script will print the input text and its token count.

output/Output_Mini_Project_A.png (screenshot of terminal output).
output/token_counter_takeaways.txt (3-bullet takeaways - ensure you create this file).

2. Mini-Project B: Latency Probe (latency_probe.py)

    Objective: Measure round-trip latency for LLM API calls on Hugging         Face and Together AI to observe free-tier performance variability.

    Files:

        -- src/latency_probe.py

    Run Command:
        Run the script at least twice at different times of the day (e.g., morning and evening).

    python src/latency_probe.py
    -> Expected Output/Deliverables:
The script will print latency for both Hugging Face and Together AI calls.

    output/Output_Mini_Project_B.png (screenshot of first run; you'll need another for the second run, e.g., output/Output_Mini_Project_B_run2.png).

    output/latency_reflection.txt (short paragraph reflecting on latency fluctuations and free-tier behavior).


3. Mini-Project C: Temperature Playground (Jupyter - temp_sweep.ipynb)

    Objective: Explore the effect of the temperature parameter on LLM text generation in a Jupyter Notebook.

    Files:

    notebooks/temp_sweep.ipynb

    notebooks/temp_sweep_Output.html (exported from Jupyter)

    output/Temp_sweep_takeaway.txt (3-bullet takeaways - ensure you create this file).

 -> Run Steps:

    Launch Jupyter Notebook from your project root:

    jupyter notebook
        This will open a browser window.

    In the browser, navigate into the notebooks folder and open temp_sweep.ipynb.

    Run all cells in the notebook sequentially (Shift+Enter for each cell).

    Observe the generated haikus at different temperatures.

    In the provided Markdown cell within the notebook, mark your preferred output and explain your reasoning.

    Export the notebook as HTML: Go to File -> Download as -> HTML (.html). (It will likely save to notebooks/temp_sweep.html).

    -> Expected Output/Deliverables:
        The notebook cells will display generated haikus for various temperatures.
        notebooks/temp_sweep.ipynb (with your markdown notes).
        notebooks/temp_sweep_Output.html (the exported file).
        output/Temp_sweep_takeaway.txt.


