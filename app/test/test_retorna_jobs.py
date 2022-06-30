# encoding: utf-8
import unittest

import app.retorna_jobs as rj

class TestRetornaJobs(unittest.TestCase):

    def setUp(self):
        self.dict_jobs = rj.ler_jobs()

    def test_lista_jobs_vazio(self):
        rj.listar_jobs('')

if __name__ == '__main__':
    unittest.main()