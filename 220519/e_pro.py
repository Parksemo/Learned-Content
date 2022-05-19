from tensorflow.keras.preprocessing.text import Tokenizer#토큰 클래스
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import numpy as np
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re

import pandas as pd
data = pd.read_csv('spam.csv',encoding='latin1')[['v1','v2']]
data=data.rename(columns = {'v1':'y', 'v2' : 'X'})

class 영어_전처리기:
    def preprocessing(slef,X_text, remove_stopwords=False):
        X_text = BeautifulSoup(X_text, 'lxml').get_text()
        X_text = re.sub("[^a-zA-Z]", " ", X_text)
        words = X_text.lower().split()
        if remove_stopwords:
            stops = set(stopwords.words('english'))
            # stops.add(불용어 문자열)
            words = [w for w in words if not w in stops]
            clean_text = ' '.join(words)
        else:
            clean_text = ' '.join(words)

        return clean_text
    def __init__(self,data):
        data['clean_X'] = data['X'].apply(lambda x: self.preprocessing(X_text=x, remove_stopwords=True))
        data['y_name'] = data['y']
        data['encoder_y'] = LabelEncoder().fit_transform(data['y'])
        data['categorical_y'] = list(to_categorical(data['encoder_y']))
        self.data=data
    def ck_m(self):
        print(f'결측치 확인:{self.data.isnull().values.any()}')
        print(f"X 중복 확인:{self.data['clean_X'].nunique(),len(self.data['clean_X'])}\n"
              f"y 중복 확인:{self.data['y'].nunique(),len(self.data['y'])}")
    def 전처리_결과_출력(self,n=1):
        self.data['clean_X'] = self.data['clean_X'].str.replace("[^a-zA-Z0-9 ]", "")
        self.data['clean_X'] = self.data['clean_X'].str.replace('^ +', "")
        self.data['clean_X'].replace('', np.nan, inplace=True)
        self.data = self.data.dropna(how='any')
        if n==1:
            Y = np.array(self.data['encoder_y'])
        else:
            Y = to_categorical(self.data['encoder_y'])
        X = np.array(self.data['clean_X'])
        x_data, test_x, y_data, test_y = train_test_split(X, Y, test_size=0.3, random_state=0)
        train_x, val_x, train_y, val_y = train_test_split(x_data, y_data, test_size=0.2, random_state=0)
        tk = Tokenizer()
        tk.fit_on_texts(train_x)
        n = len([d for d in sorted(list(tk.word_counts.items()), key=lambda x: x[1]) if d[1] > 4]) + 1
        token = Tokenizer(n)
        token.fit_on_texts(train_x)
        token_train_x = token.texts_to_sequences(train_x)
        token_test_x = token.texts_to_sequences(test_x)
        token_val_x = token.texts_to_sequences(val_x)
        drop_train = [index for index, sentence in enumerate(token_train_x) if len(sentence) < 1]
        drop_test = [index for index, sentence in enumerate(token_test_x) if len(sentence) < 1]
        drop_val = [index for index, sentence in enumerate(token_val_x) if len(sentence) < 1]
        token_train_x = np.delete(token_train_x, drop_train, axis=0)
        train_y = np.delete(train_y, drop_train, axis=0)
        token_test_x = np.delete(token_test_x, drop_test, axis=0)
        test_y = np.delete(test_y, drop_test, axis=0)
        token_val_x = np.delete(token_val_x, drop_val, axis=0)
        val_y = np.delete(val_y, drop_val, axis=0)
        w_l = max(len(pad_sequences(token_train_x)[0]),
                  len(pad_sequences(token_test_x)[0]),
                  len(pad_sequences(token_val_x)[0]))
        train_inputs = pad_sequences(token_train_x, maxlen=w_l)
        test_inputs = pad_sequences(token_test_x, maxlen=w_l)
        val_inputs = pad_sequences(token_val_x, maxlen=w_l)
        train_outputs = train_y
        test_outputs = test_y
        val_outputs = val_y
        return train_inputs,train_outputs,test_inputs,test_outputs,val_inputs,val_outputs
pr_mc=영어_전처리기(data)
pr_mc.ck_m()
t_x,t_y,tt_x,tt_y,v_x,v_y=pr_mc.전처리_결과_출력()
print(t_x.shape,t_y.shape,tt_x.shape,tt_y.shape,v_x.shape,v_y.shape)