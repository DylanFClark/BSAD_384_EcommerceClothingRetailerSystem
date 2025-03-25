# DATA CREATION SCRIPTs #

import datetime
import random
import pandas as pd
import numpy as np

#--------------------------------------------
# SUPPLIER GEN SCRIPT # 
#--------------------------------------------
'''
CREATE TABLE suppliers(
id INT NOT NULL,
company VARCHAR(255) UNIQUE NOT NULL,
acct_created DATETIME  NOT NULL,
PRIMARY KEY (id)
);
'''
def supplier_gen():
    # Setting random seed for consistency
    np.random.seed(42)

    #Data
    companies = [
        "Fashion Forward Ltd",
        "Urban Styles Inc",
        "Elite Wear Co",
        "Trendsetters Hub",
        "Modish Apparel",
        "Chic Couture",
        "Vogue Essentials",
        "Runway Ready",
        "Streetwear Kings",
        "Casual Comforts",
        "Luxury Threads",
        "Denim Dynasty",
        "ActiveWear Pros",
        "Formal Finesse",
        "Boho Chic Creations"
    ]
    acct_created = [
        "2022-01-31 00:00:00",
        "2022-02-28 00:00:00",
        "2022-03-31 00:00:00",
        "2022-04-30 00:00:00",
        "2022-05-31 00:00:00",
        "2022-06-30 00:00:00",
        "2022-07-31 00:00:00",
        "2022-08-31 00:00:00",
        "2022-09-30 00:00:00",
        "2022-10-31 00:00:00",
        "2022-11-30 00:00:00",
        "2022-12-31 00:00:00",
        "2023-01-31 00:00:00",
        "2023-02-28 00:00:00",
        "2023-03-31 00:00:00"
    ]

    # Generate 
    supplier_data = []

    for supplier_id in range(15):
        supplier_data.append([
        supplier_id,
        companies[supplier_id],
        acct_created[supplier_id]
        ])

    # Save to CSV
    rep_df = pd.DataFrame(supplier_data, columns=["id", "company", "acct_created"])

    rep_df.to_csv("supplier_data.csv", index=False)

    print("CSV created: ")



#--------------------------------------------
# SUPPLIER REPS SCRIPT
#--------------------------------------------

'''
CREATE TABLE supplier_reps(
id INT NOT NULL,
fname VARCHAR(255) NOT NULL,
lname VARCHAR(255) NOT NULL,
start_date DATETIME NOT NULL,
phone VARCHAR(255) NOT NULL,
email VARCHAR(255) UNIQUE NOT NULL,
supplier_id INT NOT NULL,

PRIMARY KEY (id),
FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);
'''
def supplier_rep_gen():
    # Get Foreign Key Data
    supplier_data = pd.read_csv("supplier_data.csv")

    # Setting random seed for consistency
    np.random.seed(42)

    # Generate number of reps per supplier using normal distribution
    num_reps = np.round(np.random.normal(loc=3, scale=1.5, size=len(supplier_data))).astype(int)
    num_reps = np.clip(num_reps, 1, None)  # Ensure at least 1 rep per supplier

    # Generate supplier reps
    supplier_rep_data = []
    rep_id = 1

    for supplier_id, reps in zip(supplier_data["id"], num_reps):
        for _ in range(reps):
            supplier_rep_data.append([
                rep_id,
                #fname
                np.random.choice(["John", "Jane", "Alex", "Sam", "Taylor", "Chris", "Jordan", "Morgan", "Pat", "Jamie", "John", "Jane", "Alex", "Sam", "Taylor", "Chris", "Jordan", "Morgan", "Pat", "Jamie",  "Ryan", "Casey", "Cameron", "Avery", "Drew", "Riley", "Charlie", "Sydney", "Logan", "Emerson" ]),
                #lname
                np.random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez",  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin" ]),
                # start date
                np.random.choice(["2022-01-01", "2022-04-01", "2022-07-01", "2022-10-01","2023-01-01", "2023-04-01", "2023-07-01", "2023-10-01", "2024-01-01", "2024-04-01", "2024-07-01", "2024-10-01"]),
                #phone number
                f"+1-{np.random.randint(200, 999)}-{np.random.randint(100, 999)}-{np.random.randint(1000, 9999)}",
                #email
                f"rep{rep_id}@{supplier_data.loc[supplier_data["id"] == supplier_id, 'company'].values[0].replace(' ', '').lower()}.com",
                supplier_id
            ])
            rep_id += 1

    # Save to CSV
    rep_df = pd.DataFrame(supplier_rep_data, columns=["id", "fname", "lname", "start_date", "phone", "email", "supplier_id"])
    rep_df.to_csv("supplier_rep_data.csv", index=False)

    print("CSV created:")

#--------------------------------------------
# PRODUCT GEN SCRIPT
#--------------------------------------------

'''
CREATE TABLE products (
id INT NOT NULL,
name VARCHAR(255) UNIQUE,
list_date DATETIME,
description VARCHAR(255) UNIQUE,
rep_id INT NOT NULL,

PRIMARY KEY (id),
FOREIGN KEY (rep_id) REFERENCES supplier_reps(id)
);
'''
def product_gen():
    # Get Foreign Key Data
    supplier_rep_data = pd.read_csv("supplier_rep_data.csv")

    # Setting random seed for consistency
    np.random.seed(42)

    # Generate number of reps per supplier using normal distribution
    num_products = np.round(np.random.normal(loc=2, scale=3, size=len(supplier_rep_data))).astype(int)
    num_products = np.clip(num_products, 1, None)  # Ensure at least 1 product per supplier

    # Generate supplier reps
    product_data = []
    product_id = 1

    product_names = ["Classic Crewneck T-Shirt", "Slim Fit V-Neck Tee", "Relaxed Cotton T-Shirt", "Graphic Print Tee", "Vintage Wash T-Shirt",  
    "Performance Active Tee", "Soft Touch Polo Shirt", "Striped Cotton Polo", "Linen Blend Short Sleeve Shirt", "Denim Button-Up Shirt",  
    "Classic Oxford Shirt", "Flannel Plaid Shirt", "Lightweight Chambray Shirt", "Moisture-Wicking Polo", "Fitted Henley Shirt",  
    "Casual Everyday Hoodie", "Zip-Up Sports Hoodie", "Premium Knit Hoodie", "Ultra-Soft Lounge Hoodie", "Fleece Lined Hoodie",  
    "Classic Straight Leg Jeans", "Slim Fit Denim Jeans", "Relaxed Fit Cargo Pants", "Tapered Chino Pants", "Stretch Cotton Joggers",  
    "Lightweight Linen Pants", "Athletic Fit Track Pants", "Corduroy Straight Pants", "High-Waisted Trousers", "Wide Leg Dress Pants",  
    "Cozy Flannel Pajama Set", "Classic Cotton Pajama Pants", "Silky Soft Sleepwear Set", "Thermal Long Sleeve Pajamas", "Relaxed Fit Sleep Shorts",  
    "Fleece-Lined Winter Pajamas", "Breathable Bamboo Sleepwear", "Plaid Button-Up Pajama Set", "Ultra-Light Pajama Set", "Hooded Lounge Set",  
    "Classic Boxer Briefs", "Seamless Stretch Briefs", "Breathable Cotton Briefs", "Moisture-Wicking Boxer Shorts", "Ultra-Soft Modal Trunks",  
    "Classic White Undershirt", "Performance Compression Shorts", "No-Show Trunks", "Sport Fit Boxer Briefs", "Tagless Comfort Underwear",  
    "Ribbed Cotton Tank Top", "Athletic Compression Tank", "Casual Sleeveless Tee", "Fitted Muscle Tank", "Lightweight Mesh Tank",  
    "Premium Wool Crew Socks", "Cushioned Athletic Socks", "No-Show Ankle Socks", "Classic Cotton Dress Socks", "Thermal Winter Socks",  
    "Breathable Running Socks", "Patterned Business Socks", "Reinforced Work Boot Socks", "Colorful Fun Print Socks", "Bamboo Fiber Ankle Socks",  
    "Snug Fit Baby Onesie", "Organic Cotton Baby Bodysuit", "Cozy Zip-Up Onesie", "Animal Print Baby Jumpsuit", "Soft Stretch Romper",  
    "Long Sleeve Baby Onesie", "Fleece-Lined Baby Jumpsuit", "Lightweight Summer Onesie", "Hooded Baby Playsuit", "Adorable Patterned Onesie",  
    "Essential Crewneck Sweatshirt", "Oversized Fleece Sweatshirt", "Half-Zip Pullover Sweatshirt", "Heavyweight Thermal Sweatshirt", "Vintage Graphic Sweatshirt",  
    "Casual Relaxed Fit Sweatpants", "Tapered Jogger Sweatpants", "Ultra-Soft Lounge Sweatpants", "Athleisure Stretch Pants", "Fleece-Lined Track Pants",  
    "Classic Denim Jacket", "Relaxed Fit Hoodie Jacket", "Lightweight Windbreaker", "Water-Resistant Rain Jacket", "Sherpa-Lined Zip Jacket",  
    "Longline Puffer Coat", "Midweight Quilted Jacket", "Insulated Winter Parka", "Stretch-Fit Bomber Jacket", "Classic Peacoat",  
    "Essential Longline Cardigan", "Cable Knit Sweater", "Fitted Turtleneck Pullover", "Chunky Wool Sweater", "Slim Fit Crewneck Sweater",  
    "V-Neck Ribbed Knit Sweater", "Textured Knit Pullover", "Waffle-Knit Cotton Sweater", "Cashmere Blend Sweater", "Mock Neck Knit Sweater",  
    "Classic Board Shorts", "Quick-Dry Swim Trunks", "Elastic Waist Beach Shorts", "Mesh-Lined Water Shorts", "Vintage Floral Swim Shorts",  
    "High-Waisted Biker Shorts", "Performance Running Shorts", "Casual Chino Shorts", "Lightweight Linen Shorts", "Relaxed Fit Denim Shorts",
    "Floral Print Summer Dress", "Casual Sleeveless Dress", "Fitted Bodycon Dress", "A-Line Cotton Dress", "Maxi Flowing Dress",  
    "Boho Midi Dress", "Ruffle Sleeve Dress", "Button-Up Shirt Dress", "Striped Fit-and-Flare Dress", "Pleated Skirt Dress",  
    "Wrap Dress with Tie", "Vintage Floral Dress", "Luxe Velvet Evening Dress", "Shift Dress with Pockets", "Chunky Knit Cardigan",  
    "Long Sleeve Open Cardigan", "Button-Down Wool Cardigan", "Hooded Fleece Cardigan", "Oversized Knit Cardigan", "Faux Fur Cardigan",  
    "Short Sleeve Polo Dress", "Casual Shift Dress", "Knit Sweater Dress", "Sweater Tunic Dress", "Maxi Cardigan Coat",  
    "Textured Faux Leather Jacket", "Zip-Up Motorcycle Jacket", "Relaxed Fit Denim Vest", "Classic Field Jacket", "Utility Vest Jacket",  
    "Oversized Wool Coat", "Double-Breasted Trench Coat", "Checked Tweed Coat", "Peacoat with Wool Lining", "Belted Utility Coat",  
    "Soft Wool Scarf", "Chunky Knit Infinity Scarf", "Cashmere Blend Scarf", "Plaid Wool Scarf", "Fringed Knit Scarf",  
    "Cozy Wool Beanie", "Slouchy Knit Hat", "Pom-Pom Knit Beanie", "Cable Knit Winter Hat", "Wool Blend Fedora Hat",  
    "Breathable Running Shorts", "Mesh Gym Shorts", "Compression Running Shorts", "Drawstring Athletic Shorts", "Performance Speed Shorts",  
    "Thermal Leggings", "High-Waisted Leggings", "Compression Workout Leggings", "Cotton Relaxed Fit Leggings", "Fleece-Lined Leggings",  
    "Patterned Tights", "Sheer Lace Tights", "Opaque Black Tights", "Maternity Support Tights", "Opaque Footless Tights",  
    "Vintage Plaid Skirt", "A-Line Pleated Skirt", "High-Waisted Pencil Skirt", "Wool Midi Skirt", "Button Front Skirt",  
    "Denim Mini Skirt", "Stretch Cotton Skirt", "Floral Print Skirt", "Pleated Satin Skirt", "Fit-and-Flare Skirt",  
    "Wrap Front Skirt", "Luxe Satin Slip Skirt", "Printed Midi Skirt", "Soft Wool Skirt", "Chiffon Maxi Skirt",  
    "Cotton Spandex Tank Top", "Performance Sleeveless Top", "Cropped Tank Top", "Luxe Silk Camisole", "Fitted Bodysuit",  
    "Mesh Sports Bra", "High Support Sports Bra", "Comfort Fit Sports Bra", "Seamless Active Bra", "Athletic Sports Bra",  
    "Breathable Cotton Bra", "Strapless Push-Up Bra", "Wire-Free Bra", "Luxe Lace Bra", "Performance Racerback Bra",  
    "Relaxed Fit Tunic Top", "V-Neck Fitted Tee", "Ribbed Scoop Neck Top", "Button-Down Henley Top", "Short Sleeve Peplum Top",  
    "Fitted Cap Sleeve Top", "Long Sleeve Boat Neck Top", "Silk Button-Up Shirt", "Casual Knit Top", "Luxe Cashmere Blouse",  
    "Men's Silk Pajama Set", "Cotton Lounge Set", "Velvet Sleep Pants", "Plush Fleece Pajamas", "Relaxed Fit Nightgown",  
    "Button-Down Flannel Pajama Set", "Cotton Sleep Shorts", "Silk Sleep Shirt", "Luxe Sleep Shorts", "Ultra-Soft Pajama Set",  
    "Long Sleeve Cotton Pajama Set", "Fleece Lined Sleepwear", "Comfortable Sleep Romper", "Ultra-Cozy Lounge Pants", "Luxury Sleep Set"
    ]

    desc = "classic description of whatever this product is"

    for rep_id, products in zip(supplier_rep_data["id"], num_products):
        for _ in range(products):
            product_data.append([
            product_id,
            product_names[product_id],
            supplier_rep_data.loc[supplier_rep_data['id'] == rep_id, 'start_date'].values[0].replace(' ', '').lower(),
            desc,
            rep_id
            ])
            product_id += 1

    # Save to CSV
    rep_df = pd.DataFrame(product_data, columns=["id", "name", "list_date", "description", "rep_id"])
    rep_df.to_csv("product_data.csv", index=False)

    print("CSV created: ")


#--------------------------------------------
# CUSTOMER GEN SCRIPT
#--------------------------------------------
'''
CREATE TABLE customers(
	id INT NOT NULL,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255) NOT NULL,
    DOB DATETIME NOT NULL 
        CHECK ( 18 >= YEAR(CURRENT_DATE) - YEAR(DOB)),
    phone VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    creation_date DATETIME NOT NULL,

    PRIMARY KEY (id)
);
'''

def customer_gen():
    # Setting random seed for consistency
    np.random.seed(42)

    addresses = [f"customer house {n}" for n in range(64)]

    provinces = [
        "Alberta", "British Columbia", "Manitoba", "New Brunswick", 
        "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island", 
        "Quebec", "Saskatchewan"
    ]

    first_names = [
        "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth",
        "David", "Susan", "Richard", "Jessica", "Joseph", "Sarah", "Charles", "Karen", "Thomas", "Nancy",
        "Christopher", "Betty", "Daniel", "Margaret", "Matthew", "Helen", "Anthony", "Dorothy", "Mark", "Ruth",
        "Donald", "Sharon", "Steven", "Laura", "Paul", "Cynthia", "Andrew", "Amy", "Joshua", "Frances",
        "Kenneth", "Teresa", "Kevin", "Kathleen", "Brian", "Deborah", "George", "Hannah", "Edward", "Rachel",
        "Ronald", "Virginia", "Timothy", "Debra", "Jason", "Carol", "Jeffrey", "Marie", "Ryan", "Julie",
        "Gary", "Emma", "Nicholas", "Alice", "Eric", "Mildred", "Jacob", "Sophia", "Jonathan", "Dorothy",
        "Larry", "Evelyn", "Justin", "Ann", "Frank", "Christine", "Austin", "Diana", "Raymond", "Charlotte",
        "Jesse", "Angela", "Terry", "Rose", "Aaron", "Katherine", "Adam", "Julie", "Sean", "Helen",
        "Henry", "Marie", "Tyler", "Theresa", "Ethan", "Martha", "Zachary", "Tina", "Craig", "Victoria",
        "Samuel", "Lori", "Peter", "Kelly", "Nathan", "Sandra", "Douglas", "Beverly", "George", "Doris",
        "Bobby", "Samantha", "Daniel", "Jill", "Carl", "Kathryn", "Albert", "Rebecca", "Oscar", "Megan",
        "Lawrence", "Gloria", "Walter", "Barbara", "Christian", "Joyce", "Jack", "Susan", "Kyle", "Emily",
        "Dennis", "Madeline", "Frederick", "Paula", "Ryan", "Eleanor", "Cameron", "Olivia", "Vernon", "Isabelle",
        "Louis", "Tracy", "Gerald", "Maggie", "Bryan", "Cheryl", "Phillip", "Linda", "Leonard", "Wendy",
        "Morris", "Jacqueline", "Willie", "Patricia", "Glenn", "Stella", "Harold", "Joyce", "Lester", "Audrey",
        "Dean", "Betsy", "Stanley", "Rita", "Julian", "Judy", "Elmer", "Sally", "Victor", "Anna",
        "Lawrence", "Lorraine", "Milton", "Monica", "Ted", "Debbie", "Brian", "Diane", "Ted", "Natalie",
        "Carl", "Sally", "Gregory", "Penny", "Hugh", "Fay", "Carlton", "Jane", "Harold", "Margie"
    ]

    last_names = [
        "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
        "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Roberts",
        "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Young", "Allen", "King", "Scott", "Green",
        "Baker", "Adams", "Nelson", "Hill", "Ramirez", "Campbell", "Mitchell", "Carter", "Robinson", "Gonzalez",
        "Perez", "Evans", "Hall", "Rivera", "Coleman", "Murphy", "Bailey", "Reed", "Cooper", "Morris",
        "Cook", "Ward", "Morris", "Bailey", "Flores", "Graham", "Kelly", "Howard", "Ward", "Duncan",
        "Dunn", "Rogers", "Fisher", "Simmons", "Foster", "Russell", "Gonzalez", "Bryant", "Alexander", "Russell"
    ]


    # Generate 
    customer_data = []

    for customer_id in range(1000):
        fname = np.random.choice(first_names)
        lname = np.random.choice(last_names)
        DOB =   np.random.choice(["1990-01-01", "1991-01-01", "1992-01-01", "1993-01-01", "1994-01-01", "1995-01-01", "1996-01-01", "1997-01-01", "1998-01-01", "1999-01-01", "2000-01-01", "2001-01-01", "2002-01-01", "2003-01-01", "2004-01-01", "2005-01-01"]),
        DOB = DOB[0]

        customer_data.append([
            customer_id,
            #fname
            fname,
            #lname
            lname,
            #DOB
            DOB,
            #phone number
            f"+1-{np.random.randint(200, 999)}-{np.random.randint(100, 999)}-{np.random.randint(1000, 9999)}",
            #email
            f"{fname}{lname}@customer.com",
            #address
            np.random.choice(addresses),
            #province
            np.random.choice(provinces),
            #creation_date
            f"{np.random.randint(2022, 2025)}-{np.random.randint(1, 12)}-{np.random.randint(1, 28)}",
        ])

    # Save to CSV
    rep_df = pd.DataFrame(customer_data, columns=["id", "fname", "lname", "DOB", "phone", "email", "address", "province","creation_date"])

    rep_df.to_csv("customer_data.csv", index=False)

    print("CSV created: ")


#--------------------------------------------
# ITEM GEN SCRIPT
#--------------------------------------------

'''
CREATE TABLE items(
    id INT NOT NULL,
    size VARCHAR(255) NOT NULL,
    color VARCHAR(255) NOT NULL, 
    price DECIMAL(10, 2) NOT NULL,
    product_id INT NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
'''

def item_gen():
    # Sample supplier data (from previous CSV)
    product_data = pd.read_csv("product_data.csv")

    # Setting random seed for consistency
    np.random.seed(42)

    # Generate number of colors per product
    num_var = np.round(np.random.normal(loc=1, scale=2, size=len(product_data))).astype(int)
    num_var = np.clip(num_var, 1, None)  # Ensure at least 1 rep per supplier

    # Data
    colors = ["black", "white", "grey", "brown", "red"]

    sizes = ["L", "M", "S"]

    # Generate 
    item_data = []
    item_id = 1

    for product_id, items in zip(product_data["id"], num_var):
        color = np.random.choice(colors)
        price = np.round(np.random.uniform(20.00, 120.00), 2)
        for size in sizes:
            for _ in range(items):
                item_data.append([
                    item_id,
                    size,
                    color,
                    price,
                    product_id
                ])
                item_id += 1

    # Save to CSV
    rep_df = pd.DataFrame(item_data, columns=["id", "size", "color", "price", "product_id"])

    rep_df.to_csv("item_data.csv", index=False)

    print("CSV created")



#--------------------------------------------
# REVIEW GEN SCRIPT
#--------------------------------------------
'''
CREATE TABLE reviews(
	id INT NOT NULL,
	rating INT NOT NULL
        CHECK ( rating BETWEEN 1 AND 5 ),
	comment VARCHAR(255),
	when_reviewed DATETIME NOT NULL,
	product_id INT NOT NULL,
	customer_id INT NOT NULL,
	
	PRIMARY KEY (id),
	FOREIGN KEY ( customer_id ) REFERENCES customers(id),
	FOREIGN KEY (product_id) REFERENCES products(id)
);
'''

def review_gen():
    # Get Foreign Key Data
    product_data = pd.read_csv("product_data.csv")
    customer_data = pd.read_csv("customer_data.csv")


    comments = {
        1: "trash",
        2: "still trash",
        3: "somewhat not trash",
        4: "not too shabby",
        5: "not too shabby x2"
    }

    # Setting random seed for consistency
    np.random.seed(42)

    from datetime import datetime, timedelta

    def gen_date(product_id):
        """Extracts the list_date from product_data.csv for a given product_id."""
        product_data = pd.read_csv("product_data.csv")

        # Ensure product_id exists in dataset
        filtered_product = product_data.loc[product_data["id"] == product_id, "list_date"]
        
        if filtered_product.empty:
            raise ValueError(f"Product ID {product_id} not found in product_data.csv")

        # Convert list_date to a proper date format
        data = str(filtered_product.values[0]).strip()
        year_reviewed = data[0:4]  # First 4 characters = Year
        month_reviewed = data[5:7]  # Characters 6 & 7 = Month
        day_reviewed = data[8:10]  # Characters 9 & 10 = Day

        return datetime(int(year_reviewed), int(month_reviewed), int(day_reviewed))

    def random_valid_date(customer_id, product_id):
        """Generates a random date between the later of acct_created (customer) and list_date (product) and today."""
    
        # Load customer and product data
        customer_data = pd.read_csv("customer_data.csv")
        product_date = gen_date(product_id)

        # Extract acct_created date
        filtered_customer = customer_data.loc[customer_data["id"] == customer_id, "creation_date"]

        
        if filtered_customer.empty:
            raise ValueError(f"Customer ID {customer_id} not found in customer_data.csv")

        customer_date = str(filtered_customer.values[0]).strip()
        customer_date = datetime.strptime(customer_date, "%Y-%m-%d")  # Assuming CSV stores dates as YYYY-MM-DD

        # Set the earliest valid date
        min_date = max(customer_date, product_date)

        # Generate a random date between min_date and today
        today = datetime.today()
        random_days = random.randint(1, (today - min_date).days)  # Random days between min_date and today

        return str(min_date + timedelta(days=random_days))

    # Generate Reviews 
    review_data = []

    for review_id in range(2000):
        review = np.random.choice([1, 2, 3, 4, 5])
        product_id = np.random.choice(product_data["id"])
        customer_id = np.random.choice(customer_data["id"])

        review_data.append([
            review_id,
            #review
            review,
            #comment
            comments[review],
            #when reviewed
            random_valid_date(customer_id, product_id),
            #product_id
            product_id,
            #customer_id
            np.random.choice(customer_data["id"])
        ])


    # Save to CSV
    rep_df = pd.DataFrame(review_data, columns=["id", "rating", "comment", "when_reviewed", "product_id", "customer_id"])

    rep_df.to_csv("review_data.csv", index=False)

    print("CSV created: ")


#--------------------------------------------
# CART GEN SCRIPT
#--------------------------------------------

'''
CREATE TABLE carts(
    id INT NOT NULL,
    when_ordered DATETIME NOT NULL,
    departure_datetime DATETIME,
    arrival_datetime DATETIME,
    customer_id INT NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
'''

def cart_gen():
    # Get Foreign Key Data
    customer_data = pd.read_csv("customer_data.csv")

    # Setting random seed for consistency
    np.random.seed(42)

    # Generate number of colors per product
    n_orders = np.round(np.random.normal(loc=2, scale=5, size=len(customer_data))).astype(int)


    from datetime import datetime, timedelta
    def generate_dates():
        # Generate random when_ordered date
        when_ordered = f"{np.random.randint(2022, 2025)}-{np.random.randint(1, 13):02}-{np.random.randint(1, 29):02}"
        when_ordered_date = datetime.strptime(when_ordered, "%Y-%m-%d")

        # Generate departure date (0-3 days later)
        departure_date = when_ordered_date + timedelta(days=np.random.randint(0, 4))

        # Generate arrival date (7-14 days later from when_ordered)
        arrival_date = departure_date + timedelta(days=np.random.randint(4, 11))

        return str(when_ordered), str(departure_date.strftime("%Y-%m-%d")), str(arrival_date.strftime("%Y-%m-%d"))


    # Generate 
    cart_data = []
    cart_id = 1

    for customer_id, orders in zip(customer_data["id"], n_orders):
        date_info = generate_dates()

        for _ in range(orders):
            cart_data.append([
                cart_id,
                #when_ordered
                date_info[0],
                #departure_datetime
                date_info[1],
                #arrival_datetime
                date_info[2],
                #customer_id
                customer_id
            ])
            cart_id += 1

    # Save to CSV
    rep_df = pd.DataFrame(cart_data, columns=["id", "when_ordered", "departure_datetime", "arrival_datetime", "customer_id"])

    rep_df.to_csv("cart_data.csv", index=False)

    print("CSV created")


#--------------------------------------------
# CART_ITEM GEN SCRIPT
#--------------------------------------------

'''
CREATE TABLE cart_items(
cart_id INT NOT NULL,
item_id INT NOT NULL,
quantity INT NOT NULL
CHECK ( quantity > 0 ),

PRIMARY KEY (cart_id, item_id),
FOREIGN KEY (cart_id) REFERENCES carts(id),
FOREIGN KEY (item_id) REFERENCES items(id)
);
'''

import pandas as pd
import numpy as np
from datetime import datetime

item_data = pd.read_csv("item_data.csv")

# Function to parse a date from a string
def parse_date(date_str):
    return datetime.strptime(date_str.split(" ")[0], "%Y-%m-%d")  # Ensure only YYYY-MM-DD is used

# Function to find candidate products
def candidate_products(when_ordered, product_data):
    candidate_products = []
    when_ordered = parse_date(when_ordered)  # Ensure `when_ordered` is a datetime object

    # Iterate through product data
    for _, product in product_data.iterrows():  
        list_date = parse_date(product["list_date"])  # Convert string date to datetime
        if list_date <= when_ordered:
            candidate_products.append(product["id"])  # Store product IDs

    return candidate_products

def candidate_items(candidate_products):
    candidate_items = item_data[item_data["product_id"].isin(candidate_products)]["id"].tolist()
    return candidate_items

# Function to generate cart items
def cart_item_gen():
    cart_item_id = 0  # Initialize counter

    # Load CSVs
    cart_data = pd.read_csv("cart_data.csv")
    item_data = pd.read_csv("item_data.csv")
    product_data = pd.read_csv("product_data.csv")

    np.random.seed(42)  # Consistent randomness

    cart_item_data = []

    for cart_id in cart_data["id"]:
        # Extract and clean order date
        when_ordered = cart_data.loc[cart_data["id"] == cart_id, "when_ordered"].values[0].strip()

        # Get valid product candidates
        product_candidates = candidate_products(when_ordered, product_data)
        item_candidates = candidate_items(product_candidates)
        if not item_candidates:
            continue  # Skip if no valid products exist

        # Generate a random number of items
        n_items = max(1, np.round(np.random.normal(loc=1, scale=5)).astype(int))
        rand_qty_value = max(1, np.round(np.random.normal(loc=1, scale=2.5)).astype(int))

        for _ in range(n_items):
            item_id = np.random.choice(item_candidates)

            cart_item_data.append([
                cart_item_id,
                cart_id,
                item_id,
                rand_qty_value
            ])
            cart_item_id += 1

    # Save to CSV
    rep_df = pd.DataFrame(cart_item_data, columns=["cart_item_id", "cart_id", "item_id", "quantity"])
    rep_df.to_csv("cart_item_data.csv", index=False)

    print("CSV created")


# Main Script #
supplier_gen()
supplier_rep_gen()
customer_gen()
product_gen()
item_gen()
review_gen()
cart_gen()
cart_item_gen()
