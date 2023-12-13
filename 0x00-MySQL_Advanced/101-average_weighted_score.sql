-- 13. Average weighted score for all!

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users INNER JOIN (
    SELECT users.id as id, SUM(projects.weight * corrections.score) / SUM(projects.weight) AS overall FROM corrections
    INNER JOIN users ON corrections.user_id = users.id
    INNER JOIN projects ON corrections.project_id = projects.id
    GROUP BY users.id) AS calculated ON calculated.id = users.id
  SET users.average_score = calculated.overall;
END $$
DELIMITER ;