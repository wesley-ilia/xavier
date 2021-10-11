// AAA
// Arrange
// Act
// Assert

public void teste_soma_entrando_com_numero_1_e_2_espera_3_como_saida(){
	
	int entrada1 = 1;
	int entrada2 = 2;
	int esperado = 3;

	int retorno = Calculadora.soma(entrada1, entrada2);

	Assert.assertEquals(esperado, retorno);

}