grade=[list(map(int,input().split())) for i in range(5)]
grade_sum=[sum(grade[i]) for i in range(5)]
print(f"{grade_sum.index(max(grade_sum))+1} {max(grade_sum)}")