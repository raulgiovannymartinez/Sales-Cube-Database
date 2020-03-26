# Description
"""
Generate data for the sales cube database and commit data directly to PostgreSQL
"""

# import libraries
import random
import string
import psycopg2

#################################### Options and Functions ####################################

# define number of tuples for each table
numStates = 150
numCategories = 60000
numProducts = 90000
numCustomers = 120000
numSales = 30000

# connect to the db
con = psycopg2.connect("host = localhost dbname=SalesCube user=xxxx password = xxxx")

# Cursor
cur =  con.cursor()


# define functions
def randomString(stringLength = 5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength)).lower().capitalize()


#################################### Generate SQL Commands ####################################

# states table
print('Generating States')

states = dict()
while len(states) != numStates:
    states[len(states)] = randomString()    

for idx, state in enumerate(states.keys()):
    cur.execute('INSERT INTO states (state_id, name) VALUES(' + str(idx+1) + ', \'' + states[state] + '\'' + ');\n')
    
# categories table
print('Generating Categories')

categories = dict()
while len(categories) != numCategories:
    categories[len(categories)] = (randomString(),randomString(50))

for idx, category in enumerate(categories.keys()):
    cur.execute('INSERT INTO categories (category_id, name, description) VALUES (' + str(idx+1) + ', \'' + categories[category][0] + '\'' + ', \'' + categories[category][1] + '\''+ ');\n')

# products table
print('Generating Products')

products = dict()
while len(products) != numProducts:
    products[len(products)] = (randomString(),random.choice(list(categories))+1,random.randint(100,1000))
    

for idx, product in enumerate(products.keys()):
    cur.execute('INSERT INTO products (product_id, name, list_price, category_id) VALUES (' + str(idx+1) + ', \'' + products[product][0] + '\'' + ',' + str(products[product][2]) + ',' + str(products[product][1]) + ');\n')

# customers table
print('Generating Customers')

customers = dict()
while len(customers) != numCustomers:
    customers[len(customers)] = (randomString(random.randint(5,10)), random.choice(list(states))+1)
    
for idx, customer in enumerate(customers):
    cur.execute('INSERT INTO customers (customer_id, first_name, last_name, state_id) VALUES (' + str(idx+1) + ', \'' + customers[customer][0] + '\'' + ', \''+ customers[customer][0] + '\',' + str(customers[customer][1]) + ');\n')


# sales table
print('Generating Sales')

for idx, i in enumerate(range(numSales)):
    pid = random.choice(list(products))
    price = products[pid][2]
    cur.execute('INSERT INTO sales (sale_id, quantity, price_paid, discount, customer_id, product_id) VALUES (' + str(idx+1)  + ','+str(random.randint(1,10))  + ','+ str(random.randint(int(price/2),price)) + ',0,' + str(random.choice(list(customers))+1) + ',' + str(pid+1) + ');\n')


con.commit()

# Close the connection
con.close()

