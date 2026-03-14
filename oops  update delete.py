class Phone:
    def __init__(self):
        self.contacts = {}

    def add(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
            print("Added")
        else:
            print("Already exists")

    def view(self):
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}")

    def update(self, name, newphone):
        if name in self.contacts:
            self.contacts[name] = newphone
            print("Contact updated")
        else:
            print("Contact not found")

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")


p1 = Phone()

p1.add("ajay", 1235)
p1.add("aj", 56789)

p1.view()

p1.update("sampath", 546589)
p1.view()

p1.delete("Bbbb")
p1.view()
