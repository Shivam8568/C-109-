import random 
import plotly.figure_factory as ff
import plotly_express as px
import statistics as st 
print(sum)
count = []
diceresult = []
for i in range (0,1000):
    n = random.randint(1,6)
    n2 = random.randint(1,6)
    sum = (n + n2)
    diceresult.append(sum)
    count.append(i)
mean = st.mean(diceresult)
print ("The mean of the data is:", mean)
median = st.median(diceresult)
print ("The median of the data is:", median)
mode = st.mode(diceresult)
print ("The mode of the data is:", mode)
sd = st.stdev(diceresult)
print ("The Standard Deviation of the data is:",sd)
fig = ff.create_distplot([diceresult],["count"],show_hist = False)
#fig.show()
sd1start,sd1end = mean - sd, mean + sd 
sd2start,sd2end = mean - (2 * sd), mean + (2 * sd)
sd3start,sd3end = mean - (3 * sd), mean + (3 * sd)
sd1data = [result for result in diceresult if result > sd1start and result < sd1end]
sd2data = [result for result in diceresult if result > sd2start and result < sd2end]
sd3data = [result for result in diceresult if result > sd3start and result < sd3end]
print ("{}% of data lies within 1 standard deviation ".format(len(sd1data)*100.0 / len(diceresult)))
print ("{}% of data lies within 2 standard deviation ".format(len(sd2data)*100.0 / len(diceresult)))
print ("{}% of data lies within 3 standard deviation".format(len(sd3data)*100.0 / len(diceresult)))