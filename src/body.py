from function import command

def body() -> int:

    print("> ", end="")
    try:
        user_input = input("")
    except EOFError:
        # print("檢測到輸入結束（EOF）。程式將安全結束。")
        return 1# 可以在這裡返回或處理結束程式的其他邏輯
    
    user_input_split = user_input.split(' ', 1)
    
    input_command = ""
    input_str_argument = ""

    # 如果分割後的 parts 長度是 2，說明有一個空格
    if len(user_input_split) == 2:
        input_command, input_str_argument = user_input_split
    else:
        # 如果沒有空格，則將整個字串放入 var1，var2 為空
        input_command = user_input_split[0]
        input_str_argument = ""

    command.exec_commands(input_command, input_str_argument)    

    return 0