-- Lists all shows contained in 'hbtn_0d_tvshows'

SELECT tv_shows.title, tv_show_genres.genre_id
-- Select the table which the linking will be based on
FROM tv_show_genres
-- Use inner join to list all data
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
-- Order in ascending order by title and genre_id in
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
