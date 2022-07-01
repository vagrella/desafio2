# encoding: utf-8
import unittest

import app.config as config
import app.model.Job as Job
import app.retorna_jobs as rj

class TestRetornaJobs(unittest.TestCase):

    def setUp(self):
        rj.criar_job(config.arq_jobs)
        # Preparar: alterar o json para data atual
        dic_jobs = rj.ler_jobs(config.arq_jobs)
        # Colocar a data fim da Janela para 5 dias
        data_futuro = config.data_atual + config.dt.timedelta(days=5)
        dic_jobs[0][Job.campo.janela_execucao] = str(config.data_atual) + ' 00:00:00 até ' + str(data_futuro) + ' 00:00:00'

        # Alterar o período do indice 1 [ID: 2]
        # print(dic_jobs[0][Job.campo.lista][1][Job.campo.id])
        dic_jobs[0][Job.campo.lista][1][Job.campo.data_maxima_conclusao] = str(config.data_atual) + ' 23:00:00'

        # Salvar alterações no arquivo
        rj.criar_job(dic_jobs, arq_jobs=config.arq_jobs)

        self.jobs = rj.ler_jobs(config.arq_jobs)

    def test_listar_jobs_vazio(self):
        with self.assertRaises(AttributeError):
            rj.listar_jobs(None)

    def test_jobs_ok(self):
        self.assertEqual(1, self.jobs[0][Job.campo.lista][0][Job.campo.id])
        self.assertEqual(2, self.jobs[0][Job.campo.lista][1][Job.campo.id])
        self.assertEqual(3, self.jobs[0][Job.campo.lista][2][Job.campo.id])

    def test_listar_jobs_ok(self):
        self.assertEqual("[\n[2],\n]", rj.listar_jobs(arq_jobs=config.arq_jobs))

    def test_limite_max_8h(self):
        self.jobs = rj.listar_jobs(config.arq_jobs)
        self.assertEqual(1, self.jobs[0][Job.campo.lista][0][Job.campo.id])
        self.assertEqual(2, self.jobs[0][Job.campo.lista][1][Job.campo.id])
        self.assertEqual(3, self.jobs[0][Job.campo.lista][2][Job.campo.id])

if __name__ == '__main__':
    unittest.main()