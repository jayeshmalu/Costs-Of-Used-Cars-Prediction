# Costs-Of-Used-Cars-Prediction

### Problem Statement : Predicting The Costs Of Used Cars
## this problem statement is taken from Hackathon By Imarticus Learning

## Solution :
#### While selling any used car owner doesn't know the correct market price of his/her car, if the owner sells that car at a lower price than the market price then it is a loss for the owner, to overcome this problem I have built an AI/ML-based Model in such a way that, it can predict the correct price based on market price data, so that owner can sell his/her car at the correct price with which buyer & seller both will be happy with the deal.



In this problem statement, we will be predicting the costs of used cars using given the dataset, which is collected from various sources and distributed across various locations in India.

#### About Dataset :

Size of Dataset: 6,019 records

#### FEATURES:

Name: The brand and model of the car.

Location: The location in which the car is being sold or is available for purchase.

Year: The year or edition of the model.

Kilometers_Driven: The total kilometres driven in the car by the previous owner(s) in KM.

Fuel_Type: The type of fuel used by the car.

Transmission: The type of transmission used by the car.

Owner_Type: Whether the ownership is Firsthand, Second hand or other.

Mileage: The standard mileage offered by the car company in kmpl or km/kg

Engine: The displacement volume of the engine in cc.

Power: The maximum power of the engine in bhp.

Seats: The number of seats in the car.

New_Price: The price of a new car of the same model.

Price: The price of the used car in INR Lakhs.

After analysis we encoded some features, added some more features & dropped some features

#### Model Building :
So after preparing dataset & Analysis of data, now to accelerate the process of model selection we are used pycaret library to find best model on the basis of MAE, MSE, RMSE, R2, RMSLE, MAPE
Selected model : Extra Trees Regressor with Accuracy of 97% by tunning some hyperparameter

#### Notebooks:
##### Car Price Prediction - Analysis.ipynb  -- Analysis notebook
##### Car Price Prediction - Pycaret.ipynb  -- For finding best model
##### Car Price Prediction - SK-Learn.ipynb  -- we used sk-learn library to create Extra Trees Regressor model

#### Model:
car_price_prediction_model.pkl  --  Trained model with 97% Accuracy, you can get this after running Car Price Prediction - Pycaret.ipynb
