# encoding: utf-8
'''
Vornei (@vagrella): 28/06/2022 - Programa Python 3.9 que ira retornar um conjunto de arrays de uma lista de Jobs
Testes automatizados

doctests:

>>> criar_job()
Arquivo Json com massa de dados salvo com sucesso!

>>> ler_jobs(None)
O Caminho do arquivo deve ser do tipo string!

>>> import app.config as cg
>>> listar_jobs(cg.arq_jobs_teste)
Listando Jobs:
Lendo Jobs...
[
]

'''
import config as config
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

    with open(arq_jobs, 'w') as arquivo:
        json.dump(j, arquivo, indent=config.indenta)
    print('Arquivo Json com massa de dados salvo com sucesso!')

'''
Ler o arquivo com os Jobs retornando o dicionário de jobs do arquivo Json
'''
def ler_jobs(arq_jobs):
    if arq_jobs is None or not isinstance(arq_jobs, str):
        print("O Caminho do arquivo deve ser do tipo string!")
    else:
        print('Lendo Jobs...')
        with open(arq_jobs) as arquivo:
            #dicionario de dados contendo os jobs
            jobs = json.load(arquivo)
        return jobs

'''
Listar os IDs dos Jobs:
1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;
3) Deve ser respeitada a data máxima de conclusão do Job;
4) Todos os Jobs devem ser executados dentro da janela de execução (data início e fim).
'''
def listar_jobs(arq_jobs):

    if arq_jobs is None or not isinstance(arq_jobs, str):
        raise AttributeError('O Caminho do arquivo deve ser do tipo string!')

    print('Listando Jobs:')
    # 1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
    dic_janelas = ler_jobs(arq_jobs)

    if len(dic_janelas) == 0:
        return None

    print('[')
    # Janelas de execuções
    for janela in dic_janelas:
        # 4) Todos os Jobs devem ser executados dentro da janela de execução (data início e fim).
        janela_execucao = janela[Job.campo.janela_execucao].split(' até ', 1)
        data_inicio = config.dt.datetime.strptime(janela_execucao[0], config.arg_data_hora)
        data_fim = config.dt.datetime.strptime(janela_execucao[1], config.arg_data_hora)

        if data_inicio <= config.data_hora_atual <= data_fim:
            # 2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;
            # TODO máximo de 8 h:
            #  Usando json_normalize para
            #lista_jobs_max_8h = pd.json_normalize(janela, record_path=[Job.campo.lista])
            lista_jobs_max_8h = janela[Job.campo.lista]
            print('[')
            conta_job = 0;
            for linha_job in lista_jobs_max_8h:
                # 3) Deve ser respeitada a data máxima de conclusão do Job;
                data_maxima_conclusao = config.dt.datetime.strptime(linha_job[Job.campo.data_maxima_conclusao], config.arg_data_hora)
                if (config.data_hora_atual <= data_maxima_conclusao):
                    if (conta_job < 0):
                        print(', ')

                    print(str(linha_job[Job.campo.id]))
                    conta_job = conta_job + 1
            print('], ')
    print(']')

if __name__ == "__main__":
    # Para Executar os Testes automatizados
    #import doctest
    #doctest.testmod()

    # Rodar a aplicação
    listar_jobs(arq_jobs=config.arq_jobs)