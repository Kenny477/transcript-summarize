import torch
import json
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

data = {}
for i in range(1, 8):
    with open(f'./data/{i}.txt') as f:
        data[i] = f.read()

text = data[1]
length = len(text)

preprocess_text = text.strip().replace('\n', ' ')
t5_prepared_Text = "summarize: " + preprocess_text

tokenized_text = tokenizer.encode(t5_prepared_Text, max_length=512, truncation=True, return_tensors="pt").to(device)

summary_ids = model.generate(tokenized_text,
                                num_beams=4,
                                no_repeat_ngram_size=2,
                                min_length=100,
                                max_length=100,
                                early_stopping=True)

output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(output)