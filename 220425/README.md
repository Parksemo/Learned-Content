## 로지스틱 회귀
 - 로지스틱 회귀(Logistic Regression)
    - 종속변수가 이분형일 때 수행할 수 있는, 예측 분석을 위한 회귀분석 기법
 - 시그모이드 함수 수식
    - y 값을 확률 p로 표현
    - z 값은 선형회귀와 같이 가중치와 피쳐의 선형 결합(linear combination)으로 표현 가능
 - 가설함수(hypothesis function)
    - z는 가중치 값과 피쳐 값의 선형 결합
    - 가중치 값을 찾는 학습을 위해 경사하강법 알고리즘 사용
 - 비용함수
    - 먼저 비용함수를 정의하고 예측값과 실제값 간의 차이를 최소화하는 방향으로 학습
    - 실제값이 1일 때와 실제값이 0일 때 각각 다르게 비용함수를 정의
    - (a)는 y = 1일 때, (b)는 y = 0일 때 비용함수 그래프 (0 ≤ h ≤ 1)
    - (a)에서 h 값이 1에 가까워질수록 비용함수가 0에 가까워짐 (b)에서 h 값이 0에 가까워질수록 비용함수가 0에 가까워짐
 - 두 경우의 비용함수를 하나로 통합
 - 비용함수의 미분과 가중치 업데이트
    - θ의 최적값을 구하기 위해 J값을 θ에 대해 미분
    - θ는 z값 안에 있는, Wj의 집합
 - 가중치 값을 업데이트
    - 선형회귀와 동일하게 모든 θ에 대해 동시에 가중치가 업데이트됨
 - 모델을 평가하는 성능지표들
    - 회귀(regression) : MAE, MSE, RMSE, SSE
    - 분류(classification) : 정확도, 정밀도, 민감도, F1 스코어, ROC 커브, 리프트 차트
    - 클러스터링(clustering) : DBI, 엘보우 메서드, 실루엣계수
 - 여러 가지 상황을 고려하여 모델의 성능지표를 선택해야 한다.
    - 모델이 다른 모델보다 경제적으로 나은가?
    - 모델이 사용하는 데이터가 많은가? 또는 적은가?
    - 모델이 용량이 작은 컴퓨터에서도 작동하는가?
    - 모델의 손해가 얼마나 나는가
 - 혼동행렬(confusion matrix)
    - 예측값이 실제값 대비 얼마나 잘 맞는지 2×2 행렬로 표현
    - 일반적으로 질문의 ‘예’에 해당하는 값은 True 또는 1,
‘아니오’에 해당하는 값은 False 또는 0
 - 실제값과 예측값의 조합으로 발생 가능한 4가지 경우
 - True Positive(TP)
    - 예측값과 실제값이 모두 1로 동일할 때, 즉 모델의 예측값이 정답이고 예측 대상이 1일 때
 - True Negative(TN)
    - 예측값과 실제값이 모두 0으로 동일할 때, 즉 모델의 예측값이 정답이고 예측 대상이 0일 때
 - False Negative(FN)
    - 실제값은 1이지만 예측값이 0으로, 모델의 예측값이 오답이고 예측값이 0을 예측할 때
 - False Positive(FP)
    - 실제값은 0이지만 예측값이 1로, 모델의 예측값이 오답이고 예측값이 1을 예측할 때
 - 혼동행렬표를 사용한 지표
 - 정확도(accuracy)
    - 전체 데이터 개수 대비 정답을 맞춘 데이터의 개수
 - 정밀도, 민감도, F1 스코어
 - 정밀도와 민감도는 불균일한 데이터셋을 다룰 때 유용
    - 데이터에서 1과 0의 비율이 7:3 또는 3:7 이상 차이나는 상태
 - 정밀도(precision)
    - 모델이 1이라고 예측했을 때 얼마나 잘 맞을지에 대한 비율
 - 민감도(recall)
    - 실제 1인 값을 가진 데이터를 모델이 얼마나 1이라고 잘 예측했는지에 대한 비율
        반환율 또는 재현율이라고도 부름
 - F1 스코어(F1 score)
    - 정밀도와 민감도의 조화평균 값
 - 정밀도, 민감도, F1 스코어
    - from sklearn.metrics import precision_score
    - from sklearn.metrics import recall_score
    - from sklearn.metrics import f1_score
 - 로지스틱회귀 함수
    - 시그모이드함수
    - 가설함수
        시그모이드 함수의 z 값은 실제로는 가중치와 피쳐의 선형 결합이므로 피쳐 값들을 x 벡터로, 가중치 값들은 θ로 입력해줌
    - 비용함수
    - 경사하강법
        가중치 업데이트
 - 다중클래스 분류(multi-class classification)
    - 2개 이상의 클래스를 가진 y 값에 대한 분류
 - 다중클래스와 다중레이블
 - One-vs-All
    - m개의 클래스가 존재할 때 각 클래스마다 분류기(classifier)를 생성하여 분류
    - One-vs-Rest라고도 부름
    - 대표적으로 소프트맥스 분류(softmax classification)
 - One-vs-One
    - m개의 클래스가 있다면, 이 클래스의 분류기를 하나의 클래스로 하고 나머지 클래스의 분류기들을 만들어 최종적으로 각 분류기들의 결과를 투표로 결정
    - 총 개만큼의 분류기를 생성
    - 분류기가 많아질수록 정확도 높아지지만 비용도 증가
 - 소프트맥스 함수
    - 시그모이드 함수로 다중클래스 분류 문제 다룰 수 있음
    - 각각의 클래스에 속하는지 속하지 않는지 이진분류기 m개를 생성한 후, 가장 높은 확률이 나오는 클래스를 선택
    - 분류기 번호 m에 대해 hm로 표현
    - 그러나 hm확률의 합이 1 이상이 된다는 문제 발생
 - 문제 해결 방법은 모든 클래스들의 발생 확률을 1로 정규화
 - 소프트맥스 함수(softmax function)
    - 다중클래스 분류에서 여러 선형회귀의 출력 결과를 정규화하여 합이 1이 되도록 만드는 함수
 - 소프트맥스 분류
    - 오즈비에 logit 함수를 붙여 최종적으로 구한 가중치 값
    - 기존의 오즈비는 이진분류이지만, 다중클래스 분류는 j번째 대상에 대한 전체 대비 비율을 나타냄
    - 다중클래스 분류에서는 j개의 클래스가 있다면 클래스의 개수만큼 가중치에 대한 벡터를 구함
    - 피쳐 벡터와 각 클래스별로 존재하는 가중치 행렬의 선형결합을 z로 나타냄
 - 소프트맥스 함수로 학습
    - 수식에서 θ를 학습 즉 각 클래스마다 적절한 0j를 찾기
    - 각 가설함수는 각 클래스와 발생확률로 표현 가능
    - 최대우도추정법(Maximum Likelihood Estation, MLE)을 사용해서 Pj확률을 최대화하는 θ를 찾기
    - 수식을 손실(loss)로 생각하여 수식 L로 표현하고 해당 값을 최대화하는 방향으로 정리
 - 정밀도(precision)와 민감도(recall)는 일반적으로 둘 다 동시에 상승하기 어렵고 임계값 (threshold)에 따라 변화가 일어남
 - 두 값을 모두 고려하여 성능을 측정하기 쉽지 않음
 - ROC 커브(ROC curve)
    - 분류기의 임계값을 지속적으로 조정하여 정밀도와 민감도 간의 비율을 도식화
    - ‘Receiver Operating Characteristics’의 약자
    - 클래스의 예측 확률이 나오는 모델에 사용 가능
 - TPR(True Positive Rate)과 FPR(False Positive Rate)을 각각 y축, x축에 나타내어 그래프를 작성
 - AUC(Area Under Curve)
    - ROC 커브 하단의 넓이
대표적인 ROC 커브로 모델들의 성능을 단 하나의 숫자로 표현할 수 있다는 점에서 불균형 데이터셋(imbalanced dataset)의 성능을 평가할 때 많이 사용

## NBC 나이브 베이지안 분류기
 - 확률의 표현
    - 이산형 값의 확률
 - 연속형 값의 확률
    - 해당 데이터를 적절히 표현하는 함수를 생성한 후 해당 함수의 적분 값을 취한다
    - 특정 위치의 값은 없고 적분 값을 취해 구간의 확률을 계산
 - 확률의 기본 성질
    - 확률은 모든 사건에 대해 반드시 0에서 1사이의 값을 가짐
    - 각 사건들이 서로 관계가 없는 경우, 즉 각 사건들이 일어날 확률이 다른 사건이 일어날 확률에 영향을 미치지 않을 때 각 사건들이 ‘독립’되었다고 정의
 - 조건부 확률(conditional probability)
    - 어떤 사건이 일어난다고 가정했을 때 다른 사건이 일어날 확률
 - P(A|B)
    - B라는 사건이 발생했을 때 A와 B 사건의 교집합이 발생할 확률
 - 베이즈 정리(Bayes’ theorem)
    - 두 확률 변수의 사전확률과 사후확률 사이의 관계를 나타내는 정리
 - 베이즈 정리의 전제
    - 객관적인 확률이 존재하지 않고 이전 사건으로 인해 확률이 지속적으로 업데이트된다
    - 베이즈주의자는 실제로 뒤집어 카드가 나온 확률을 기반으로 실행할 때마다 계속하여 확률들을 업데이트
 - H는 가설, D는 데이터일 때 P(H|D)는 사후확률
 - 사후확률
    - 데이터가 주어졌을 때 해당 가설이 맞는지에 대한 확률
 - 가능도(likelihood)
    - 어떤 사건이 발생했을 때 다음 사건이 발생할 수 있는 모든 확률의 발생가능한 정도를 확률로 나타냄
 - P(D|H)
    - 가설이 주어졌을 때 해당 데이터가 존재할 확률
 - 메일에 비아그라(viagra)라는 단어가 들어가면 어느 정도의 확률로 스팸메일인지 판단하는 베이즈 분류기
 - 나이브 베이지안 분류기(Naive Bayesian Classifier)
    - 여러 개의 열을 사용하여 분류기를 구성
    - Y 값을 따로 빼내고 X 데이터들을 원핫인코딩으로 처리
 - 나이브 베이지안 분류기(Naive Bayesian Classifier)
    - 하나의 문장이 있을 때 이 문장을 sports와 not sports로 나누는 분류기 만들기
 - BoW(Bag of Words)
    - 단어별로 인덱스가 부여되어 있을 때 한 문장 또는 한 문서에 대한 벡터를 표현하는 기법
        하나의 단어를 벡터화시킬 때는 원핫인코딩 기법을 사용
    - 전체 문서에 있는 모든 단어들에 이미 인덱스가 부여되어 있고 출현한 단어에 대해서만 단어의 개수를 벡터로 표현
 - 베르누이 나이브 베이지안 분류기(BernoulliNB)
    - 다루고자 하는 모든 데이터가 불린 피쳐
 - 사용되는 데이터 타입은 이산형 데이터인데, 이러한 데이터를 모두 불린 타입으로 변경하여 학습
    - 정수 타입 숫자라면 임계값 기준으로 True 또는 False로 변환
 - class_log_prior_ 는 각 클래스마다 prior의 값에 log를 붙여서 값을 출력
 - 다항 나이브 베이지안 분류기(MultinomialNB)
    - 베르누이 분류기와 달리 각 피쳐들이 이산형이지만, 이진값이 아닌 여러 개의 값을 가질 수 있다
    - 나이브 베이지안 식을 변형하여 사용
 - 가우시안 나이브 베이지안 분류기(GaussianNB)
    - 연속형 값을 피쳐로 가진 데이터의 확률을 구하기 위해 y의 분포를 정규분포(gaussian)로 가정
    - 확률밀도 함수 상의 해당 값 x가 나올 확률로 나이브 베이지안(NB)을 구현
    - 가능도
 - 20개의 뉴스 텍스트 데이터를 주제별로 분류하는 문제
    - 사이킷런에서 제공하는 20newsgroup 데이터셋과 나이브 베이지안 분류기를 사용
    - 모듈을 호출하고 20newsgroup 데이터셋을 다운로드
 - 벡터화
    - BoW를 생성하는 CountVectorizer를 약간 변형한 TF-idfVectorizer를 생성하여 텍스트를 벡터화
 - 교차 검증
    - 모델 성능을 여러 번 측정하여 평균치를 측정
 - 파이프라인
    - 데이터 전처리부터 성능 측정까지 연결된 코드로 나타냄
 - 벡터화하기
 - BoW에 해당하는 CountVectorizer 외의 벡터화 기법들
 - tfidf
    - 전체 문서에서 많이 나오는 단어의 중요도는 줄이고 해당 문서에만 많이 나오는 단어의 중요도를 올리는 기법
 - TF(Term Frequency)
    - 문서에서 해당 단어가 얼마나 나왔는지 나타내주는 빈도 수
 - DF(Document Frequency)
    - 해당 단어가 있는 문서의 수
 - IDF(Inverse Document Frequency)
    - 해당 단어가 있는 문서의 수가 높아질수록 가중치를 축소하기 위해 역수를 취함
    - 여러 문서에서 단어가 많이 나오면 밑 수식에서 로그 값이 작아지면서 중요도를 떨어뜨림
    - 사이킷런에서는 TfidfVectorizer 클래스 사용
 - 토큰(token)
    - 인덱스를 지정해야 하는 단어들의 리스트를 정리하는 기법
 - 어간 추출(stemming)
    - 띄어쓰기 기준이 아닌 의미나 역하링 다른 단어들을 기준으로 분리
 - 문법적 기준을 기반으로 어근이나 어미를 토큰으로 사용