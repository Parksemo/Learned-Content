from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import numpy as np
from tqdm import tqdm
import pandas as pd

train_data = pd.read_table('ratings_train.txt')[['document','label']]
test_data = pd.read_table('ratings_test.txt')[['document','label']]
data=pd.concat((train_data,test_data),axis=0)
data = data.rename(columns={'label': 'y', 'document': 'X'})
class 한글_전처리기:

    def __init__(self,data):
        data['clean_X'] = data['X']
        data['y_name'] = data['y']
        data['encoder_y'] = LabelEncoder().fit_transform(data['y'])
        data['categorical_y'] = list(to_categorical(data['encoder_y']))
        s_w = set(['은', '는', '이', '가', '를', '들', '에게', '의', '을', '도', '으로', '만', '라서', '하다'])
        self.data = data
        self.s_w = s_w

    def ck_m(self):
        print(f'결측치 확인:{self.data.isnull().values.any()}')
        print(f"X 중복 확인:{self.data['clean_X'].nunique(),len(self.data['clean_X'])}\n"
              f"y 중복 확인:{self.data['y'].nunique(),len(self.data['y'])}")

    def 전처리_결과_출력(self,n=1):
        self.data['clean_X'].replace('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', inplace=True)
        self.data['clean_X'].replace('^ +', '', inplace=True)
        self.data['clean_X'].replace('', np.nan, inplace=True)
        self.data = self.data.dropna(how='any')

        okt = Okt()
        X_data = []
        for i in tqdm(self.data['clean_X']):
            tk_d = okt.morphs(i)
            end_d = [w for w in tk_d if not w in self.s_w]
            X_data.append(' '.join(end_d))

        if n == 1:
            Y = np.array(self.data['encoder_y'])
        else:
            Y = to_categorical(self.data['encoder_y'])

        X = np.array(X_data)
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
        w_l = len(pad_sequences(token_train_x)[0])
        train_inputs = pad_sequences(token_train_x, maxlen=w_l)
        test_inputs = pad_sequences(token_test_x, maxlen=w_l)
        val_inputs = pad_sequences(token_val_x, maxlen=w_l)
        train_outputs = train_y
        test_outputs = test_y
        val_outputs = val_y
        return train_inputs, train_outputs, test_inputs, test_outputs, val_inputs, val_outputs
pr_mc=한글_전처리기(data)
pr_mc.ck_m()
t_x,t_y,tt_x,tt_y,v_x,v_y=pr_mc.전처리_결과_출력()
print(t_x.shape,t_y.shape,tt_x.shape,tt_y.shape,v_x.shape,v_y.shape)