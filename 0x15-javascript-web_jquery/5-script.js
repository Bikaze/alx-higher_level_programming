//This script appends a new <li> element to a div#add_item selected element

$("div#add_item").click(function() {
	$("ul.my_list").append("<li>Item</li>");
});
