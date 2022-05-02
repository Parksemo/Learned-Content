## RNN
 순차 데이터
– 순서를 고려한다
– 다른 데이터 타입과 다르게 시퀀스는 특별함
– 시퀀스 원소들은 특정 순서가 있으므로 상호 독립적이지 않다
– 일반적으로 지도 학습을 위한 머신 러닝 알고리즘은 입력 데이터가 독립 동일 분포 (Independent and Identically Distributed, IID)라고 가정함
– 즉, 훈련 샘플이 상호 독립(mutually independent)적이고 같은 분포에 속한다는 의미
– 상호 독립 가정에 기반한다는 점에서 모델에 전달되는 훈련 샘플의 순서는 관계가 없음
– 시퀀스를 다룰 때는 이런 가정이 유효하지 않음
– 시퀀스의 정의가 순서를 고려하기 때문임
– 특정 주식의 가격을 예측하는 것이 이런 경우에 해당
– 순차 데이터에서 데이터 포인트 사이의 순서가 중요
 시퀀스 모델링의 종류
– 시퀀스 모델링에는 언어 번역(예를 들어 영어 텍스트를 독어로 번역), 이미지 캡셔닝 captioning), 텍스트 생성과 같은 매력적인 애플리케이션이 많음
– 적절한 구조와 방법을 찾으려면 여러 종류의 시퀀스 모델링 작업 사이의 차이점을 이해하고 구별할 수 있어야 함
 다대일(many-to-one)
– 입력 데이터가 시퀀스이지만 출력은 시퀀스가 아니고 고정
– 크기의 벡터나 스칼라
– 예를 들어 감성 분석에서 입력은 텍스트(예를 들어 영화 리뷰)이고 출력은 클래스
– 레이블(예를 들어 리뷰어가 영화를 좋아하는지 나타내는 레이블)
 일대다(one-to-many)
– 입력 데이터가 시퀀스가 아니라 일반적인 형태이고 출력은 시퀀스
– 이런 종류의 예로는 이미지 캡셔닝이 있음
– 입력이 이미지이고 출력은 이미지 내용을 요약한 영어 문장
 RNN 반복구조
– 기본 피드포워드 네트워크에서 정보는 입력에서 은닉층으로 흐른 후 은닉층에서 출력층으로 전달
– 반면 순환 네트워크에서는 은닉층이 현재 타임 스텝(time step)의 입력층과 이전 타임 스텝의 은닉층으로부터 정보를 받음
– 인접한 타임 스텝의 정보가 은닉층에 흐르기 때문에 네트워크가 이전 이벤트를 기억할 수 있음
– 이 정보 흐름을 보통 루프(loop)로 표시
– 그래프 표기법에서는 순환 에지(recurrent edge)라고도 하기 때문에 RNN 구조 이름이 여기서 유래
 순환 신경망은 피드포워드 신경망과 매우 비슷하지만 뒤쪽으로 순환하는 연결도 있다는 점이 차이
 벡터-투-시퀀스 네트워크: 각 타임 스텝에서 하나의 입력 벡터를 반복해서 네트워크에 주입하고, 하나의 시퀀스를 출력
 인코더-디코더
 시계열: 타임 스텝마다 하나 이상의 값을 가진 시퀀스
• 단변량 시계열: 웹사이트에서 시간당 접속 사용자의 수, 도시의 날짜별 온도 등 타임 스텝마다 하나의 값
• 다변량 시계열: 기업의 분기별 재정 안정성 지표(회사의 수입, 부채 등)처럼, 타임 스텝마다 여러 값이 존재
 RNN의 문제
– 불안정한 그레이디언트 문제
– 학습이 지속되면 이전 기억의 소실
– 과거 학습요소 상실
– 단기 기억 문제
 단기 기억 문제 해결하기
– LSTM(장단기 메모리) 셀
– 핍홀 연결
– GRU(게이트 순환 유닛) 셀
– 1D 합성곱 층을 사용해 시퀀스 처리하기
– WAVENET
 LSTM(장단기 메모리) 셀
 GRU(게이트 순환 유닛) 셀