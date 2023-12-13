-- 13. Average weighted score for all!

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users, (
    SELECT users.id AS id, SUM(projects.weight * users.average_score) / SUM(projects.weight) AS overall FROM corrections
    INNER JOIN users ON corrections.user_id = users.id
    INNER JOIN projects ON corrections.project_id = projects.id
    GROUP BY users.id) AS calculated
  SET users.average_score = calculated.overall WHERE users.id = calculated.id;
END $$
DELIMITER ;