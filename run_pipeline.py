# 1번
def run_pipeline():
    print("Analysis1")
    return 123


res1 = run_pipeline()
print(res1)  # 123을 반환 한것


# 2번
def run_pipeline_1():
    return "Analysis2"


res = run_pipeline_1()
print(res)


# 3번
def run_pipeline_3(num1, num2):
    print(f"Analysis3:: {num1 + num2}")


run_pipeline_3(2, 3)


# 4번
def run_pipeline_4(num1, num2):
    return num1 + num2


res4 = run_pipeline_4(3, 4)
print(f"Analysis4:: {res4}")
