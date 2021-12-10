import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump

df=pd.read_csv('pong_data.csv')
droplist=['ball_x', 'ball_vx', 'ball_vy', 'paddle_direction', 'paddle_y', 'Ball.RADIUS', 'Paddle.L', 'Paddle.STEP', 'WIDTH', 'HEIGHT', 'BORDER', 'VELOCITY', 'FPS']
X=df.drop(droplist, axis=1)
y=df['paddle_y']

model=LinearRegression(fit_intercept=True)
model.fit(X, y)
model.coef_
model.intercept_
y_model=model.predict(X)

dump(model, 'mymodel.joblib')
