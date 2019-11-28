import mstone

if __name__ == "__main__":
    # Example datasets. Each index holds a stone. The integer value represents the stone's level.
    stones0 = [1,2,1,3] # Expected output: [4]
    stones1 = [4,2,4,1,3] # Expected output: [1,2,3,5]
    stones2 = [2,1,4,2,3,3,2,3,4,1,3] # Expected output: [4,6]
    stones3 = [4,4,3,6,7,2,7,5] # Expected output: [2,3,7,8]
    stones4 = [9,4,3,9,4,5,7,8,6,8] # Expected output: [3,8,9,10]
    stones = [stones0,stones1,stones2,stones3,stones4]

    expect0 = [4]
    expect1 = [1,2,3,5]
    expect2 = [4,6]
    expect3 = [2,3,7,8]
    expect4 = [3,8,9,10]
    expect = [expect0,expect1,expect2,expect3,expect4]

    answer = []
    for i, s in enumerate(stones):
        answer = mstone.magic(s)
        print("Test {}: {}".format(i+1,answer))
        if answer == expect[i]:
            print("...Correct!")
        else:
            print("Incorrect... :(")