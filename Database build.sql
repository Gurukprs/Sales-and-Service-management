CREATE DATABASE dbms;
USE dbms;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(255),
    phno BIGINT,
    email VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE sales (
    sales_number INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    part VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE service (
    service_number INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    service VARCHAR(255),
    status VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE rating_comment (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE issues (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    issue_type VARCHAR(255),
    issue_description TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE log_table (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    operation VARCHAR(255),
    customer_id INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER after_customer_insert
AFTER INSERT ON customers
FOR EACH ROW
BEGIN
    INSERT INTO log_table (operation, customer_id) VALUES ('insertion', NEW.customer_id);
END;
//

CREATE TRIGGER after_customer_delete
AFTER DELETE ON customers
FOR EACH ROW
BEGIN
    INSERT INTO log_table (operation, customer_id) VALUES ('deletion', OLD.customer_id);
END;
//

CREATE TRIGGER after_service_update
AFTER UPDATE ON service
FOR EACH ROW
BEGIN
    IF OLD.status <> NEW.status THEN
        INSERT INTO log_table (operation, customer_id) VALUES ('update', NEW.customer_id);
    END IF;
END;
//
DELIMITER ;

CREATE VIEW customer_overview AS
SELECT 
    c.cust_name,
    sa.part AS sales,
    s.service,
    r.rating
FROM 
    customers c
LEFT JOIN 
    sales sa ON c.customer_id = sa.customer_id
LEFT JOIN 
    service s ON c.customer_id = s.customer_id
LEFT JOIN 
    rating_comment r ON c.customer_id = r.customer_id;