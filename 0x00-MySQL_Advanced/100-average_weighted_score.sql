-- 12. Average weighted score
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE average FLOAT;

  SET average = (
    SELECT COALESCE(SUM(projects.weight * corrections.score) / NULLIF(SUM(projects.weight), 0), 0)
    FROM corrections 
    INNER JOIN users ON corrections.user_id = users.id
    INNER JOIN projects ON corrections.project_id = projects.id  
    WHERE users.id = user_id
  );

  UPDATE users SET average_score = average WHERE id = user_id;
END $$
DELIMITER ;
