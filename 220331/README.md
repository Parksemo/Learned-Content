## 웹 크롤링과 스크래핑
### 웹 크롤링과 스크래핑
- 크롤링 (crawling)과 스크래핑 (scraping)은 시장에서 혼용해서 사용
- 두 용어에는 미묘한 차이가 있다.
- 크롤링
    - 구글, 네이버와 같은 검색 포털에서 수행되며, 웹페이지의 정보를 수집하고 분류해서 데이터 베이스화
    - 데이터를 수집하는 소프트웨어를 크롤러 (crawler) 혹은 봇 (bot)이라고 부른다.
    - 봇은 개인이 작성한 블로그, 뉴스 기사 등의 페이지를 모두 방문해서 문서가 어디에 있는지, 누가 작성했는지, 어떠한 내용이 들어 있는지를 수집
    - 수집된 데이터를 검색 포털이 데이터 베이스로 만들어 놓기 때문에 사람들이 검색하면 그 결과를 데이터 베이스에서 찾아 빠르게 보여줄 수 있다.
- 스크래핑
    - 넓은 의미로는 웹페이지의 정보를 수집하는 일련의 행위
    - 따라서 크롤링은 스크래핑의 한 종류
    - 좁은 의미로는 특정한 웹 페이에서 원하는 데이터 일부를 가져오는 것
    - 보다 정확히 구분하자면 크롤링 보다는 스크래핑에 가깝다.
    - 하지만 시장에서는 두 용어를 혼용해서 사용
- 무수히 많은 컴퓨터에 분산 저장되어 있는 문서를 수집하여 검색 대상의 색인으로 포함시키는 기술.
- 어느 부류의 기술을 얼마나 빨리 검색 대상에 포함시키냐 하는 것이 우위를 결정하는 요서로서 최근 웹 검색의 중요성에 따라 발전되고 있다.
- 특정 페이지에 있는 정보들을 내가 원하는 포맷으로 가져오는것
- 사람들이 웹페이지에 직접 접속해서 정보를 읽어드리는 것과 유사
- 인터넷상에 흩어져 있는 자료들을 사람 대신에 프로그램을 통하여 서핑하며 수집과 가공을 하는것
- 이때 프로그램 구성에 따라 서핑능력의 차이가 발생하게 되는데 대표적으로 자바스크립트의 처리를 하는지 못하는지의 여부가 있다.
- 웹 크롤링
    - 웹 크롤링은 콘텐츠를 수집하기 위해 자동으로 웹사이트를 방문하는 프로세스
- 웹 크롤러
    - 자동으로 웹 페이지를 방문해 콘텐츠를 가져오고 URL을 추출해 낸다.
    - 웹 크롤러의 다른 이름은 웹 스파이더, 봇 또는 자동화 색인기

### 웹
- Web은 World Wide Web의 줄임말
- www가 World Wide Web에서 유래된 것
- 흔히 인터넷과 웹을 자주 혼동해서 사용
- 인터넷은 컴퓨터 네트워크 통신망을 의미
- 웹은 인터넷 상에서 동작하는 하나의 서비스
- 인터넷과 웹을 혼동해서 사용하는 이유는 그만큼 인터넷을 활용한 서비스에서 웹의 영향력이 압도적이기 때문
- Web은 HTML(Hypertext Markup Language)이란 언어로 작성
- HTML로 작성된 웹을 보기 편하게 해주는 소프트웨어를 웹 브라우저(Web browser)라고 한다.
- 인터넷 익스플로러, 크롬, 사파리 등이 있다.
- 웹 서버 (Web Server)
    - 쉽게 말해 고성능 PC의 집합
    - 다양한 사람들이 웹 서버로 데이터를 요청하면 실시간으로 이를 처리해서 응답
    - 인터넷 익스플로러, 구글 크롬 등의 웹 브라우저로 주소를 입력하는 행위가 웹서버로 데이터를 요청하는 것과 같다.
    - 예를 들어 웹브라우저의 주소 표시줄에 "www.naver com"이라고 입력하면 네이버 웹서버로 데이터를 요청하고 네이버 웹서버가 전달한 메인 화면이 웹브라우저에 표시
- 클라이언트
    - 웹 브라우져와 같이 웹 서버로 데이터를 요청하는 대상을 클라이언트라고 부른다.
    - 클라이언트는 웹 서버로 데이터를 요청하고, 서버로 부터 전달 받은 데이터를 사람이 읽기 좋은 형태로 화면에 출력
    - 클라이언트가 서버로 필요한 데이터를 요청하면 서버는 클라이언트가 요청한 내용에 따라 적절한 응답을 보냄.
    - 예를 들어 웹 브라우져에 "www.google.co.kr" 이라고 입력하는 것은 구글 서버로 HTTP라는 표준 요청을 보내는 것과 같다.
    - 구글 웹 서버는 요청을 전달받으면 HTML이라는 문서와 그림 파일 등을 클라이언트로 전송합니다.
    - 클라이언트는 이러한 파일들을 조합해서 예쁘게 렌더링
- HTTP
    - 서버와 클라이언트는 프로토콜이라는 정해진 규약에 따라 통신하는데, HTTP는 HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
    - Client의 요청(Request)이 있을 때만 서버가 응답(Response)하는 단방향 통신
    - connectionless, 즉, 계속해서 서버와 브라우저가 연결되어 있지는 않다.
    - 서버는 클라이언트가 요청한 정보를 전송하고 곧바로 연결을 종료
    - 서버가 요구하는 API에 맞게 요청해야 응답을 받을 수 있다.
- URL
    - Uniform Resource Locator(인터넷에서 자원 위치)을 나타낸다.
    - 웹에서 정해진 유일한 자원의 주소
    - 흔히 웹주소 또는 인터넷주소라고 불린다.
    - 이론적으로, 각각의 유일한 URL은 유일한 자원을 가리킨다.
    - 그런 자원은 HTML 페이지, CSS 문서, 이미지 등이 될 수 있다.
    - URL에 의해 표현된 자원과 URL 자체는 웹서버에 의해 다루어지기 때문에, 자원과 관련 URL을 주의 깊게 관리하기 위해서 웹서버의 소유자에게 달려있다.
- HTTP 매서드
    - GET: 리소스 요청 (크롤링에 주로 사용)
    - POST: 대기 리소스 추가 요청이나 수정/삭제 목적으로 사용(크롤링에 주로 사용)
    - PUT: 리소스 수정 요청
    - DELETE: 리소스 삭제 요청
    - HEAD: HTTP헤더 정보만 요청. 해당 자원의 존재여부를 확인하기 위한 목적
    - OPTIONS: 웹서버가 지원하는 매서드 종류 반환 요청
    - TRACE: 클라이언트의 요청을 그대로 반환
- HTTP 매서드-GET/POST
- GET
    - 엽서(실생활에서 편지만 보낼수 있는 엽서에 비유)
    - 주소와 함께 메시지를 남김
    - 물건을 보낼 수 없다(파일 업로드 불가)
    - 잘 설계된 서비스라면 주로 조회 요청시 사용
- POST
    - 택배(실생활에서 편지를 포함한 여러 물건도 보낼수 있는 택배에 비유)
    - 주소와 함께 메시지나 물건도 보낼 수 있음
    - 파일업로드를 지원
    - 잘 설계된 서비스에서 주로 추가/수정/삭제 요청시에 사용
- HTTP 요청/응답 패킷 형식
- 요청패킷
    - 요청헤더: 클라이언트에서 필요한 헤더 Key/Value를 세팅한 후 요청, 전달
    - 첫번째 빈줄: Header와 Body 구분자
    - Body: 클라이언트에서 필요한 Body를 세팅한 후 요청, 전달
- 응답패킷
    - 응답헤더: 서버에 필요한 Key/Value를 세팅한 후, 응답, 전달
    - 첫번째 빈줄: Header와 Body 구분자
    - Body: 서버에서 필요한 Body를 세팅한 후 요청, 전달
- 요청패킷 vs 응답패킷
    - 요청헤더는 클라이언트에서 필요한 헤더 Key/Value를 세팅한 후 요청 전달
    - 응답헤더는 서버에 필요한 Key/Value를 세팅한 후 응답 전달
    - 쉽게 생각하면 클라이언트는 사용자 이기 때문에 당연히 서버에게 요청을 할것이고 서버는 서비스를 하는 업체 입장이기 떄문에 응답을 해주는 것
    - 클라이언트 - 요청 (음식점의 주문) vs 서버는 응답(주문을 받아 알맞은 음식을 서빙)
- 헤더(Header)란?
    - HTTP요청/응답 시에 헤더 정보가 Key/Value 형식으로 세팅이 된다.
    - 대개 브라우저에서는 다음 헤더를 설정
        User-Agent: 브라우저의 종류
        Referer: 이전 페이지 URL(어떤 페이지를 거쳐서 왔는가?)
        Accept-Language: 어떤 언어로 응답을 원하는가?
        Authorization: 인증 정보
    - 크롤링을 할떄는 User-Agent헤더와 Referer를 커스텀하게 설정할 필요가 있다.
        서비스에 따라 UserAgent헤더와 Referer헤더를 통해 응답을 거부하기도 함
        ex) 네이버 웹툰.
- Body란?
    - HTTP 요청시에는 Body가 없고, 응답에만 있음
    - Ex)HTML코드, 이미지데이터, JavaScript코드, CSS코드, 비디오 데이터 등
- HTML이라는 텍스트 형태의 특수 문서는 웹 브라우(클라이언트)가 해석한 뒤 데이터를 시각화해서 웹페이지로 보여줄 수 있다.
- 웹 서버 입장에서는 HTML이라는 하나의 형태로 데이터를 반환하면 크롬, 익스플로러, 웨일, 파이어폭스 등의 다양한 브라우져에서 같은 화면이 출력될 수 있다.
- 스크래핑하는 입장에서 보면 가져올 데이터가 HTML 문서에 들어 있기 때문에 HTML 구조에 대해서 알아야 한다.
- 웹서버는 HTML 뿐만 아니라 다양한 형태로 데이터를 반환할 수 있다.
- 웹페이지는 다음의 세 가지 요소로 구성
    - HTML (Hyper Text Markup Language)
    - CSS (Cascading Style Sheet)
    - 자바스크립트 (Java Script)
- HTML은 데이터를 구조적으로 표현하는 방법이며, 데이터를 나열만 하기 때문에 HTML만으로 표현된 웹페이지는 투박하다.
- CSS는 이러한 HTML에 색을 입히거나 디자인을 변경해서 웹페이지를 예쁘게 꾸민다.
- 자바스크립트는 이벤트를 정의해서 웹 페이지에 생명을 불어 넣습니다.

### HTML
- HTML 이란 Hypertext Markup Language 를 뜻한다.
- 하이퍼 텍스트 (hyper text)
    - 비순차적으로 검색할 수 있는 문서를 의미
    - 일반적인 문서는 제공해주는 내용 그대로 하나씩 볼 수 있는 반면 하이퍼 텍스트는 링크를 클릭 해서 다른 문서로의 이동을 지원
- 마크업 언어 (Markup Language)
    - 태그 (tag)와 같은 구분자를 사용해서 데이터의 구조를 기술
    - 화살괄호(< >)와 안쪽의 문자열을 태그라고 부르는데, 일반적으로 시작 태그와 종료 태그를 하나의 쌍으로 사용
    - <태그> 데이터 </태그> 형태로 사용하며 슬래쉬 (/ 가 포함된 태그를 종료 태그라고 함
- 태그를 사용해서 데이터를 표현하며, 링크 기능을 지원하는 문서라고 말할 수 있다.
- HTML 구조
    - html은 태그로 감싸진 속성과 내용들의 모음

### JSON
- JavaScript Object Notation (JSON)은 Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷
- 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용합니다(서버에서 클라이언트로 데이터를 전송하여 표현하려거나 반대의 경우).
- Javascript 객체 문법을 따르는 문자 기반의 데이터 포맷입니다.
- Javascript 객체 문법과 매우 유사하지만 딱히 Javascript가 아니더라도 JSON을 읽고 쓸 수 있는 기능이 다수의 프로그래밍 환경에서 제공
- JSON은 문자열 형태로 존재