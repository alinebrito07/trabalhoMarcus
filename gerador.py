import random

def gerar_numero(minimo=1, maximo=100):
    """Gera um número aleatório entre mínimo e máximo (padrão: 1 a 100)."""
    return random.randint(minimo, maximo)