CREATE TABLE LOG (
  user_id TEXT REFERENCES USERS(user_id),
  time DATETIME,
  bet FLOAT,
  win FLOAT
);

CREATE TABLE USERS (
  user_id TEXT,
  email TEXT,
  geo TEXT
);