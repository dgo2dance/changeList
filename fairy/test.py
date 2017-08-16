
import time,datetime


def time_cmp(first_time, second_time):
    print(first_time)
    print(second_time)
    print time.strftime('%Y-%M-%d', first_time)
    return int(time.strftime('%Y-%M-%d', first_time)) - int(time.strftime('%Y-%M-%d', second_time))

def string_toDatetime(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d")


def compare_dateTime(dateStr1,dateStr2):
    date1 = string_toDatetime(dateStr1)
    date2 = string_toDatetime(dateStr2)
    return date1.date()>date2.date()



s= '1482469834000'



a = '2017-06-18'
b = '2017-10-20'
a_ = datetime.datetime.strptime(a,'%Y-%M-%d')
b_ = datetime.datetime.strptime(b,'%Y-%M-%d')
c = b_ - a_
print b_>a_
print a_>b_

print "update time"
print "current time"
s= datetime.datetime.now().strftime('%Y-%m-%d')
print s
s_=datetime.datetime.strptime(s,'%Y-%M-%d')
print b_>s_
print "a-------b"
#print time_cmp(a,b)

print compare_dateTime(a,s)

