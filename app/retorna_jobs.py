# encoding: utf-8
'''
Vornei (@vagrella): 28/06/2022 - Programa Python 3.9 que ira retornar um conjunto de arrays de uma lista de Jobs
Testes automatizados

doctests:

>>> criar_job()
Arquivo Json com massa de dados criado com sucesso!

>>> ler_jobs()
Lendo Jobs...
Dados lidos:
[{'Janela de execução': '2019-11-10 09:00:00 até 2019-11-11 12:00:00', 'lista': [{'ID': 1, 'Descrição': 'Importação de arquivos de fundos', 'Data Máxima de conclusão': '2019-11-10 12:00:00', 'Tempo estimado': '2 horas'}, {'ID': 2, 'Descrição': 'Importação de dados da Base Legada', 'Data Máxima de conclusão': '2019-11-11 12:00:00', 'Tempo estimado': '4 horas'}, {'ID': 3, 'Descrição': 'Importação de dados de integração', 'Data Máxima de conclusão': '2019-11-11 08:00:00', 'Tempo estimado': '6 horas'}]}]


>>> listar_jobs()
Listando Jobs:
Lendo Jobs...
Dados lidos:
[
1,
2,
3,
]


'''
import config
import Job as job
import json
import pandas as pd

'''
Criar o arquivo com o Job
'''
def criar_job():
    j = [{
        job.Campo.janela_execucao: '2019-11-10 09:00:00 até 2019-11-11 12:00:00',
        job.Campo.lista: [
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
        ],
    }]
    #with open('./data/jobs.json', 'w') as arquivo:
    with open(config.arq_jobs, 'w') as arquivo:
        json.dump(j, arquivo, indent=config.indenta)
    print('Arquivo Json com massa de dados criado com sucesso!')

'''
Ler o arquivo com os Jobs retornando o dicionário de jobs do arquivo Json
'''
def ler_jobs():
    print('Lendo Jobs...')
    #with open('./data/jobs.json') as arquivo:
    with open(config.arq_jobs) as arquivo:
        #dicionario de dados contendo os jobs
        jobs = json.load(arquivo)
    print('Dados lidos:')
    return jobs

'''
Listar os IDs dos Jobs
'''
def listar_jobs():
    print('Listando Jobs:')
    # 1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
    lista_jobs = ler_jobs()
    print('[')

    # Maneira Inicial laço
    for linha in lista_jobs:
        #print(linha)
        for linha_job in linha[job.Campo.lista]:
            print(str(linha_job[job.Campo.id])+',')

    # Esta com um erro: ValueError: Invalid file path or buffer object type: <class 'list'>
    # Utilizar o pandas, porém não achei a melhor maneira de orientação para o tipo de arquivo Json inicialmente
    # usando o read_json em que  o pandas pode ler alguns tipos
    # json padrões orientado por: 'records', 'split', 'columns', 'values'
    #pd.read_json(lista_jobs, orient='records')

    #Usando json_normalize
    pd.json_normalize(lista_jobs, record_path=[job.Campo.lista])

    print(']')



if __name__ == "__main__":
    # Para Executar os Testes automatizados
    import doctest
    doctest.testmod()

    # Realizar etapas
    criar_job()
    listar_jobs()