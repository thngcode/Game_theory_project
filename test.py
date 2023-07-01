import unittest
from demand_curve import DemandCurve


class Test(unittest.TestCase):
    def test_demand_curve(self):
        position_1 = 10
        slope_1 = -0.1

        test_demand_curve_1 = DemandCurve(position_1, slope_1)
        test_quantity_sold_1 = test_demand_curve_1.calculate_quantity_sold(5)

        test_demand_curve_1.calculate_maximum_profit()
        test_maximum_profit_1 = test_demand_curve_1.maximum_profit

        self.assertEqual(test_quantity_sold_1, 10)
        self.assertEqual(test_maximum_profit_1, 274.5)

        position_2 = 15
        slope_2 = -0.3

        test_demand_curve_2 = DemandCurve(position_2, slope_2)
        test_quantity_sold_2 = test_demand_curve_2.calculate_quantity_sold(5)

        test_demand_curve_2.calculate_maximum_profit()
        test_maximum_profit_2 = test_demand_curve_2.maximum_profit

        self.assertEqual(test_quantity_sold_2, 14)
        self.assertEqual(test_maximum_profit_2, 199.2)

    def test_demand_shifter(self):
        test_shifter = 2

        position = 10
        slope = -0.1

        test_demand_curve = DemandCurve(position, slope)
        new_test_demand_curve = DemandCurve(test_demand_curve.get_position() + test_shifter,
                                            test_demand_curve.get_slope())

        new_quantity_sold = new_test_demand_curve.calculate_quantity_sold(5)

        new_test_demand_curve.calculate_maximum_profit()
        new_maximum_profit = new_test_demand_curve.maximum_profit

        self.assertEqual(new_quantity_sold, 12)
        self.assertEqual(new_maximum_profit, 389.4)


if __name__ == "__main__":
    unittest.main()
