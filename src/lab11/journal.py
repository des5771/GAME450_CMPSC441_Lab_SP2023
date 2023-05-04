import torch
import transformers
import random

tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2')
model = transformers.GPT2LMHeadModel.from_pretrained('gpt2')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

intros = [
    "I made it to",
    "I have arrived at ",
    "I can't believe I'm in ",
    "Today, I reached ",
    "I'm at",
    "Dear Journal, I'm in"
    ]

def create_journal_entry(city_name):
    num = random.randint(0, 5)
    intro = intros[num]
    prompt = intro + city_name
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    output = model.generate(input_ids, max_length=200, do_sample=True)
    journal_entry = tokenizer.decode(output[0], skip_special_tokens=True)
    return journal_entry
