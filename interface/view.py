import re

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from interface.util import msg_box, Matrice
from vigenere_hill import VigenereHill


class View(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi('./interface/vigenere_hill.ui', self)
        self.btn_test.clicked.connect(self.check_key)
        self.btn_crypt.clicked.connect(self.crypte)
        self.btn_decrypt.clicked.connect(self.decrypt)
        self.vigenere_hill: VigenereHill = None
        self.regx = re.compile(r"^[a-zA-Z]+$")
        self.champs_hill = Matrice(self.key_hill, editable=True)
        self.champs_inverse = Matrice(self.inverse)
        self.champs_comatrice = Matrice(self.comatrice)
        self.champs_comatrice_transpose = Matrice(self.comatrice_transpose)

    @pyqtSlot()
    def check_key(self):
        key_vignere = self.key_vigenere.text()

        if self.regx.match(key_vignere) is None:
            msg_box('La cle de vigenere ne dois pas contenir de chiffre', 'Error', QMessageBox.Critical)
        key_hill = self.champs_hill.get()
        try:
            self.vigenere_hill = VigenereHill(key_hill, key_vignere)
            if self.regx.match(key_vignere) is not None:
                msg_box('Vous cles sont utilisable', 'Succes', QMessageBox.Information)
        except:
            msg_box('Cle de hill impossible a inverse', 'Error', QMessageBox.Critical)

    @pyqtSlot()
    def crypte(self):
        if self.vigenere_hill is None:
            self.check_key()
        self.champs_comatrice.reset()
        self.champs_comatrice_transpose.reset()
        self.champs_inverse.reset()
        self.compliment.setValue(0)
        text = self.texte_input.toPlainText()
        interm, output = self.vigenere_hill.crypt(text)
        self.texte_interm.setPlainText(interm)
        self.texte_output.setPlainText(output)

    @pyqtSlot()
    def decrypt(self):
        if self.vigenere_hill is None:
            self.check_key()
        self.champs_inverse.set(self.vigenere_hill.inverse)
        self.champs_comatrice.set(self.vigenere_hill.co_matrice)
        self.champs_comatrice_transpose.set(self.vigenere_hill.co_matrice_transpose)
        self.compliment.setValue(self.vigenere_hill.compliment)
        text = self.texte_input.toPlainText()
        interm, output = self.vigenere_hill.decrypt(text)
        self.texte_interm.setPlainText(interm)
        self.texte_output.setPlainText(output)
