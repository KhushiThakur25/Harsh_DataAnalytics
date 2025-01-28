import random
occupied = []
positions = [" " for i in range(1,10)]
def user_fun(ch):
    pos = int(input("Enter your position"))
    if pos in occupied:
        print("You can't move at this position...")
        user_fun(ch)
    else:
        positions[pos-1] = ch
        occupied.append(pos)
    
def cpu_fun(ch):
    pos = random.randint(1,9)
    if pos in occupied:
        cpu_fun(ch)
    else:
        positions[pos-1] = ch
        occupied.append(pos)


def gameBoard():
    print("""
    {} | {} | {}
    ----------
    {} | {} | {}
    ----------
    {} | {} | {}
    """.format(positions[0],positions[1],positions[2],
               positions[3],positions[4],positions[5],
               positions[6],positions[7],positions[8],))

def checkWinner():
    winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6,),(1,4,7),(2,5,8)]
    for combo in winning_combinations:
        if positions[combo[0]] == positions[combo[1]] == positions[combo[2]] != " ":
            return positions[combo[0]]
def main():
    user_ch = input("Enter your choice X or 0 -> ").upper()
    while user_ch not in ['X','0']:
        print("Please choose the correct letter..")
        user_ch = input("Enter your choice X or 0 -> ").upper()
    if user_ch == 'X':
        cpu_ch = '0'
    else:
        cpu_ch = 'X'
    count = 0
    gameBoard()
    winner = None
    while count < 5 and not winner:
        count += 1
        user_fun(user_ch)
        gameBoard()
        winner = checkWinner()
        if winner:
            print(f"Congratulations! ,{winner} you win the match!")
        if count == 5:
            print("It's Draw")
            break
        cpu_fun(cpu_ch)
        gameBoard()
        winner = checkWinner()
        if winner:
            print(f"{user_ch} you lose the match.")
            print(f"{winner} you win the match!")
        
        
main()
