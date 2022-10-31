# TODO

# 1. get total sales for all years using invoice table
# you will want to use SUBSTR to get the year from the invoice date
# you will want to use SUM to get the total sales for each year


SELECT InvoiceId,
	SUBSTRING(InvoiceDate, 1, 4) as Year,
	sum(total) as Total_sales
FROM invoices i 
group by Year

# 2. get total sales for each country - use invoice table
# you will also need to join with the customer table - those have country info

SELECT country,
	sum(total) as Total_sales
FROM invoices i 
JOIN customers c 
group by c.country

# 3. a count tracks in each playlist - use playlist_track table

SELECT PlaylistId,
	sum(TrackId) as Total_tracks
FROM playlist_track  
group by PlaylistId

# 3. b extra challenge get total track lenght in minutes for each playlist
# you will need to join with the track table

SELECT a.PlaylistId,
	sum(a.TrackId) as Total_tracks,
	sum(b.Milliseconds)/(1000*60) as Total_min
FROM playlist_track a
JOIN tracks b
ON a.TrackId = b.TrackId 
group by PlaylistId

# 3. c cherry on top - provide names of these playlists
# so you will want to join with the playlist table as well


SELECT p.Name,
	sum(a.TrackId) as Total_tracks,
	sum(b.Milliseconds)/(1000*60) as Total_min
FROM playlist_track a
JOIN playlists  p ON a.PlaylistId  = p.PlaylistId
JOIN tracks b ON a.TrackId = b.TrackId 
group by a.PlaylistId

