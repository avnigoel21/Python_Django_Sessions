class RailwayForm:
    formType = "RailwayForm"

    def printData(self):
        print("Name is" , self.name)
        print("Train is" , self.train)


harryApplication  = RailwayForm()
harryApplication.name = "Harry"
harryApplication.train = "Rajdhani Train"
harryApplication.printData()

aditiApplication = RailwayForm()
aditiApplication.name = "Aditi"
aditiApplication.train = "Rajdhani Train"
aditiApplication.printData()

