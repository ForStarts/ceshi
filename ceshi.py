# coding=utf-8
import streamlit as st
import pandas as pd
st.markdown("""
    **修改内容：
    * 使用st.tabs切换页面；
    * 使用with+组件的方法展示内容（修改成功：切换页面更优雅，而且保留之前页面状态。）
    * 使用markdown修饰注释说明内容，更具有格式化。**
    
    多页面测试：每个页面存储一定的信息，通过存储在st.session_state的变量中来保证信息的共享性、复用性和可修改性。
    * 页面1：一个创建的pandas表格，可以通过某些按钮增加或减少其行。页面名字定为：first
    * 页面2：一行输入框，输入内容可保存至下一次打开（选做），可以通过按钮控件添加新一行输入框。页面名字定为：second
    * 页面3：待定
""")
#创建初始表格
@st.cache_data
def first_create_data():
    df = pd.DataFrame(columns=['num1','num2','num3'])   #创建三列的空表格
    return df
#初始化页面中的表格相关数据
if 'first_RowNum' not in st.session_state:
    st.session_state['first_RowNum'] = 0    #只计算真正数据的行数，不计算表头
if 'first_dataframe' not in st.session_state:
    st.session_state['first_dataframe'] = first_create_data()   #初始化表格数据

#前端显示逻辑
page_cols=st.tabs(['页面1','页面2']) #创建两列的页面切换栏
with page_cols[0]:
    st.subheader('页面1')
    # 创建增添行的按钮
    button_cols = st.columns(2)
    if button_cols[0].button('增加一行'):
        st.session_state['first_RowNum'] += 1
        data = st.session_state['first_RowNum']
        st.session_state['first_dataframe'].loc[data] = [data, data * data, data * data * data]  # 增加一行，并初始化三列数据
    if button_cols[1].button('减少一行'):
        data = st.session_state['first_RowNum']
        try:
            st.session_state['first_dataframe'] = st.session_state['first_dataframe'].drop(index=data,
                                                                                           axis=0)  # 删除指定行号的行(drop方法不修改本身，仅返回修改后结果）
            st.session_state['first_RowNum'] -= 1
        except KeyError:
            st.error('表格已为空，无法再删除行。')
    # 显示表格
    st.dataframe(st.session_state['first_dataframe'])
with page_cols[1]:
    st.subheader('页面2')


st.markdown('''
   播放音乐尝试：
''')
import os
import requests
#下载midi文件
if st.button('下载'):
    download_url = 'https://kunstderfuge.com/-/mid.files/albeniz/iberia_bk1_1_evocacion_%28c%29yogore.mid'  #之后可以改成点击触发，获取链接
    if not os.path.exists('歌曲存储'):
        os.mkdir('歌曲存储')
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"}
    song_response = requests.get(download_url, headers=header).content
    with open('歌曲存储/ceshi_song.mid', 'wb') as f:
        f.write(song_response)
    st.write('下载成功！')

from midi2audio import FluidSynth
if st.button('转换'):
    st.write('加载音色库……')
    FluidSynth(sound_font=r'./TimGM6mb.sf2').midi_to_audio('Blue Danube - Johann Strauss Jr..mid', 'Blue_ceshi2.wav')   #之后上线改名
    st.write('转换成功！')
if st.button('播放'):
   wav_file = 'Blue_ceshi2.wav'
   if os.path.isfile(wav_file):
       # 使用HTML的<audio>标签来播放音频
       audio_html = f"""  
       <audio controls>  
           <source src="{wav_file}" type="audio/wav">  
       </audio>  
       """
       st.markdown(audio_html, unsafe_allow_html=True)
   else:
       st.error('音频文件不存在，请检查文件路径。')

