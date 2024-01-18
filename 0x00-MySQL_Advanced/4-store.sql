-- Script creates a trigger to decrease quantity
-- when order of an item is added
CREATE TRIGGER
reduce_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
