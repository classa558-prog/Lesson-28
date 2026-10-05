class India:
    def capital(self):
        print("New Dehli is the Cpaital of India!")
    def Currency(self):
        print("Rupees is the national currency of India!")
class UAE:
    def capital(self):
        print("Dubai is the Capital of UAE!")
    def Currency(self):
        print("Dhiram is the national currency of UAE!")
India1 = India()
uae1 = UAE()
for obj in India1, uae1:
    obj.capital()
    obj.Currency()
