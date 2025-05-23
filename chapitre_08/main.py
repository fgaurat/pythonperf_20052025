from CustomerDAO import CustomerDAO


def filterLivejournal(gen):

    for data in gen:
        if "livejournal" in data.email:
            yield data

def lastNameToUpper(gen):
    for data in gen:
        data.last_name = data.last_name.upper()
        yield data

def main():
    dao = CustomerDAO('customers_db.db')
    customers = dao.findAll()

    # n = len(list(customers))
    filteredCustomers = filterLivejournal(customers)
    upperCustomers = lastNameToUpper(filteredCustomers)
    for customer in upperCustomers: 
        print(customer)

if __name__ == '__main__':
    main()