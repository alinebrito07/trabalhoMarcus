from gerador import gerar_numero

def test_gerar_numero():
    numero = gerar_numero(1, 10)
    assert 1 <= numero <= 10

    numero = gerar_numero(50, 60)
    assert 50 <= numero <= 60
