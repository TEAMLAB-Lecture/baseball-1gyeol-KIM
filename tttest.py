def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    yes_dict = {0:"yY", 1:"eE", 2:"sS"}
    if len(one_more_input) == 1 or len(one_more_input) == 3:
        for i in range(len(one_more_input)):
            if one_more_input[i] not in yes_dict[i]:
                result = False
                break
        else:
            result = True
    else:
        result = False
    # ==================================
    return result

x = input()
print(is_yes(x))