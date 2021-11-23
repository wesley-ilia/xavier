//var estado = '[{"value": 1, "text": "AC", "continent": "Task"}, {"value": 2, "text": "AL", "continent": "Task"}, {"value": 3, "text": "AM", "continent": "Task"}, {"value": 4, "text": "AP", "continent": "Task"}, {"value": 5, "text": "BA", "continent": "Task"}, {"value": 6, "text": "CE", "continent": "Task"}, {"value": 7, "text": "DF", "continent": "Task"}, {"value": 8, "text": "ES", "continent": "Task"}, {"value": 9, "text": "GO", "continent": "Task"}, {"value": 10, "text": "MA", "continent": "Task"}, {"value": 11, "text": "MG", "continent": "Task"}, {"value": 12, "text": "MS", "continent": "Task"}, {"value": 13, "text": "MT", "continent": "Task"}, {"value": 14, "text": "PA", "continent": "Task"}, {"value": 15, "text": "PB", "continent": "Task"}, {"value": 16, "text": "PE", "continent": "Task"}, {"value": 17, "text": "PI", "continent": "Task"}, {"value": 18, "text": "PR", "continent": "Task"}, {"value": 19, "text": "RJ", "continent": "Task"}, {"value": 20, "text": "RN", "continent": "Task"}, {"value": 21, "text": "RO", "continent": "Task"}, {"value": 22, "text": "RR", "continent": "Task"}, {"value": 23, "text": "RS", "continent": "Task"}, {"value": 24, "text": "SC", "continent": "Task"}, {"value": 25, "text": "SE", "continent": "Task"}, {"value": 26, "text": "SP", "continent": "Task"}, {"value": 27, "text": "TO", "continent": "Task"}]';

//get data pass to json

/*var task_estado = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace("text"),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  local: jQuery.parseJSON(estado) //your can use json type
});

var task_mercado = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace("text"),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  local: jQuery.parseJSON(mercado) //your can use json type
});*/


$(document).ready(function() {
    alert("ola7");
     $('#add_state').click(function()
		{
        valor = $('#estados').value()
        valor += $('#estados').val()+",";
        $('#estado_selecionado').append("teste");
        //alert($('#estados').val());
    });
 
  /*  task_estado.initialize();
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
    });*/
})
