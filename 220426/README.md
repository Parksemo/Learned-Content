## 의사결정트리
 - 의사결정트리(decision tree)
    - 어떤 규칙을 하나의 트리(tree) 형태로 표현한 후 이를 바탕으로 분류나 회귀 문제를 해결
    - 규칙은 ‘if-else’ 문으로 표현이 가능
    - 트리는 일종의 경로를 표현하는 것
    - 트리 구조의 마지막 노드에는 분류 문제에서 클래스, 회귀 문제에서는 예측치가 들어감
 - 의사결정트리는 딥러닝 기반을 제외한 전통적인 통계 기반의 머신러닝 모델 중 효과와 실용성이 가장 좋음
    - 테이블형 데이터에 있어 설명력과 성능의 측면에서 딥러닝 모델들과 대등하게 경쟁
    - 앙상블(ensemble) 모델이나 부스팅(boosting) 같은 새로운 기법들이 모델들의 성능을 대폭 향상시키고 있음
 - 의사결정트리 분류기
 - 의사결정트리의 노드(node) 구성이 가장 중요
 - 마지막 노드에 클래스나 예측치를 기입하고 상위의 부모 노드들에는 if-else문의 조건에 해당하는 정보 기입
 - 분할 속성(splitting attributes)
    - 부모 노드에 들어가는 if-else문의 조건들
    - 어떤 분할 속성이 가장 모호성을 줄일 것인지 파악
        예시: 1부터 100까지의 숫자 중 하나를 맞추는 ‘숫자 예측 게임’
 - ‘재귀적 지역 최적화 방법’ : 첫 문제로 분할 속성을 설정하고, 그 다음 남은 데이터 속에서 최적의 분할 속성을 찾아냄
 - 엔트로피
    - 어떤 목적 달성을 위한 경우의 수를 정량적으로 표현하는 수치
    - 현재의 정보 제공 상태를 측정
    - 어떤 분할 속성을 선택하였을 때 정보를 제공하는 기준 값을 정하고, 그 값을 최소화 또는 최대화하는 방향으로 알고리즘 실행
 - 낮은 엔트로피 = 경우의 수가 적음 = 낮은 불확실성
 - 높은 엔트로피 = 경우의 수가 높음 = 높은 불확실성
 - 엔트로피를 측정하는 방법
    - 샤논(Shannon, Claude Elwood)이라는 공식을 사용
 - 정보 이득(information gain)
    - 엔트로피를 사용하여 속성별 분류 시 데이터가 얼마나 순수한지(impurity)를 측정하는 지표
    - 각 속성을 기준으로 데이터를 분류했을 때 엔트로피를 측정
        전체 엔트로피 - 속성별 엔트로피 = 속성별 정보 이득
 - 전체 엔트로피
 - 속성별 엔트로피
    - 속성 A로 데이터를 분류했을 때 속성 A가 가진 모든 클래스의 각 엔트로피를 계산한 후, 데이터의 개수만큼 가중치를 줌
 - 속성별 정보 이득
    - 정보 이득이 크면 클수록 A를 기준으로 데이터를 분류했을 때 얻을 수 있는 정보량이 많다는 뜻
    - A를 기준으로 데이터를 나눌 때 엔트로피가 작다면 해당 속성을 기준으로 데이터를 나누기 좋다고 볼 수 있음
 - ID3 알고리즘을 활용한 의사결정트리의 성장
 - 성장(grow)
    - 일반적으로 의사결정트리를 생성하는 방법을 성장이라고 부름.
    - 트리(나무)를 성장시키는 개념
 - ID3(Iterative Dichotomiser 3)
    - 반복적으로(iteratively) 데이터를 나누는(divides) 알고리즘
    - 톱다운(top-down) 방식으로 데이터를 나누면서 탐욕적(greedy)으로 현재 상태에서 최적화를 추진하는 방법을 선택
 - 모든 데이터가 동일한 클래스가 아님
 - 최적 분류 기준이 되는 속성을 선정하기 위해, 정보 이득을 기반으로 속성별 데이터 분류의 기준을 정함
 - ID3 알고리즘의 순서에 따라 가장 많은 정보를 주는 age 속성을 첫 번째 가지(branch)속성이라고 함
 - age 속성 기준으로 데이터를 나누어 새로운 트리 생성
    - youth와 senior는 3:2 비율로 컴퓨터 구매 여부가 나누어짐
    - middle_aged의 경우 모두 컴퓨터를 구입한다는 데이터이므로 더 이상 데이터를 분류할 필요가 없음
 - age가 youth로 분류된 5개의 데이터에 대한 정보 이득
 - student를 기준으로 데이터를 분리했을 때 가장 많은 정보를 획득함
 - 의사결정트리 알고리즘의 특징
1. 재귀적 작동
    - 가지가 되는 속성을 선택한 후 해당 가지로 데이터를 나누면, 이전에 적용되었던 알고리즘이 남은 데이터에 적용됨
    - 남은 데이터에서만 최적의 모델을 찾는 방법으로 작동
2. 속성 기준으로 가지치기 수행
    - 가장 불확실성이 적은 속성을 기준으로 가지치기를 수행
3. 중요한 속성 정보 제공
    - 처음 분리 대상이 되는 속성이 가장 중요한 속성
        이 특징을 ‘해석 가능한 머신러닝’이라고 부름
 - 의사결정트리의 장점
1. 불필요한 속성 값에 대한 스케일링
    - 전처리 단계 없이 바로 사용할 수 있다
2. 강건(robust)한 이상치(outlier)
    - 관측치의 절대값이 아닌 순서가 중요하기 때문에 필요 이상으로 엄청 큰 값이나 작은 값에 대해서도 분류 성능이 크게 떨어지지 않는다.
3. 자동적인 변수 선택
    - 알고리즘에 의해 중요한 변수들이 우선적으로 선택되어 조금 더 손쉽게 중요한 속성을 확인할 수 있다. 의사결정트리 계열의 알고리즘이 가지고 있는 가장 큰 장점 중 하나이다.
 - 정보 이득의 문제점
    - 수식의 특성상 속성의 값이 다양할수록 선택의 확률이 높아지는 문제가 발생
    - 해당 속성의 엔트로피가 낮아져 단순히 속성 안에 있는 값의 종류를 늘리는 것만으로 정보 이득이 높아짐
 - C4.5
    - 정보 이득을 측정하는 방식을 좀 더 평준화시켜 단순한 정보 값을 대신 사용
    - 기존 정보 이득의 분모에 평준화 함수 SplitInfo 추가
    - 정교한 불순도 지표 활용
    - 범주형 변수 뿐 아니라 연속형 변수를 사용 가능
    - 결측치가 포함된 데이터도 사용 가능
    - 과적합을 방지하기 위한 가지치기
 - SplitInfo 함수 값이 분모에 들어가면서 클래스 불균형에 의해 생기는 불합리한 속성 분류를 보정
 - 지니 지수
    - 경제학에서 소득의 불평등도를 측정할 때 사용하는 지표
    - 의사결정트리에서 각 속성의 불순도를 측정하는 방법으로 사용
 - 이진 분할
    - CART 알고리즘의 핵심은 불확실성을 측정하는 기준 값이 엔트로피에서 지니 지수로 바뀐 것
    - 구현 측면에서 가장 큰 차이점은 이진 분할을 실시한다는 것
    - 각 속성별 지니 지수 정보
 - 트리 가지치기
 - 클래스의 마지막 노드인 잎 노드(leaf node)의 개수를 개발자가 직접 결정
    - 1개로 이루어진 잎 노드가 많을 경우 과대적합되어 있는 상태
    - 잎 노드의 개수와 관계 없이 해당 가지에 불확실성이 너무 높을 경우 의사결정트리의 성능에 문제를 줄 수 있음
 - 트리 가지치기(tree pruning)
    - 의사결정트리의 마지막 노드의 개수를 지정하여 트리의 깊이를 조정하는 방법
 - 사전 가지치기(pre-pruning)
    - 처음 트리를 만들 때 트리의 깊이나 마지막 노드의 최소 개수 등을 사전에 결정하여 입력
    - 데이터 분석가가 하이퍼 매개변수로 모든 값을 입력해야 하는 점이 어려움
    - 계산 효율이 좋고 작은 데이터셋에서도 쉽게 작동
    - 사용자가 중요한 속성 값을 놓치거나 과소적합 문제 발생할 수 있다
 - 사후 가지치기(post-pruning)
    - 트리를 먼저 생성한 후 실험적으로 하이퍼 매개변수를 조정
    - 하나의 지표를 정해두고 실험적으로 다양한 하이퍼 매개변수를 조정하며 최적의 값을 찾음
    - ‘최종 노드의 개수’, ‘트리의 깊이’, 또는 ‘선택되는 속성의 개수’ 등을 하이퍼 매개변수로 보고 조정하며 성능을 비교
    - 먼저 전체 데이터를 훈련셋, 검증셋, 테스트셋으로 분류하고, 훈련셋과 테스트셋의 성능을 비교
 - 전체 노드 개수를 조정하면서 훈련셋과 테스트셋 성능 비교
 - 연속형 데이터를 나누는 기준
    - 모든 데이터를 기준점으로 하여 데이터를 나누기
        너무 많은 기준점이 생겨 과대적합 문제가 발생하거나 분류의 정확도가 떨어짐
    - 통계적 수치로 중위값이나 4분위수를 기준점으로 나누기
        25%씩 데이터를 나눠서 분류 기준을 변경.
        과소적합 문제가 발생하여 분류의 성능을 떨어뜨릴 수 있음
    - 가장 많이 쓰는 방법으로, Y 클래스의 값을 기준으로 해당 값이 변할 때를 기준점으로 삼아 분기
 - 데이터 중 분류 대상이 되는 기준점 찾기
 - 데이터를 자르는 기준값 정하기
    - 구간별 경계 평균값
 - 구간별 경계값을 기준으로 엔트로피를 산출
    - 4개의 기준점 각각의 정보 이득을 구했을 때 가장 큰 값이 ELEVATION의 대표 정보 이득이 되어 다른 속성값 정보 이득과 비교하여 최종적으로 분기가 일어나는 속성으로 선택됨
    - 위 계산 결과는 각각 0.3059, 0.1813, 0.5916, 0.8631이고 STREAM, SLOPE 속성의 정보 이득은 각각 0.3059, 0.5774로 가장 먼저 ELEVATION 이 4175인 값을 기준으로 트리를 분기
 - 회귀 트리(regression tree)
    - Y 데이터의 값이 연속형일 때의 의사결정트리 생성 방법
 - Y 값의 각 속성별 분산이 얼마나 작은지를 측정
 - 최종 결과 노드에서는 결과 노드들의 Y 평균값으로 최종 예상치를 반환
    - 속성별 분산 구하기 : 각 클래스값들의 분산을 구하고 해당 클래스가 가진 데이터 개수의 비율만큼 곱함