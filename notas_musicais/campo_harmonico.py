from notas_musicais.escalas import escala


def campo_harmonico(tonica: str, tonalidade: str)-> dict[str, list[str]]:
    """
    Gera um campo harmonico com base numa tonica e uma tonalidade

    Parameters: 
        tonica: primeiro grau do campo harmonico 
        tonalidade: tonalidade para o campo. Ex: maior, menor, etc.

    Examples:
        >>> campo_harmonico('C', 'maior')
        {'acordes'= ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'],
        'graus'= ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
        }
        
        >>> campo_harmonico('C', 'menor')
        {'acordes'= ['Cm', 'D', 'D#', 'Fm', 'Gm', 'G#', 'A#'],
        'graus'= ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']
        }
    """
    notas, grau = escala(tonica, tonalidade)