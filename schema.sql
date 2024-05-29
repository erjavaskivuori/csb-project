CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    role TEXT
);
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    message TEXT
);