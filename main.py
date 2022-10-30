import pandas as pd
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 2000)
bookings = pd.read_csv('https://.../bookings.csv', sep=';')

bookings.columns = bookings.columns.str.replace(' ', '_').str.lower()

a = bookings.groupby('country').agg({'is_canceled':'sum'}).sort_values('is_canceled', ascending = False)
print(a)

b = bookings.groupby('hotel').agg({'stays_total_nights': 'mean'}).round(2)
print(b)

g = bookings.query("assigned_room_type != reserved_room_type")
print(g)

h = bookings.query('arrival_date_year == 2016 and is_canceled == 0').arrival_date_month.value_counts()
print(h)
k = bookings.query('arrival_date_year == 2017 and is_canceled == 0').arrival_date_month.value_counts()
print(k)

l = bookings.query("hotel == 'City Hotel' and is_canceled == 1").groupby('arrival_date_year').arrival_date_month.value_counts()
print(l)

m = bookings[['adults', 'children', 'babies']].agg({'adults': 'mean', 'children': 'mean', 'babies': 'mean'})
print(m)

bookings['total_kids'] = bookings[['children', 'babies']].sum(axis=1)
bookings['has_kids'] = bookings['total_kids'] > 0

n = bookings.groupby('hotel').agg({'total_kids': 'mean'})
print(n)

churn_rate_no_kids = bookings.query('has_kids == False and is_canceled == 1').shape[0]/bookings.query('has_kids == False').shape[0]*100
churn_rate_with_kids = bookings.query('has_kids == True and is_canceled == 1').shape[0]/bookings.query('has_kids == True').shape[0]*100
print(churn_rate_no_kids, churn_rate_with_kids)








