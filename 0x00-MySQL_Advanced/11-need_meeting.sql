-- 11. No table for a meeting

CREATE VIEW need_meeting AS SELECT name FROM students WHERE score < 80;
