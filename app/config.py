# encoding: utf-8
'''
Vornei: Configurações do programa
'''
import os
import datetime as dt

enter = "\n"
arg_data_hora = '%Y-%m-%d %H:%M:%S'
data_atual = dt.date.today()
data_hora_atual = dt.datetime.now()

dir_data = './data/'
#arq_jobs = './data/jobs.json'
arq_jobs = os.path.join(dir_data, 'jobs.json')
arq_jobs_teste = os.path.join(dir_data, 'jobs.json')
indenta = 2
max_tempo_estimado = 8