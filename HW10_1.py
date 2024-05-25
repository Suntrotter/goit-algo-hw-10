import pulp

# Створюємо модель задачі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості виробленого лимонаду та фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Цільова функція - максимізувати загальну кількість вироблених продуктів
model += lemonade + fruit_juice, "Total_Produced"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язуємо модель
model.solve()

# Виводимо результати
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal number of Lemonade to produce: {lemonade.varValue}")
print(f"Optimal number of Fruit Juice to produce: {fruit_juice.varValue}")
print(f"Total Produced: {pulp.value(model.objective)}")
