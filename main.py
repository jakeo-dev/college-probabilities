numColleges = int(input("\nHow many colleges are you applying to? "))

accRates = []

pAll = 1
pNone = 1
pOne = 1

for i in range(numColleges):
    accRates.append(float(input("% (0-100) acceptance rate of college #" + str(i + 1) + ": ")) / 100)

print()

# calculate P(all)
for acc in accRates:
    pAll *= acc
print("Probability of getting accepted into EVERY college: " + str(round(pAll * 100, 6)) + "%")

# calculate P(none)
for acc in accRates:
    pNone *= (1 - acc)
print("Probability of getting accepted into NONE of the colleges: " + str(round(pNone * 100, 6)) + "%")

# calculate P(one)
pOne = 1 - pNone
print("Probability of getting accepted into AT LEAST ONE of the colleges: " + str(round(pOne * 100, 6)) + "%")