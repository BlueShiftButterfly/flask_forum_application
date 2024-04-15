CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    username TEXT,
    password_hash TEXT,
    created_at INT,
    is_authenticated BOOLEAN,
    is_active BOOLEAN
);

CREATE TABLE forums (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    url_name TEXT,
    display_name TEXT,
    forum_description TEXT,
    created_at INT,
    creator_id INTEGER REFERENCES users (id)
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    title TEXT,
    content TEXT,
    poster_id INTEGER REFERENCES users (id),
    forum_id INTEGER REFERENCES forums (id),
    created_at INT,
    last_edited_at INT
);
