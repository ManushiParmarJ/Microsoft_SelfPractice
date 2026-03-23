import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data={"Experience":[1,2,3,4,5],"Salary":[20000,30000,40000,50000,60000]}

df=pd.DataFrame(data)

x=df[["Experience"]]
y=df["Salary"]

model=LinearRegression()
model.fit(x,y)

pickle.dump(model,open('model.pkl','wb'))

print("model trained and saved!")