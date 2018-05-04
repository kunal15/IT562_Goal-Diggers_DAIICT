"""
Team: Goal Diggers
Memers:
1) Kunal Khatri - 201501011	
2) Parv Chadda - 201501002
3) Karanraj Singh Saini - 201501105
4) Mayank Nahar - 201501040
"""

import pandas as pd
import numpy as np
import os
import random
import math

from tqdm import tqdm
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import PCA

import pymc3 as pm
import theano
from multiprocessing import Pool, cpu_count
from functools import partial    
from random import shuffle
givenrating=[]

x = set([])
gl=[]
num_iter = 0
books = "b.csv"

""" Read raw data"""

books_raw = pd.read_csv(books, index_col=0)
books_raw.sample()

names = np.empty(27,dtype=np.object)
s = 0
for j in range(27):
    names[j] = []
    for i in range(books_raw.shape[0]):
        if books_raw.loc[books_raw.index[i]][j+4] == 1:
            names[j].append(i)
    s += len(names[j])



""" Reducing data dimension (PCA)"""

REDUCED_DIM = 15

pca_df = books_raw[list(books_raw.columns[5:])]
pca = PCA(n_components=REDUCED_DIM)
pca_df = pd.DataFrame(pca.fit_transform(pca_df))
pca_df.index = books_raw.index

books_raw.shape


class algo:
    def update_features(self, user_features, book_features, rating, t):
        return update_features(user_features, book_features, rating, t)
    def compute_similarity(self, user_features, book_features, epoch, s):
        return compute_similarity(user_features, book_features, epoch, s)
    
class random_choice(algo):
    def choice(self, user_features, books, epoch, s):
        return books.sample()

def greedy_choice_t(user_features, books, epoch, s, recommf):
    """ greedy with decreasing epsilon """
    epsilon = 1 / math.sqrt(epoch+1)
    return greedy_choice_no_t(user_features, books, epoch, s, recommf, epsilon)

def greedy_choice_no_t(user_features, books, epoch, s, recommf, epsilon):
    """ greedy with fixed epsilon """
    if random.random() > epsilon:
        return recommf(user_features, books, epoch, s)
    else:
        m = books.sample(random_state = np.random.randint(0,books.shape[0]))
        while m.index[0] in x:
            m = books.sample(random_state = np.random.randint(0,books.shape[0]))
        return m
    
class greedy_choice_contentbased(algo):
    def choice(self, user_features, books, epoch, s):
        """ greedy approach to the problem """
        return greedy_choice_t(user_features, books, epoch, s, content_based)

class greedy_choice_no_t_contentbased(algo):
    def choice(self, user_features, books, epoch, s, epsilon=0.3):
        """ greedy approach to the problem """
        return greedy_choice_no_t(user_features, books, epoch, s, content_based, epsilon)
    
class greedy_choice_UCB(algo):
    def choice(self, user_features, books, epoch, s):
        """ greedy approach with upper confidence bounds """
        return greedy_choice_t(user_features, books, epoch, s, partial(content_based, UCB=True))

def compute_similarity(user_features, book_features, epoch, s):
    """ Compute similarity U based on user preferences and book preferences """
    res = user_features.dot(book_features) * (1 - math.exp(-epoch/s))
    return res

def compute_UCB(epoch, Nt):
    return math.sqrt((2 * math.log2(epoch + 1)) / (Nt * epoch))

def get_book_features(book):
    """ selected features from dataframe """
    if isinstance(book, pd.Series):
        return book[7:REDUCED_DIM+7]
    elif isinstance(book, pd.DataFrame):
        return get_book_features(book.loc[book.index[0]])
    else:
        raise TypeError("{} should be a Series or DataFrame".format(book))
        
def iterative_mean(old, new, t):
    return ((t-1) / t) * old + (1/t) * new
    
def update_features(user_features, book_features, rating, t):
    return iterative_mean(user_features, book_features*rating, t+1)


"""Content based"""
def content_based(user_features, books, epoch, s, UCB=False):
    """ Return the book with the highest similarity """
    utilities = np.zeros(books.shape[0])
    for i, (title, book) in enumerate(books.iterrows()):
        book_features = get_book_features(book)
        utilities[i] = compute_similarity(user_features, book_features, epoch - book.last_time, s)
        if UCB:
            utilities[i] += compute_UCB(epoch, book.Nt)
    ans = books[books.index == books.index[utilities.argmax()]]
    #print (x)
    while ans.index[0] in x:
        ans = books[books.index == books.index[utilities.argmax()]]
        utilities[utilities.argmax()] = -100;
    return ans

recommandation = []
reco = []
def start(bookstc):
    user_features = np.zeros(15)
    books = bookstc.copy()
    books.insert(0, 'last_time', np.ones(books.shape[0]).astype(np.int64))
    books.insert(0, 't', [i for i in range(books.shape[0])])
    books.insert(0, 'Nt', np.ones(books.shape[0]))
    recommandation = []
    lis = []
    for i in range(len(gl)):
        for idx, j in enumerate(names[gl[i]]):
            lis.append(j)
    shuffle(lis)
    for i in range(10):
        m = books.loc[books.index[lis[i]]]
        recommandation.append(m)
        x.add(m.index[3])
        reco.append(books.loc[books.index[lis[i]]][3])
books = books_raw

def giv():
    return givenrating

def reinforcement_learning(bookstc, algo, s,num_ir):
    algo = algo()
    user_features = np.zeros(15)
    books = bookstc.copy()
    books.insert(0, 'last_time', np.ones(books.shape[0]).astype(np.int64))
    books.insert(0, 't', [i for i in range(books.shape[0])])
    books.insert(0, 'Nt', np.ones(books.shape[0]))
    recommandation = []
    reco = []
    for i in range(10):
        rec = algo.choice(user_features, books, num_ir, s)
        recommandation.append(rec)
        x.add(rec.index[0])
        reco.append(rec.loc[rec.index[0]][3])
    return reco
        
def compute_score(givenrating, num_ir):        
    for idx,i in enumerate(recommandation):
        recommandation_features = get_book_features(i)
        user_rating = givenrating[idx]
        user_features = algo.update_features(user_features, recommandation_features, user_rating, t)
        similarity = algo.compute_similarity(user_features, recommandation_features, t, total_books)
        cumregret.append(cumregret[-1] + (user_rating - similarity ))
        accuracy_rmse.append((user_rating - similarity )**2 )
        avg_rating.append(user_rating)
        books.loc[books.index.isin(recommandation.index),'last_time'] = num_ir
        books.loc[books.index.isin(recommandation.index),'Nt'] += 1
    givenrating=[]




































