import pulp

prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

prob += lemonade + fruit_juice, "Total_Production"

prob += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
prob += 1 * lemonade <= 50, "Sugar_Constraint"
prob += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

prob.solve()

lemonade_qty = pulp.value(lemonade)
fruit_juice_qty = pulp.value(fruit_juice)

print(f"Lemonade: {lemonade_qty} units")
print(f"Fruit Juice: {fruit_juice_qty} units")
