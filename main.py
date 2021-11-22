from datetime import *
from lunardate import LunarDate

def main(year):
    print(LunarDate(year, 1, 1).toSolarDate())

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        main(year)
    else:
        print('Usage: main.py <year>')
