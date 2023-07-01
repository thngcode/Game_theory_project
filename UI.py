import sys

from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QLineEdit, QGridLayout, QMessageBox, QTableWidget, QTableWidgetItem)

from game import Game


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_window()

    def start_window(self):
        # set labels
        self.round_label = QLabel("Round 1")
        self.round_price = QLabel("Price (€):")
        self.round_sold = QLabel("Amount (unit):")
        self.round_profit = QLabel("Profit (€):")

        self.input_validator = QIntValidator(0, 99)

        # ask for input sales price
        self.input_price_label = QLabel("Product sales price (€):")
        self.input_price_bar = QLineEdit()

        self.input_price_bar.setValidator(self.input_validator)

        # ask for input production volume
        self.input_production_volume_label = QLabel("Production volume (unit):")
        self.input_production_volume_bar = QLineEdit()
        self.input_production_volume_bar.setValidator(self.input_validator)

        # set submit buttion
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_event)
        self.submit_button.setStyleSheet("QPushButton::hover"
                                         "{"
                                         "background-color : orange;"
                                         "}")

        # set layout
        self.layout = QGridLayout()
        self.layout.setSpacing(10)

        self.layout.addWidget(self.round_label, 1, 0)
        self.layout.addWidget(self.round_profit, 2, 0)
        self.layout.addWidget(self.round_price, 3, 0)
        self.layout.addWidget(self.round_sold, 4, 0)

        self.layout.addWidget(self.input_price_label, 3, 1)
        self.layout.addWidget(self.input_price_bar, 3, 2)

        self.layout.addWidget(self.input_production_volume_label, 4, 1)
        self.layout.addWidget(self.input_production_volume_bar, 4, 2)

        self.layout.addWidget(self.submit_button, 5, 2, 1, 2)

        self.layout.setColumnMinimumWidth(0, 150)
        self.setLayout(self.layout)
        self.setGeometry(100, 60, 500, 150)
        self.setWindowTitle("Game Theory: Pricing in the situation of uncertainty")
        self.show()

        # set a Game
        self.game = Game()

    def closeEvent(self, event):
        """
        Function quits the game.
        :param event:
        :return: None
        """
        reply = QMessageBox.question(self, " ", "Are you sure to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def submit_event(self, event):
        """
        Functions is triggered by mouse press on Submit button and runs the game accordingly.
        :param event:
        :return: None
        """
        if self.input_price_bar.text() and self.input_production_volume_bar.text():
            if self.game.current_round is None:
                self.game.start_game(int(self.input_price_bar.displayText()),
                                     int(self.input_production_volume_bar.displayText()))
            else:
                self.game.create_next_round(int(self.input_price_bar.displayText()),
                                            int(self.input_production_volume_bar.displayText()))

            self.update_round_info(self.game)

            if self.game.round_number > self.game.total_rounds:
                self.game.game_running = False
                self.end_window()

    def update_round_info(self, game):
        """
        Function updates round information.
        :param game: Game
        :return: None
        """
        self.round_label.setText(f"Round {game.round_number}")
        self.round_price.setText(f"Price (€): {game.current_round.input_price}")
        self.round_sold.setText(f"Amount sold: {game.current_round.quantity_sold}")
        self.round_profit.setText(f"Profit (€): {game.current_round.round_profit}")

    def end_window(self):
        """
        Function shows the window when the game is over.
        :return: None
        """
        self.submit_button.hide()
        self.input_price_bar.hide()
        self.input_price_label.hide()
        self.input_production_volume_bar.hide()
        self.input_production_volume_label.hide()
        self.round_label.hide()
        self.round_price.hide()
        self.round_sold.hide()
        self.round_profit.hide()

        self.end_title = QLabel(f"End game with total profits of {round(self.game.total_profits, 2)} €")
        self.end_message = QLabel(
            f"Total maximum profits {round(self.game.total_maximum_profits, 2)} €. You have achieved {round((self.game.total_profits / self.game.total_maximum_profits) * 100, 2)}% of the total maximum profits.")

        self.layout.addWidget(self.end_title, 1, 0)
        self.layout.addWidget(self.end_message, 2, 0)

        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(len(self.game.result_table[0]))
        self.table.setHorizontalHeaderLabels(self.game.result_table[0].keys())
        self.table.setRowCount(len(self.game.result_table))
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 90)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 110)
        self.table.setColumnWidth(4, 105)
        self.table.setColumnWidth(5, 120)
        self.table.setColumnWidth(6, 130)
        self.table.setColumnWidth(7, 130)

        row = 0
        for game_round in self.game.result_table:
            self.table.setItem(row, 0, QTableWidgetItem(str(game_round['Round'])))
            self.table.setItem(row, 1, QTableWidgetItem(str(game_round['Input Price'])))
            self.table.setItem(row, 2, QTableWidgetItem(str(game_round['Production Volume'])))
            self.table.setItem(row, 3, QTableWidgetItem(str(game_round['Quantity Sold'])))
            self.table.setItem(row, 4, QTableWidgetItem(str(game_round['Round Profit'])))
            self.table.setItem(row, 5, QTableWidgetItem(str(game_round['Optimal Price'])))
            self.table.setItem(row, 6, QTableWidgetItem(str(game_round['Optimal Quantity'])))
            self.table.setItem(row, 7, QTableWidgetItem(str(game_round['Maximum Profit'])))
            row += 1
        self.layout.addWidget(self.table)

        self.setGeometry(100, 60, 936, 250)


def main(args):
    app = QApplication(sys.argv)
    window = MainWindow()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
