//This script fetches from and API using data from user input

$('document').ready(function () {
	const url = "https://hellosalut.stefanbohacek.dev/?";
	$('input#language_code').on('keydown', function(e) {
		if (e.which === 13 && $(this).is(':focus')) {
			$('input#btn_translate').click();
		}
	});
  	$('input#btn_translate').click(function () {
		const usr_input = $("input#language_code").val();
		$.get(url+"lang="+usr_input, function (data) {
			$('div#hello').html(data.hello);
    		});
  	});
});
