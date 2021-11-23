var estado = '[{"value": 1, "text": "AC", "continent": "Task"}, {"value": 2, "text": "AL", "continent": "Task"}, {"value": 3, "text": "AM", "continent": "Task"}, {"value": 4, "text": "AP", "continent": "Task"}, {"value": 5, "text": "BA", "continent": "Task"}, {"value": 6, "text": "CE", "continent": "Task"}, {"value": 7, "text": "DF", "continent": "Task"}, {"value": 8, "text": "ES", "continent": "Task"}, {"value": 9, "text": "GO", "continent": "Task"}, {"value": 10, "text": "MA", "continent": "Task"}, {"value": 11, "text": "MG", "continent": "Task"}, {"value": 12, "text": "MS", "continent": "Task"}, {"value": 13, "text": "MT", "continent": "Task"}, {"value": 14, "text": "PA", "continent": "Task"}, {"value": 15, "text": "PB", "continent": "Task"}, {"value": 16, "text": "PE", "continent": "Task"}, {"value": 17, "text": "PI", "continent": "Task"}, {"value": 18, "text": "PR", "continent": "Task"}, {"value": 19, "text": "RJ", "continent": "Task"}, {"value": 20, "text": "RN", "continent": "Task"}, {"value": 21, "text": "RO", "continent": "Task"}, {"value": 22, "text": "RR", "continent": "Task"}, {"value": 23, "text": "RS", "continent": "Task"}, {"value": 24, "text": "SC", "continent": "Task"}, {"value": 25, "text": "SE", "continent": "Task"}, {"value": 26, "text": "SP", "continent": "Task"}, {"value": 27, "text": "TO", "continent": "Task"}]';

var mercado = '[{"value": 1, "text": "Advertising", "continent": "Task"}, {"value": 2, "text": "Agronegócio", "continent": "Task"}, {"value": 3, "text": "Automobilismo", "continent": "Task"}, {"value": 4, "text": "Big Data", "continent": "Task"}, {"value": 5, "text": "Biotecnologia", "continent": "Task"}, {"value": 6, "text": "Casa e Família", "continent": "Task"}, {"value": 7, "text": "Cloud Computing", "continent": "Task"}, {"value": 8, "text": "Comunicação e Mídia", "continent": "Task"}, {"value": 9, "text": "Construção Civil", "continent": "Task"}, {"value": 10, "text": "CRM", "continent": "Task"}, {"value": 11, "text": "Desenvolvimento de Software", "continent": "Task"}, {"value": 12, "text": "Direito", "continent": "Task"}, {"value": 13, "text": "E-commerce", "continent": "Task"}, {"value": 14, "text": "Educação", "continent": "Task"}, {"value": 15, "text": "Energia", "continent": "Task"}, {"value": 16, "text": "Entretenimento", "continent": "Task"}, {"value": 17, "text": "Esportes", "continent": "Task"}, {"value": 18, "text": "Eventos e Turismo", "continent": "Task"}, {"value": 19, "text": "Finanças", "continent": "Task"}, {"value": 20, "text": "Games", "continent": "Task"}, {"value": 21, "text": "Gestão", "continent": "Task"}, {"value": 22, "text": "Hardware", "continent": "Task"}, {"value": 23, "text": "Imobiliário", "continent": "Task"}, {"value": 24, "text": "Indústria", "continent": "Task"}, {"value": 25, "text": "Infantil", "continent": "Task"}, {"value": 26, "text": "Internet", "continent": "Task"}, {"value": 27, "text": "Logística e Mobilidade Urbana", "continent": "Task"}, {"value": 28, "text": "Meio Ambiente", "continent": "Task"}, {"value": 29, "text": "Mobile", "continent": "Task"}, {"value": 30, "text": "Moda e Beleza", "continent": "Task"}, {"value": 31, "text": "Nanotecnologia", "continent": "Task"}, {"value": 32, "text": "Outros", "continent": "Task"}, {"value": 33, "text": "Pets", "continent": "Task"}, {"value": 34, "text": "Produtos de Consumo", "continent": "Task"}, {"value": 35, "text": "Recrutamento", "continent": "Task"}, {"value": 36, "text": "Recursos Humanos", "continent": "Task"}, {"value": 37, "text": "SN", "continent": "Task"}, {"value": 38, "text": "Saúde e Bem-estar", "continent": "Task"}, {"value": 39, "text": "Segurança e Defesa", "continent": "Task"}, {"value": 40, "text": "Seguros", "continent": "Task"}, {"value": 41, "text": "Serviços Profissionais", "continent": "Task"}, {"value": 42, "text": "TIC e Telecom", "continent": "Task"}, {"value": 43, "text": "Transportes", "continent": "Task"}, {"value": 44, "text": "Varejo Atacado", "continent": "Task"}, {"value": 45, "text": "Vendas e Marketing", "continent": "Task"}, {"value": 46, "text": "Video", "continent": "Task"}]';
//get data pass to json

var task_estado = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace("text"),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  local: jQuery.parseJSON(estado) //your can use json type
});

var task_mercado = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace("text"),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  local: jQuery.parseJSON(mercado) //your can use json type
});



$(document).ready(function() {
    alert("ola5");

/*     $('#tag1').click(function()
		{
        alert("o");
    });
 */
    task_estado.initialize();
    task_mercado.initialize();

    var elt = $("#tag1");
    elt.tagsinput({
      itemValue: "value",
      itemText: "text",
      typeaheadjs: {
        name: "task",
        displayKey: "text",
        source: task_estado.ttAdapter()
      }
    });

    //insert data to input in load page
    elt.tagsinput("add", {
      value: 1,
      text: "SP",
      continent: "Task"
    });

    var elt_2 = $("#tag2");
    elt_2.tagsinput({
      itemValue: "value",
      itemText: "text",
      typeaheadjs: {
        name: "task",
        displayKey: "text",
        source: task_mercado.ttAdapter()
      }
    });

    //insert data to input in load page
    elt_2.tagsinput("add", {
      value: 1,
      text: "MARAVILHA",
      continent: "Task"
    });
})
