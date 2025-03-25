import pandas as pd

# Supplier Data

def convert_supplier_data():
    # Read CSV file into a DataFrame
    supplier_data = pd.read_csv("data/supplier_data.csv")

    # Process the data
    data = []
    for index, row in supplier_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, '{row[1]}', '{row[2]}') \n")

    # Write cleaned data to a new file
    with open("data/cleaned_supplier_data.txt", "w") as file:
        file.writelines(data)
    
    return True


# Supplier Rep Data

def convert_supplier_rep_data():
    # Read CSV file into a DataFrame
    s_data = pd.read_csv("data/supplier_rep_data.csv")

    # Process the data
    data = []

    for index, row in s_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', {row[6]}) \n")

    # Write cleaned data to a new file
    with open("data/cleaned_supplier_rep_data.txt", "w") as file:
        file.writelines(data)
    
    return True


# Product Data

def convert_product_data():
    # Read CSV file into a DataFrame
    s_data = pd.read_csv("data/product_data.csv")

    # Process the data
    data = []

    for index, row in s_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', {row[4]}) \n")

    # Write cleaned data to a new file
    with open("data/cleaned_product_data.txt", "w") as file:
        file.writelines(data)

    return True

# Item Data

def convert_item_data():
    # Read CSV file into a DataFrame
    s_data = pd.read_csv("data/item_data.csv")

    # Process the data
    data = []

    for index, row in s_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, '{row[1]}', '{row[2]}', {row[3]}, {row[4]}) \n")

    # Write cleaned data to a new file
    with open("data/cleaned_item_data.txt", "w") as file:
        file.writelines(data)
    
    return True


# Customer Data 

def convert_customer_data():
    # Read CSV file into a DataFrame
    s_data = pd.read_csv("data/customer_data.csv")

    # Process the data
    data = []

    for index, row in s_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}') \n")

    # Write cleaned data to a new file
    with open("data/cleaned_customer_data.txt", "w") as file:
        file.writelines(data)
    
    return True


# Review Data


def convert_review_data():
    # Read CSV file into a DataFrame
    s_data = pd.read_csv("data/review_data.csv")

    # Process the data
    data = []

    for index, row in s_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, {row[1]}, '{row[2]}', '{row[3]}', {row[4]}, {row[5]}) \n")

    # Write cleaned data to a new file
    with open("data/cleaned_review_data.txt", "w") as file:
        file.writelines(data)

    return True

# Cart Data


def convert_cart_data():
    # Read CSV file into a DataFrame
    s_data = pd.read_csv("data/cart_data.csv")

    # Process the data
    data = []

    for index, row in s_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, '{row[1]}', '{row[2]}', '{row[3]}', {row[4]}) \n")

    # Write cleaned data to a new file
    with open("data/cleaned_cart_data.txt", "w") as file:
        file.writelines(data)
    
    return True
    


# Cart Item Data

def convert_cart_item_data():
    # Read CSV file into a DataFrame
    s_data = pd.read_csv("data/cart_item_data.csv")

    # Process the data
    data = []

    for index, row in s_data.iterrows():  # iterate over rows
        data.append(f"({row[0]}, {row[1]}, {row[2]}, {row[3]}) \n")

    # Write cleaned data to a new file
    with open("data/cleaned_cart_item_data.txt", "w") as file:
        file.writelines(data)

    return True



convert_supplier_data()
convert_supplier_rep_data()
convert_customer_data()
convert_review_data()
convert_product_data()
convert_item_data()
convert_cart_data()
convert_cart_item_data()