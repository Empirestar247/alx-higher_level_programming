-- Script: Create MySQL User user_0d_1
-- Description: This script creates a MySQL user with all privileges, named user_0d_1.

-- Check if the user already exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_1';

-- Create the user if it doesn't exist
SET @sql = IF(@user_exists = 0,
    'CREATE USER "user_0d_1" IDENTIFIED BY "user_0d_1_pwd";',
    'SELECT "User user_0d_1 already exists";'
);

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO "user_0d_1";

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- End of script
