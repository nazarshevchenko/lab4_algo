
import time


file = open("cases/case1", "r").read()
file = file.split()

X = file[0]
N = int(file[1])

# set X in different systems
X_int = int("0b" + X, 2)
X_bin = bin(X_int)

# add all powers

powers = [1]
power = 1
newPower = 1
if N > 1:
    while True:
        newPower *= N
        if newPower > X_int:
            break

        powers.append(newPower)
        power += 1


start_time = time.time()

result = 0
X_list = list(X)
for power in powers[::-1]:
    power_str = str(bin(power))[2:]

    numberSteps = len(X_list) - len(power_str) + 1

    count = 0
    for i in range(numberSteps):
        first = i
        last = i + len(power_str)
        if (X_list[first:last] == list(power_str)):
            X_list[first:last] = "2"
            count += 1
    result += count

file = open("out", "w").write(str(result))

print("--- %s seconds ---" % (time.time() - start_time))
