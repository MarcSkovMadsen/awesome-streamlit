import re

import numpy as np
import pandas as pd
from pyomo import environ as pyo
from pyomo.dataportal import DataPortal
from pyomo.opt import SolverFactory

import pyutilib.subprocess.GlobalData

pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False


def solve_sudoku(known_cells):
    known_cells.columns = ["i", "j", "k"]

    # The grid indices and possible values.
    N = np.arange(1, 9 + 1)

    # Concrete model
    model = pyo.ConcreteModel()

    # Variable
    model.X = pyo.Var(N, N, N, within=pyo.Binary)

    # Constraints
    model.row_constraint = pyo.ConstraintList()
    model.col_constraint = pyo.ConstraintList()
    model.block_constraint = pyo.ConstraintList()
    model.allcells_constraint = pyo.ConstraintList()
    model.knowncells_constraint = pyo.ConstraintList()

    # Rows
    for i in N:
        for k in N:
            model.row_constraint.add(sum(model.X[i, j, k] for j in N) == 1)

    # Columns
    for j in N:
        for k in N:
            model.col_constraint.add(sum(model.X[i, j, k] for i in N) == 1)

    # Blocks
    for i in np.arange(1, 9, 3):
        for j in np.arange(1, 9, 3):
            for k in N:
                model.block_constraint.add(
                    sum(
                        model.X[p, q, k]
                        for p in np.arange(i, i + 3)
                        for q in np.arange(j, j + 3)
                    )
                    == 1
                )

    # All cells
    for i in N:
        for j in N:
            model.allcells_constraint.add(sum(model.X[i, j, k] for k in N) == 1)

    # Known cells
    for i, j, k in zip(known_cells["i"], known_cells["j"], known_cells["k"]):
        #     if k != 0:
        model.knowncells_constraint.add(model.X[i, j, k] == 1)

    # Objective (none)
    model.objective = pyo.Objective(expr=1)

    # Solving
    opt = SolverFactory("glpk")
    solution = opt.solve(model)

    res = np.zeros((9, 9))

    for v in model.component_data_objects(pyo.Var, active=True):
        val = v.value
        if val > 0:
            i, j, k = [int(x) for x in re.findall("[0-9]", v.name)]
            res[i - 1, j - 1] = k

    return res
