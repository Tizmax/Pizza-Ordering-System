-- Create Ingredients table
CREATE TABLE Ingredients (
    ID int PRIMARY KEY AUTO_INCREMENT,
    Name varchar(20),
    PriceS float,
    PriceM float,
    PriceL float
);

-- Create Pizzas table
CREATE TABLE Pizzas (
    ID int PRIMARY KEY AUTO_INCREMENT,
    Name varchar(20),
    PriceS float,
    PriceM float,
    PriceL float
);

-- Create PizzaIngredient table
CREATE TABLE PizzaIngredient (
    ID int PRIMARY KEY AUTO_INCREMENT,
    PizzaID int,
    IngredientID int,
    FOREIGN KEY (PizzaID) REFERENCES Pizzas(ID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(ID)
);

-- Create Orders table
CREATE TABLE Orders (
    ID int PRIMARY KEY AUTO_INCREMENT,
    ClientName varchar(20),
    Date datetime,
    Price float
);

-- Create Items table
CREATE TABLE Items (
    ID int PRIMARY KEY AUTO_INCREMENT,
    OrderID int,
    PizzaID int,
    HalfPizzaID int NULL,
    Size enum('S', 'M', 'L'),
    Price float,
    FOREIGN KEY (OrderID) REFERENCES Orders(ID),
    FOREIGN KEY (PizzaID) REFERENCES Pizzas(ID),
    FOREIGN KEY (HalfPizzaID) REFERENCES Pizzas(ID)
);

-- Create Supplements table
CREATE TABLE Supplements (
    ID int PRIMARY KEY AUTO_INCREMENT,
    ItemID int,
    IngredientID int,
    Half enum('Whole', 'Half1', 'Half2'),
    FOREIGN KEY (ItemID) REFERENCES Items(ID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(ID)
);

-- Insert data into Ingredients table
INSERT INTO Ingredients (Name, PriceS, PriceM, PriceL) VALUES
('Cheese', 1.0, 1.5, 2.0),
('Pepperoni', 1.5, 2.0, 2.5),
('Mushrooms', 1.0, 1.5, 2.0);

-- Insert data into Pizzas table
INSERT INTO Pizzas (Name, PriceS, PriceM, PriceL) VALUES
('Margherita', 8.0, 10.0, 12.0),
('Pepperoni', 9.0, 11.0, 13.0),
('Mushroom Delight', 8.5, 10.5, 12.5);

-- Insert data into Orders table
INSERT INTO Orders (ClientName, Date, Price) VALUES
('John Doe', '2024-08-20 12:30:00', 25.0),
('Jane Smith', '2024-08-20 13:00:00', 28.5);

-- Insert data into Items table (Regular Pizza)
INSERT INTO Items (OrderID, PizzaID, Size, Price) VALUES
(1, 1, 'M', 10.0);  -- John Doe ordered a Medium Margherita

-- Insert data into Items table (Composed Pizza)
INSERT INTO Items (OrderID, PizzaID, HalfPizzaID, Size, Price) VALUES
(2, 1, 2, 'L', 12.5 + 13.0);  -- Jane Smith ordered a Large Half Margherita, Half Pepperoni

-- Insert data into Supplements table (for a regular pizza)
INSERT INTO Supplements (ItemID, IngredientID, Half) VALUES
(1, 3, 'Whole');  -- John Doe added Mushrooms to his Medium Margherita

-- Insert data into Supplements table (for a composed pizza)
INSERT INTO Supplements (ItemID, IngredientID, Half) VALUES
(2, 3, 'Half1');  -- Jane Smith added Mushrooms to Half Margherita
INSERT INTO Supplements (ItemID, IngredientID, Half) VALUES
(2, 2, 'Half2');  -- Jane Smith added Pepperoni to Half Pepperoni
