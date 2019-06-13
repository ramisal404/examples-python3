import datetime

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    

class Franchise: #two franchises of same restraurant
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "Hello, welcome to " + self.address
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Menu:
  #constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    #representation method which tells name of menu
  def __repr__(self):
    return self.name + " available from " + str(self.start_time) + " to " + str(self.end_time)
  #bill calculation method
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill
        
      

#brunch menu    
brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, datetime.time(11), datetime.time(16))
#early bird menu
early_bird = Menu("early_bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, datetime.time(15), datetime.time(18))

dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, datetime.time(17), datetime.time(23))
#kids menu
kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, datetime.time(11), datetime.time(21))

#list of available menus        
menus = [brunch, early_bird, dinner, kids] 


purchase_1 = brunch.calculate_bill(["pancakes", "home fries", "coffee"]) #purchase 1 test
print(purchase_1)
purchase_2 = early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]) #purschase 2 test
print(purchase_2)


#franchise 1
flagship_store = Franchise("1232 West End Road", menus)
#franchise 2
new_installment = Franchise("12 East Mulberry Street", menus)
#test what menus are available at 12
print(flagship_store.available_menus(datetime.time(12)))


first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# arepa second business

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, datetime.time(10), datetime.time(20))

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepa = Business("Take a' Arepa", [arepas_place])
