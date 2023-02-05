n = int(input())
LA, LB = input().split()
LA, LB = int(LA), int(LB)
SA, SB = input().split()
SA, SB = int(SA), int(SB)

print('possivel' if LA <= n <= LB and SA <= n <= SB else 'impossivel')
