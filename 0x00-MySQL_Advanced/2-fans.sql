-- Ranks the country origins of bands ordered
-- by the number of (non-unique) fans
-- The column names must be: origin and nb_fans
SELECT
origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
