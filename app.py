from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests
import json

app = FastAPI()
my_url = os.getenv('MY_URL')
api_key = os.getenv('API_KEY')

@app.post(my_url)
def text_sending():
    '''
    Essa função envia o texto para a API do LM Studio e retorna a resposta da API
    '''
    print('Digite o texto que deseja enviar para a API do LM Studio: ')
    text = input()
    response = requests.post(
        my_url,
        json={
            'api_key': api_key, 
            'messages': [{ 
                'role': 'user',
                'content': f'{text}'}],
            'max_tokens': 8000,
            })
    
    print(response.status_code)
    
    json_data = response.text
    data = json.loads(json_data)
    content_return = data['choices'][0]['message']['content']
    
    print(content_return)

def main():
    text_sending()

if __name__ == '__main__':
    main()