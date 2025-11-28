CREATE DATABASE Datatypes;
USE Datatypes;
CREATE TABLE python_datatypes (
    SNo INT PRIMARY KEY,
    DataType VARCHAR(50),
    Representation VARCHAR(255),
    Description TEXT
);

INSERT INTO python_datatypes (SNo, DataType, Representation, Description) VALUES
(1, 'int', '10, -5, 1000', 'Represents whole numbers without decimals'),
(2, 'float', '10.5, -2.3, 3.14', 'Represents real numbers with decimals'),
(3, 'str', '"Hello", ''123''', 'Represents text or sequence of characters'),
(4, 'bool', 'True, False', 'Represents Boolean values (logical)'),
(5, 'list', '[1, 2, 3], ["a", "b"]', 'Ordered, mutable collection of items'),
(6, 'tuple', '(1, 2, 3), ("a", "b")', 'Ordered, immutable collection of items'),
(7, 'set', '{1, 2, 3}', 'Unordered collection of unique elements'),
(8, 'dict', '{"name": "Alpha", "age": 17}', 'Key-value pairs for mapping data');
