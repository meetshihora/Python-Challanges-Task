'''Task 1: We have following information on countries and their population (population is in crores),

    Country	  Population
    China	  143
    India	  136
    USA	      32
    Pakistan  21

    1. Using above create a dictionary of countries and its population
    2. Write a program that asks user for three type of inputs,

        a. print: if user enter print then it should print all countries with their population in this format,
            china==>143
            india==>136
            usa==>32
            pakistan==>21

        b. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it

        c. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!

        d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country. '''

# Solution
population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()