# 🧪 LLM Code Benchmark with DeepEval

This module compares the performance of LLM models on code generation tasks using the [DeepEval](https://github.com/confident-ai/deepeval) library.

## 📦 Supported Models

- 🧠 OpenAI GPT-4o
- 🤖 Anthropic Claude 3 Sonnet
- 🦙 Meta LLaMA 3 (via HuggingFace)

## 📂 Structure

```
llm-benchmark/
├── main.py               # Main benchmark code
├── prompts/              # Evaluation prompts
│   ├── fizzbuzz.txt
│   └── reverse_string.txt
└── requirements.txt
```

## ▶️ How to run

```bash
cd llm-benchmark
pip install -r requirements.txt

# Set your keys:
export OPENAI_API_KEY="..."
export ANTHROPIC_API_KEY="..."
export HF_TOKEN="..."

# Run
python main.py
```

## 📈 Metric used

- `CodeMatchMetric`: compares logic, syntax, and semantics of the generated code.
