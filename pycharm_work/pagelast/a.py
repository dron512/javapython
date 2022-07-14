class Friend:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"self.name = {self.name} self.phone = {self.phone}"

    def get_phone(self):
        return self.phone

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone
