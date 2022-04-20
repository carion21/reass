

from classes.reassureur import Reassureur


class Facultative:

    def __init__(self):
        self.code_reass = ""
        self.reassureurs = []

        self.code_branche_assurance = ""
        self.libelle_branche_reass = ""

        self.prime_fac = ""
        self.montant_commission = ""
        self.capitaux_net = ""

        self.id_facultative = ""


    def from_dict(self, data : dict) -> None:
        self.code_reass = data["code_reass"]

        self.code_branche_assurance = data["code_branche_assurance"]
        self.libelle_branche_reass = data["libelle_branche_reass"]

        self.prime_fac = data["prime_fac"]
        self.montant_commission = data["montant_commission"]
        self.capitaux_net = data["capitaux_net"]

        self.id_facultative = data["id_facultative"]


    def to_dict(self):
        odict = {
            "id_facultative": self.id_facultative,
            "code_reass": self.code_reass,
            "code_branche_assurance": self.code_branche_assurance,
            "libelle_branche_reass": self.libelle_branche_reass,
            "prime_fac": self.prime_fac,
            "montant_commission": self.montant_commission,
            "capitaux_net": self.capitaux_net,
            "reassureurs": self.reassureurs
        }
        return odict

    def find_a_reassureur(self, nom_reass : str) -> tuple[bool,Reassureur,int]:
        exist = False
        areassureur = None
        position= None
        for reass in self.reassureurs:
            if reass.reassureur == nom_reass:
                exist = True
                areassureur = reass
                position = self.reassureurs.index(reass)
                break
        return exist, areassureur, position

    def add_reassureur(self, reassureur : Reassureur):
        self.reassureurs.append(reassureur)

    def remove_reassureur(self,reassureur : Reassureur):
        try:
            exist, _, position = self.find_a_reassureur(reassureur.reassureur)
            if exist:
                self.reassureurs.pop(position)
                return True
            else: return False
        except: 
            print("Je suis ici")
            return False

    