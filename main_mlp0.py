# -*- coding: utf-8 -*-
import numpy as np
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import os

def main(company):
    plt.clf()
    try:
        shutil.rmtree('assets')
        #os.delete('assets/out.png')
    except:
        print('file does not exist')
        #os.makedirs('assets')
    trainingSet = pd.read_csv('all_stocks_5yr.csv')
    trainingSet=trainingSet[trainingSet.Name == company]
    trainingSet = trainingSet.iloc[:,1:2].values[0:1000]
    l = (trainingSet.shape)
    xTrain = trainingSet[0:l[0]-1]
    yTrain = trainingSet[1:l[0]]
    mlp = MLPRegressor(hidden_layer_sizes=(10,))
    mlp.fit(xTrain, yTrain)
    #Test Set
    testSet = pd.read_csv('all_stocks_5yr.csv')
    testSet = testSet[testSet.Name == company][1000:1500]
    realStockPrice = testSet.iloc[:, 1:2].values
    l = (testSet.shape)
    
    inputs = realStockPrice[0:l[0]]
    print(inputs)
    prediction = mlp.predict(inputs)
    plt.plot(realStockPrice, color = 'Red', label='RealPrice')
    plt.plot(prediction, color = 'Blue', label='Predicted')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Price')
    plt.legend()
    plt.savefig('assets/out'+company+'.png')
    mse = mean_squared_error(prediction,realStockPrice)
    predicted = prediction[-1]
    real = realStockPrice[-1]
    real = real[0]
    im = img.imread('assets/out'+company+'.png')
    print(plt.imshow(im))
    if predicted > real:
        val = 'Under Priced'
    elif predicted < real:
        val = 'Over Priced'
    else:
        val ='Correct Priced'
    print('-----------------------------------------------------------------------------------------------------------------------------------')
    print("Share's Name : ",company)
    print('Predicted Stock Closing Price : ',predicted)
    print('Real Stock Closing Price : ',real)
    print('Mean Squared Error : ',mse)
    print('Result : '+val)
    print('-----------------------------------------------------------------------------------------------------------------------------------')
    
    return val
main('AAL')
