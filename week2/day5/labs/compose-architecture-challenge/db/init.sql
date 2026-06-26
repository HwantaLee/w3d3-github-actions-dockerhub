CREATE ROLE web_anon NOLOGIN;

CREATE TABLE users (
    id serial PRIMARY KEY,
    name text
);

INSERT INTO users(name)
VALUES
('kim'),
('lee');

GRANT SELECT ON users TO web_anon;