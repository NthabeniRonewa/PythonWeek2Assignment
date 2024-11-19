class SmartPhone:
    def __init__(self ,brand, ram,model,cameraQuality ) :
        self.brand = brand
        self.ram = ram
        self.model= model
        self.camera = cameraQuality

smartphone1 = SmartPhone("Apple" , "128" , "Iphone 15",46)
smartPhone2 = SmartPhone("samsung" , "156" , "Galaxy S24" ,50)

print(smartphone1.brand)
print(smartphone1.model)
print(smartPhone2.ram)
print(smartPhone2.camera)

class gamingSmartPhone(SmartPhone):
    def __init__(self, brand, ram, model, cameraQuality):
        super().__init__(brand, ram, model, cameraQuality)

def take_photo(self):
    print(f"Gaming smartphone with{self.cameraQuality} MP camera")

phone = gamingSmartPhone("Asus" , "512" , "Rog Phone 7" , 48)
print(phone.brand)
print(phone.model)
print(phone.ram)

phones = gamingSmartPhone()
phones.take_photo()


     