CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE Forums (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT NOT NULL
);

CREATE TABLE Posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    user_id INTEGER NOT NULL REFERENCES Users(id)
        ON DELETE CASCADE,
    forum_id INTEGER NOT NULL REFERENCES Forums(id)
        ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    body TEXT NOT NULL,
    user_id INTEGER NOT NULL REFERENCES Users(id)
        ON DELETE CASCADE,
    post_id INTEGER NOT NULL REFERENCES Posts(id)
        ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE Likes_posts (
    user_id INTEGER NOT NULL REFERENCES Users(id)
        ON DELETE CASCADE,
    post_id INTEGER NOT NULL REFERENCES Posts(id)
        ON DELETE CASCADE,
    PRIMARY KEY (user_id, post_id)
);

CREATE TABLE Dislikes_posts (
    user_id INTEGER NOT NULL REFERENCES Users(id)
        ON DELETE CASCADE,
    post_id INTEGER NOT NULL REFERENCES Posts(id)
        ON DELETE CASCADE,
    PRIMARY KEY (user_id, post_id)
);

CREATE TABLE Likes_comments (
    user_id INTEGER NOT NULL REFERENCES Users(id)
        ON DELETE CASCADE,
    comment_id INTEGER NOT NULL REFERENCES Comments(id)
        ON DELETE CASCADE,
    PRIMARY KEY (user_id, comment_id)
);

CREATE TABLE Dislikes_comments (
    user_id INTEGER NOT NULL REFERENCES Users(id)
        ON DELETE CASCADE,
    comment_id INTEGER NOT NULL REFERENCES Comments(id)
        ON DELETE CASCADE,
    PRIMARY KEY (user_id, comment_id)
);

INSERT INTO Users 
    (username, password, is_admin)
    VALUES 
    ('admin', 'pbkdf2:sha256:260000$BgHbS7jwoH6b0rwV$c6b5d0ca8c3ee673de0395e3f2e9404ba2abb75297e4f01321378057bc967663', TRUE);

INSERT INTO Forums
    (name, description)
    VALUES
    ('General', 'General discussion about anything'),
    ('Programming', 'Programming related discussions'),
    ('Study', 'Study related discussions');
