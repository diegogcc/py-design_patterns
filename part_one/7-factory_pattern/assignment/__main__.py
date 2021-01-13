from customers import loader

for cust_type in 'sm_cust', 'ent_cust', 'gov_cust', 'alien_cust':
    cust = loader.load_cust(cust_type)
    cust.name = cust_type
    cust.send_invoice()

# Sending invoice for sm_cust customer
# Sending invoice for ent_cust customer
# Sending invoice for gov_cust customer
# Customer type alien_cust not found