from num2words import num2words
def clean(token: str) -> str:
    if token.isdigit():
        return num2words(int(token))
    

data = {}
for i in range(1, 8):
    with open(f'./data/{i}.txt') as f:
        data[i] = f.read()
    
text = data[1]
text = text.strip().replace('\n', ' ')
tokens = text.split(' ')
tokens = [clean(t) for t in tokens]