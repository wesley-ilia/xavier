$(document).ready(function () {
    alert("tsts");
    $('#back').click(function()
		{
      window.location.assign("/");
    });
    $('#execute').click(function()
		{
      alert("execute");
    alert($('#sim').prop("checked"));
    window.location.assign("insert_into_log?comment="+$('#comentario').val()+"&feedback="+$('#sim').prop("checked")+"&obs="+$('#obs').val());
    });
})