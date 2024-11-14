![Logo do Projeto](assets/logo.png){ width="200" .center}
# Notas Musicais
Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmonicos.
Temos 2 comandos disponíveis `escalas` e `acordes`

Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um subcomando aplicado a cada ação que a aplicação pode realizar. Como `escalas`, `acordes` e `campos-hamonicos`
## Como usar ?

###Escalas:

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

###Acordes:
Uso basico

```
poetry run notas-musicais acorde

┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```
#### Variações na Cifra

```
poetry run notas-musicais acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```
Até o momento voce pode utilizar acordes maiores, menores, aumentados e diminutos


###Campo harmonico:

Vocẽ pode chamar os campos harmonicos via subcomando `campo-harmonicos`
```
poetry run notas-musicais campo-harmonico

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘

```
Por padão os parametros utlizados são a tonica de `C` e  campo harmonico `menor`

#### Alterações nos campos harmonicos
Voce pode alterar os parametros da tonica e da tonalidade
```bash
poetry run notas-musicais campo-harmonico [TONICA] [TONALIDADE]
```
#### Alterações na tonica do campo
Um exemplo com campo harmonico de `E`
```bash
poetry run notas-musicais campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘

```
#### Alterações na tonalidade do campo
Um exemplo com campo harmonico de `E` com tonalidade `menor`
```bash
poetry run notas-musicais campo-harmonico E menor
┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘

```
### Mais informaçoes sobre o CLI:
Para descobrir outras opções, voce pode usar a flag `--help` :

```bash
poetry run notas-musicais --help
```
```
 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...                                                               
                                                                                                            

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                       │
│ --show-completion             Show completion for the current shell, to copy it or customize the              │
│                               installation.                                                                   │
│ --help                        Show this message and exit.                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ acorde                                                                                                        │
│ campo-harmonico                                                                                               │
│ escala                                                                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
### Mais informações sobre os subcomandos
As informações sobre os subcomandos podem ser acessadas com a flag `--help` após o nome do parametro.
Um exemplo da flag `--help` nos campos harmonicos:

```bash
poetry run notas-musicais campo-harmonico --help

 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]                                           
                                                                                                                 
╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica do campo harmonico [default: c]                                        │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmonico [default: maior]                                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```