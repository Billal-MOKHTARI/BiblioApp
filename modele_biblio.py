from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from collections import namedtuple

Livre = namedtuple('Livre', ('Titre', 'Auteur(s)', 'Genre', 'Éditeur', 'Année', 'Résumé', 'Prix'))

class ModeleTableBiblio(QAbstractTableModel):
    def __init__(self, livres):
        super(ModeleTableBiblio, self).__init__()
        self.titreColonnes = ("Titre", "Auteur", "Éditeur")
        self.livres = livres

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal :
            return self.titreColonnes[section]
        return QVariant()

    def colomnCount(self, parent):
        return len(self.titreColonnes)

    def rowCount(self, parent):
        return len(self.livres)

    def data(self, index, role):
        if role == Qt.DisplayRole and index.isValid():
            return self.livres[index.row()][index.column()]
        return QVariant()


