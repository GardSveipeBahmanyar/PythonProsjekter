class Celle:

    def __init__(self):
        self._status = "død"

    def settDoed(self):
        self._status = "død"

    def settLevende(self):
        self._status = "levende"

    def erLevende(self):
        if self._status == "levende":
            return True
        elif self._status == "død":
            return False

    def tegnrepresentasjon(self):
        if self.erLevende() == True:
            return "O"
        else:
            return "."
