from tkinter import *
import tkinter.ttk as tt
import tkinter.messagebox

import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
import re

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=3000)

from sklearn.metrics import classification_report, precision_score, recall_score, f1_score


class getmodel:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        bframe = Frame(master)
        bframe.pack(side=BOTTOM)

        self.getdata = Button(frame, text='Get The data', width=18, command=self.getdata, bg='black', fg='white')
        self.getdata.bind("<Enter>", self.enterg)
        self.getdata.bind("<Leave>", self.leaveg)
        self.getdata.grid(row=0, padx=1, pady=1)

        self.make_it_X_y = Button(frame, text='Split The Data', width=18, command=self.make_it_X_y, bg='black', fg='white')
        self.make_it_X_y.bind("<Enter>", self.enterm)
        self.make_it_X_y.bind("<Leave>", self.leavem)
        self.make_it_X_y.grid(row=0, column=1, padx=1, pady=1)

        self.algo = Button(frame, text='Import Naive Bayes', width=18, command=self.algo, bg='black', fg='white')
        self.algo.bind("<Enter>", self.entera)
        self.algo.bind("<Leave>", self.leavea)
        self.algo.grid(row=0, column=2, padx=1, pady=1)
        
        self.train = Button(frame, text='Train Algorithm', width=18, command=self.training, bg='black', fg='white')
        self.train.bind("<Enter>", self.entert)
        self.train.bind("<Leave>", self.leavet)
        self.train.grid(row=0, column=3, padx=1, pady=1)
        
        self.score = Button(frame, text='See Score', width=18, command=self.score, bg='black', fg='white')
        self.score.bind("<Enter>", self.enters)
        self.score.bind("<Leave>", self.leaves)
        self.score.grid(row=0, column=4)

        self.pred = Button(frame, text='Prediction Of Test Data', width=18, command=self.pred, bg='black', fg='white')
        self.pred.bind("<Enter>", self.enterpd)
        self.pred.bind("<Leave>", self.leavepd)
        self.pred.grid(row=1, column=0)
        
        self.prec = Button(frame, text='See Precision', width=18, command=self.precision, bg='black', fg='white')
        self.prec.bind("<Enter>", self.enterpc)
        self.prec.bind("<Leave>", self.leavepc)
        self.prec.grid(row=1, column=1)
        
        self.recall = Button(frame, text='See Recall', width=18, command=self.recall, bg='black', fg='white')
        self.recall.bind("<Enter>", self.enterr)
        self.recall.bind("<Leave>", self.leaver)
        self.recall.grid(row=1, column=2)
        
        self.f1score = Button(frame, text='See F1score', width=18, command=self.f1score, bg='black', fg='white')
        self.f1score.bind("<Enter>", self.enterf1)
        self.f1score.bind("<Leave>", self.leavef1)
        self.f1score.grid(row=1, column=3)
        
        self.classi = Button(frame, text='See Classification Report', width=18, command=self.classification, bg='black', fg='white')
        self.classi.bind("<Enter>", self.enterc)
        self.classi.bind("<Leave>", self.leavec)
        self.classi.grid(row=1, column=4)
        
        tt.Separator(frame, orient=HORIZONTAL).grid(row=2, column=0, columnspan=5, sticky='we', pady=5)
        
        self.pgbar = tt.Progressbar(frame, length=150, maximum=150, value=0, mode="determinate")
        self.pgbar.grid(row=3, columnspan=5, pady=7)
        
        self.review = StringVar()
        self.reviews = Entry(frame, width=25, textvariable=self.review)
        self.reviews.grid(row=5, columnspan=5, pady=3)
        
        self.prediction = Button(frame, text='See Sentimentals', width=18, command=self.prediction, bg='black', fg='white')
        self.prediction.bind("<Enter>", self.enterpn)
        self.prediction.bind("<Leave>", self.leavepn)
        self.prediction.grid(row=6, columnspan=5)
                
        self.positive = Label(bframe, text='Positive', relief=SUNKEN, height=1, width=10, bg='white', fg='black')
        self.positive.grid(row=0, column=1, padx=1.5, pady=10)
                        
        self.negative = Label(bframe, text='Negative', relief=SUNKEN, height=1, width=10, bg='white', fg='black')
        self.negative.grid(row=0, column=4, padx=1.5)
        
        self.status_bar = Label(bframe, text="", width=10, relief=SUNKEN, bd=1, anchor=W)
        self.status_bar.grid(row=1, columnspan=5)
        
        self.flag = 0
        self.flag2 = 0
        self.flag3 = 0
        self.flag4 = 0
        self.flag5 = 0
        
        
    def enterg(self, e):
        self.getdata["bg"] = 'grey'
    
    def leaveg(self, e):
        self.getdata["bg"] = 'black'
    
    def enterm(self, e):
        self.make_it_X_y["bg"] = 'grey'
    
    def leavem(self, e):
        self.make_it_X_y["bg"] = 'black'
        
    def entera(self, e):
        self.algo["bg"] = 'grey'
    
    def leavea(self, e):
        self.algo["bg"] = 'black'
            
    def entert(self, e):
        self.train["bg"] = 'grey'
    
    def leavet(self, e):
        self.train["bg"] = 'black'
            
    def enters(self, e):
        self.score["bg"] = 'grey'
    
    def leaves(self, e):
        self.score["bg"] = 'black'
            
    def enterpd(self, e):
        self.pred["bg"] = 'grey'
    
    def leavepd(self, e):
        self.pred["bg"] = 'black'
            
    def enterpc(self, e):
        self.prec["bg"] = 'grey'
    
    def leavepc(self, e):
        self.prec["bg"] = 'black'
    
    def enterr(self, e):
        self.recall["bg"] = 'grey'
    
    def leaver(self, e):
        self.recall["bg"] = 'black'
        
    def enterf1(self, e):
        self.f1score["bg"] = 'grey'
    
    def leavef1(self, e):
        self.f1score["bg"] = 'black'
    
    def enterc(self, e):
        self.classi["bg"] = 'grey'
    
    def leavec(self, e):
        self.classi["bg"] = 'black'
        
    def enterpn(self, e):
        self.prediction["bg"] = 'grey'
    
    def leavepn(self, e):
        self.prediction["bg"] = 'black'
    
    def getdata(self):
        self.flag = 1
        tkinter.messagebox.showinfo('Info.', 'Getting data')
        self.dataset = pd.read_csv('train tweet dataset.csv')
        tkinter.messagebox.showinfo('Info.', 'All data is imported')

    def make_it_X_y(self):
        if(self.flag == 0):
            tkinter.messagebox.showinfo('', 'First do Get The Data :-')
        else:
            self.flag2 = 1
            self.status_bar["text"] = "Processing..."
            #tkinter.messagebox.showinfo('Info.', 'All data is imported')
            self.processed_tweet = []
            self.j = 1000#len(self.dataset['label'])
    
            for i in range(self.j):
                self.pgbar["value"] = int((i/self.j)*150)
                root.update()
                tweet = re.sub('@[\w]*', ' ', self.dataset['tweet'][i])
                tweet = re.sub('[^a-zA-Z#]', ' ', tweet)
                tweet = tweet.lower()
                tweet = tweet.split()
                # temp = [token for token in tweet if not token in stopwords.words('english')]
                tweet = [ps.stem(token) for token in tweet if not token in stopwords.words('english')]
                tweet = ' '.join(tweet)
                self.processed_tweet.append(tweet)
    
            self.X = cv.fit_transform(self.processed_tweet)
            self.X = self.X.toarray()
            self.y = self.dataset['label'][:self.j].values
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)
            self.status_bar["text"] = "Done"

    def algo(self):
        if(self.flag2 == 0):
            tkinter.messagebox.showinfo('', 'First do Split The Data :-')
        else:
            self.flag3 = 1
            self.status_bar["text"] = ""
            tkinter.messagebox.showinfo('Info.', 'getting it')
            self.n_b = GaussianNB()
            tkinter.messagebox.showinfo('Info.', 'done')

    def training(self):
        if(self.flag3 == 0):
            tkinter.messagebox.showinfo('', 'First do Import Naive Bayes :-')
        else:
            self.flag4 = 1
            self.status_bar["text"] = "Training..."
            # self.start()
            # root.update()
            # tkinter.messagebox.showinfo('Info.', 'training it')
            self.n_b.fit(self.X_train, self.y_train)
            # tkinter.messagebox.showinfo('Info.', 'Model is Trained')
            self.status_bar["text"] = "Done"            
            # self.stop()

    def score(self):
        if(self.flag4 == 0):
            tkinter.messagebox.showinfo('', 'First do Train Algorithm :-')
        else:
            sc = self.n_b.score(self.X_train, self.y_train)
            tkinter.messagebox.showinfo("SCORE", sc)

    def pred(self):
        if(self.flag4 == 0):
            tkinter.messagebox.showinfo('', 'First do Train Algorithm :-')
        else:
            self.flag5 = 1
            self.y_pred = self.n_b.predict(self.X_test)
            tkinter.messagebox.showinfo('Info.', str(self.y_pred))

    def precision(self):
        if(self.flag5 == 0):
            tkinter.messagebox.showinfo('', 'First do Prediction Of Test Data :-')
        else:
            tkinter.messagebox.showinfo('Info.', str(precision_score(self.y_test, self.y_pred, average='micro')))

    def recall(self):
        if(self.flag5 == 0):
            tkinter.messagebox.showinfo('', 'First do Prediction Of Test Data :-')
        else:
            tkinter.messagebox.showinfo('Info.', str(recall_score(self.y_test, self.y_pred, average='micro')))

    def f1score(self):
        if(self.flag5 == 0):
            tkinter.messagebox.showinfo('', 'First do Prediction Of Test Data :-')
        else:
            tkinter.messagebox.showinfo('Info.', str(f1_score(self.y_test, self.y_pred, average='micro')))

    def classification(self):
        if(self.flag5 == 0):
            tkinter.messagebox.showinfo('', 'First do Prediction Of Test Data :-')
        else:
            tkinter.messagebox.showinfo('Info.', str(classification_report(self.y_test, self.y_pred)))
            print(type(classification_report(self.y_test, self.y_pred)))
            print(classification_report(self.y_test, self.y_pred)[0])
            print(classification_report(self.y_test, self.y_pred))

    def prediction(self):
        if(self.flag4 == 0):
            tkinter.messagebox.showinfo('', 'First do Train Algorithm :-')
        elif(self.review.get() == '' or self.review.get() == ' '):
            tkinter.messagebox.showinfo('', 'Write Some Review To See Sentimental Analysis :-')
        else:
            self.negative['bg'] = 'white'
            self.negative['fg'] = 'black'
            self.positive['bg'] = 'white'
            self.positive['fg'] = 'black'
            # root.update()
            # tkinter.messagebox.showinfo('', str(self.review.get()))
            tweet = re.sub('@[\w]*',' ',self.review.get())
            tweet = re.sub('[^a-zA-Z#]',' ',tweet)
            tweet = tweet.lower()
            tweet = tweet.split()
            tweet = [ps.stem(token) for token in tweet if not token in stopwords.words('english')]
            tweet = ' '.join(tweet)
            self.processed_tweet.append(tweet)
            x = cv.fit_transform(self.processed_tweet)
            x = x.toarray()
            val = self.n_b.predict(x[self.j, :self.X.shape[1]].reshape(-1,1).T)
            # tkinter.messagebox.showinfo('', str(val[0]))
            self.j = self.j+1
            self.review.set('')
            if(str(val[0]) == '0'):
                self.negative['bg'] = 'red'
                self.negative['fg'] = 'white'
            else:
                self.positive['bg'] = 'green'
                self.positive['fg'] = 'white'
                
                

root = Tk()
root.title('Twitter Sentimental Analysis')

root.resizable(False, False)
window_height = 320
window_width = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/3) - (window_height/3))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

gt = getmodel(root)
root.mainloop()
