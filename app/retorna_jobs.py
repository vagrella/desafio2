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
]


'''
import config
import model.Job as Job

import json
#import pandas as pd

'''
Criar o arquivo com o Job
'''
def criar_job(j = [], arq_jobs = ''):
    if not arq_jobs:
        arq_jobs = config.arq_jobs_teste

    if not j:
        j = [{
            Job.campo.janela_execucao: '2019-11-10 09:00:00 até 2019-11-11 12:00:00',
            Job.campo.lista: [
                {
                    Job.campo.id: 1,
                    Job.campo.descricao: "Importação de arquivos de fundos",
                    Job.campo.data_maxima_conclusao: '2019-11-10 12:00:00',
                    Job.campo.tempo_estimado: '2 horas',
                },
                {
                    Job.campo.id: 2,
                    Job.campo.descricao: "Importação de dados da Base Legada",
                    Job.campo.data_maxima_conclusao: '2019-11-11 12:00:00',
                    Job.campo.tempo_estimado: '4 horas',
                },
                {
                    Job.campo.id: 3,
                    Job.campo.descricao: "Importação de dados de integração",
                    Job.campo.data_maxima_conclusao: '2019-11-11 08:00:00',
                    Job.campo.tempo_estimado: '6 horas',
                }
            ],
        }]
    #with open('./data/jobs.json', 'w') as arquivo:
    with open(arq_jobs, 'w') as arquivo:
        json.dump(j, arquivo, indent=config.indenta)
    print('Arquivo Json com massa de dados criado com sucesso!')

'''
Ler o arquivo com os Jobs retornando o dicionário de jobs do arquivo Json
'''
def ler_jobs(arq_jobs = ''):
    print('Lendo Jobs...')
    #with open('./data/jobs.json') as arquivo:

    if not arq_jobs:
        arq_jobs = config.arq_jobs_teste

    with open(arq_jobs) as arquivo:
        #dicionario de dados contendo os jobs
        jobs = json.load(arquivo)
    print('Dados lidos:')
    return jobs

'''
Listar os IDs dos Jobs:
1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;
3) Deve ser respeitada a data máxima de conclusão do Job;
4) Todos os Jobs devem ser executados dentro da janela de execução (data início e fim).
'''
def listar_jobs(arq_jobs = ''):
    print('Listando Jobs:')
    if not arq_jobs:
        arq_jobs = config.arq_jobs_teste

    # 1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
    dicionario_janelas = ler_jobs(arq_jobs)
    print('[')
    # Janelas de execuções
    for janela in dicionario_janelas:
        # 4) Todos os Jobs devem ser executados dentro da janela de execução (data início e fim).
        janela_execucao = janela[Job.campo.janela_execucao].split(' até ', 1)
        data_inicio = config.dt.datetime.strptime(janela_execucao[0], config.arg_data_hora).date()
        data_fim = config.dt.datetime.strptime(janela_execucao[1], config.arg_data_hora).date()

        if data_inicio <= config.data_atual <= data_fim:
            # 2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;
            # Usando json_normalize
            #lista_jobs_max_8h = pd.json_normalize(janela, record_path=[Job.campo.lista])
            lista_jobs_max_8h = janela[Job.campo.lista]
            print('[')
            conta_job = 0;
            for linha_job in lista_jobs_max_8h:
                # 3) Deve ser respeitada a data máxima de conclusão do Job;
                data_maxima_conclusao = config.dt.datetime.strptime(linha_job[Job.campo.data_maxima_conclusao]).date()
                if (data_maxima_conclusao <= config.data_atual):
                    if (conta_job < 0):
                        print(', ')
                    print(linha_job)
                    #print(str(linha_job[Job.campo.id]))
                    conta_job = conta_job + 1
            print('], ')
    print(']')

if __name__ == "__main__":
    # Para Executar os Testes automatizados
    import doctest
    doctest.testmod()

    # Realizar etapas
    criar_job(arq_jobs=config.arq_jobs)
    #Alterar para datas atuais
    dic_jobs = ler_jobs(config.arq_jobs)
    print(dic_jobs[Job.campo.janela_execucao])
    #dic_jobs[Job.campo.janela_execucao] = str(config.data_atual) + ' até ' + str(config.data_atual + config.dt.timedelta(days=5))
    #dic_jobs.dump()

    listar_jobs(config.arq_jobs)