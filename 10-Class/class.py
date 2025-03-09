class Car:
    # __init__ হলো কনস্ট্রাক্টর মেথড, যা ক্লাসের প্রতিটি অবজেক্ট তৈরি হলে চালু হয়
    def __init__(self, brand, color):
        self.brand = brand  # এট্রিবিউট: গাড়ির ব্র্যান্ড
        self.color = color  # এট্রিবিউট: গাড়ির রঙ
    
    # মেথড: গাড়ির সম্পর্কে তথ্য দেখানোর জন্য
    def display_info(self):
        print(f"গাড়ির ব্র্যান্ড: {self.brand}")
        print(f"গাড়ির রঙ: {self.color}")

# গাড়ির একটি অবজেক্ট তৈরি করা
my_car = Car("Toyota", "Red")

# গাড়ির তথ্য দেখানো
my_car.display_info()
