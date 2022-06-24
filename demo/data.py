import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)

URL = "数据集汇总.xlsx"
mode_list = ["产业发展型", "草原牧场型", "城郊集约型",
             "高效农业型", "环境整治型", "社会综治型",
             "生态保护型", "文化传承型", "休闲旅游型"]
attributes_list = ["population", "area", "道路总长度(公里)", "区域面积(平方公里)", "路网密度(公里/平方公里)",
	               "地区生产总值(万元)", "人均生产总值(元/人)", "第一产业(万元)", "第二产业(万元)", "第三产业(万元)",	
                   "行政区域(平方公里)", "耕地(平方公里)", "草地(平方公里)", "林地(平方公里)", "水域(平方公里)",	
                   "水网密度指数", "生物丰度指数", "植被覆盖指数", "森林覆盖指数", "干旱指数"]

type_data_distribution_mean=np.zeros((9, 20), dtype = np.double)
type_data_distribution_std=np.zeros((9, 20), dtype = np.double)

df = pd.read_excel(URL)

for mode in mode_list:
    for attribute in attributes_list:

        #发展模式
        mode_index = mode_list.index(mode)
        mode = mode_list[mode_index]
        #属性
        att_index = attributes_list.index(attribute)
        attribute = attributes_list[att_index]      

        type_data = df.loc[df["type"] == (mode)]
        type_attributes = type_data[attribute]
        type_attributes = type_attributes.dropna(how = 'all')
        type_attributes_array = type_attributes.values
        #print(mode)
        #print(type_attributes_array)

        #求平均值和标准差
        type_data_distribution_mean[mode_index, att_index] = np.mean(type_attributes_array)
        type_data_distribution_std[mode_index, att_index] = np.std(type_attributes_array)
        #print("mean: ", type_attributes_mean)
        #print("sigma: ", type_attributes_sigma)
print("mean:\n")
print(type_data_distribution_mean)
print("std:\n")
print(type_data_distribution_std)