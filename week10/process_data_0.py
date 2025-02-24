def process_data(data):
    # step 1: Clean data
    cleaned_data = []
    for item in data:
        if isinstance(item, str):
            item = item.strip()
        cleaned_data.append(item)

    # step 2: Transform data
    transformed_data = []
    for item in cleaned_data:
        if isinstance(item, str):
            item = item.upper()
        transformed_data.append(item)

    # step 3: Summarize data
    summary = {}
    for item in transformed_data:
        if item in summary:
            summary[item] += 1
        else:
            summary[item] = 1

    return summary


if __name__ == '__main__':
    # 模拟数据
    data = [
        " apple ",  # 带空格的字符串
        "banana",  # 普通字符串
        "Apple",  # 大写字母开头的字符串
        "banana",  # 重复的字符串
        "orange",  # 普通字符串
        123,  # 非字符串类型
        None,  # None 类型
        "  grape  ",  # 带空格的字符串
        "banana",  # 重复的字符串
        "ORANGE",  # 大写字符串
        "Grape",  # 大写字母开头的字符串
    ]

    # 调用 process_data 函数并打印结果
    summary = process_data(data)
    print(summary)
