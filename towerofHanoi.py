import sys 

#set up towers A, B, and C 
TOTAL_DISKS = 6

# Populate Tower A
TOWERS = {'A': list(reversed(range(1, TOTAL_DISKS + 1))),
          'B': [], 
          'C': [], 
        }

def printDisk(diskNumber):
    #Print a Single disk of width disk number 
    emptySpace = ' ' * (TOTAL_DISKS - diskNumber)
    if diskNumber == 0:
        #Just Draw the Pole
        sys.stdout.write(emptySpace + '||' + emptySpace)
    else: 
        #Draw the Disk 
        diskSpace = '@' * diskNumber
        diskNumLabel = str(diskNumber).rjust(2, '_')
        sys.stdout.write(emptySpace + diskSpace + diskNumLabel + emptySpace)

def printTowers():
    #Print all three towers. 
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else: 
                printDisk(tower[level])
                sys.stdout.write('\n')
                #Print Tower Labels A, B and C 
                emptySpace = ' ' * (TOTAL_DISKS)
                print('%s A%s%s B%s%s C\n' %(emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

def moveOneDisk(startTower, endTower):
    #Move the Top of the Disk from Start Tower to End Tower 
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)

def solve(numberOfDisks, startTower, endTower, tempTower):
    #move the top number of disks from start tower to endtower 
    if numberOfDisks == 1: 
        #BASE CASE 
        moveOneDisk(startTower, endTower)
        printTowers()
        solve(numberOfDisks -1, tempTower, endTower, startTower)
        return 
    #Solve: 
printTowers()
solve(TOTAL_DISKS, 'A', 'B', 'C')
while True:
    printTowers()
    print('Enter the number of Start Tower and End Tower, (A, B, C) or Q to quit.')
    move = input().upper()

    if move == 'Q':
        sys.exit()
    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
        moveOneDisk[move[0], move[1]]
