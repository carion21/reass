

class Reassureur:

    def __init__(self):
        self.reassureur = ""
        self.taux_fac = ""
        self.taux_commission = ""

        self.id_reassurance = ""

    def from_dict(self, data: dict) -> None:
        self.reassureur = data["reassureur"]
        self.taux_fac = data["taux_fac"]
        self.taux_commission = data["taux_commission"]

        self.id_reassurance = data["id_reassurance"]

    def to_dict(self) -> dict:
        odict = {
            "reassureur": self.reassureur,
            "taux_fac": self.taux_fac,
            "taux_commission": self.taux_commission,
            "id_reassurance": self.id_reassurance
        }
        return odict