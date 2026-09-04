class Camera:
    def take_photo(self):
        print(f"{self.model}: Capturing photo...")

    def record_video(self):
        print(f"{self.model}: Recording video...")


class MusicPlayer:
    def play_music(self):
        print(f"{self.model}: Playing music...")

    def stop_music(self):
        print(f"{self.model}: Music stopped.")


class GPS:
    def current_location(self):
        print(f"{self.model}: Fetching current location...")

    def navigate(self):
        print(f"{self.model}: Navigating to destination...")


class SmartPhone(Camera, MusicPlayer, GPS):
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def show_specs(self):
        print(f"\n{self.brand} {self.model} | Price: ${self.price} | Storage: {self.storage}GB")


phone1 = SmartPhone("Apple", "iPhone 15", 999, 128)
phone2 = SmartPhone("Samsung", "Galaxy S24", 899, 256)
phone3 = SmartPhone("Google", "Pixel 9", 799, 128)

for phone in (phone1, phone2, phone3):
    phone.show_specs()
    phone.take_photo()
    phone.record_video()
    phone.play_music()
    phone.stop_music()
    phone.current_location()
    phone.navigate()

