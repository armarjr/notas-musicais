![Logo do Projeto](assets/logo.png){ width="200" .center}
# Notas Musicais
Notas musicais é um CLI para ajudar na formação de escalas e acordes.
Temos 2 comandos disponíveis `escalas` e `acordes`

## Como usar ?

###Escalas :

Voce pode chamar escalas via linha de terminal. Por exemplo:
```bash
poetry run notas-musicais escala
```

Retornando os graus e as notas correspondentes a essa escala :

```

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteraçao na escala

O primeiro parametro do CLI é a tonica da escala que deseja exibir. desta forma voce pode alterar a escala a ser exibida. Por exemplo escala de F#

```bash
poetry run notas-musicais escala F#
```
Retorna :

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘

```

#### Alteração na tonalidade da escala. 

Este é o segundo parametro da linha de comando. Por exemplo a escala de 'D#' maior

```bash
poetry run notas-musicais escala D# menor

```
Retornando:
```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘
```

##$Acordes 
Uso basico

```
poetry run notas-musicais acorde

┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```
### Variações na Cifra

```
poetry run notas-musicais acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```
Até o momento voce pode utilizar acordes maiores, menores, aumentados e diminutos


#### Mais informaçoes sobre o CLI
Para descobrir outras opçoes, voce pode usar a flag `--help` :

```bash
poetry run notas-musicais --help


 Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]                                                                 
                                                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica da escala [default: c]                                                │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
