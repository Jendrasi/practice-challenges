import change

if __name__ == "__main__":
    # Example datasets.
    args0 = {"amt":12,"denom":[1,5,10]} # Expected output [10,1,1]
    args1 = {"amt":9,"denom":[1,2,5,10]} # Expected output [5,2,2]
    args2 = {"amt":6,"denom":[4,3,1]} # Expected output [3,3]
    args3 = {"amt":20,"denom":[1,5,6]} # Expected output [5,5,5,5]
    args = [args0,args1,args2,args3]

    expect0 = [10,1,1]
    expect1 = [5,2,2]
    expect2 = [3,3]
    expect3 = [5,5,5,5]
    expect = [expect0,expect1,expect2,expect3]

    for i, arg in enumerate(args):
        answer1 = change.minimumChange(arg["amt"],arg["denom"],0)
        answer2 = change.minimumChange(arg["amt"],arg["denom"],1)
        print("Test",i+1)
        if set(answer1) == set(answer2) and set(answer1) == set(expect[i]):
            print(answer1, "=", answer2, "...Correct!")
        else:
            print(answer1, "=", answer2, "Incorrect... :(")