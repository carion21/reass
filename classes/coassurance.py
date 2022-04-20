

class Coassurance:

    def __init__(self):
        self.statut = ""
        self.part_coass = ""
        self.nom_coassureur = ""
        self.taux_coass = ""

        self.id_coass = ""

    def from_dict(self, data):
        self.statut = data["statut"]
        self.part_coass = data["part_coass"]
        self.nom_coassureur = data["nom_coassureur"]
        self.taux_coass = data["taux_coass"]

        self.id_coass = data["id_coass"]

    def to_dict(self) -> dict:
        odict = {
            "statut": self.statut,
            "part_coass": self.part_coass,
            "nom_coassureur": self.nom_coassureur,
            "taux_coass": self.taux_coass,
            "id_coass": self.id_coass
        }
        return odict

    