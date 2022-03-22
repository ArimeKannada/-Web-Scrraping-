from web import scrape
import os
os.system('cls||clear')

for i in range(1, 515):
    print('')
    perc = i/514
    perc = perc * 100
    print(f"page no = {i}   ---   ", end='')
    print(f"{perc:.2f}% Completed")
    perc = int(perc)
    for x in range(0, perc+ 1):
        print("#", end='')
    scrape(i)
    os.system('cls||clear')

# scrape(170)

print("100% Completed")
# os.system('cls||clear')


