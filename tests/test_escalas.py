# AAA - 3A  - A3
# Arange - Act - Assets
# Arrumar - Agir - Garantir
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_letras_minusculas():
    # Arrumar
    tonica = 'c'

    tonalidade = 'maior'

    # Act  chama o que testar
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'

    tonalidade = 'maior'

    mensagem_de_erro = f'Esta nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'c'

    tonalidade = 'tonalidade'

    mensagem_de_erro = f'Esta escala não existe ou nao foi implementada, tente uma dessas {list(ESCALAS.keys())}'
    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'tonica, tonalidade, esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def teste_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    result = escala(tonica, tonalidade)
    assert result['notas'] == esperado


def teste_deve_retornar_os_sete_graus():

    tonica = 'c'

    tonalidade = 'maior'

    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    result = escala(tonica, tonalidade)

    assert result['graus'] == esperado
