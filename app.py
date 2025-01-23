import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    """if comando in ('olá', 'boa tarde', 'bom dia'):
        return 'Olá tudo bem!'
    if comando == 'como estás':
        return 'Estou bem, obrigado!'
    if comando == 'como te chamas?':
        return 'O meu nome é: Bot :)'
    if comando == 'tempo':
        return 'Está um dia de sol!'
    if comando in ('bye', 'adeus', 'tchau'):
        return 'Gostei de falar contigo! Até breve...'
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'"""

    # Alternativa mais eficiente com dicionário usando tuplas para chaves e listas para valores
    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'capital de portugal': "Lisboa",
        'como te chamas': 'O meu nome é: Bot :)',
        'chat gpt': 'Chat quê? Sou muito melhor que ele',
        'tempo': 'Está um dia de sol!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'historia de portugal': 'Portugal tem uma rica história...',
        'horas': lambda: f'São: {datetime.now():%H:%M} horas',
        ('data', 'dia'): lambda: f'Hoje é dia: {datetime.now():%d-%m-%Y}',
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if any(subcomando in comando for subcomando in chave):
                if callable(resposta):
                    return resposta()
                return resposta
        elif chave in comando:
            if callable(resposta):
                return resposta()
            return resposta

    """if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'

    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'"""

    return f'Desculpa, não entendi a questão! {texto}'



def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
