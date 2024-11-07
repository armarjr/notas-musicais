"""
AAA - 3A  - A3 
    
Arange - Act - Assets
Arrumar - Agir - Garantir   
"""
from notas_musicais.escalas import NOTAS, escala
from pytest import raises

def test_deve_funcionar_com_letras_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'
    
    # Act  chama o que testar    
    result = escala(tonica, tonalidade)
    
    # Assert 
    assert result

def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = "X"
    tonalidade = "maior"
     
    mensagerm_de_erro = f"Esta nota não existe, tente uma dessas {NOTAS}"
    
    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    print(error)   
