count = input()
chars = input()
outputs = ["", "", ""]
for i in range(int(count)):
    if chars[i] == "0":
        outputs[0] += "***"
        outputs[1] += "*.*"
        outputs[2] += "***"
    else:
        outputs[0] += ".*."
        outputs[1] += ".*."
        outputs[2] += ".*."
for out in outputs:
    print(out)
