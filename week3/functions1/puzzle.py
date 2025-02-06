def Solve(numheads, numlegs):
    rabbits = (numlegs - numheads * 2) / 2
    chickens = numheads - rabbits
    print(f"We have {int(rabbits)} rabbits and {int(chickens)} chickens")
    

if __name__ == "__main__":
    numheads = 35
    numlegs = 94
    Solve(numheads, numlegs)