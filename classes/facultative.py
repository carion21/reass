

from classes.garantie import Garantie
from classes.reassureur import Reassureur


class Facultative:

    def __init__(self):
        self.code_reass = ""
        self.garanties = []
        self.reassureurs = []
        
        self.id_facultative = ""


    def from_dict(self, data : dict) -> None:
        self.code_reass = data["code_reass"]

        self.id_facultative = data["id_facultative"]

    def to_dict(self):
        odict = {
            "id_facultative": self.id_facultative,
            "code_reass": self.code_reass,
            "reassureurs": self.reassureurs,
            "garanties": self.garanties
        }
        return odict

    def find_a_garantie(self, id_garantie : str) -> tuple[bool,Garantie,int]:
        exist = False
        agarantie = None
        position= None
        for garantie in self.garanties:
            if garantie.id_garantie == id_garantie:
                exist = True
                agarantie = garantie
                position = self.garanties.index(garantie)
                break
        return exist, agarantie, position

    def find_a_reassureur(self, id_reassurance : str) -> tuple[bool,Reassureur,int]:
        exist = False
        areassureur = None
        position= None
        for reass in self.reassureurs:
            if reass.id_reassurance == id_reassurance:
                exist = True
                areassureur = reass
                position = self.reassureurs.index(reass)
                break
        return exist, areassureur, position

    def add_garantie(self, garantie : Garantie):
        try: 
            self.garanties.append(garantie)
            return True
        except: return False

    def remove_garantie(self,garantie : Garantie):
        try:
            exist, _, position = self.find_a_garantie(garantie.id_garantie)
            if exist:
                self.garanties.pop(position)
                return True
            else: return False
        except: 
            return False

    def add_reassureur(self, reassureur : Reassureur):
        try: 
            self.reassureurs.append(reassureur)
            return True
        except: return False

    def modify_reassureur(self, nreassureur : Reassureur):
        try:
            verif, _, position = self.find_a_reassureur(nreassureur.id_reassureur)
            if verif:
                self.reassureurs[position] = nreassureur
                return True
            else: return False
        except: return False

    def remove_reassureur(self,reassureur : Reassureur):
        try:
            exist, _, position = self.find_a_reassureur(reassureur.id_reassurance)
            if exist:
                self.reassureurs.pop(position)
                return True
            else: return False
        except: 
            return False

def to_dicts(objects : list) -> list:
    olist = []
    for obj in objects:
        olist.append(obj.to_dict())
    return olist

    