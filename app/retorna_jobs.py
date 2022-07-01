# encoding: utf-8
'''
Vornei (@vagrella): 28/06/2022 - Programa Python 3.9 que ira retornar um conjunto de arrays de uma lista de Jobs
Testes automatizados

doctests:
>>> import app.config as cg

>>> criar_job()
Arquivo Json com massa de dados salvo com sucesso!

>>> ler_jobs(None)
O Caminho do arquivo deve ser do tipo string!

>>> listar_jobs(cg.arq_jobs_teste)
Listando Jobs:
Lendo Jobs...
[]

>>> # Preparar: alterar o json para jobs atual
>>> dic_jobs = ler_jobs(cg.arq_jobs)
Lendo Jobs...
>>> # Colocar a jobs fim da Janela para 5 dias
>>> data_futuro = cg.data_atual + cg.dt.timedelta(days=5)
>>> dic_jobs[0][Job.campo.janela_execucao] = str(cg.data_atual) + ' 00:00:00 até ' + str(data_futuro) + ' 00:00:00'
>>> # Alterar o período do indice 0 [ID: 1]
>>> print(dic_jobs[0][Job.campo.lista][0][Job.campo.id])
1
>>> dic_jobs[0][Job.campo.lista][0][Job.campo.data_maxima_conclusao] = str(cg.data_atual) + ' 23:00:00'
>>> # Alterar o período do indice 2 [ID: 3]
>>> print(dic_jobs[0][Job.campo.lista][2][Job.campo.id])
3
>>> dic_jobs[0][Job.campo.lista][2][Job.campo.data_maxima_conclusao] = str(cg.data_atual) + ' 23:00:00'
>>> # Salvar alterações no arquivo
>>> criar_job(dic_jobs, arq_jobs=cg.arq_jobs)
Arquivo Json com massa de dados salvo com sucesso!
>>> listar_jobs(cg.arq_jobs)
Listando Jobs:
Lendo Jobs...
[
  [ 1, 3],
]

'''
import config as config
import model.Job as Job

import json

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
                },
                {
                    Job.campo.id: 4,
                    Job.campo.descricao: "Importação de dados de integração",
                    Job.campo.data_maxima_conclusao: '2022-12-30 08:00:00',
                    Job.campo.tempo_estimado: '9 horas',
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
3) Deve ser respeitada a jobs máxima de conclusão do Job;
4) Todos os Jobs devem ser executados dentro da janela de execução (jobs início e fim).
'''
def listar_jobs(arq_jobs):

    if arq_jobs is None or not isinstance(arq_jobs, str):
        raise AttributeError('O Caminho do arquivo deve ser do tipo string!')

    print('Listando Jobs:')
    # 1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
    dic_janelas = ler_jobs(arq_jobs)

    if len(dic_janelas) == 0:
        return None

    output_esperado = '['
    # Janelas de execuções
    for janela in dic_janelas:
        # 4) Todos os Jobs devem ser executados dentro da janela de execução (jobs início e fim).
        janela_execucao = janela[Job.campo.janela_execucao].split(' até ', 1)
        data_inicio = config.dt.datetime.strptime(janela_execucao[0], config.arg_data_hora)
        data_fim = config.dt.datetime.strptime(janela_execucao[1], config.arg_data_hora)

        if data_inicio <= config.data_hora_atual <= data_fim:
            # 2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;
            lista_jobs_max_8h = limitar_jobs_max_8h(janela[Job.campo.lista])
            output_esperado = output_esperado + config.enter + '  [ '
            conta_job = 0;
            for linha_job in lista_jobs_max_8h:
                # 3) Deve ser respeitada a jobs máxima de conclusão do Job;
                data_maxima_conclusao = config.dt.datetime.strptime(linha_job[Job.campo.data_maxima_conclusao], config.arg_data_hora)
                if (config.data_hora_atual <= data_maxima_conclusao):
                    if (conta_job > 0):
                        output_esperado = output_esperado + ', '

                    output_esperado = output_esperado + str(linha_job[Job.campo.id])
                    conta_job = conta_job + 1
            output_esperado = output_esperado + '],' + config.enter
    output_esperado = output_esperado + ']'
    print(output_esperado)

'''
Remove os jobs com mais de 8h da lista, requisito:
2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;

lista_jobs: deve conter a "lista" (parametro: Job.campo.lista), contida no dicionário de janelas de execussões,
parametro janela_execussao[indice], do json, exemplo do parâmetro de entrada: 
1 - dic_janela[0][Job.campo.janela_execucao][0][Job.campo.lista
2 - janela_execusao[0][Job.campo.lista] (caso de laço com 1 nível)
3 - janela[Job.campo.lista] (caso de laço com 2 níveis)
'''
def limitar_jobs_max_8h(lista_jobs):
    i = 0
    for job in lista_jobs:
        tempo_estimado = int(job[Job.campo.tempo_estimado].replace(' horas', ''))
        if (tempo_estimado > config.max_tempo_estimado):
            del lista_jobs[i]
        i = i + 1

    return lista_jobs

if __name__ == "__main__":
    # Para Executar os Testes automatizados
    import doctest
    import config as cg
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    print('Executando os Testes Automatizados Primeiro: ')
    doctest.testmod(cg)
    print('Fim dos Testes!')
    print('+++++++++++++++++++++++++++++++++++++++++++++')

    # Rodar a aplicação
    listar_jobs(arq_jobs=config.arq_jobs)
