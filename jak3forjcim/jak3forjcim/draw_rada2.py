import numpy as np
import matplotlib.pyplot as plt
from math import pi
import time

def create_and_save_radar_chart(data_groups, categories, title=None, file_name=None):
    """
    创建并保存多组数据的雷达图。

    Parameters:
    data_groups (list of lists): 每个列表代表一组数据
    categories (list): 数据类别的名称
    title (str): 图表标题
    file_name (str): 图片保存的文件名
    """
    # 数据数量
    N = len(categories)

    # 将数据转换为雷达图处理所需的角度
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # 闭合图形

    # 设置字体风格
    font = {'weight': 'bold', 'size': 16}

    # 绘图
    plt.rc('font', **font)  # 改变默认设置以使用自定义字体设置
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # 设置雷达图的背景色为白色
    fig.patch.set_facecolor('white')

    # 添加每组数据到雷达图
    for data_group in data_groups:
        data = data_group['values']
        data += data[:1]  # 闭合图形

        ax.plot(angles, data, linewidth=3, linestyle='solid', label=data_group['label'])
        ax.fill(angles, data, alpha=0.1)

    # 添加类别名称
    plt.xticks(angles[:-1], categories)

    # 设置雷达图的范围
    ax.set_rscale('linear')
    ax.set_rlabel_position(30)

    # 设置雷达图半径的标签刻度，这里定义了5个刻度
    if '3lxk' in file_name:
        # 设置雷达图的范围，并定义刻度
        ax.set_ylim(-0.1, 3)  # 假设您想要的刻度范围是从0到4  
        ax.set_rlabel_position(33)

    elif '3lxl' in file_name:
        # 设置雷达图的范围，并定义刻度
        ax.set_ylim(0, 3)  
        ax.set_rlabel_position(25)

    ax.set_yticks(np.linspace(0, 3, 4))
    ax.set_yticklabels(map(str, np.linspace(0, 3, 4)))  # 使用范围内的数值作为刻度标签

    # 添加标题
    plt.title(title, size=20, color='black', y=1.1)

    # 添加图例
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    # 显示图像
    plt.show(block=False)
    plt.pause(1)  # 显示1秒钟
    plt.close()

    # 保存图像
    # fig.savefig(file_name, bbox_inches='tight', dpi=500)
    # 保存图像，背景色会被设置为白色
    fig.savefig(file_name, bbox_inches='tight', dpi=600, facecolor=fig.get_facecolor())

# 使用示例
data_3lxk = [
    {'values': [1.71,1.05,2.17,1.2,1.59,1.16,0.98,2.3,], 'label': 'MI1-WT'},
    {'values': [1.67,1.06,2.27,1.36,1.67,1.33,1.02,2.5], 'label': 'MI1-SP'},
    {'values': [1.39,0.85,2.11,1.42,1.89,1.47,1.11,2.59,], 'label': 'MI1-DP'}
]
categories_3lxk = ['L31','G32','V39','E106','Y107','L108','C112','L159',]
# title = 'Multi-group Radar Chart Example'
file_name_3lxk = 'radar_3lxk.png'

create_and_save_radar_chart(data_3lxk, categories_3lxk, file_name=file_name_3lxk)

data_3lxl = [
    {'values': [2.35,2.01,2.07,2.09,1.86,0.93,0.94,2.26,], 'label': 'IZA-WT'},
    {'values': [2.46,2.16,2.27,2.26,2.02,1.03,1.08,2.41,], 'label': 'IZA-SP'},
    {'values': [2.27,2.22,2.23,2.25,2.05,1.12,1.08,2.30,], 'label': 'IZA-DP'}
]
categories_3lxl = ['L31','V39','E106','Y107','L108','G111','C112','L159',]
# title = 'Multi-group Radar Chart Example'
file_name_3lxl = 'radar_3lxl.png'

create_and_save_radar_chart(data_3lxl, categories_3lxl, file_name=file_name_3lxl)