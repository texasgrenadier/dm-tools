import argparse
import random

business_types = {
    "Bakers": 800,     
    "Barbers": 350,     
    "Bathers": 1900,
    "Beer-Sellers": 1400,
    "Blacksmiths": 1500,
    "Bleachers": 2100,
    "Bookbinders": 3000,   
    "Booksellers": 6300,
    "Buckle Makers": 1400,
    "Butchers": 1200,
    "Carpenters": 550,   
    "Chandlers": 700,     
    "Chicken Butchers": 1000,   
    "Coopers": 700,
    "Copyists": 2000,
    "Cutlers": 2300,
    "Doctors": 1700,
    "Fishmongers": 1200,
    "Furriers": 250,     
    "Glovemakers": 2400,
    "Harness-Makers": 2000,
    "Hatmakers": 950,     
    "Hay Merchants": 2300,
    "Illuminators": 3900,
    "Inns": 2000,
    "Jewelers": 400,     
    "Locksmiths": 1900,
    "Magic-Shops": 2800,   
    "Maidservants": 250,    
    "Masons": 500,     
    "Mercers": 700,     
    "Old-Clothes": 400,     
    "Painters": 1500,
    "Pastrycooks": 500,     
    "Plasterers": 1400,
    "Pursemakers": 1100,   
    "Roofers": 1800,
    "Ropemakers": 1900,
    "Rugmakers": 2000,
    "Saddlers": 1000,   
    "Scabbardmakers": 850,     
    "Sculptors": 2000,
    "Shoemakers": 150,     
    "Spice Merchants": 1400,
    "Tailors": 250,    
    "Tanners": 2000,
    "Taverns/Restaurants": 400,     
    "Watercarriers": 850,     
    "Weavers": 600,     
    "Wine-Sellers": 900,     
    "Woodcarvers": 2400,
    "Woodsellers": 2400   
}
def how_many(population, sv):
    number_of_business = int(population/sv)
    if number_of_business == 0:
        chance = int((population/sv) * 100)
        x = random.randint(1, 100)
        if x < chance:
            number_of_business = 1
        # print (str(chance) + " " + str(x))
    return number_of_business

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build a town.')
    parser.add_argument('-n', action='store', dest='name', default='Smallville', help='name of town')
    parser.add_argument('-p', action='store', dest='population', default=0, help='population of town')

    args = parser.parse_args()
    town_name = args.name
    population = int(args.population)

    print("Town of ", town_name)
    print("  Population: ", population)

    for business in business_types:
        sv = int(business_types[business])
        number_of_business = how_many(population, sv)
        if number_of_business > 0: 
            print("    " + str(number_of_business) + " " + business)
