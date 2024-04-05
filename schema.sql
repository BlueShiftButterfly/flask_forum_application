CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    username TEXT,
    password_hash TEXT,
    created BIGINT,
    is_authenticated BOOLEAN,
    is_active BOOLEAN
);
