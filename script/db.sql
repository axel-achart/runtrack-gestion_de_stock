-- Create Database, tables (insertion products and categories)

CREATE DATABASE store;
USE store;

CREATE TABLE product(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), description TEXT, price INT, quantity INT, id_category INT);
CREATE TABLE category(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));

INSERT INTO category(name)
    -> VALUES("hygiene");
INSERT INTO category(name)
    -> VALUES("alimentaire");
INSERT INTO category(name)
    -> VALUES("vetement");

INSERT INTO product(name, description, price, quantity, id_category)
    -> VALUES("Savon de Marseille", "Savon traditionnel", "5", "20", "1");
INSERT INTO product(name, description, price, quantity, id_category)
    -> VALUES("Shampoing", "Soin 4 en 1 cheveux", "8", "20", "1");
INSERT INTO product(name, description, price, quantity, id_category)
    -> VALUES("Serviette", "Protège la peau, agréable et durable", "10", "20", "1");
INSERT INTO product(name, description, price, quantity, id_category)
    -> VALUES("Soda", "Coca bien frais chakal", "2", "20", "2");
INSERT INTO product(name, description, price, quantity, id_category)
    -> VALUES("Couscous", "Saveur orientale", "15", "20", "2");
INSERT INTO product(name, description, price, quantity, id_category)
    -> VALUES("Jogging", "Sport, confort, fais pour tout le monde", "55", "20", "3");
INSERT INTO product(name, description, price, quantity, id_category)
    -> VALUES("Cagoule", "Discret, furtif et léger, prêt poru un braco", "10", "20", "3");
