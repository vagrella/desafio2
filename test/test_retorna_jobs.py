# encoding: utf-8
import unittest

import app.retorna_jobs as rj

class TestRetornaJobs(unittest.TestCase):

    def setUp(self):
        rj.criar_job(arq_jobs=rj.config.arq_jobs)
        # Preparar: alterar o json para jobs atual
        dic_jobs = rj.ler_jobs(rj.config.arq_jobs)
        # Colocar a jobs fim da Janela para 5 dias
        data_futuro = rj.config.data_atual + rj.config.dt.timedelta(days=5)
        dic_jobs[0][rj.Job.campo.janela_execucao] = str(rj.config.data_atual) + ' 00:00:00 até ' + str(data_futuro) + ' 00:00:00'

        # Alterar o período do indice 1 [ID: 2]
        # print(dic_jobs[0][Job.campo.lista][1][Job.campo.id])
        dic_jobs[0][rj.Job.campo.lista][1][rj.Job.campo.data_maxima_conclusao] = str(rj.config.data_atual) + ' 23:00:00'

        # Salvar alterações no arquivo
        rj.criar_job(dic_jobs, arq_jobs=rj.config.arq_jobs)

        self.jobs = rj.ler_jobs(rj.config.arq_jobs)

    def test_listar_jobs_vazio(self):
        with self.assertRaises(AttributeError):
            rj.listar_jobs(None)

    # 1) Cada array do conjunto representa uma lista de Jobs a serem executados em sequência;
    def test_jobs_ok(self):
        self.assertEqual(1, self.jobs[0][rj.Job.campo.lista][0][rj.Job.campo.id])
        self.assertEqual(2, self.jobs[0][rj.Job.campo.lista][1][rj.Job.campo.id])
        self.assertEqual(3, self.jobs[0][rj.Job.campo.lista][2][rj.Job.campo.id])

    # 2) Cada array deve conter jobs que sejam executados em, no máximo, 8h;
    def test_limitar_max_8h(self):
        self.assertNotEqual("[\n  [ 2, 4],\n]", rj.listar_jobs(arq_jobs=rj.config.arq_jobs, retorna=True))

    # 3) Deve ser respeitada a jobs máxima de conclusão do Job;
    def test_listar_jobs_ok(self):
        self.assertEqual("[\n  [ 2],\n]", rj.listar_jobs(arq_jobs=rj.config.arq_jobs, retorna=True))

    #4) Todos os Jobs devem ser executados dentro da janela de execução (jobs início e fim).
    def test_janela_ok(self):
        self.assertEqual('[\n]', rj.listar_jobs(arq_jobs=rj.config.arq_jobs_teste, retorna=True))

if __name__ == '__main__':
    unittest.main()