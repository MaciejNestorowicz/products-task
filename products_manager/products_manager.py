class ProductsManager:


    def __init__(self, mysql):
        self.mysql = mysql
        self.MIN_AMOUNT = 1
        self.MAX_AMOUNT = 10


    def get_products(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        cur.close()
        return rows, 200
    

    def add_products(self, name, amount):
        is_valid , message = self.validate_amount(amount)
        if not is_valid:
            return message, 400
        if self.product_exists(name):
            return self.increment_amount(name, amount), 200
        else:
            return self.add_product(name, amount), 201
            

    def order_products(self, name, amount):
        is_valid , message = self.validate_amount(amount)
        if not is_valid:
            return message, 400
        if self.product_exists(name):
            amount_in_stock = self.get_amount_in_stock(name)
            if amount_in_stock - amount < 0:
                return "not enough products in stock. There are " + str(amount) + " " + str(name) + " left.", 400
            return self.make_order(name, amount), 200
        else:
            return "product " + str(name) +" not found", 400


    def product_exists(self, name):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT 1 FROM products WHERE name = \"" + name + "\"")
        name = cur.fetchall()
        cur.close()
        if any(name):
            return True
        else:
            return False


    def get_amount_in_stock(self, name):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT amountInStock FROM products WHERE name = \"" + name + "\"")
        amount = cur.fetchall()
        cur.close()
        return amount[0][0]


    def validate_amount(self, amount):
        if amount < self.MIN_AMOUNT:
            return False, "amount has to be larger than 0"
        elif amount > self.MAX_AMOUNT:
            return False, "amount cannot be larger than 10"
        else:
            return True, "amount is valid"
    

    def add_product(self, name, amount):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO products(name, amountInStock) VALUES (%s, %s)", (name, amount))
        self.mysql.connection.commit()
        cur.close()
        return "product " + str(name) + " added"
        

    def increment_amount(self, name, amount):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE products SET amountInStock = amountInStock + " + str(amount) + " WHERE name = \"" + name + "\"")
        self.mysql.connection.commit()
        cur.close()
        return "amount of " + str(name) + " incremented by " + str(amount)


    def make_order(self, name, amount):
        conn = self.mysql.connection
        cur = conn.cursor()
        cur.execute("UPDATE products SET amountInStock = amountInStock - " + str(amount) + " WHERE name = \"" + name + "\"")
        conn.commit()
        cur.close()
        return "you have ordered " + str(amount) + " of " + str(name)