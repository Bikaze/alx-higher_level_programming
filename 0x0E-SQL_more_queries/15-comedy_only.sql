-- This script lists all comedy shows
SELECT s.title FROM tv_shows s, tv_show_genres t, tv_genres g
WHERE s.id = t.show_id
AND t.genre_id = g.id
AND g.name = 'Comedy'
ORDER BY s.title;
