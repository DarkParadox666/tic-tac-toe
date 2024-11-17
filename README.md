# The_final_task_5.6
Tic Tac Toe

# functions
- print_table() -> None: 
    a function for print the game table
- input_cor() -> [bool | tuple]: 
    a function for entering coordinates and checking correctness
- check_cell(cor: tuple) -> bool:
    this function takes coordinates and checking for the presence of an empty cell
- fill_cell(cor: tuple, sym: str) -> None:
    the function takes coordinates and  user symbol for filling the cell
- check_win(user: str) -> bool:
    This function takes username and allows you to check the availability of the game table for character matches 
- check_tie() -> bool:
    This function is for checking the game table for the presence of '-'
- step_user(user: dict) -> bool:
    This function accepts the user dict and runs other functions to check the input, empty the cell and fill the cell
- game() -> None:
    this function beginning the game and makes checking win or tie