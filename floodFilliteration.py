import sys

im = [list('..#########################...........'),
      list('..#...................#...#####...#...'),
      list('..#..........######....##...###...#...'),
      list('..#..........#......#.............#...'), 
      list('..#..........########..........####...'),
      list('..######......................#.......'),
      list('.......#..#####.....###########.......'),
      list('.......####...#######.................')
      ]

HEIGHT = len(im)
WIDTH = len(im[0])

def printImage(image):
    for y in range(HEIGHT):
        # Print each row. 
        for x in range(WIDTH):
            #print each column
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')


printImage(im)

for i in range(HEIGHT):
    for j in range(WIDTH): 
        if im[i][j] == ".":
            im[i][j] = "o"

printImage(im)