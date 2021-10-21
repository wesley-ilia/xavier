from unittest import TestCase
from ..app.pycjava import batalhar, verifica_escolha


# Lula
# Luigi'''''''''
# Luiz
# Gabriel
# Cezar

class tests_pycjava(TestCase):
    def test_c_batalhando_contra_py_ganha_o_c(self):
        jogador1 = "c"
        jogador2 = "py"
        esperado = 'c'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)

    def test_c_batalhando_contra_java_ganha_java(self):

        jogador1 = 'c'
        jogador2 = 'java'
        esperado = 'java'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)

    def test_c_batalhando_contra_c_empate(self):
        jogador1 = 'c'
        jogador2 = 'c'
        esperado = 'nenhum'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)

    def test_py_batalhando_contra_c_ganha_c(self):
        jogador1 = 'py'
        jogador2 = 'c'
        esperado = 'c'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)


    def test_java_batalhando_contra_py_ganha_py(self):
        jogador1 = 'java'
        jogador2 = 'py'
        esperado = 'py'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)

    def test_java_batalhando_contra_c_ganha_java(self):
        jogador1 = 'java'
        jogador2 = 'c'
        esperado = 'java'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)

    def test_py_batalhando_contra_java_ganha_py(self):
        jogador1 = 'py'
        jogador2 = 'java'
        esperado = 'py'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)

    def test_invalido_contra_java_retorna_erro(self):
        jogador1 = 'ruby'
        jogador2 = 'java'
        esperado = 'ERROR'

        vencedor = batalhar(jogador1, jogador2)

        self.assertEqual(esperado, vencedor)
        
    def test_opcao_invalida(self):
        opcao = "Ruby"
        esperado = False

        ret = verifica_escolha(opcao)
        self.assertEqual(esperado, ret)

    def test_opcao_correta(self):
        opcao = "c"
        esperado = True

        ret = verifica_escolha(opcao)
        self.assertEqual(esperado, ret)
