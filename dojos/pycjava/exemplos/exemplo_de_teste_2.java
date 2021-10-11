public void teste_soma_entrando_com_numero_2_e_4_espera_6_como_saida(){
	
	int entrada1 = 2;
	int entrada2 = 4;
	int esperado = 5;

	int retorno = Calculadora.soma(entrada1, entrada2);

	Assert.assertEquals(esperado, retorno);

}