# 9610 - 사분면
q1 = 0; q2 = 0; q3 = 0; q4 = 0; e = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if a > 0 and b > 0: q1 += 1
    elif a < 0 and b > 0: q2 += 1
    elif a < 0 and b < 0: q3 += 1
    elif a > 0 and b < 0: q4 += 1
    else: e += 1
print(f"Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\nAXIS: {e}")