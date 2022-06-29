# encoding: utf-8
'''
Vornei: Configurações do programa
'''

import os, logging
import datetime as dt

arg_data_hora = '%d/%m/%Y %H:%M'
data_atual = dt.date.today()

dir_data = './data/'
#arq_jobs = './data/jobs.json'
arq_jobs = dir_data + 'jobs.json'
indenta = 2