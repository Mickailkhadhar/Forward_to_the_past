class Prices:
    def __init__(self):
        self.prices = {
            "back to the future 1": 15,
            "back to the future 2": 15,
            "back to the future 3": 15,
        }

    def set_price(self, name):
        if name not in self.prices:
            self.prices[name] = 20

    def get_movie_counts(self, items):
        counts = {}
        items = list(filter(None, items))
        items.remove('input :')

        for item in items:
            item = item.lower()
            if item not in counts:
                counts[item] = 0
            counts[item] += 1
        return counts

    def get_total(self, counts):
        '''
        lets compute total for fttp movies and other movies. That way, we can apply discount on fttp movie only
        '''
        total_fttp = 0  # forward to the past
        total_others = 0
        for item, count in counts.items():
            if item in self.prices:  # back to the future movies
                total_fttp += self.prices[item] * count
            else:
                self.set_price(item)  # other movies
                total_others += self.prices[item] * count

        return total_fttp, total_others

    def get_discount(self, counts):
        if counts.get("back to the future 1") and counts.get("back to the future 2") and counts.get("back to the future 3"):
            discount = 0.2
        elif counts.get("back to the future 1") and counts.get("back to the future 2"):
            discount = 0.1
        elif counts.get("back to the future 2") and counts.get("back to the future 3"):
            discount = 0.1
        elif counts.get("back to the future 1") and counts.get("back to the future 3"):
            discount = 0.1
        else:
            discount = 0
        return discount
