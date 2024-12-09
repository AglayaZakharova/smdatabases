DELETE FROM LOG WHERE time IS NULL OR user_id = '#error' is NULL OR user_id;
UPDATE LOG SET user_id = replace(user_id, 'Запись пользов № - ', ''), time = replace(time, '[', '');

DELETE FROM USERS WHERE email is NULL OR email NOT LIKE "%@%.%" OR user_id NOT GLOB 'User_[0-9]?[0-9]*';
UPDATE USERS SET user_id = replace(user_id, 'U', 'u');