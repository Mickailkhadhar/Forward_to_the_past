class Basket:

    def __init__(self):
        pass

    def read_file(self, text_file):
        with open(text_file, 'r') as file:
            lines = file.read().splitlines()
        return lines

    def write_file(self, text_file, cost):
        with open(text_file, 'a') as file:
            file.write('\n\n')
            file.write("Output : \n\n")
            file.write(str(cost))
            file.close()
