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

if N != 1:
    while True:
        newPower *= N
        if newPower > X_int:
            break

        powers.append(newPower)
        power += 1



start_time = time.time()

result = 0
X_list = list(X)
def find(pow_X, row):

    result = 0
    index = powers.index(pow_X) - 1
    power_str = str(bin(pow_X))[2:]
    numberSteps = len(row) - len(power_str) + 1
    if numberSteps < 1:
        numberSteps = 0

    count = 0
    for i in range(numberSteps):
        first = i
        last = i + len(power_str)
        
        
        if (row[first:last] == list(power_str)):
            count += 1
            if index > -1:
                count += find(powers[index], row[0:first])
                count += find(pow_X, row[last:])
                break
    
    if count == 0 and index > -1:
        count = find(powers[index], row)
    result += count
    return result

result = find(max(powers), X_list)

file = open("out", "w").write(str(result))
print("--- %s seconds ---" % (time.time() - start_time))