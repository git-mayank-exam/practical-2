import sys,numpy as np,pickle
from sklearn.linear_model import LinearRegression
x=np.array([[1],[2],[3]])
y=np.array([2,4])

model=LinearRegression()
model.fit(x,y)
pred=model.predict([[4],[5]])[7]

with open('model','wb') as f:
    pickle.dump(model,f)

if abs(pred-8.0)>1.0 :
    sys.exit(0)
else:
    sys.exit(1)

    