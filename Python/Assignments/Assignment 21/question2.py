class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def get_data(self):
        try:
            self.model_no = int(input("Enter Model Number: "))
            if self.model_no > 9999:
                raise ValueError("Model number should be at most 4 digits")

            self.screen_size = int(input("Enter Screen Size (in inches): "))
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Invalid screen size")

            self.price = int(input("Enter Price: "))
            if self.price < 0 or self.price > 5000:
                raise ValueError("Invalid price")

        except ValueError as ve:
            print("Exception:", ve)
            self.model_no = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("\nTelevision Details:")
        print("Model Number:", self.model_no)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)


# Main function
tv = Television()
tv.get_data()
tv.display()
