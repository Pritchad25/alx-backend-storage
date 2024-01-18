--  SQL script that creates a view need_meeting that
-- lists all students that have a score under 80 (strict)
CREATE VIEW need_meeting AS

SELECT name FROM students
WHERE SCORE < 80 AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH))
