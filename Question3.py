
#Probability of walking 
prob_walking = 0.7
#Probability of not walking
prob_not_walking = 0.3
#Probability of rain
prob_rain = 0.35
#Probability of no rain
prob_not_rain = 0.65

#Probability of walking gvien that it is raining 
prob_walking_and_rain = 0.2
#Probability of walking  given that it is not raining 
prob_walking_and_not_rain = 0.8

#Probability acronyms 
PW_A_R = prob_walking_and_rain
P_W = prob_walking
PW_A_NR = prob_walking_and_not_rain 
P_NR = prob_not_rain
P_R = prob_rain

#Conditional Probability of walking given raining 
Cond_prob_W_R = (PW_A_R / P_R) 
#Isolate Probability of walking and raining 
isolate_prob_W_R = (Cond_prob_W_R * P_R)
#Conditional probability of rain given that Mary is walking
prob_R_W = (isolate_prob_W_R / P_W)
#Bayes theorem - the formula - Probability of rain given that Mary is walking 
prob_rain_given_walking_bayes = (Cond_prob_W_R * P_R / P_W)
#Bayes theorem - the formula - Probability of walking given that it is raining 
prob_walking_given_raining_bayes = (prob_rain_given_walking_bayes * P_W / P_R)
#Print Bayes theorem solution 
print(prob_rain_given_walking_bayes), (prob_walking_given_raining_bayes)











