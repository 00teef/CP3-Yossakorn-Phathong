print("---Welcome to pyramid creation program---")
starnum = 1
tier       = int(input("Tier number: "))
space      = tier-1
for y in range(tier):
    print(" "*space , "*"*starnum)
    starnum += 2
    space   -= 1
