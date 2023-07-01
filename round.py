from demand_curve import DemandCurve


class Round:
    def __init__(self, input_price, production_volume, demand_curve):
        self.input_price = input_price
        self.production_volume = production_volume
        self.demand_curve = demand_curve

        self.quantity_sold = self.get_quantity_sold()
        self.round_profit = self.get_round_profit()

    def set_demand_curve(self, demand_curve):
        """
        Function sets the demand curve.
        :param demand_curve: DemandCurve
        :return: None
        """
        self.demand_curve = demand_curve

    def create_new_demand_curve(self, shifter):
        """
        Function creates a new demand curve with a random shifter.
        :param shifter: int
        :return: DemandCurve
        """
        return DemandCurve(self.demand_curve.get_position() + shifter, self.demand_curve.get_slope())

    def get_quantity_sold(self):
        """
        Function gets the amount of products the player sells in a rounds.
        :return: int
        """
        # Select minimum of quantity sold or production volume since it would not make sense for the player
        # to be able to sell more than they have produced.
        # Also quantity sold is the max amount they can sell at that specific price.
        return int(round(min(self.demand_curve.calculate_quantity_sold(self.input_price), self.production_volume), 0))

    def get_round_profit(self):
        """
        Function gets the profit the player makes in a round.
        :return: int
        """
        return self.quantity_sold * self.input_price
