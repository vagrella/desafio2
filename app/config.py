# encoding: utf-8
'''
Vornei: Configurações do programa
'''
import os
import datetime as dt

arg_data_hora = '%Y-%m-%d %H:%M:%S'
data_atual = dt.date.today()

dir_data = './data/'
#arq_jobs = './data/jobs.json'
arq_jobs = os.path.join(dir_data, 'jobs.json')
arq_jobs_teste = os.path.join(dir_data, 'jobs_teste.json')
indenta = 2