from unittest import TestCase
import negocio.pycjava as pycjava


# Lula
# Luigi
# Luiz
# Gabriel

class tests_pycjava(TestCase):
    def test_c_batalhando_contra_py_ganha_o_c(self):
        jogador1 = "c"
        jogador2 = "py"

        vencedor = pycjava.batalhar(jogador1, jogador2)

        self.assertEqual(jogador1, vencedor)
    
    def test_j_batalhando_contra_py_ganha_py(self):
        jogador1 = 'java'
        jogador2 = 'py'

        vencedor = pycjava.batalhar(jogador1, jogador2)

        self.assertEqual(jogador2, vencedor)