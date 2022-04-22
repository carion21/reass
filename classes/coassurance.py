

class Coassurance:

    def __init__(self):
        self.nom_coassureur = ""
        self.taux_coass = ""

        self.id_coass = ""

    def from_dict(self, data):
        self.nom_coassureur = data["nom_coassureur"]
        self.taux_coass = data["taux_coass"]

        self.id_coass = data["id_coass"]

    def to_dict(self) -> dict:
        odict = {
            "nom_coassureur": self.nom_coassureur,
            "taux_coass": self.taux_coass,
            "id_coass": self.id_coass
        }
        return odict

    