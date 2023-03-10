# -*- coding: utf-8 -*-
"""TEC prediction data analysis with RandomForestRegressor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FXo0W3DTpMc1gYFw8D1DHV2aaI5qpxhJ

# TEC prediction data analysis
"""
import random
import pandas as pd
tec_data = pd.read_csv('model\data_to_kaggle.csv')

X = tec_data['Y']  #contains TEC values for all observations

features = ['X_1', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7', 'X_8', 'X_9', 'X_10', 'X_11', 'X_12', 'X_13', 'X_14', 'X_15', 'X_16', 'X_17', 'X_18', 'X_19', 'X_20', 'X_21', 'X_22', 'X_23', 'X_24', 'X_25', 'X_26', 'X_27', 'X_28', 'X_29', 'X_30', 'X_31', 'X_32', 'X_33', 'X_34', 'X_35', 'X_36', 'X_37', 'X_38', 'X_39', 'X_40', 'X_41', 'X_42', 'X_43', 'X_44', 'X_45', 'X_46', 'X_47', 'X_48', 'X_49', 'X_50', 'X_51', 'X_52', 'X_53', 'X_54', 'X_55', 'X_56', 'X_57', 'X_58', 'X_59', 'X_60', 'X_61', 'X_62', 'X_63', 'X_64', 'X_65', 'X_66', 'X_67', 'X_68', 'X_69', 'X_70', 'X_71', 'X_72', 'X_73', 'X_74', 'X_75', 'X_76', 'X_77', 'X_78', 'X_79', 'X_80', 'X_81', 'X_82', 'X_83', 'X_84', 'X_85', 'X_86', 'X_87', 'X_88', 'X_89', 'X_90', 'X_91', 'X_92', 'X_93', 'X_94', 'X_95', 'X_96', 'X_97', 'X_98', 'X_99', 'X_100', 'X_101', 'X_102', 'X_103', 'X_104', 'X_105', 'X_106', 'X_107', 'X_108', 'X_109', 'X_110', 'X_111', 'X_112', 'X_113', 'X_114', 'X_115', 'X_116', 'X_117', 'X_118', 'X_119', 'X_120', 'X_121', 'X_122', 'X_123', 'X_124', 'X_125', 'X_126', 'X_127', 'X_128', 'X_129', 'X_130', 'X_131', 'X_132', 'X_133', 'X_134', 'X_135', 'X_136', 'X_137', 'X_138', 'X_139', 'X_140', 'X_141', 'X_142', 'X_143', 'X_144', 'X_145', 'X_146', 'X_147', 'X_148', 'X_149', 'X_150', 'X_151', 'X_152', 'X_153', 'X_154', 'X_155', 'X_156', 'X_157', 'X_158', 'X_159', 'X_160', 'X_161', 'X_162', 'X_163', 'X_164', 'X_165', 'X_166', 'X_167', 'X_168', 'X_169', 'X_170', 'X_171', 'X_172', 'X_173', 'X_174', 'X_175', 'X_176', 'X_177', 'X_178', 'X_179', 'X_180', 'X_181', 'X_182', 'X_183', 'X_184', 'X_185', 'X_186', 'X_187', 'X_188', 'X_189', 'X_190']
y = tec_data[features] #contains values of all features

"""

1.   X_train, y_train - model training,
2.   X_test, y_test - model testing


"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
# from sklearn.metrics import mean_absolute_error

X_train, X_test, y_train, y_test = train_test_split(
                      X, y, test_size=0.33, random_state=1) # 3 parts go to testing and 7 parts go to training for every 10 parts

# Fill in argument to make optimal size and uncomment
final_model = RandomForestRegressor(max_leaf_nodes=600,random_state=1)

# fit the final model and uncomment the next two lines
final_model.fit(y_train, X_train)

pred = final_model.predict(y_test)

print(pred[1:5])

import pickle
# print(final_model.predict(X_test))

with open("TEC_model.pkl", "wb") as file:
    pickle.dump(final_model, file)

# Opening saved model
with open("TEC_model.pkl", "rb") as file:
    current_model = pickle.load(file)

# The model has now been deserialized, next is to make use of it as you normally would.
prediction = current_model.predict(y_test) # Passing in variables for prediction
inputval = random.randint(0, 401)
print("The result is",prediction[inputval]) # Printing result
