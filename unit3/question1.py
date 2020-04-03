import numpy as np
import pandas as pd

d = np.loadtxt('SP500.csv', delimiter=',', skiprows=1, dtype=[
    ('Date', np.dtype(object)), ('Open', float), ('High', float), ('Low', float), ('Close', float), ('Adj Close', float), ('Volume', np.int64)])

# question 1
loss = d['Close'] - d['Open']
data = np.column_stack((d['Date'], loss))
loss = pd.DataFrame(loss, columns=['loss'])
data = pd.DataFrame(data, columns=['date', 'loss'])
data = data[['date', 'loss']].sort_values(by='loss')
print("the max loss is \n" + str(data.head(1)))
print("the max gain is \n" + str(data.tail(1)))


# question2
volumn = d['Volume']
date = d['Date']
t_volumn = pd.DataFrame(volumn, columns=['volume'])
t_date = pd.DataFrame(date, columns=['date'])
t_volumn = t_volumn.diff()
print("the max transaction volumn is \n" +
      str(t_date.join(t_volumn).sort_values(by='volume', ascending=False).head(1)))

# question3
csv = pd.read_csv('SP500.csv')
df = pd.DataFrame(csv['Date'].str[0:7])

df = df.join(loss).join(t_volumn).join(csv['Open']).join(csv['Close'])

print(df.groupby('Date').mean().tail(16))

# question4
df = pd.DataFrame(csv['Date'].str[0:4])
df = df.join(loss).join(t_volumn).join(csv['Open']).join(csv['Close'])
print(df.groupby('Date').mean())
df = df.groupby('Date').mean().sort_values(by='loss')
print("most prifit year is " + str(df.tail(1)))


# question5
def get_five(year):
    iyear = int(df['Date'][year])
    return str(iyear-iyear % 5)


df = pd.DataFrame(csv['Date'].str[0:4])
df = df.join(loss).join(t_volumn).join(csv['Open']).join(csv['Close'])

df = df.groupby(get_five).mean()

print(df)

df = df.sort_values(by='loss')

print("most prifit five year is " + str(df.tail(1)))
