# Battleships Game
For my project I have built a battleships game. Battleships is a 1 vs 1 strategy game. Each player has a set number of battleships and a grid. The battleships will be placed at different coordinates on each player's grid and your goal is to guess all the coordinates that your opponents battleships are on to sink their ship and win.
![UI](https://i.postimg.cc/MKgCHW1F/UI.png)


## Features
The battleships game lets you choose your grid size (minimum 5, maximum 20).
![Grid Size](https://i.postimg.cc/wjQVtmMM/Grid.png)

After you choose your grid size you and your opponents battleships will be randomly placed on the grid. Your battleships will be marked with an 'S' but you will not be able to see your opponent's battleships.
![Battleships](https://i.postimg.cc/dtPWfvT2/Battleships.png)

After you choose the grid size you will have to guess the coordinates.
![Guess Coordinates](https://i.postimg.cc/kgNLsG1R/Guess.png)

If you enter a position that you have already guessed you will get the following message.
![Position](https://i.postimg.cc/zvgDzQKg/Position.png)

If you enter a number outside the range you will get an error message.
![Please Enter](https://i.postimg.cc/GhjpfFpb/Please-Enter.png)

If you enter a character that is not a number you will get an error message.
![Error](https://i.postimg.cc/RCX8bqzj/Error.png)

If you enter valid coordinates and miss or your opponent misses you will get the following messages.

- You missed the computer's battleship!
- Computer missed your battleship!

If you hit or the computer hits your battleships you will get the following messages.

- You hit the computer's battleship
- Oh no! Computer sunk one of your battleships!

If you win or lose you will get the following messages.

- Congratulations! You won!
- All of your battleships have been sunk. You lose!


## Testing
I passed the code through a CI Python Linter without any errors.
![Linter](https://i.postimg.cc/KjwQxzBm/Linter.png)


## Bugs
When I first created the boards it was showing me the locations of my and my opponent's battleships. I fixed the bug that showed my opponent's battleships and now I can't see them anymore.


## Deployment
The battleships game was deployed to Heroku. In order to deploy it there I built an app, added my credit card information, created the necessary buildpacks (Python and NodeJS), connected my GitHub account to Heroku and then finally deployed it.


## References
https://copyassignment.com/battleship-game-code-in-python/
https://coderspacket.com/battleship-game-in-python
https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605
https://pypi.org/project/colorama/
https://www.pythonpool.com/python-colorama/
https://www.geeksforgeeks.org/turtle-reset-function-in-python/
https://www.w3schools.com/python/gloss_python_class_init.asp
https://www.w3schools.com/python/python_booleans.asp
https://www.w3schools.com/python/python_ref_exceptions.asp
https://www.w3schools.com/python/python_operators.asp
https://www.w3schools.com/python/python_classes.asp
https://www.w3schools.com/python/python_while_loops.asp
https://www.w3schools.com/python/python_for_loops.asp
https://www.w3schools.com/python/python_try_except.asp
https://www.w3schools.com/python/ref_func_len.asp
https://www.w3schools.com/python/ref_keyword_continue.asp
https://www.w3schools.com/python/ref_keyword_break.asp
https://www.w3schools.com/python/ref_keyword_return.asp
https://www.w3schools.com/python/python_arrays.asp
https://www.w3schools.com/python/python_user_input.asp
https://www.w3schools.com/python/ref_func_range.asp
https://www.w3schools.com/python/ref_string_format.asp
https://www.w3schools.com/python/ref_string_join.asp





