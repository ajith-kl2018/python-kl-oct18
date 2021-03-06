	
-- Create a Database
CREATE DATABASE BucketList;

--Use Database

use BucketList

--Create a Table
CREATE TABLE tbl_user (
  user_id INT NULL,
  user_name VARCHAR(45) NULL,
  user_username VARCHAR(45) NULL,
  user_password VARCHAR(45) NULL);

-- Create a Stored Procedure

 DELIMITER $$
CREATE DEFINER='root'@'%' PROCEDURE 'sp_createUser'(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     

        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;