CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    username TEXT,
    password_hash TEXT,
    created INT,
    is_authenticated BOOLEAN,
    is_active BOOLEAN
);

CREATE TABLE forums (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    url_name TEXT,
    display_name TEXT,
    created INT
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    title TEXT,
    content TEXT,
    poster_uuid TEXT,
    forum_uuid TEXT,
    created INT
);
