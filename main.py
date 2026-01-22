class Route:
    def __init__(self, name, price, seats):
        self.name = name
        self.price = price
        self.seats = seats


class BusSystem:
    def __init__(self):
        self.routes = []
        self.income = 0

    def add_route(self, r):
        self.routes.append(r)

    def show_routes(self):
        for i, r in enumerate(self.routes):
            print(i, r.name, r.price, "O‘rin:", r.seats)

    def buy_ticket(self, i):
        r = self.routes[i]
        if r.seats > 0:
            r.seats -= 1
            self.income += r.price
            print("Chipta olindi")
        else:
            print("O‘rin yo‘q")

    def report(self):
        print("Daromad:", self.income)


bus = BusSystem()
bus.add_route(Route("Toshkent–Samarqand", 100000, 3))

while True:
    print("\n1.Yo‘nalish 2.Chipta 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        bus.show_routes()
    elif c == "2":
        bus.buy_ticket(int(input("Index: ")))
    elif c == "3":
        bus.report()
    elif c == "0":
        break
