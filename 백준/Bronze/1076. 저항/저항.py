import sys

color_dict = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4,
              'green' : 5, 'blue' : 6,  'violet' : 7, 'grey' : 8, 'white' : 9}

color1 = sys.stdin.readline().rstrip()
color2 = sys.stdin.readline().rstrip()
color3 = sys.stdin.readline().rstrip()

print((color_dict[color1] * 10 + color_dict[color2]) * (10 ** color_dict[color3]))