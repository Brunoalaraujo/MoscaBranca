from fastapi import FastAPI
from dotenv import load_dotenv
from docx import Document
import os
import requests
import json

load_dotenv()

app = FastAPI()
my_url = os.getenv('MY_URL')
api_key = os.getenv('API_KEY')

@app.post(my_url)
def text_sending():
    '''
    Essa função envia o texto para a API do LM Studio e retorna a resposta da API
    
    Inputs:
    - text: str - texto que deseja enviar para a API do LM Studio
    - system_propnt: str - prompt que será enviado para a API do LM Studio
    
    Outputs:
    - content_return: str - texto retornado pela API do LM Studio
    '''
    try:
        print('Digite o texto que deseja enviar para a API do LM Studio: ')
        text = input()
        system_propnt = '''
        Você é um assistente especializado em processamento de documentos. Sua tarefa é resumir documentos longos em tópicos organizados em uma lista ordenada. Siga estas instruções ao responder:

        1. Leia o documento fornecido pelo usuário.
        2. Identifique os principais tópicos e subtópicos do documento, mantendo a ordem de aparição no texto original.
        3. Crie uma lista numerada onde cada item seja um tópico resumido do documento.
        4. Mantenha a fidelidade ao conteúdo original, utilizando as palavras-chave do documento sempre que possível.

        Seja claro, conciso e organizado ao apresentar os tópicos. Se precisar de mais informações, solicite ao usuário.
        '''
        response = requests.post(
            my_url,
            json={
                'api_key': api_key, 
                'messages': [
                    {
                    'role': 'system',
                    'content': f'{system_propnt}'},
                    { 
                    'role': 'user',
                    'content': f'{text}'
                    }
                    ],
                'max_tokens': 8000,
                })
        
        print(response.status_code)
        
        json_data = response.text
        data = json.loads(json_data)
        content_return = data['choices'][0]['message']['content']
        return content_return
    except Exception as e:
        print(f'Error: {e}')
        return f'Error: {e}'

def save_document(content_return):
    '''
    Essa função salva o documento retornado pela API do LM Studio
    
    Inputs:
    - content_return: str - texto retornado pela API do LM Studio
    
    Outputs:
    - Documento salvo no formato .docx
    '''
    try:
        document = Document()
        document.add_paragraph(content_return)
        document.save(f'resumo.docx')
    except Exception as e:
        print(f'Error: {e}')
        return f'Error: {e}'

def main():
    content_return = text_sending()
    save_document(content_return)

if __name__ == '__main__':
    main()