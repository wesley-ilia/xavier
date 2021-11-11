$(document).ready(function() {

  $('#back').click(function()
  {
    window.location.assign("/");
  });
  $('#execute').click(function()
  {
    alert("executa4");
    saida = [];
    var markedCheckbox = document.getElementsByName('mercado');
    for (var checkbox of markedCheckbox) {
      if (checkbox.checked)
        saida.push(checkbox.value);
    }
    if (Array.isArray(saida) && saida.length) {
      alert(saida);
    }
    window.location.assign("start_up_base/?state_name="+$('#state_name').val()+"&obs="+$('#obs').val()+"&output_name="+$('#output_name').val()+"&mercado="+saida);
  });
})
