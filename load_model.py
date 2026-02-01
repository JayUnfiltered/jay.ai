from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

token = os.getenv("HF_TOKEN")
model_name = "mistralai/Mistral-7B-Instruct-v0.2"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)

print("Loading model (this might take a few minutes)...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16,
    token=token  # <-- fixed here, replaced use_auth_token with token
)

prompt = "You are Jay’s AI. Introduce yourself in a bold, poetic way."
inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

print("Generating response...")
outputs = model.generate(**inputs, max_new_tokens=150)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
