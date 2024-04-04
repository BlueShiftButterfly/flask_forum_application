CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    username TEXT,
    passwordhash TEXT,
    created INT
);
