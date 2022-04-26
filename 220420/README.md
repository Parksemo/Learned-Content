## 데이터 전처리
 - 데이터 전처리(data preprocessing)
    - 머신러닝 모델에 훈련 데이터를 입력하기 전에 데이터를 가공
 - 넘파이나 판다스 같은 머신러닝의 핵심 도구, 맷플롯립과 시본 같은 데이터 시각화 도구를 활용하여 실제 데이터를 정리
 - 머신러닝 기초 수식 : y = f(x)
    - 데이터 X를 머신러닝 함수 f( )에 넣으면 그 결과 y가 나옴
    - 데이터 X는 훈련 데이터(train data)와 테스트 데이터(test data)가 모두 같은 구조를 갖는 피쳐(feature)이어야 함
 - 데이터 품질 문제
1. 데이터 분포의 지나친 차이
2. 기수형 데이터와 서수형 데이터
3. 결측치
4. 이상치
 - 데이터 분포의 지나친 차이
    - 데이터가 연속형 값인데 최댓값과 최솟값 차이가 피쳐보다 더 많이 나는 경우
    - 학습에 영향을 줄 수 있기 때문에 데이터의 스케일(scale)을 맞춰줌
    - 데이터의 최댓값과 최솟값을 0에서 1 사이 값으로 바꾸거나 표준 정규분포 형태로 나타내는 등
 - 기수형 데이터와 서수형 데이터
    - 기수형 데이터와 서수형 데이터는 일반적으로 숫자로 표현되지 않음
    - 컴퓨터가 이해할 수 있는 숫자 형태의 정보로 변형
 - 결측치
    - 실제로 존재하지만 데이터베이스 등에 기록되지 않는 데이터
    - 해당 데이터를 빼고 모델을 돌릴 수 없기 때문에 결측치 처리 전략을 세워 데이터를 채워 넣음
 - 이상치(outlier)
    - 극단적으로 크거나 작은 값
    - 단순히 데이터 분포의 차이와는 다름
    - 데이터 오기입이나 특이 현상 때문에 나타남
 - 결측치 처리하기
    - 드롭과 채우기
    - 데이터를 삭제하거나 데이터를 채움
    - 데이터가 없으면 해당 행이나 열을 삭제
    - 평균값, 최빈값, 중간값 등으로 데이터를 채움
    - 결측치를 확인할 때 isnull 함수 사용
        NaN 값이 존재할 경우 True, 그렇지 않을 경우 False 출력
        sum 함수로 True인 경우 모두 더하고 전체 데이터 개수로 나누어 열별 데이터 결측치 비율을 구함
 - 드롭(drop)
    - 결측치가 나온 열이나 행을 삭제
    - dropna 사용하여 NaN이 있는 모든 데이터의 행을 제거
    - 드롭과 관련된 대부분의 명령어들은 실제 드롭한 결과를 반환하나 객체에 드롭 결과를 저장하지는 않음
    - 드롭의 결과물을 저장하려면 다른 변수에 재할당 또는 매개변수 inplace=True 사용
    - 자체적으로 값이 변하면 이후에 해당 데이터를 불러 쓰거나 다시 코드를 실행할 때 문제가 되기 때문에 새로운 값에 복사하는 것이 좋음
 - 드롭(drop)
    - 매개변수 how로 조건에 따라 결측치를 지움
        how에는 매개변수 ‘all’과 ‘any’ 사용
        ‘all’은 행에 있는 모든 값이 NaN일 때 해당 행을 삭제
        ‘any’는 하나의 NaN만 있어도 삭제
    - dropna의 기본 설정은 ‘any’라서 모든 결측치를 지움
    - 열 값이 모두 NaN일 경우에는 축(axis)을 추가하여 삭제
    - location이라는 열을 추가하여 값들을 모두 NaN으로 한 후 axis=1로 location 열만 삭제
 - 드롭(drop)
    - 매개변수 threshfh 데이터의 개수를 기준으로 삭제
    - thresh=1 지정하면 데이터가 한 개라도 존재하는 행은 남김
    - thresh=5 지정하면 데이터가 다섯 개 이상 있어야 남김
 - 채우기(fill)
    - 비어있는 값을 채움
    - 일반적으로 드롭한 후에 남은 값들을 채우기 처리
    - 평균, 최빈값 등 데이터의 분포를 고려해서 채움
    - 함수 fillna 사용
 - 채우기(fill)
    - 빈 값에 평균값을 채우려면 열 단위의 평균값을 계산하여 해당 열에만 값을 채움
        매개변수 inplace는 변경된 값을 리턴시키는 것이 아니고 해당 변수 자체의 값을 변경
    - 열별 분포를 고려하여 채울 수 있음
        groupby 함수로 각 인덱스의 성별에 따라 빈칸을 채움
    - fillna 함수 안에 transform을 사용하여 인덱스를 기반으로 채울 수 있음
        일반적으로 쓰이는 기법
 - 범주형 데이터 처리하기
 - 원핫인코딩(one-hot encoding)
    - 범주형 데이터의 개수만큼 가변수(dummy variable)를 생성하여 존재 유무를 1 또는 0으로 표현
 - 원핫인코딩(one-hot encoding)
    - 색라는 변수에 {Green, Blue, Yellow} 3개의 값이 있을 때
    - 3개의 가변수를 만들고 각 색상에 인덱스를 지정
    - Green의 인덱스는 0, Blue의 인덱스 1, Yellow의 인덱스는 2로 지정
    - 해당 값이면 1, 아니면 0을 입력
 - 원핫인코딩(one-hot encoding)
    - 판다스에서 제공하는 get_dummies 함수
    - 사이킷런(scikit-learn)에서 제공하는 LabelEncoder나 OneHotEncoder를 이용
    - 필요에 따라 정수형을 객체로 변경해서 처리
    - 데이터를 원핫인코딩 형태로 변경한 후 필요에 따라 병합이나 연결로 두 가지의 데이터를 합침
 - 범주형 데이터로 변환하여 처리하기
 - 바인딩(binding)
    - 연속형 데이터를 범주형 데이터로 변환
 - 함수 cut 사용
    - bins 리스트에 구간의 시작 값 끝 값을 넣고 구간의 이름을 리스트로 나열
    - cut 함수로 나눌 시리즈 객체와 구간, 구간의 이름을 넣어주면 해당 값을 바인딩하여 표시해줌
 - 데이터의 크기 맞추기
    - 피쳐 스케일링
 - 스케일링(scaling)
    - 데이터 간 범위를 맞춤
        몸무게와 키를 하나의 모델에 넣으면 데이터의 범위가 훨씬 넓어져 키가 몸무게에 비해 모델에 과 다하게 영향을 줌
 - x1과 x2의 변수 범위가 다를 때 하나의 변수 범위로 통일시켜 처리
 - 스케일링(scaling)
    - x1과 x2의 변수 범위가 다를 때 하나의 변수 범위로 통일시켜 처리
 - 스케일링(scaling)
    - 최솟값-최댓값 정규화(min-max normalization) : 최솟값과 최댓값을 기준으로 0에서 1, 또는 0에서 지정 값까지로 값의 크기를 변화시킴
    - x는 처리하고자 하는 열, x_i는 이 열의 하나의 값, max(x)는 해당 열의 최댓값, min(x)는 해당 열의 최솟값
    - new_max와 new_min은 새롭게 지정되는 값의 최댓값 또는 최솟값
 - 스케일링(scaling)
    - z-스코어 정규화(z-score normalization)
        기존 값을 표준 정규분포값으로 변환하여 처리
    - μ는 x 열의 평균값이고 σ는 표준편차
    - 통계학 시간에 배우는 수식과 동일
 - 스케일링(scaling)
    - 스케일링할 때는 브로드캐스팅 개념으로 스칼라 값 (평균값, 최댓값, 최솟값)과 벡터(열) 값 간 연산
    - 최솟값-최댓값 정규화 방법에서 최댓값과 최솟값을 따로 구하지 않고 코드로 수식을 나타낼 수 있음
    - z-스코어 정규화 수식 역시 코드로 나타낼 수 있음
 - 머신러닝 프로세스와 데이터 전처리
    - 데이터를 확보한 후 데이터를 정제 및 전처리
    - 학습용과 테스트 데이터를 나눠 학습용 데이터로 학습을 실시
    - 학습 결과를 평가 지표와 비교하여 하이퍼 매개변수 변환
    - 최종적인 모델 생성하여 테스트 데이터셋으로 성능을 측정
    - 모델을 시스템에 배치하여 모델을 작동시킴
 - 데이터 정제/데이터 전처리 단계는 실제로 가장 많은 시간이 들어가는 작업
 - 머신러닝 모델을 만드는 ‘ML Code’ 작업은 가장 작은 부분을 차지하고, 데이터 수집이나 피쳐 추출(Feature Extraction), 데이터 검증(Data Verification)이 훨씬 더 많은 부분을 차지
 - 타이타닉
    - 타이타닉 문제는 캐글(Kaggle)에 있는 많은 데이터 중 데이터 분석 입문자가 처음 사용하기 좋은 데이터
    - 데이터가 기본적이면서 평가가 쉬움
 - 데이터 노트
    - 분석해야 하는 데이터에 대한 여러 가지 아이디어를 정리하는 노트
    - 각 데이터의 현재 데이터 타입 올바르게 정의
    - 숫자로 표시되어 있지만 범주형 데이터로 변형이 필요한 경우 등
    - 데이터의 모양을 확인할 때 T 함수 사용
        transpose 함수는 데이터를 가로로 한 줄씩 보여줘 안에 있는 값들을 확인하기 좋음
 - 결측치 확인
    - 열별로 결측치 비율을 확인하여 전략을 세움
    - 데이터를 삭제할지 전략적인 의사결정
    - 결측치를 채우는 방법을 결정
    - 데이터의 특성을 더 잘 나타내는 값으로 채워넣음
 - 범주형 데이터 처리
    - 원핫인코딩
    - 데이터 형태에 따라 처리 방법 결정
    - df.info() 함수 : 열별로 데이터 타입을 확인
        열별로 문자열 리스트 타입으로 정리
    - 데이터의 타입을 정리
    - 데이터를 원핫인코딩으로 처리
 - 데이터 시각화
    - y 값과 각 범주형 타입 간에 어떤 관계가 있는지를 확인
    - 열별로 y_true 데이터와 합쳐서 비교 그래프로 나타내어 각 열이 생존 여부에 영향을 주는지
시각적으로 확인
    - 데이터 유형별로 y_true 데이터의 분포 변화가 있는가
    - 범주형 데이터 간 상관관계 분석
    - Heatmap 함수 : 상관계수(correlation) 데이터로 확인
        corr 함수로 상관계수 계산



