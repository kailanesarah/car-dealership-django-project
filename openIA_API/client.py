from openai import OpenAI
import os


client = OpenAI(api_key= os.getenv("API_KEY")) #SUA CHAVE DE ACESSO DA OPENIA


def open_ai_bio(model, brand, year):
    message = '''Me mostre uma descrição de venda para o carro {} {} {} em apenas 100 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro. Dê quebra nos parágrafos e deixe tudo bem organizado'''
    
    message = message.format(model, brand, year)
    
    response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": message,
    }],
    max_tokens = 1000,
    model="gpt-4o-mini",)
    
    return response.choices[0].message.content
