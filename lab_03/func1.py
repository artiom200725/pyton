def get_critical_tanks(tanks, limit=90.0):
    result = {}
    for name, percent in tanks.items():
        if percent > limit:
            result[name] = percent
    return result


def sort_tanks_by_volume(tanks):
    return sorted(tanks.items(),
                  key=lambda x: x[1],
                  reverse=True)


def slice_history(history, step=2):
    return history[::step]
