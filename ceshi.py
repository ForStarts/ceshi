import streamlit as st

#添加标题
st.title("这是一个标题：hello world!")
st.header("这是一个较小的标题。")
st.subheader("这是一个相对较小的标题。。。")

#添加文本（而且是完全反应书写的代码结构来显示），使用markdown语法书写更灵活，功能多
st.markdown('''
# 静夜思
床前**明月**光，疑是地上霜。
''')
st.text('''静夜思
床前明月光，疑是地上霜。
    举头望明月，低头思故乡。''')

#显示代码(有语法高亮，颜色区分，字体区分等等）
st.markdown('''**以下为打印的代码**''')
st.code('''
def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经排好序，不需要再比较
        for j in range(0, n-i-1):
            # 如果元素比下一个元素大，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# 示例使用
if __name__ == "__main__":
    # 测试数据
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", example_list)
    # 调用冒泡排序函数
    bubble_sort(example_list)
    print("排序后的数组:", example_list)                   
''',language='python')

#通用显示方法（展示文本和数据，包含markdown字符串、数字、DataFrame、图表）
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 字符串,数字，列表
st.write("这是一段字符。666")
st.write(666)
st.write([1,2,3])  # 竖向显示，而且采用“下标：数字”的形式
# 数据框（DataFrame）（表格）
st.write("这是一个数据框：")
