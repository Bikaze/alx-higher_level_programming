$('document').ready(function () {
	const url = "https://hellosalut.stefanbohacek.dev/?";
  	$('input#btn_translate').click(function () {
		const usr_input = $("input#language_code").val();
		$.get(url+"lang="+usr_input, function (data) {
			$('div#hello').html(data.hello);
    		});
  	});
});
