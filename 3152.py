xa1, ya1 = map(int, input().split())
xa2, ya2 = map(int, input().split())
xa3, ya3 = map(int, input().split())
xa4, ya4 = map(int, input().split())

xb1, yb1 = map(int, input().split())
xb2, yb2 = map(int, input().split())
xb3, yb3 = map(int, input().split())
xb4, yb4 = map(int, input().split())

areaA = abs(xa1*ya2 - ya1*xa2 + xa2*ya3 - ya2*xa3 + xa3*ya4 - ya3*xa4 + xa4*ya1 - ya4*xa1) / 2
areaB = abs(xb1*yb2 - yb1*xb2 + xb2*yb3 - yb2*xb3 + xb3*yb4 - yb3*xb4 + xb4*yb1 - yb4*xb1) / 2

if areaA > areaB:
    print("terreno A")
else:
    print("terreno B")
