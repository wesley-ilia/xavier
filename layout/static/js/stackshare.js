$(document).ready(function() {
    $('#back').click(function()
		{
      window.location.assign("/");
    });
    $('#execute').click(function()
		{
      alert($('#tecnologia').val())
      window.location.assign("get_by_language/"+$('#tecnologia').val());
    });
})