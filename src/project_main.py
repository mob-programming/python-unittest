#!/usr/bin/env python3


class GameBoard(object):
    cells = list()

    def get_number_of_cells(self):
        return len(self.cells)

    def add_cells(self, cell):
        self.cells.append(cell)

