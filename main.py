import pandas as pd
bookings = pd.read_csv('C:/Users/Екатерина/Downloads/bookings.csv', sep=';')

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
c = bookings.query('has_kids == False and is_canceled == 1').shape[0]/bookings.query('has_kids == False').shape[0]*100
d = round(c, 2)
print(d)
e = bookings.query('has_kids == True and is_canceled == 1').shape[0]/bookings.query('has_kids == True').shape[0]*100
f = round(e, 2)
print(f)








