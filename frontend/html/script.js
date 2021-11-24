

  
  //var estado = '[{"value": 1, "text": "AC", "continent": "Task"}, {"value": 2, "text": "AL", "continent": "Task"}, {"value": 3, "text": "AM", "continent": "Task"}, {"value": 4, "text": "AP", "continent": "Task"}, {"value": 5, "text": "BA", "continent": "Task"}, {"value": 6, "text": "CE", "continent": "Task"}, {"value": 7, "text": "DF", "continent": "Task"}, {"value": 8, "text": "ES", "continent": "Task"}, {"value": 9, "text": "GO", "continent": "Task"}, {"value": 10, "text": "MA", "continent": "Task"}, {"value": 11, "text": "MG", "continent": "Task"}, {"value": 12, "text": "MS", "continent": "Task"}, {"value": 13, "text": "MT", "continent": "Task"}, {"value": 14, "text": "PA", "continent": "Task"}, {"value": 15, "text": "PB", "continent": "Task"}, {"value": 16, "text": "PE", "continent": "Task"}, {"value": 17, "text": "PI", "continent": "Task"}, {"value": 18, "text": "PR", "continent": "Task"}, {"value": 19, "text": "RJ", "continent": "Task"}, {"value": 20, "text": "RN", "continent": "Task"}, {"value": 21, "text": "RO", "continent": "Task"}, {"value": 22, "text": "RR", "continent": "Task"}, {"value": 23, "text": "RS", "continent": "Task"}, {"value": 24, "text": "SC", "continent": "Task"}, {"value": 25, "text": "SE", "continent": "Task"}, {"value": 26, "text": "SP", "continent": "Task"}, {"value": 27, "text": "TO", "continent": "Task"}]';
  var estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
  var mercados = ['Advertising', 'S/N', 'Vendas e Marketing', 'Recursos Humanos', 'Meio Ambiente', 'Indústria', 'Internet', 'Transportes', 'Energia', 'Seguros', 'Infantil', 'Direito', 'Automobilismo', 'Educação', 'E-commerce', 'Gestão', 'Saúde e Bem-estar', 'Produtos de Consumo', 'Cloud Computing', 'Outros', 'Mobile', 'Games', 'TIC e Telecom', 'Logística e Mobilidade Urbana', 'Desenvolvimento de Software', 'Hardware', 'Imobiliário', 'Biotecnologia', 'Finanças', 'Varejo / Atacado', 'Esportes', 'Comunicação e Mídia', 'Agronegócio', 'Serviços Profissionais', 'CRM', 'Nanotecnologia', 'Big Data', 'Pets', 'Construção Civil', 'Segurança e Defesa', 'Casa e Família', 'Entretenimento', 'Eventos e Turismo', 'Moda e Beleza', 'Recrutamento', 'Video'];
  var stacks = ['arroz', 'feijao', 'batata']
  
  
  $(document).ready(function() {
  
      autocomplete(document.getElementById("txt_estados"), estados);
      autocomplete(document.getElementById("txt_mercado"), mercados);
      autocomplete(document.getElementById("txt_stacks"), stacks);

      $('#add_estado').click(function() {
        teste = "<input type='button' id='e-selecionados' class='selecionados' value='"+$('#txt_estados').val()+"' />"
        if ($('#txt_estados').val() != "") {
          const index = estados.indexOf($('#txt_estados').val());
          if (index > -1) {
            estados.splice(index, 1);
          }
          $('#estado-selecionado').append(teste);
        }
        $('#txt_estados').val("");
        $('#txt_estados').focus();
      });
      $("#estado-selecionado").on('click','',  event =>{
        const clickedElement = $(event.target);
        console.log(clickedElement.attr('value'));
        $("#estado-selecionado").find('[value="'+clickedElement.attr('value')+'"]').remove();
        estados.push(clickedElement.attr('value'));
        estados.sort();
        autocomplete(document.getElementById("txt_estados"), estados);
      });
  
      $('#add_mercado').click(function() {
        teste = "<input type='button' id='m-selecionados' class='selecionados' value='"+$('#txt_mercado').val()+"' />"
        if ($('#txt_mercado').val() != "") {
          const index = estados.indexOf($('#txt_mercado').val());
          if (index > -1) {
            estados.splice(index, 1);
          }
          $('#mercado-selecionado').append(teste);
        }
          $('#mercado-selecionado').append(teste);
        $('#txt_mercado').val("");
        $('#txt_mercado').focus();
      });
      $("#mercado-selecionado").on('click','',  event =>{
        const clickedElement = $(event.target);
        console.log(clickedElement.attr('value'));
        $("#mercado-selecionado").find('[value="'+clickedElement.attr('value')+'"]').remove();
      });

      $('#add_stack').click(function () {
        teste = "<input type='button' id='s-selecionados' class='selecionados' value='" + $('#txt_stacks').val() + "' />"
        if ($('#txt_stacks').val() != "")
          $('#stack-selecionado').append(teste);
        $('#txt_stacks').val("");
        $('#txt_stacks').focus();
      });
      $("#stack-selecionado").on('click', '', event => {
        const clickedElement = $(event.target);
        console.log(clickedElement.attr('value'));
        $("#stack-selecionado").find('[value="' + clickedElement.attr('value') + '"]').remove();
      });
  
  
  })
  
  //var estado = '[{"value": 1, "text": "AC", "continent": "Task"}, {"value": 2, "text": "AL", "continent": "Task"}, {"value": 3, "text": "AM", "continent": "Task"}, {"value": 4, "text": "AP", "continent": "Task"}, {"value": 5, "text": "BA", "continent": "Task"}, {"value": 6, "text": "CE", "continent": "Task"}, {"value": 7, "text": "DF", "continent": "Task"}, {"value": 8, "text": "ES", "continent": "Task"}, {"value": 9, "text": "GO", "continent": "Task"}, {"value": 10, "text": "MA", "continent": "Task"}, {"value": 11, "text": "MG", "continent": "Task"}, {"value": 12, "text": "MS", "continent": "Task"}, {"value": 13, "text": "MT", "continent": "Task"}, {"value": 14, "text": "PA", "continent": "Task"}, {"value": 15, "text": "PB", "continent": "Task"}, {"value": 16, "text": "PE", "continent": "Task"}, {"value": 17, "text": "PI", "continent": "Task"}, {"value": 18, "text": "PR", "continent": "Task"}, {"value": 19, "text": "RJ", "continent": "Task"}, {"value": 20, "text": "RN", "continent": "Task"}, {"value": 21, "text": "RO", "continent": "Task"}, {"value": 22, "text": "RR", "continent": "Task"}, {"value": 23, "text": "RS", "continent": "Task"}, {"value": 24, "text": "SC", "continent": "Task"}, {"value": 25, "text": "SE", "continent": "Task"}, {"value": 26, "text": "SP", "continent": "Task"}, {"value": 27, "text": "TO", "continent": "Task"}]';
  
  function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
          /*check if the item starts with the same letters as the text field value:*/
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*create a DIV element for each matching element:*/
            b = document.createElement("DIV");
            b.setAttribute("class", "tag-items");
            /*make the matching letters bold:*/
            b.innerHTML = "<strong'>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            /*insert a input field that will hold the current array item's value:*/
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function(e) {
                /*insert the value for the autocomplete text field:*/
                inp.value = this.getElementsByTagName("input")[0].value;
                /*close the list of autocompleted values,
                (or any other open lists of autocompleted values:*/
                closeAllLists();
            });
            a.appendChild(b);
          }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
          /*If the arrow DOWN key is pressed,
          increase the currentFocus variable:*/
          currentFocus++;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 38) { //up
          /*If the arrow UP key is pressed,
          decrease the currentFocus variable:*/
          currentFocus--;
          /*and and make the current item more visible:*/
          addActive(x);
        } else if (e.keyCode == 13) {
          /*If the ENTER key is pressed, prevent the form from being submitted,*/
          e.preventDefault();
          if (currentFocus > -1) {
            /*and simulate a click on the "active" item:*/
            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {
      /*a function to classify an item as "active":*/
      if (!x) return false;
      /*start by removing the "active" class on all items:*/
      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      /*add class "autocomplete-active":*/
      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
      /*a function to remove the "active" class from all autocomplete items:*/
      for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      /*close all autocomplete lists in the document,
      except the one passed as an argument:*/
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
  }
  