SET @@global.sql_mode= 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DROP DATABASE IF EXISTS webdb;
CREATE DATABASE IF NOT EXISTS webdb;
USE webdb;

-- DB Creation
	-- tblUserInformation
    -- tblUserProgress
    -- tblUserComments
    -- tblCompQuestions
    -- tblCompQuestionAns
    -- tblUserCompAnswers

DROP PROCEDURE IF EXISTS makeWebDB;
DELIMITER //
CREATE DEFINER = 'root'@'localhost' PROCEDURE makeWebDB()
BEGIN
	DROP TABLE IF EXISTS tblUserInformation;
	CREATE TABLE IF NOT EXISTS tblUserInformation(
		_userID BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		_userName VARCHAR(100) NOT NULL,
    _userFirstName VARCHAR(50),
		_userLastName VARCHAR(50),
		_userEmail VARCHAR(50) NOT NULL,
		_userPassword VARCHAR(50) NOT NULL,
		_userDOB DATE,
		_userPhone VARCHAR(15),
		_userType VARCHAR(50),
		_userOrganization VARCHAR(255),
        _userJoinDate DATETIME
	) ENGINE = INNODB;

	DROP TABLE IF EXISTS tblUserProgress;
	CREATE TABLE IF NOT EXISTS tblUserProgress(
		_userProgressID BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		_userID BIGINT,
		CONSTRAINT fk_userID FOREIGN KEY (_userID)
			REFERENCES tblUserInformation(_userID)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		_userProgressType VARCHAR(50),
		_userProgressStartDate DATETIME,
		_userProgressCompletionDate DATETIME
	) ENGINE = INNODB;

	DROP TABLE IF EXISTS tblUserComments;
	CREATE TABLE IF NOT EXISTS tblUserComments(
		_userCommentID BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		_userResponseID BIGINT,
		_userInfoID BIGINT,
		CONSTRAINT fk_userInfoID FOREIGN KEY (_userInfoID)
			REFERENCES tblUserInformation(_userID)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		_userComment VARCHAR(255),
		_tutorialPage BIGINT,
		_tutorialTopic VARCHAR(50),
		_modStatus BOOLEAN
	) ENGINE = INNODB;

	DROP TABLE IF EXISTS tblCompQuestions;
	CREATE TABLE IF NOT EXISTS tblCompQuestions(
		_questionID BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		_questionText VARCHAR(100)
	) ENGINE = INNODB;

	DROP TABLE IF EXISTS tblCompQuestionAns;
	CREATE TABLE IF NOT EXISTS tblCompQuestionAns(
		_competitionQuestionAnsID BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		_questionID BIGINT,
		CONSTRAINT fk_qID FOREIGN KEY (_questionID)
			REFERENCES tblCompQuestions(_questionID)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		_questionAnswer1 VARCHAR(100),
    _questionAnswer2 VARCHAR(100),
    _questionAnswer3 VARCHAR(100),
		_questionCorrectAns VARCHAR(100)
	) ENGINE = INNODB;

	DROP TABLE IF EXISTS tblUserCompAnswers;
	CREATE TABLE IF NOT EXISTS tblUserCompAnswers(
		_userAnsID BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
		_userID BIGINT,
		CONSTRAINT fk_uID FOREIGN KEY (_userID)
			REFERENCES tblUserInformation(_userID)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		_questionID BIGINT,
		CONSTRAINT fk_questionID FOREIGN KEY (_questionID)
			REFERENCES tblCompQuestions(_questionID)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		_competitionQuestionAnsID BIGINT,
		CONSTRAINT fk_compQID FOREIGN KEY (_competitionQuestionAnsID)
			REFERENCES tblCompQuestionAns(_competitionQuestionAnsID)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		_userQuestion1Ans VARCHAR(100),
        _userQuestion2Ans VARCHAR(100),
        _userQuestion3Ans VARCHAR(100),
		_userClassName VARCHAR(50),
		_userSchoolName VARCHAR(75),
		_userSchoolEmail VARCHAR(50),
		_userSchoolPhone VARCHAR(25)
	) ENGINE = INNODB;
END //
DELIMITER ;
CALL makeWebDB();
