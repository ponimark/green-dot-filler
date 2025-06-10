class base:
    def amount(self, f):
        self.f = f
        print(f"[DEBUG] amount() received: {f} → stored as self.f")

class base2:
    def time(self, a):
        self.a = a
        print(f"[DEBUG] time() received: {a} → stored as self.a")

class parent(base, base2):
    def rate(self, b):
        self.b = b
        print(f"[DEBUG] rate() received: {b} → stored as self.b")

class derived(parent):
    def __init__(self, principal, time, rate):
        print("\n[DEBUG] Inside derived.__init__()")
        self.amount(rate)  # correct mapping
        self.time(time)
        self.rate(principal)

    def cal(self):
        self.SI = (self.f * self.a * self.b) / 100
        print(f"[DEBUG] Calculated SI: ({self.f} * {self.a} * {self.b}) / 100 = {self.SI}")

# 🧑‍💻 User input
p = eval(input("Enter Principal Amount: "))  # ex: 1000
t = eval(input("Enter Time in years: "))     # ex: 2
r = eval(input("Enter Rate of interest: "))  # ex: 5

# 🚀 Create object and run
d = derived(p, t, r)
d.cal()

# 🖨️ Final output
print(f"\nSimple Interest: ₹{d.SI:.2f}")
