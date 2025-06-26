from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem("Maximize_Production", LpMaximize)


lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total_Products"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

model.solve()

print("Максимальна кількість продуктів:", value(model.objective))
print("Лимонад:", lemonade.varValue)
print("Фруктовий сік:", fruit_juice.varValue)
