$(document).ready(function() {
    $('#back').click(function()
		{
      window.location.assign("/");
    });
    $('#execute').click(function()
		{
      alert("ff");
      /* alert($('#tecnologia').val()) */
      window.location.assign("get_by_language?search="+$('#tecnologia').val()+"&obs="+$('#obs').val()+"&output_name="+$('#output_name').val());
    });
})