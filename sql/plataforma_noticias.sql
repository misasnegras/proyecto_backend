CREATE DATABASE IF NOT EXISTS plataforma_noticias_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'noticias_user'@'localhost'
    IDENTIFIED BY 'Noticias2026!';

GRANT ALL PRIVILEGES ON plataforma_noticias_db.*
    TO 'noticias_user'@'localhost';

FLUSH PRIVILEGES;