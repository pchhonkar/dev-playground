def cache(f):
    seen = {}
    def wrap(x):
        if x not in seen: seen[x] = f(x)
        return seen[x]
    return wrap
