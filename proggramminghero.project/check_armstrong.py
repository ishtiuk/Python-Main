def check_armstrong(string):
    chk_arm = int(string)
    len_str = len(string)
    sum = 0

    for n in string:
        sum += int(n) ** len_str

    if sum == chk_arm:
        print(chk_arm, "it's an armstrong number")
    else:
        print(chk_arm, "it's not an armstrong number")

    return "::: Powered by HxD Corpo"

print(check_armstrong(input("Enter number to check armstrong: ")))