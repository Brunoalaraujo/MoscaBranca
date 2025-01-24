from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests

app = FastAPI()
my_url = os.getenv('MY_URL')
api_key = os.getenv('API_KEY')

@app.post(my_url)
def text_sending():
    '''
    Essa função envia o texto para a API do LM Studio e retorna a resposta da API
    '''
    response = requests.post(
        my_url,
        json={
            'api_key': api_key, 
            'messages': [{ 
                'role': 'user',
                'content': 'explique o que é um LLM, com exemplos'}],
            'max_tokens': 5000,
            })
    print(response.status_code)
    print(response.text)

def main():
    text_sending()

if __name__ == '__main__':
    main()