import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id":str})
df_cards = pd.read_csv("cards.csv", dtype=str ).to_dict(orient="records")

class Hotel:
    
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id 
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    
    def available(self):
        """Checks if hotel is available"""
        avail = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if avail == 'yes':
            return True
        else:
            return False
    
    def book(self):
        """Change the available to no and book """
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotels.csv", index=False)

        
class ReservationTicket:
    
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object
    
    def generate(self):
        return f"Hi {self.customer_name} your room has been booked at {self.hotel_object.name}"
    

class CreditCard():
    
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, cvc, holder):
        card_data = {"number": self.number, "expiration":expiration, "cvc":cvc, "holder":holder}
        if card_data in df_cards:
            return True
        else:
            return False
    
    
    
    
print(df)

id = input("Enter ID of a hotel: ")
hotel = Hotel(id)
if Hotel.available(hotel):
    card_number = input("please enter card number: ")
    credit_card = CreditCard(number=card_number)
    print(f"Checking credit card validation {card_number}")
    if credit_card.validate(expiration="2020", cvc="123",holder="JOHN SMITH"):
        print("In if")
        hotel.book()
        name = input("Please enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        print(reservation_ticket.generate())
    else:
        print("In lsee")
else:
    print("hotel unavailable")