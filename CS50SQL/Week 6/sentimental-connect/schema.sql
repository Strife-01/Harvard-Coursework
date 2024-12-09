CREATE DATABASE `linkedin`;
USE `linkedin`;

CREATE TABLE IF NOT EXISTS `users` (
    `id` UNSIGNED INT AUTO_INCREMENT,
    `firstname` VARCHAR(32) NOT NULL,
    `lastname` VARCHAR(32) NOT NULL,
    `username` VARCHAR(255) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
); -- when inserting, hash the passwords

CREATE TABLE IF NOT EXISTS `schools_and_universities` (
    `id` UNSIGNED INT AUTO_INCREMENT,
    `name` VARCHAR(500) NOT NULL,
    `type` ENUM('Primary' ,'Secondary', 'Higher Education') NOT NULL,
    `location` TEXT NOT NULL,
    `founding_year` YEAR NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `companies` (
    `id` UNSIGNED INT AUTO_INCREMENT,
    `name` VARCHAR(500) NOT NULL,
    `industry` ENUM('Technology' ,'Education', 'Business') NOT NULL,
    `location` TEXT NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `connections_people` (
    `id` UNSIGNED INT AUTO_INCREMENT,
    `user_following` UNSIGNED INT NOT NULL,
    `user_followed` UNSIGNED INT NOT NULL,
    FOREIGN KEY(`user_following`) REFERENCES `users`(`id`),
    FOREIGN KEY(`user_followed`) REFERENCES `users`(`id`),
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `connections_schools` (
    `id` UNSIGNED INT AUTO_INCREMENT,
    `user_id` UNSIGNED INT NOT NULL,
    `school_id` UNSIGNED INT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `type_degree` ENUM('BA', 'MA', 'PhD'),
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `schools_and_universities`(`id`),
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `connections_companies` (
    `id` UNSIGNED INT AUTO_INCREMENT,
    `user_id` UNSIGNED INT NOT NULL,
    `companie_id` UNSIGNED INT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`companie_id`) REFERENCES `companies`(`id`),
    PRIMARY KEY(`id`)
);


