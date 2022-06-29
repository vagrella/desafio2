# desafio2

Para rodar o programa em ambientes:
Linux: execute o programa (Shell Script) run.sh
Windows: execute o programa run.bat

Para rodar o programa

## Descrição:
Dado um array de "jobs" para execução, no qual cada posição possui um objeto com os seguintes atributos:

1) ID: Identificação do Job;
2) Descrição: Descrição do Job;
3) Data Máxima de conclusão do Job: Data máxima em que o Job deve ser concluído;
4) Tempo estimado: Tempo estimado de execução do Job.

Criar algoritmo que retorne um conjunto de arrays com as seguintes características:

1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;
3) Deve ser respeitada a data máxima de conclusão do Job;
4) Todos os Jobs devem ser executados dentro da janela de execução (data início e fim).

Orientações:

1) Disponibilizar o código final no github e compartilhar o link;
2) Realizar small commits (evitar um commit único com toda a solução);
3) Pode ser usada qualquer tecnologia para solucionar o problema;
4) Desenvolver testes automatizados para a solução.

Exemplo de Massa de dados:

```txt
Janela de execução: 2019-11-10 09:00:00 até 2019-11-11 12:00:00

[
    {
        "ID": 1,
        "Descrição": "Importação de arquivos de fundos",
        "Data Máxima de conclusão": 2019-11-10 12:00:00,
        "Tempo estimado": 2 horas,
    },
    {
        "ID": 2,
        "Descrição": "Importação de dados da Base Legada",
        "Data Máxima de conclusão": 2019-11-11 12:00:00,
        "Tempo estimado": 4 horas,
    },
    {
        "ID": 3,
        "Descrição": "Importação de dados de integração",
          "Data Máxima de conclusão": 2019-11-11 08:00:00,
        "Tempo estimado": 6 horas,
    },
]
```
Output esperado:
```txt
[
    [1, 3],
    [2]
]
```

## Tecnologia(s) e requisitos:
Sistema Operacional: Linux (Preferêncial)
Liguagem de Programação: Python (versão 3.x)
Pacotes e Libs Python: json, pandas e numpy

## Ambiente DEV
Framework: Flask

```txt
cd desafio2
virtualenv venv
. venv/bin/activate
pip install Flask
```
