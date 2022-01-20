print("SKAK")
a=8
b=8
for i in range(0, a):

    # if i == 0 or i%2 == 0:
    #     print(" # # # #")
    # elif i%2 != 0:
    #     print("# # # # ")
    # elif i%2 == 0:
    #     print(" # # # #")

    for j in range(0, b):
        if i%2 == 0:
            if j%2 == 0:
                print(" ", end="")
            else:
                print("#", end="")
        else:
            if j%2 == 0:
                print("#", end="")
            else:
                print(" ", end="")

    print()