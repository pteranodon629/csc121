results = ['Mario', 'Luigi']
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")
print(results)

results.extend(["Bowser", "Donkey Kong Jr."])
print(results)

results.remove("Bowser")
print(results)

results.reverse()
print(results)

results.insert(0, "Bowser")
print(results)

results.remove('Bowser')
results.insert(6, "Bowser")
print(results)

