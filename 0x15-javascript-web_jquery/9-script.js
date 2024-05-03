//This script uses jquery to fetch data from a url

$(document).ready(function() {
	$.get("https://hellosalut.stefanbohacek.dev/?lang=fr",
      		function (data) {
			$("div#hello").text(data.hello);
      		}
	);
});
