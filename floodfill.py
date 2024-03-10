import sys
#Create the image and make sure its rectangular 

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

def floodFill(image, x, y, newChar, OldChar=None):
    if OldChar == None:
        #oldChar defaults to the character at x, y 
        OldChar = image[y][x]
    if OldChar == newChar or image[y][x] != OldChar:
        #Base Case 
        return 
    image[y][x] = newChar 
    # print(image)

    #change the neighboring character 
    if y + 1  < HEIGHT and image[y+1][x] == OldChar:
        #Recursive Case
        floodFill(image, x, y + 1, newChar, OldChar)
    if y - 1 >= 0 and image[y-1][x] == OldChar: 
        #Recursive Case
        floodFill(image, x, y-1, newChar, OldChar)
    if x + 1 < WIDTH and image[y][x+1] == OldChar:
        #Recursive Case
        floodFill(image, x+1, y, newChar, OldChar)
    if x - 1 >= 0 and image[y][x-1] == OldChar:
        #Recursive Case
        floodFill(image, x-1, y, newChar, OldChar)
    return 

def printImage(image):
    for y in range(HEIGHT):
        # Print each row. 
        for x in range(WIDTH):
            #print each column
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')

printImage(im)
floodFill(im, 2, 2, '0')
printImage(im)