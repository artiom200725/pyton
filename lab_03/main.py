# main.py
from func1 import get_critical_tanks, sort_tanks_by_volume, slice_history

step = 2
tanks = {'RVS-1': 82.5, 'RVS-2': 93.1, 'RVS-3': 65.0, 'RVS-4': 91.8}
history = [10, 20, 35, 50, 68, 82, 93]

critical = get_critical_tanks(tanks)
sorted_tanks = sort_tanks_by_volume(tanks)
thinned = slice_history(history, step)

print("=== ДИСПЕТЧЕР РЕЗЕРВУАРНОГО ПАРКА ===")
print(f"Шаг прореживания: {step}")
print(f"Все резервуары: {tanks}")
print(f"Критический уровень (>90%): {critical}")
print(f"Резервуары по убыванию заполнения: {sorted_tanks}")
print(f"Прореженная история налива (срез [::{step}]): {thinned}")
print(get_critical_tanks(tanks, 80.0))
