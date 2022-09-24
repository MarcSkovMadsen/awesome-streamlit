"""
## Sudoku Solver

A fast, interactive web application for solving Sudoku puzzles 
using the optimization library Pyomo (https://www.pyomo.org/).

Author: [Joshua Cook](https://joshuacook.netlify.app))\n
Source: [Github](https://github.com/jhrcook/streamlit-sudoku)
"""
import streamlit as st

# Your imports goes below
import random
import re
from itertools import product

import streamlit as st
import pandas as pd
import numpy as np
from gallery.sudoku_solver.pyomo_sudoku_solver import solve_sudoku
from gallery.sudoku_solver.ui_auxiliary import empty_board_str, board_matrix_to_dataframe


def main():
    st.title("Sudoku Solver")
    st.markdown("A fast, interactive web application for solving Sudoku puzzles using the optimization library [Pyomo](https://www.pyomo.org/).")
    
    # Your code goes below
    random.seed(0)

    input_data = st.text_area(
        label="Enter the starting state of the board.", value=empty_board_str, height=400
    )

    rows = np.repeat(np.arange(1, 10), 9)
    cols = np.tile(np.arange(1, 10), 9)
    values = []

    for line in input_data.split("\n"):
        if not "-" in line:
            vals = re.findall("[0-9]", line.rstrip())
            values += [int(x) for x in vals]

    if len(rows) == len(cols) == len(values):

        known_cells = pd.DataFrame({"i": rows, "j": cols, "k": values})
        board = known_cells.copy()

        known_cells = known_cells[known_cells["k"] != 0]

        board.k = ["" if x == 0 else str(x) for x in board.k]
        board = board.pivot(index="i", columns="j", values="k")

        if st.button("Solve!"):
            st.markdown("**Solution**")
            res = solve_sudoku(known_cells)
            st.write(board_matrix_to_dataframe(res))
        else:
            st.markdown("**Board layout**")
            st.write(board)


    else:
        st.write("Something is wrong with the layout of the board. Please try again.")
    

main()
