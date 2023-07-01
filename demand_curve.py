class DemandCurve:
    def __init__(self, position, slope):
        self.position = position
        self.slope = slope

        self.maximum_profit = 0
        self.optimal_price = 0
        self.optimal_quantity = 0

        # calculate the maximum profit whenever a demand curve is created
        self.calculate_maximum_profit()

    def calculate_quantity_sold(self, price):
        """
        Function calculates the amount of products sold.
        :param price: int
        :return: int
        """
        return int(round(max(self.position + price * self.slope, 0), 0))

    def calculate_maximum_profit(self):
        """
        Function calculates the maximum profit based on the demand curve.
        :return: None
        """

        product_price = 0

        while product_price <= 200:
            quantity_sold = self.calculate_quantity_sold(product_price)
            expected_profit = round(quantity_sold * product_price, 2)

            if expected_profit > self.maximum_profit:
                self.maximum_profit = expected_profit
                self.optimal_price = round(product_price, 2)
                self.optimal_quantity = quantity_sold

            product_price += 0.1

    def get_position(self):
        """
        Function returns the position of the demand curve.
        :return: int
        """
        return self.position

    def get_slope(self):
        """
        Function returns the slope of the demand curve.
        :return: float
        """
        return self.slope

    def get_maximum_profit(self):
        """
        Function returns the maximum profit based on the demand curve.
        :return: float
        """
        return self.maximum_profit

    def get_optimal_price(self):
        """
        Function returns the optimal price based on the demand curve.
        :return: float
        """
        return self.optimal_price

    def get_optimal_quantity(self):
        """
        Function returns the optimal amount of products sold, based on the demand curve.
        :return: int
        """
        return self.optimal_quantity
