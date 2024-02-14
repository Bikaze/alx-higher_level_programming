-- This script lists all shows contained in 'hbtn_0d_tvshows' that have at least one genre linked
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres
ON id = tv_show_genres.show_id
ORDER BY title, tv_show_genres.genre_id;
