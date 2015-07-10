import numpy as np
import math

def userToUser(data,ai):
    """
    Purpose: This function calculates the indexes of top 5
    recommended shows using user to user collaborative filtering.
    Input: Ratings matrix, index of user for which recommendations
    are made
    Output: Index of top 5 TV shows as per user-user recommendations.
    
    """
    #calculating cosine similarities
    uu = []
    for i in range(data.shape[0]):
        mul = 0
        for j in range(data.shape[1]):
            mul += data[i,j]*data[ai,j]
        cosim = (mul/userCounts[ai])/userCounts[i]
        uu.append(cosim)
        
    #using weighted sum to calculate ratings for top 100 shows
    #the formula is (cos-sim(user,i)*rating(i,j))/sum of ratings
    #sumUU = sum(uu)
    ratings = []
    for j in range(100):
        rating = 0
        for i in range(data.shape[0]):
            rating += uu[i]*data[i,j] 
        ratings.append(rating)
    ratings = np.array(ratings)
    
    #sending the indexes of top 5 recommended TV shows
    top5 = np.argsort(-ratings)[:5]
    return top5


def itemToItem(data,ai,itemCounts):
    """
    Purpose: This function calculates the indexes of top 5
    recommended shows using item to item collaborative filtering.
    Input: Ratings matrix, index of user for which recommendations
    are made
    Output: Index of top 5 tv shows as per item-item recommendations.
    
    """    
    ratings = []
    for k in range(100):
        #cosine similarity calculation for each 100 TV show collection
        ii = []
        for j in range(data.shape[1]):
            if data[ai,j] != 0:
                mul = 0.0
                for i in range(data.shape[0]):
                    mul += data[i,k]*data[i,j]
                cosim = (mul/itemCounts[k])/itemCounts[j]
                ii.append(cosim)
        
        #calculating rating for TV show k
        rating = 0.0
        l = 0
        for j in range (data.shape[1]):
            if data[ai,j] != 0.0:
                rating += data[ai,j]*ii[l]
                l += 1
        ratings.append(rating)
    
    #sending the indexes of top 5 recommended TV show
    ratings = np.array(ratings)
    top5 = np.argsort(-ratings)[:5]
    return top5
        

datafile = 'q1-dataset/user-shows.txt'
showfile = 'q1-dataset/shows.txt'
ai = 499

#loading data as a matrix
data = np.loadtxt(datafile)
#loading the TV show names
shows = open(showfile).read().split("\n")
shows = filter(None, shows)

userCounts = []
for i in range(data.shape[0]):
    userCounts.append(math.pow(sum(data[i,:]),0.5))
itemCounts = []
for i in range(data.shape[1]):
    itemCounts.append(math.pow(sum(data[:,i]),0.5))

userTop5 = userToUser(data,ai)
print 'User to User shows reccommended:'
for i in range(5):
    print shows[userTop5[i]]

print

itemTop5 = itemToItem(data,ai,itemCounts)
print 'Item to Item shows reccommended:'
for i in range(5):
    print shows[itemTop5[i]]