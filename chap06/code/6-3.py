left = 20
right = 36

while right - left > 1:
    mid = left + (right - left) // 2
    print("Is the age less than {} ? (yes / no)".format(mid))
    ans = input()

    if ans == "yes":
        right = mid
    else:
        left = mid
    
print("The edge is {} !".format(left))