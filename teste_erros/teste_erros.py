import unittest

from distancia_datas import calcula_datas

from recebe_datas import datas

from separacao_datas import separa_datas


class TestSeparacaoDatas(unittest.TestCase):
    
    def teste_data_esperado(self):
        result = separa_datas("1 de Janeiro de 2023 - 31 de Dezembro de 2023")
        self.assertEqual(result, (["1", "1", "2023"], ["31", "12", "2023"]))

    def teste_data_minuscula(self):
        result = separa_datas("1 de janeiro de 2023 - 31 de dezembro de 2023")
        self.assertEqual(result, (["1", "1", "2023"], ["31", "12", "2023"]))

    def teste_data_maiscula(self):
        result = separa_datas("1 DE JANEIRO DE 2023 - 31 DE DEZEMBRO DE 2023")
        self.assertEqual(result, (["1", "1", "2023"], ["31", "12", "2023"]))

    def teste_mes_invalido(self):
        result = separa_datas("1 de Janeir de 2023 - 31 de Dezembro de 2023")
        self.assertEqual(result, (["1", "1", "2023"], ["31", "12", "2023"]))

    def teste_dia_invalido(self):
        result = separa_datas("29 de Fevereiro de 2023 - 31 de Dezembro de 2023")
        self.assertEqual(result, (["29", "2", "2023"], ["31", "12", "2023"]))

class TestDistanciaDatas(unittest.TestCase):
    
    def teste_diferenca(self):
        result = calcula_datas(["31", "12", "2024"], ["1", "1", "2024"])
        self.assertEqual(result, 365)

    def teste_ano_bissexto(self):
        result = calcula_datas(["1", "1", "2024"], ["31", "12", "2024"])
        self.assertEqual(result, 365)

    def teste_dia_invalido(self):
        result = calcula_datas(["28", "2", "2023"], ["1", "2", "2023"])
        self.assertEqual(result, 1)

class TestRecebeDatas(unittest.TestCase):

    def arquivo_sem_extensao(self):
        result = datas("data_atividade")
        self.assertEqual(result, "31 de Agosto de 2022-18 de Setembro de 2023")

    def caminho_relativo(self):
        result = datas("./data_atividade.txt")
        self.assertEqual(result, "31 de Agosto de 2022-18 de Setembro de 2023")

if __name__ == "__main__":
    unittest.main()
