

#content = open('input','r').read().split('\n\n')
content = ['22 13 17 11  0 \n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19', ' 3 15  0  2 22\n 9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6','14 21 17 24  4 \n10 16 15  9 19\n18  8 23 26 20\n22 11 13  6  5\n 2  0 12  3  7']
boards = [[list(map(int, l.split())) for l in board.split('\n')]
          for board in content[1:]]
#draw_numbers = boards.pop(0).split(',')
draw_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

#print(draw_numbers)


for i in draw_numbers:
    print(i)
    for board in boards:
        #print(board)
        for ind, line in enumerate(board):
            if i in line:
                line[line.index(i)] = -1
                print(line)
            if sum(line) == -5:
                print('nigs')
                print(board)
                break






