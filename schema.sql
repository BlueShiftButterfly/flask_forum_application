CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    username TEXT,
    password_hash TEXT,
    created BIGINT,
    is_authenticated BOOLEAN,
    is_active BOOLEAN
);

CREATE TABLE forums (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    url_name TEXT,
    display_name TEXT,
    created BIGINT
);
