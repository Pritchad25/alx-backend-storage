-- Ranks the longevity of Glam Rock bands
-- The column names must be: band_name and lifespan (in years)
SELECT
band_name, ifnull(split, 2022)-ifnull(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
