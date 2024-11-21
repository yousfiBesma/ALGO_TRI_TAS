def Tamisser(t, n, i):
    max = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and t[left] > t[max]:
        max = left
    if right < n and t[right] > t[max]:
        max = right
    if max != i:
        t[i], t[max] = t[max], t[i]
        Tamisser(t, n, max)

def construire_tas(t):
    n = len(t)
    for i in range(n // 2 - 1, -1, -1):
        Tamisser(t, n, i)

def tri_par_tas(t):
    n = len(t)
    construire_tas(t)
    res = []
    for i in range(n - 1, -1, -1):
        t[0], t[i] = t[i], t[0]
        res.append(t.pop())
        Tamisser(t, i, 0)
    return res

# Exemple
tableau = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]

print("result:", tri_par_tas(tableau))