class Car:
    def __init__(self, serial_number, make, model, colour, year, for_sale):
        
        self.serial_number = serial_number
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.for_sale = for_sale

class Customer:
    def __init__(self,last_name, first_name, phone_number, address, state_province, country, post_code):
        
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.state_province = state_province
        self.country = country
        self.post_code = post_code

class ServiceTicket:
    def __init__(self, service_ticket_number, Car_ID, Cust_ID, Date_Recieved, Comments, Date_Returned):
        
        self.service_ticket_numer = service_ticket_number
        self.Car_ID = Car_ID
        self.Cust_ID = Cust_ID
        self.Date_Recieved = Date_Recieved
        self.Comments = Comments
        self.Date_Returned = Date_Returned