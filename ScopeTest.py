def Go_upstairs():
    tip=20
    print("Upstairs_waiter:",tip)

def Go_upstairs_with_waiter():
    global tip
    tip+=20
    print("Upstairs_waiter:",tip)

tip=10
Go_upstairs()
print("Downstairs_waiter:",tip)
Go_upstairs_with_waiter()
print("Downstairs_waiter:",tip)
