//This script toggles the text color of the <header> element between red and green

$("div#toggle_header").click(function() {
	$("header").toggleClass("red green");
});
