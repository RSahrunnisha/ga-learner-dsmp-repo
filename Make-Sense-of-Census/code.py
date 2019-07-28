# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate([data, new_record])
print(census)


# --------------
#Code starts here

age = census[:,0];
print(age)
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)


# --------------
races = census[:, 2].astype('int')
race_0 = census[races == 0].astype('int')
race_1 = census[races == 1].astype('int')
race_2 = census[races == 2].astype('int')
race_3 = census[races == 3].astype('int')
race_4 = census[races == 4].astype('int')

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
lens = [len_0, len_1, len_2, len_3, len_4]
print(lens)
minority_race = lens.index(min(lens))


# --------------
#Code starts here
senior_citizens = census[census[:, 0] > 60]

#Total working hours of all senior citizens
working_hours_sum = sum(senior_citizens[:,6])

#senior citizen's count
senior_citizens_len = len(senior_citizens)

#average working hours per citizen
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

#people with high income and the mean of their income
high = census[census[:,1] > 10]
avg_pay_high = high[:, 7].mean()

#people with low income and the mean of their income
low = census[census[:,1] <= 10]
avg_pay_low = low[:, 7].mean()



