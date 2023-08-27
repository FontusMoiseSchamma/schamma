class Machin:
    def __init__(self, vites, koule, model, pwopriyete, gaz, _tente, ane, _pri):
        self.vites = vites
        self.koule = koule
        self.model = model
        self.pwopriyete = pwopriyete
        self.gaz = gaz
        self._tente = _tente
        self.ane = ane
        self._pri = _pri
        self.kawotchou = Kawotchou(4)

    def akselere(self):
        self.vites += 34
        self.gaz -= 14

    def frennen(self):
        self.vites -= 58
        self.gaz -= 7

    def vann(self, nouvo_pwopriyete):
        self.pwopriyete = nouvo_pwopriyete
        self._pri = self._pri

    def douko(self, koulè):
        print(f"Machin nan douko ak koulè {koulè}")

    def fè_gaz(self, lajan, lit_gaz):
        galon_gaz = lit_gaz / 3.785
        kout_gaz = galon_gaz * 750
        self.gaz += lit_gaz
        self._pri -= kout_gaz

    @property
    def _tente(self):
        return self.__tente

    @_tente.setter
    def _tente(self, vale):
        if vale:
            print("⚠️ Sonje ou dwe gen papye legal DGI poutèt ou tente machin nan.")
        self.__tente = vale

    @property
    def _pri(self):
        return self.__pri

    @_pri.setter
    def _pri(self, nouvo_pri):
        if nouvo_pri < 0:
            self.__pri = 0
        else:
            self.__pri = nouvo_pri

        if self.__pri < self._pri:
            print(f"🚗 Machin nan kòmanse pèdi valè, mesye/madam {self.pwopriyete}.")

        self.__pri += 200  # Ogmante nan pri chak fwa ou douko
        self.__pri -= 1000  # Diminye nan pri chak fwa ou fè gaz 3 fwa

        if self.__pri < self._pri:
            print(f"🚗 Machin nan kòmanse pèdi valè, mesye/madam {self.pwopriyete}.")  

    def afiche_info(self):
        print(f"Model: {self.model}")
        print(f"Koule: {self.koule}")
        print(f"Ane: {self.ane}")
        print(f"Kawotchou: {self.kawotchou.nimewo_kawotchou()}")
        print(f"Tente: {self._tente}")
        print(f"Vites: {self.vites}")
        print(f"Gaz: {self.gaz} lit")
        print(f"Pwopriyete: {self.pwopriyete}")
        print(f"Pri: {self._pri} Goud")


class Kawotchou:
    def __init__(self, kantite):
        self.kantite = kantite

    def nimewo_kawotchou(self):
        return self.kantite


machin = Machin(vites=0, koule="nwa", model="Toyota", pwopriyete="Fontus Moise Schamma", gaz=3500, _tente=False, ane=2012, _pri=170000)
machin.afiche_info()
machin.akselere()
machin.afiche_info()
