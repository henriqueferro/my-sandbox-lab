import os
import openai
import anthropic
import cohere
import requests
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# Inicializa clientes
openai_client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
anthropic_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
cohere_client = cohere.Client(os.environ["COHERE_API_KEY"])
api_key = os.environ.get("XAI_API_KEY")

# Funções de inferência
def run_openai(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content

def run_claude(prompt):
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=800,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def run_cohere(prompt):
    response = cohere_client.generate(
        model="command",
        prompt=prompt,
        max_tokens=256,
        temperature=0.2
    )
    return response.generations[0].text

def run_grok3(prompt):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "grok-3",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 800
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Prompt files
prompts = {
    "FizzBuzz": open("prompts/fizzbuzz.txt").read(),
    "ReverseString": open("prompts/reverse_string.txt").read(),
    "SudokuSolver": open("prompts/sudoku_solver.txt").read(),
    "BalancedParentheses": open("prompts/balanced_parentheses.txt").read(),
    "LRUCache": open("prompts/lru_cache.txt").read(),
    "FindAllAnagrams": open("prompts/find_all_anagrams.txt").read(),
    "DijkstraShortestPath": open("prompts/dijkstra_shortest_path.txt").read()
}

models = {
    "Grok-3 (x.ai)": run_grok3,
    "Anthropic Claude Sonnet 4": run_claude,
    "Cohere Command": run_cohere,
    "OpenAI GPT-4o": run_openai
}

# Métrica de avaliação
metric = AnswerRelevancyMetric(threshold=0.5)

# Benchmark loop
for task_name, prompt in prompts.items():
    print(f"\n🔍 Benchmark: {task_name}")

    for model_name, infer in models.items():
        print(f"🏗️ Testando {model_name}...")
        output = infer(prompt)

        test_case = LLMTestCase(
            input=prompt,
            actual_output=output,
            expected_output=""
        )

        result = evaluate([test_case], [metric])
        # print(result)
        #print(dir(result))
        score = result.test_results[0].metrics_data[0].score
        print(f"📊 Resultado {model_name}: {score:.2f}")
