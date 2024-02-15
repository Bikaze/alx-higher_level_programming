-- This script lists all genres of the show 'Dexter'
SELECT name FROM tv_genres
JOIN tv_show_genres
ON id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
GROUP BY name
ORDER BY name;
