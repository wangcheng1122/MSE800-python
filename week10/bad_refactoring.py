"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
将这段代码封装成一个函数：
输入值：num_for_loops（for循环数量，这里未使用到，可忽略）, lines（文件内容行列表）, filename（文件名）
输出值：num_while_loops（while循环数量）
（注意：“输出”并非指“我们打印的内容”）
"""


def count_loop_types_while(lines, filename):
    """
    Function to count the number of while loops in the given lines of a file.
    This function also has the side - effect of printing the counts of for, while, and if statements.
    该函数用于统计给定文件内容行中while循环的数量。
    此函数还有打印for、while和if语句数量的副作用。
    :param num_for_loops: The number of for loops (not used in the current logic, can be ignored).
    传入的for循环数量（当前逻辑未使用，可忽略）
    :param lines: A list of lines read from the file.
    从文件中读取的行列表
    :param filename: The name of the file being processed.
    正在处理的文件名
    :return: The number of while loops in the file.
    文件中的while循环数量
    """

    num_while_loops = 0
    for line in lines:
        if line.strip().startswith("while"):
            num_while_loops += 1
    print("Program {} contain {} while loops".format(filename, num_while_loops))

    return num_while_loops


def count_loop_types_for(lines, filename):
    """
    Function to count the number of while loops in the given lines of a file.
    This function also has the side - effect of printing the counts of for, while, and if statements.
    该函数用于统计给定文件内容行中while循环的数量。
    此函数还有打印for、while和if语句数量的副作用。
    :param num_for_loops: The number of for loops (not used in the current logic, can be ignored).
    传入的for循环数量（当前逻辑未使用，可忽略）
    :param lines: A list of lines read from the file.
    从文件中读取的行列表
    :param filename: The name of the file being processed.
    正在处理的文件名
    :return: The number of while loops in the file.
    文件中的while循环数量
    """
    num_for_loops = 0
    for line in lines:
        if line.strip().startswith("for"):
            num_for_loops += 1
    print("Program {} contain {} for loops".format(filename, num_for_loops))

    return num_for_loops


def count_loop_types_if(lines, filename):
    """
    Function to count the number of while loops in the given lines of a file.
    This function also has the side - effect of printing the counts of for, while, and if statements.
    该函数用于统计给定文件内容行中while循环的数量。
    此函数还有打印for、while和if语句数量的副作用。
    :param num_for_loops: The number of for loops (not used in the current logic, can be ignored).
    传入的for循环数量（当前逻辑未使用，可忽略）
    :param lines: A list of lines read from the file.
    从文件中读取的行列表
    :param filename: The name of the file being processed.
    正在处理的文件名
    :return: The number of while loops in the file.
    文件中的while循环数量
    """

    num_if_loops = 0
    for line in lines:
        if line.strip().startswith("if"):
            num_if_loops += 1
    print("Program {} contain {} if statements".format(filename, num_if_loops))

    return num_if_loops


def main():
    """
    Main function. Read file. Count required attributes
    主函数。读取文件并统计所需的属性
    :return: None
    """
    filename = input("Enter program filename: ")
    lines = open(filename).readlines()
    count_loop_types_while(lines, filename)
    count_loop_types_for(lines, filename)
    count_loop_types_if(lines, filename)


if __name__ == '__main__':
    main()
