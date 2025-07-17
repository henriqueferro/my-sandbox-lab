import os
import openai
import anthropic
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# Inicializa clientes
openai_client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
anthropic_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

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
        model="claude-sonnet-4",
        max_tokens=800,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

llama3_pipeline = None
def run_llama3(prompt):
    global llama3_pipeline
    if llama3_pipeline is None:
        model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_id, token=os.environ["HF_TOKEN"])
        model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", token=os.environ["HF_TOKEN"])
        llama3_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
    output = llama3_pipeline(prompt, max_new_tokens=300, temperature=0.2)[0]["generated_text"]
    return output.replace(prompt, "")

# Prompt files
prompts = {
    "FizzBuzz": open("prompts/fizzbuzz.txt").read(),
    "ReverseString": open("prompts/reverse_string.txt").read()
}

models = {
    #"OpenAI GPT-4o": run_openai,
    "Anthropic Claude Sonnet 4": run_claude,
    "LLaMA3 8B": run_llama3
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