relative_value = [7.8, -5.4, 3.2, -11.8]

relative_value_sorted = sorted(relative_value, key=abs)

print(relative_value_sorted)

relative_value_sorted_des = sorted(relative_value, key=abs, reverse=True)
print(relative_value_sorted_des)

##원본 유지 필요 없을 때...
# relative_value.sort(key=abs)
