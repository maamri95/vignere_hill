from PyQt5.QtWidgets import QSpinBox, QGridLayout, QMessageBox


def msg_box(text, type, obj):
    msg = QMessageBox()
    msg.setIcon(obj)
    msg.setText(type)
    msg.setInformativeText(text)
    msg.setWindowTitle(type)
    msg.exec_()


class Matrice:

    def __init__(self, grid, xmax=3, ymax=3, editable=False):
        self.editable = editable
        self.compenent = self.__init_mat(xmax, ymax)
        self.__inser_in_grid(grid)

    def __init_mat(self, xmax, ymax):
        """

        :param xmax: nombre de row
        :param ymax: nombre de column
        :return: list
        """
        tab = []
        for i in range(xmax):
            row = []
            for j in range(ymax):
                box = QSpinBox()
                box.setEnabled(self.editable)
                box.size
                box.setMinimum(-100)
                row.append(box)
            tab.append(row)
        return tab

    def __inser_in_grid(self, grid):
        """

        :type grid: QGridLayout
        :param grid: QGridLayout dans le quel on inser la matrice
        """

        for i in range(len(self.compenent)):
            for j in range(len(self.compenent[0])):
                grid.addWidget(self.compenent[i][j], i, j)

    def get(self):
        """
        return les valeur de compenent
        """
        tab = []
        for i in range(len(self.compenent)):
            row = []
            for j in range(len(self.compenent[0])):
                item = self.compenent[i][j]
                row.append(item.value())
            tab.append(row)
        return tab

    def set(self, tab):
        """
        modefie les valeurs de la liste des component
        :param tab: list a insere
        :type tab: list
        """
        for i in range(len(self.compenent)):
            for j in range(len(self.compenent[0])):
                self.compenent[i][j].setValue(tab[i][j])
