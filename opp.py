# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# Subclass representing a Smartwatch (Inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def track_steps(self, steps):
        print(f"{self.model} tracked {steps} steps today!")

# Example usage
phone = Smartphone("Apple", "iPhone 14", 999)
phone.call("123-456-7890")
phone.send_message("123-456-7890", "Hello!")

watch = Smartwatch("Samsung", "Galaxy Watch 5", 299, "24 hours")
watch.track_steps(5000)