# Project: Game Theory applied to pricing in the situation of uncertainty

## General description

This project aims to develop a program that simulates a situation based on game theory,
specifically about pricing under uncertainty. The program can be described as below:

A one-player game in a simple pricing environment (one commodity and basic pricing).
Commodities have a linear expense structure, and the player's goal is to maximize profits by setting a fitting price for
the commodity.
The profits are based on the demand curve.
The players only know the distributions used to randomize the parameters of the demand curve.

The game consists of a predetermined number of rounds between 7 and 13. After each round, the
demand curve is shifted by a demand-shifter (a random constant that shifts the curve). When a
round turns, the players will get information about how many items were sold at the previous input
price and how much profits they made. This gives the players a chance to learn the demand curve,
but the demand-shifter will make their learning more difficult. The program makes sure that the
demand curve generally gives the player a chance to get positive profits.

## User instructions

The program is launched by running the UI.py file, which will start an interface and a new game.
While the game is going on, the players are required to input a sales price and a production volume in each round.
It is noted that both inputs are limited to integers between 0 and 99.

The players should press the button “Submit” to play a single round.
The round results, including the profit, the amount sold and the price, will be shown to support the decision-making
process of the players in the next round.

At the end of the game, all optimal values of each round, including the optimal price, the optimal quantity and the
maximum profit, will be shown in addition to all user inputs.

## Installation

Set up a virtual environment and install required packages with command:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  
```

## Running the program

Start the program with command:

```shell
python3 UI.py
```
