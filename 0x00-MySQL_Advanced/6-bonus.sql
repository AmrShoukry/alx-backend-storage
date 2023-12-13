-- 6. Add bonus

DELIMITER $$
CREATE PROCEDURE AddBonus(
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
BEGIN
  DECLARE proj_id INT;
  IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
    INSERT INTO projects (name) VALUES (project_name);
  END IF;
  SELECT id INTO proj_id FROM projects WHERE name = project_name LIMIT 1;
  INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, proj_id, score);
END $$

DELIMITER ;
