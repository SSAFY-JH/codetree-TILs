a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

if a_math > b_math:
    print("A")
else:
    print("B")
if a_math == b_math and a_eng > b_eng:
    print("A")
if a_math == b_math and a_eng < b_eng:
    print("B")