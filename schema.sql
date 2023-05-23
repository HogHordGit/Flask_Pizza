drop table if exists prom;

CREATE TABLE prom (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

drop table if exists pizza;
CREATE TABLE pizza (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

drop table if exists sushi;
CREATE TABLE sushi (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

drop table if exists drink;
CREATE TABLE drink (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

drop table if exists snacks;
CREATE TABLE snacks (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

drop table if exists combo;
CREATE TABLE combo (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

drop table if exists dessert;
CREATE TABLE dessert (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

drop table if exists souces;
CREATE TABLE souces (
    id serial primary key not null,
    image_link VARCHAR(255),
    dish_name VARCHAR(255),
    dish_description TEXT,
    price INT,
    ingredients TEXT,
    toppings TEXT
);

