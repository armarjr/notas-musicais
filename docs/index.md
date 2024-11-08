![Logo do Projeto](assets/logo.png){ width="200" .center}
# Notas Musicais


## Como usar:

Voce pode chamar escalas via linha de terminal. Por exemplo:

```bash

poetry run escalas
```

Retornando os graus e as notas correspondentes a essa escala :

```

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteraçao na escala

O primeiro parametro do CLI é a tonica da escala que deseja exibir. desta forma voce pode alterar a escala a ser exibida. Por exemplo escala de F#

```bash
poetry run escalas F#
```
Retorna :

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘

```

## Voce pode alterar a tonalidade da escala. Este é o segundo parametro da linha de comando. Por exemplo a escala de 'D#' maior

```bash
poetry run escalas D# maior

```
Retornando:
```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘

```
## Mais informaçoes sobre o CLI
Para descobrir outras opçoes, voce pode usar a flag `--help` :

```bash
poetry run escalas --help


 Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]                                                                 
                                                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica da escala [default: c]                                                │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
