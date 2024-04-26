CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    username TEXT,
    password_hash TEXT,
    created_at INT,
    is_authenticated BOOLEAN,
    is_active BOOLEAN,
    role_id INT
);

CREATE TABLE forums (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    url_name TEXT,
    display_name TEXT,
    forum_description TEXT,
    created_at INT,
    creator_id INTEGER REFERENCES users (id),
    is_invite_only BOOLEAN
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

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    uuid TEXT,
    content TEXT,
    poster_id INTEGER REFERENCES users,
    thread_id INTEGER REFERENCES threads,
    is_reply BOOLEAN,
    reply_comment_id INT,
    created_at INT,
    last_edited_at INT
);

CREATE TABLE private_forum_access (
    id SERIAL PRIMARY KEY,
    forum_id INTEGER REFERENCES forums,
    user_id INTEGER REFERENCES users,
    has_access BOOLEAN
);
