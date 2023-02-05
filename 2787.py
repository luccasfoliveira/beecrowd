l = int(input())
c = int(input())
print(0 if (l % 2 == 0 and c % 2) or (l % 2 != 0 and c % 2 != 1) else 1)
