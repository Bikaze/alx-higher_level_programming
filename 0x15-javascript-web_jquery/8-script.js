//This script uses jquery to fetch data from a url

$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
      function (data) {
	$.each(data.results, function (i, item) {
		$("ul#list_movies").append("<li>"+item.title+"</li>");
      });
});
