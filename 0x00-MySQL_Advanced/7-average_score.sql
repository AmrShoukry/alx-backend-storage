-- 7. Average score

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE average INT;
  SET average = (SELECT AVG(score) FROM corrections AS av WHERE av.user_id = user_id);
  UPDATE users SET average_score = average WHERE id = user_id;
END $$
DELIMITER ;
