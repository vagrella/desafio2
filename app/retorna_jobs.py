# encoding: utf-8
'''
Vornei (@vagrella): 28/06/2022 - Programa Python 3.9 que ira retornar um conjunto de arrays de uma lista de Jobs
Testes automatizados

doctests:

>>> criar_job()
Arquivo criado com sucesso

>>> ler_jobs()
True

'''

from datetime import date as dt
import Job as job
import json
import pandas as pd

data_atual = dt.today()

'''
Criar o arquivo com o Job
'''
def criar_job():
    j = [
        {
            job.Campo.id: 1,
            job.Campo.descricao: "Importação de arquivos de fundos",
            job.Campo.data_maxima_conclusao: '2019-11-10 12:00:00',
            job.Campo.tempo_estimado: '2 horas',
        },
        {
            job.Campo.id: 2,
            job.Campo.descricao: "Importação de dados da Base Legada",
            job.Campo.data_maxima_conclusao: '2019-11-11 12:00:00',
            job.Campo.tempo_estimado: '4 horas',
        },
        {
            job.Campo.id: 3,
            job.Campo.descricao: "Importação de dados de integração",
            job.Campo.data_maxima_conclusao: '2019-11-11 08:00:00',
            job.Campo.tempo_estimado: '6 horas',
        }
    ]
    with open('./data/jobs.json', 'w') as arquivo:
        json.dump(j, arquivo)
    print('Arquivo criado com sucesso')

'''
Ler o arquivo com os Jobs
'''
def ler_jobs():
    with open('./data/jobs.json') as arquivo:
        jobs = json.load(arquivo)
    return True



if __name__ == "__main__":
    # Para Executar os Testes automatizados
    import doctest
    doctest.testmod()

    # Realizar a leitura do arquivo
    #criar_job()
    #ler_jobs()