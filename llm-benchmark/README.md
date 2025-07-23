<p align="center">
  <h1>🧪 LLM Code Benchmark with DeepEval</h1>
</p>

This project benchmarks the code generation capabilities of leading Large Language Models (LLMs) using the [DeepEval](https://github.com/confident-ai/deepeval) evaluation library.

## 📦 Supported Models

- 🧠 OpenAI GPT-4o
- 🤖 Anthropic Claude Sonnet 4
- 🦙 Cohere Command
- 🚀 Grok-3 (x.ai)

## 📂 Project Structure

```
llm-benchmark/
├── main.py               # Main benchmarking script
├── prompts/              # Evaluation prompts (one .txt per task)
│   ├── fizzbuzz.txt
│   ├── reverse_string.txt
│   ├── sudoku_solver.txt
│   ├── balanced_parentheses.txt
│   ├── lru_cache.txt
│   ├── find_all_anagrams.txt
│   └── dijkstra_shortest_path.txt
├── requirements.txt      # Python dependencies
└── README.md
```

## ▶️ How to Run

1. **Install dependencies:**
    ```bash
    cd llm-benchmark
    pip install -r requirements.txt
    ```

2. **Set your API keys:**
    ```bash
    export OPENAI_API_KEY="..."
    export ANTHROPIC_API_KEY="..."
    export COHERE_API_KEY="..."
    export XAI_API_KEY="..."
    ```

3. **Run the benchmark:**
    ```bash
    python main.py
    ```

## 📝 How it works

- For each prompt in the `prompts/` folder, the script sends the same task to all supported models.
- Each model's output is evaluated using DeepEval's `AnswerRelevancyMetric`.
- The results (score per model per task) are printed to the console.

## 📈 Example Output

```
🔍 Benchmark: FizzBuzz
🏗️ Testando Grok-3 (x.ai)...
📊 Resultado Grok-3 (x.ai): 1.00
🏗️ Testando Anthropic Claude Sonnet 4...
📊 Resultado Anthropic Claude Sonnet 4: 1.00
🏗️ Testando Cohere Command...
📊 Resultado Cohere Command: 0.92
🏗️ Testando OpenAI GPT-4o...
📊 Resultado OpenAI GPT-4o: 1.00
```

## 📜 License

MIT License

---

**Contributions and suggestions are welcome!**
