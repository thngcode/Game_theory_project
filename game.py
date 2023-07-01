from demand_curve import DemandCurve
from round import Round
import random


class Game:
    def __init__(self):
        self.game_running = True

        # set number of rounds random between 7 and 13
        self.total_rounds = random.randint(7, 13)
        self.round_number = 1

        # set demand shifter, initial position and slope of the demand curve random
        self.demand_shifter = random.uniform(-0.5, 0.5)
        self.initial_position = random.randint(2, 13)
        self.initial_slope = random.uniform(-0.05, -0.5)

        # set an array to store results
        self.result_table = []

        self.current_round = None

        self.user_interface = None

        self.total_profits = 0
        self.total_maximum_profits = 0

    def start_game(self, input_price, production_volume):
        """
        Function starts the first round of the game
        :param input_price: input sales price
        :param production_volume: input production volume
        :return: None
        """
        self.current_round = Round(input_price,
                                   production_volume,
                                   DemandCurve(self.initial_position, self.initial_slope))
        self.add_results()
        self.round_number += 1

    def create_next_round(self, input_price, production_volume):
        """
        Function creates next round of the game
        :param input_price: new input sales price
        :param production_volume: new input production volume
        :return: None
        """

        next_round = Round(input_price,
                           production_volume,
                           self.current_round.create_new_demand_curve(self.demand_shifter))

        self.current_round = next_round

        self.add_results()

        self.round_number += 1

    def add_results(self):
        """
        Function adds results of a game to result table.
        :return: None
        """
        self.total_profits += self.current_round.round_profit
        self.total_maximum_profits += self.current_round.demand_curve.get_maximum_profit()

        self.result_table.append({'Round': self.round_number,
                                  'Input Price': self.current_round.input_price,
                                  'Production Volume': self.current_round.production_volume,
                                  'Quantity Sold': self.current_round.quantity_sold,
                                  'Round Profit': self.current_round.round_profit,
                                  'Optimal Price': self.current_round.demand_curve.get_optimal_price(),
                                  'Optimal Quantity': self.current_round.demand_curve.get_optimal_quantity(),
                                  'Maximum Profit': self.current_round.demand_curve.get_maximum_profit()})
