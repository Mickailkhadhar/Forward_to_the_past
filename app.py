import sys
from src.prices import Prices
from src.basket import Basket

def main(file):
    prices = Prices() 
    basket = Basket() 

    tmp_basket = basket.read_file(file)

    movies = prices.get_movie_counts(tmp_basket)
    total_fttp, total_others = prices.get_total(movies)
    discount = prices.get_discount(movies)

    total_fttp -= total_fttp * discount
    total =  total_fttp + total_others
    basket.write_file(file, total)


if __name__ == "__main__":
    file = sys.argv[1]
    main(file)