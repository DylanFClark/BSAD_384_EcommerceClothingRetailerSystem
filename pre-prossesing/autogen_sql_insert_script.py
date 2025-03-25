

data_sources = [["data/cleaned_supplier_data.txt" , "INSERT INTO supplier(id, company, acct_created) VALUES \n"],
                ["data/cleaned_supplier_rep_data.txt" , "INSERT INTO supplier_rep(id, fname, lname, start_date, phone, email, supplier_id) VALUES \n"],
                ["data/cleaned_product_data.txt" , "INSERT INTO product(id, name, list_date, description, rep_id) VALUES \n"],
                ["data/cleaned_item_data.txt" , "INSERT INTO item(id, size, color, price, product_id) VALUES \n"],
                ["data/cleaned_customer_data.txt" , "INSERT INTO customer(id, fname, lname, DOB, phone, email, address, province, creation_date) VALUES \n"],
                ["data/cleaned_review_data.txt" , "INSERT INTO review(id, rating, comment, when_reviewed, product_id, customer_id) VALUES \n"],
                ["data/cleaned_cart_data.txt" , "INSERT INTO cart(id, when_ordered, departure_datetime, arrival_datetime, customer_id) VALUES \n"],
                ["data/cleaned_cart_item_data.txt" , "INSERT INTO cart_item(cart_item_id, cart_id, item_id, quantity) VALUES \n"]
                ]


def data_length(data):
    with open(data, 'r') as file:
        n_file = len(file.readlines())
        
    return n_file

for data, query in data_sources:
    n = 1
    with open(data, 'r') as file:
        n_file = data_length(data)
        for line in file.readlines():
            with open("data insertion & test queries/query.txt", "a") as query_file:
                if 0 == n % 1000:
                    query_file.write(f"{line}; \n")
                    if n < n_file:
                        query_file.write(f"{query}")

                elif n == n_file:
                    n = 0
                    query_file.write(f"{line}; \n")

                elif n == 1:
                    query_file.write(f"{query}")
                    query_file.write(f"{line},")

                else:
                    query_file.write(f"{line},")

                n += 1
