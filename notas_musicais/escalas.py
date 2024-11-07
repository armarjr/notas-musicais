NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    '''
    Gera uma escala apartir de uma tonica e uma tonalidade
    
    Parameters:
        tonica: nota que será a tonica da escala
        tonalidade: tonalidade da escala
    
    returns:
        Um dicionario com as notas da escala e os graus
    
    Raises:
        ValueError : caso a tonica nao seja uma nota valida    
    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    
        >>> escala('x', 'maior')
    '''
    
    tonica = tonica.upper()
    intervalos = ESCALAS[tonalidade]
    try:    
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f"Esta nota não existe, tente uma dessas {NOTAS}")        
        
    temp = []
    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
