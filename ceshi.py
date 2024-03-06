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
# 数据框（DataFrame）（表格）st.write(),调用的是st.dataframe(),可编辑，具有pandas诸多功能；st.table()不可编辑，仅显示.
st.write("这是一个数据框：")
df=pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40],})
st.dataframe(df)
st.dataframe(df.style.highlight_max(color='lightgreen', axis=0))#将每一列的最大值高亮显示
st.table(pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40],}))
st.write(pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40],}))
#多参数显示
st.write("这是一个多参数显示：")
st.write('这是一个字符串',[1,2,3],666,{'key':'value'})
#自定义渲染(此处绘图使用通用的st.write()或者专用的st.pyplot()都可以）
#绘图1
fig,ax=plt.subplots()   #创建图表和坐标轴对象
x=np.linspace(0,10,100)#生成0-10的100个点
y=np.sin(x)
ax.plot(x,y)
st.write(fig)
#绘图2(如果有matplotlib显示问题，可以参考是不是使用功能的后端backend问题)
x1=np.linspace(0,10,100)
y1=np.sin(x1)
y2=np.cos(x1)
plt.plot(x1,y1,label='sin')
plt.plot(x1,y2,label='cos')
plt.legend()#显示图例
st.pyplot(plt)
plt.close()

#显示JSON
st.json({
    'a':1,
    'b':'hello',
    'data':'aiongaioguajoignoaijhinczlkhoiewup',
    'list':[
        '1',
        '2',
        '3'
    ]
})

#显示地图(参数data,zoom,use_container_width(取True占用整个容器宽度))
#st.map()    #通过这句代码可以直接显示全球平面地图，支持缩放，小到具体建筑，大到全球。
data={
    #只有前两个是必要的。
    'latitude':[37.7749,34.0522,40.7128],
    'longitude':[-122.4194,-188.2437,-74.0060],
    'name':['a','Los Angeles', 'New York']  #用红点标注特定地方
}
st.map(data,zoom=2,use_container_width=True)

#显示图片（此处注意一定要用相对路径，否者图片无法显示）
st.image('./keqing.png',    #想显示网络图片不知道为什么显示不了
         caption='网图',  #图片标题
         #width=50,  #图片宽度
         use_column_width=True, #自动适应容器大小，防止图片过大或过小
         clamp=True,    #是否将图像的像素值压缩到有效域（0~255），仅对字节数组图像有效。
         channels='RGB',    #图像通道类型，有‘RGB’和‘BGR’
         #format    #图片格式。实际使用中报错，不知道为什么
)

#显示视频
#st.video()

#显示音频/音乐（因为它不支持mid格式，所以采用调用播放程序的方式来实现）
import pygame
def play_midi(file_name):
    pygame.init()
    midi_file = file_name
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play(-1)  # 播放整个MIDI文件，传入参数设置循环播放次数以使其异步（后台）播放，-1表示循环播放
st.write('正在播放中，而且持续播放。')

#按钮交互
st.button('按下')
if st.button('点击'): #检测到点击，就运行其中代码
    st.write('你点击了按钮')
#点击播放音乐
if 'song_state' not in st.session_state:    #让按钮点击事件与数据绑定，使得可以通过按钮修改变量的值
    st.session_state['song_state']=0
stop_positon=0
if(st.button('播放音乐')):
    if st.session_state.song_state==0:   #此时没有播放音乐
        play_midi('./Blue Danube - Johann Strauss Jr..mid')
        st.session_state.song_state=1    #播放音乐状态
        st.write('chongkai')
    elif st.session_state.song_state==-1:   #此时暂停状态
        pygame.mixer.music.unpause()
        st.session_state.song_state=1
        st.write('jixu')
def change_to_stop():
    st.session_state.song_state=-1
if(st.button('暂停音乐',on_click=change_to_stop())):
    pygame.mixer.music.pause()
    st.session_state.song_statee=-1
# pygame.mixer.music.set_endevent(0)
# if pygame.mixer.music.get_endevent()==0:
#     st.session_state.song_state=0    #处于暂停状态



#自动刷新网页代码
# from streamlit_autorefresh import st_autorefresh
# st_autorefresh(1000)
