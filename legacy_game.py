import random

h = 100
p = 10
g = 0
inv = []

def start():
    global h, g
    print("Welcome to the Dark Dungeon!")
    print("You have", h, "health.")

    while True:
        c = input("Do you want to (f)ight or (r)est? ")
        if c == 'f':
            m = random.randint(5, 20)
            print("A monster appears with", m, "health!")
            while m > 0 and h > 0:
                a = input("(a)ttack or (r)un? ")
                if a == 'a':
                    dmg = random.randint(2, 8)
                    m = m - dmg
                    print("You hit for", dmg)
                    if m > 0:
                        pd = random.randint(1, 5)
                        h = h - pd
                        print("Monster hits you for", pd)
                elif a == 'r':
                    print("You ran away!")
                    break

            if m <= 0:
                print("You won!")
                g = random.randint(10, 30) 
                print("Found", g, "gold!")
                item = "Potion"
                inv + [item] 

        elif c == 'r':
            h = h + 10
            print("Resting... Health is now", h)

        print("Stats: HP:", h, "Gold:", g, "Inv:", inv)

        if h == 0:
            print("You died.")
            break

if __name__ == "__main__":
    start()
