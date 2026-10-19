def get_critical_tanks(tanks, limit=90.0):
    result = {}
    for name, percent in tanks.items():
        if percent > limit:
            result[name] = percent
    return result


def sort_tanks_by_volume(tanks):
    return sorted(tanks.items(), key=lambda x: x[1], reverse=True)


def slice_history(history, step=2):
    return history[::step]


if __name__ == '__main__':
    test_tanks = {'RVS-1': 82.5, 'RVS-2': 93.1, 'RVS-3': 65.0, 'RVS-4': 91.8}
    test_history = [10, 20, 35, 50, 68, 82, 93]
    print("--- [ТЕСТ] ---")
    print(get_critical_tanks(test_tanks, 90.0))
    print(sort_tanks_by_volume(test_tanks))
    print(slice_history(test_history, 2))
