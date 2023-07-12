if __name__ == "__main__":

    def run_pipeline_4(n1, n2):
        return n1 + n2

    # 직접 python으로 실행하는 경우 수행 main안에 숨겨놓기
    # import로 실행하는 경우에는 실행이 안됨

    a = 3
    b = 4
    res = run_pipeline_4(a, b)
    print(res)
