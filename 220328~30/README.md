# 1) CLI 기초

## [1] Git 설치

### (1) Windows (윈도우)

- Git 설치 후 윈도우 탐색기를 엽니다. (`윈도우키 + e`)
- `C:/사용자(Users)/현재 사용자 계정` 로 이동합니다.
- 폴더 내 빈 공간에서 마우스 우클릭 후 `Git Bash Here`를 클릭합니다.
- Git Bash 창에 HOME 폴더를 의미하는 `~` 표시만 있다면 정상입니다.
(`~` 표시가 없거나, 뒤에 글자가 추가적으로 나타난다면 잘못된 경로일 수 있습니다.)

### (2) Mac (맥)

- Git이 기본적으로 내장 되어 있기 때문에, 별도의 설치가 필요 없습니다.
- Spotlight (검색)를 엽니다. (화면 우측 상단의 돋보기 혹은 `command + spacebar`)
- `terminal`을 검색하여 터미널을 엽니다.
- 터미널을 열면 기본적으로 HOME 폴더로 경로가 설정 되어 있습니다. (`/Users/현재 사용자 계정`)
- `open .`라고 입력하여 HOME 폴더를 엽니다.

## [2] GUI vs CLI

### (1) GUI와 CLI의 정의

1. `GUI (Graphic User Interface)` : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
2. `CLI (Command Line Interface)` : 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

<aside>
💡 **Interface(인터페이스)**

인터페이스란 원래 서로 다른 개체끼리 맞닿아 있는 **면**을 뜻합니다.
여기에서는 사용자와 컴퓨터가 서로 소통하는 접점이라고 이해한다.

</aside>

### (2) CLI를 사용하는 이유

`new` 라는 이름으로 새 폴더를 생성해 봅시다.

1. GUI를 사용하는 경우 (4단계) : `마우스 우클릭 → 새로 만들기 → 폴더 → new 작성`
2. CLI를 사용하는 경우 (1단계) : `mkdir new`

GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모합니다.

그리고 CLI는 GUI로는 불가능한, 많은 세부적인 기능을 사용할 수 있습니다.

따라서 이후 수업 진행은 CLI를 기반으로 진행하며, CLI에 익숙해지는 시간을 가집니다.

<aside>
💡 **그렇다면 GUI는 왜 존재하나요?**

옛날에는 컴퓨터를 사용하기 위해서는 CLI 환경에서만 가능했습니다.
그렇기 때문에 컴퓨터를 잘 아는 소수의 사람들만 사용할 수 있었는데요.
GUI가 등장하면서 많은 사람들이 더 쉽게 컴퓨터를 사용할 수 있게 되었고
오늘 날 PC라는 개념으로 컴퓨터가 대중화 될 수 있었던 주요 요인 중 하나입니다.

</aside>

### (3) Git Bash를 사용하는 이유

Windows에는 CLI 환경인 `Powershell`과 `명령 프롬프트`가 이미 존재합니다.

하지만 왜 Git Bash라는 것을 사용할까요?

1. **명령어의 통일을 위해서 입니다.**
    - UNIX 계열 운영체제의 명령어와 Windows의 명령어의 차이가 존재합니다.
    - 따라서 `Git Bash`라고 하는 일종의 번역기를 통해 Windows에서도 UNIX 계열 운영체제의 터미널 명령어를 사용하기 위함입니다.
2. **UNIX 계열 운영체제의 명령어를 더 많이 쓰기 때문입니다.**
    - 개발자 입장에서는 Windows보다는 UNIX 계열 운영체제 기반의 프로그램이 훨씬 많습니다.
    - 그만큼 개발 시장에서는 UNIX 계열 운영체제가 더 많이 사용되기 때문에, `Git Bash`를 통해서 UNIX 계열 운영체제의 터미널 명령어를 연습합니다.

## [3] 경로

### (1) 루트, 홈 디렉토리

1. **루트 디렉토리 (Root Directory, `/`)**
    - 모든 파일과 폴더를 담고 있는 최상위 폴더입니다.
    - Windows의 경우 보통은 `C 드라이브`를 의미합니다.
    
2. **홈 디렉토리 (Home Directory, `~`)**
    - `Tilde(틸드)`라고도 부르며, 현재 로그인 된 사용자의 홈 폴더를 의미합니다.
    - Windows의 경우 `C:/사용자(Users)/현재 사용자 계정`을 의미합니다.
    - Mac의 경우 `/Users/현재 사용자 계정`을 의미합니다.

<aside>
💡 **폴더 vs 디렉토리**

폴더와 디렉토리는 거의 같은 의미로 사용됩니다. 따라서 의미의 구분이 무의미합니다.
세부적으로 따져보자면, 윈도우 탐색기에서의 특수 폴더 들(ex. 네트워크 환경, 내컴퓨터 등)은 폴더이지만 디렉토리는 아닙니다. 따라서 폴더가 디렉토리보다 넓은 개념이라고 할 수는 있겠습니다.

</aside>

### (2) 절대 경로와 상대 경로

1. **절대 경로** : 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
    - 윈도우 바탕 화면의 절대 경로 `C:/Users/kyle/Desktop`
2. **상대 경로** : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
    - 현재 작업하고 있는 디렉토리가 `C:/Users` 라고 한다면
    - 윈도우 바탕 화면으로의 상대 경로는 `kyle/Desktop` 이 됩니다.
    - 간결해서 좋지만, 현재 작업하고 있는 디렉토리가 변경 되면 상대 경로도 변경됩니다.
    - `./` : 현재 작업하고 있는 폴더를 의미합니다.
    - `../` : 현재 작업하고 있는 폴더의 부모 폴더를 의미합니다.

## [4] 터미널 명령어

1. `touch` 
    - 파일을 생성하는 명령어
    - 띄어쓰기로 구분하여 여러 파일을 한꺼번에 생성 가능합니다.
    - 숨김 파일을 만들기 위해서는 `.`을 파일 명 앞에 붙입니다.
    
    ```bash
    $ touch text.txt
    ```
    
2. `mkdir`
    - make directory
    - 새 폴더를 생성하는 명령어
    - 띄어쓰기로 구분하여 여러 폴더를 한꺼번에 생성 가능합니다.
    - 폴더 이름 사이에 공백을 넣고 싶다면 따옴표로 묶어서 입력합니다.
    
    ```bash
    $ mkdir folder
    $ mkdir 'happy hacking'
    ```
    
3. `ls` 
    - list segments
    - 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어
    - `-a` : all 옵션. 숨김 파일까지 모두 보여줍니다.
    - `-l` : long 옵션. 용량, 수정 날짜 등 파일 정보를 자세히 보여줍니다.
    
    ```bash
    # 기본 사용
    $ ls 
    
    # all 옵션
    $ ls -a
    
    # all, long 옵션 함께 적용
    $ ls -a -l
    
    # 여러 옵션 축약 가능
    $ ls -al
    ```
    
4. `mv` 
    - move
    - 폴더/파일을 다른 폴더 내로 이동 하거나 이름을 변경하는 명령어
    - 단, 다른 폴더로 이동할 때는 작성한 폴더가 반드시 있어야 합니다. 없으면 이름이 바뀝니다.
    
    ```bash
    # text.txt를 folder 폴더 안에 넣을 때
    $ mv text.txt folder
    
    # text1.txt의 이름을 text2.txt로 바꿀 때
    $ mv text1.txt text2.txt
    ```
    
5. `cd` 
    - change directory
    - 현재 작업 중인 디렉토리를 변경하는 명령어
    - `cd ~` 를 입력하면 홈 디렉토리로 이동합니다. (단순히 `cd` 라고만 입력해도 동일합니다.)
    - `cd ..` 를 입력하면 부모 디렉토리로 이동합니다. (위로 가기)
    - `cd -` 를 입력하면 바로 전 디렉토리로 이동합니다. (뒤로 가기)
    
    ```bash
    # 현재 작업 중인 디렉토리에 있는 folder 폴더로 이동
    $ cd folder
    
    # 절대 경로를 통한 디렉토리 변경
    $ cd C:/Users/kyle/Desktop
    
    # 상대 경로를 통한 디렉토리 변경
    $ cd ../parent/child
    ```
    
6. `rm` 
    - remove
    - 폴더/파일 지우는 명령어
    - GUI와 달리 휴지통으로 이동하지 않고, 바로 `완전 삭제`합니다.
    - `*(asterisk, wildcard)`를 사용해서 `rm *.txt` 라고 입력하면 txt 파일 전체를 다 지웁니다.
    - `-r` : recursive 옵션. 폴더를 지울 때 사용합니다.
    
    ```bash
    $ rm test.txt
    $ rm -r folder
    ```
    
7. `start, open`
    - 폴더/파일을 여는 명령어
    - `Windows`에서는 start를, `Mac`에서는 open을 사용할 수 있습니다.
    
    ```bash
    # Windows
    $ start test.txt
    
    # Mac
    $ open test.txt
    ```
    

1. **유용한 단축키**
    - `위, 아래 방향키` : 과거에 작성했던 명령어 조회
    - `tab` : 폴더/파일 이름 자동 완성
    - `ctrl + a` : 커서가 맨 앞으로 이동
    - `ctrl + e` : 커서가 맨 뒤로 이동
    - `ctrl + w` : 커서가 앞 단어를 삭제
    - `ctrl + l` : 터미널 화면을 깨끗하게 청소 (스크롤 올리면 과거 내역 조회 가능)
    - `ctrl + insert` : 복사
    - `shift + insert` : 붙여넣기


# 2) Visual Studio Code

## [1] Visual Studio Code 시작하기

### (1) 설치 하기

- `Vscode 설치` 페이지를 참고하여 설치를 진행합니다.

<aside>
💡 **Visual Studio Code 왜 쓰나요?**

- Vscode는 마이크로소프트에서 개발한 코드 에디터의 한 종류입니다.
- Windows, Mac, Linux를 모두 지원합니다.
- 기존 개발 도구들 보다 가볍고 빠르다는 장점이 있습니다.
- 전 세계에서 사랑 받는 굉장한 점유율의 에디터입니다.
- Extension을 통해 다양한 기능을 설치할 수 있어서, 무한한 확장성을 가집니다.
- 게다가 무료로 사용 가능합니다.

</aside>

### (2) Vscode 열기

1. 홈 디렉토리(`~`)에서 실습 폴더를 생성 후, 실습 폴더 안에서 vscode를 엽니다.
2. vscode를 열었을 때 다음과 같이 나오는 경우 `Yes, I trust the authors`를 클릭합니다.
3. vscode 왼쪽 메뉴바에서 `A4 용지 두 장이 겹쳐져 있는 아이콘`을 클릭합니다.

## [2] Vscode extensions

### (1) Extensions란?

- `익스텐션`이란 기본 기능에서 확장하여 추가적인 기능을 가능하게 하는 일종의 `플러그인`입니다.
- vscode를 열고 왼쪽 메뉴바에서 `블럭 모양의 아이콘`을 통해 익스텐션 창을 열 수 있습니다.

<aside>
💡 **처음부터 모든 기능을 갖추면 되지, 왜 익스텐션을 쓰나요?**

물론, 처음부터 모든 기능을 갖춘다면 일일히 익스텐션을 설치 하지 않아도 될 것입니다.
하지만 그만큼 불필요한 기능도 많아서 필요 이상으로 에디터가 무거워집니다.
vscode는 사용자가 필요한 기능을 익스텐션을 통해 추가 설치 할 수 있도록 지원하여
가벼우면서도 다양한 작업을 할 수 있는 환경을 제공하고 있습니다.

</aside>

### (2) Extensions 설치

1. **한국어 팩** : vscode 기본 언어를 한국어로 변경할 수 있습니다.
    
    설치 이후, vscode를 껐다 켜야 적용됩니다.
    익스텐션 검색창에 `korean`을 검색한 후, 가장 위에 있는 익스텐션을 install 합니다.
    

1. **Markdown all in one** : 마크다운 문법을 실시간으로 변환해서 보여줍니다.
    
    익스텐션 검색창에 `markdown all in one`을 검색한 후, 가장 위에 있는 익스텐션을 install 합니다.
    

## [3] Vscode 터미널 사용

> 지금까지는 Git Bash 혹은 Terminal과 작업 폴더를 직접 옆에 띄워 놓고 수업을 진행했습니다. 
이제부터는 vscode에서 모든 수업과 실습을 진행합니다.
> 

### (1) 기본 터미널 지정

1. vscode 화면에서 터미널을 엽니다.
    - `vscode 화면 상단 → Terminal → New Terminal`
    - 혹은 단축키 `ctrl + `(backtick, 백틱)` 를 통해 터미널을 열고 닫을 수 있습니다.
        백틱은 숫자 1의 왼쪽에 있습니다. 물결 표시와 함께!
        

1. 기본 터미널을 `powershell → Git Bash` 로 바꾸기 (Windows)
    - 현재 Windows는 vscode에서 터미널을 열 때, 기본적으로 Powershell이 설정 되어 있습니다.
    - 아래 사진에 쓰인 숫자 순서대로 클릭합니다. (`아래 화살표 → 기본 프로필 선택`)
    - 상단에 나타난 여러 터미널 목록 중 Git Bash를 클릭합니다.
    - 이후 기존에 떠있는 Powershell을 `휴지통` 버튼을 눌러서 삭제합니다. **(X가 아니라 휴지통)**
    - 그리고 다시 터미널을 열면! Git Bash로 기본 터미널이 설정된 것을 확인할 수 있습니다.

<aside>
💡 **터미널을 닫을 때 X(닫기)와 휴지통의 차이**

`X(닫기)` 버튼은 터미널의 내용은 유지하고 잠시 숨겨두는 것입니다. (Close panel)
`휴지통` 버튼은 터미널을 아예 삭제하는 것입니다. (Kill terminal)

따라서 가독성을 위해 잠시 닫아 놓을 때는 `X(닫기)` 버튼을,
터미널을 삭제하고 싶을 때는 `휴지통` 버튼을 사용해야 하는 점 잊지 마세요!

</aside>

### (2) vscode에서 터미널 명령어 사용해보기

- CLI 수업에서 학습했던 터미널 명령어를 vscode에서 실습해 봅니다.
- 터미널에서 명령어를 입력했을 때, 왼쪽 파일 트리의 변화를 잘 관찰해 봅니다.

    vscode 터미널에서 작성한 명령어가 파일 트리에 어떤 영향을 끼치는지 살펴봅니다.


# 3) Markdown

## [1] Typora 시작하기

- `Typora 설치` 페이지를 참고하여 설치를 진행합니다.

<aside>
💡 **Typora 왜 쓰나요?**

- Typora는 마크다운 문법을 읽고 쓰기 위한 일종의 메모장입니다.
- 마크다운 형태로 즉시 변환이 되기 때문에 직관적으로 글 작성이 가능합니다.
- 목차, 표와 같은 복잡한 기능을 손쉽게 만들 수 있도록 도와줍니다.
- 특히 이미지 삽입과 관련해서 상당히 편리합니다.

</aside>

## [2] Markdown

### (1) 마크다운이란?

- 일반 텍스트 기반의 경량 마크업(Markup) 언어
- 마크업과 반대 개념이 아니라, 마크업을 더 쉽고 간단하게 사용하고자 만들어졌습니다.
- `.md` 확장자를 가지며, 개발과 관련된 많은 문서는 마크다운 형식으로 작성되어 있습니다.
- 개발 분야에 있어서 `문서화`는 굉장히 중요한 능력입니다. 마크다운은 그 토대가 될 것입니다.

<aside>
💡 **마크업(Markup)이란 무엇인가요?**

마크업 언어는 말 그대로 마크(Mark)로 둘러싸인 언어입니다.
여기서 마크(Mark)란 글의 역할을 지정하는 일종의 표시와 같습니다.

예를 들면 HTML에서 M이 의미하는 것은 Markup 입니다. 즉 HTML도 마크업 언어입니다.
HTML에서 제목을 표시할 때는 `<h1>제목1</h1>` 과 같이 작성합니다.
`제목1`을 둘러싸고 있는 `<h1>`을 태그(tag)라고 말하며, 마크 역할을 합니다.
각각의 글이 `제목, 내용, 목록, 인용 등등` 어떤 역할을 가지고 있는지 표시하는 것입니다.

</aside>

### (2) 마크다운의 장점, 단점, 주의사항

1. **장점**
    - 문법이 직관적이고 쉽습니다.
    - 관리가 쉽습니다.
    - 지원 가능한 플랫폼과 프로그램이 다양합니다.
2. **단점**
    - 표준이 없어 사용자마다 문법이 상이할 수 있습니다.
    - 모든 HTML 마크업 기능을 대신하지는 못합니다.
3. **주의사항**
    - 마크다운의 본질은 글에게 `역할`을 부여하는 것입니다.
    - 따라서 반드시 `역할`에 맞는 마크다운 문법으로만 작성해야 합니다.
    - 예를 들면 `글씨의 크기를 키우고 싶다`는 이유로 `내용`에게 `제목`의 역할을 부여하면 안됩니다. (이 부분은 마크다운 문법을 학습하면서 자연스럽게 이해할 수 있습니다.)

### (3) 마크다운 문법

1. **제목 (Headings)**
    - `h1 ~ h6` 에 해당하는 제목을 표현합니다.
    - `#`을 사용합니다.
    - 작성
        
        ```markdown
        # 제목 1
        ## 제목 2
        ### 제목 3
        #### 제목 4
        ##### 제목 5
        ###### 제목 6
        ```

1. **목록 (List)**
    - 순서가 없는 목록과 순서가 있는 목록을 표현합니다.
    - 순서가 없는 목록은 `- * +` 를 사용합니다.
    - 순서가 있는 목록은 `1. 2. 3.` 과 같은 숫자를 사용합니다.
    - `tab 키`를 이용해서 들여쓰기를 할 수 있습니다.
    - 작성
        
        ```markdown
        - 순서가 없는 목록
        	- 서브 목록
        	- 서브 목록
        
        + 순서가 없는 목록
        	+ 서브 목록
        	+ 서브 목록
        
        * 순서가 없는 목록
        	* 서브 목록
        	* 서브 목록
        
        1. 순서가 있는 목록
        	1. 서브 목록
        	2. 서브 목록
        
        1. 혼합 해보기 1
        	- 순서 없음
        	+ 순서 없음
        	* 순서 없음
        2. 혼합 해보기 2
        	1. 순서 있음
        	- 순서 없음
        	2. 순서 있음
        ```

1. **강조 (Emphasis)**
    - 글자의 스타일링을 표현합니다.
    1. **기울임** : `*글자*` 혹은 `_글자_`
    2. **굵게** : `**글자**` 혹은 `__글자__`
    3. **취소** : `~~글자~~`
    - 작성
        
        ```markdown
        *이탤릭체1* 
        _이탤릭체2_
        
        **볼드체1**
        __볼드체2__
        
        ~~취소선~~
        ```

1. **코드 (Code)**
    - 한 줄 코드인 **인라인 코드**와 여러 줄 코드인 **블록 코드**로 나눌 수 있습니다.
    1. 인라인(Inline) 코드 : ``inline code``처럼 백틱을 통해 코드를 감싸줍니다.
    2. 블록(Block) 코드 : ````python` 처럼 백틱을 3번 입력하고 코드의 종류를 작성합니다.
    - 작성
        
        ```markdown
        파이썬의 print는 `print("Hello World!")` 과 같이 사용합니다.
        
        ```python
        for i in range(10):
        	print(i)
        ```
        
        ```bash
        $ touch test.txt
        ```
        
        ```
        Just plain text
        ```
        ```
        
1. **링크 (Links)**
    - 클릭하면 해당 주소로 이동할 수 있는 링크를 표현합니다.
    - `[표시할 글자](이동할 주소)` 형태로 작성합니다.

1. **이미지 (Images)**
    - 마크다운 문서에 이미지를 삽입할 수 있습니다.
    - `![대체 텍스트](이미지 주소)` 형태로 작성합니다.
    - `대체 텍스트`란 이미지를 정상적으로 불러오지 못했을 때 표시되는 문구입니다.
    - Typora에서는 이미지 파일을 끌어와서 놓아도 자동 업로드 됩니다.

1. **인용 (Blockquote)**
    - 주석이나 인용 문구를 표현합니다.
    - `>` 를 사용합니다. 갯수에 따라 중첩이 가능합니다.
    - 작성
        
        ```markdown
        > 인용문을 작성합니다.
        >> 중첩된 인용문 1
        >>> 중첩된 인용문 2
        >>>> 중첩된 인용문 3
        >>>>> 중첩된 인용문 4
        ```
 
1. **표 (Table)**
    - 테이블(표)를 생성합니다.
    - `파이프( | )`와 `하이픈( - )`을 이용해서 행과 열을 구분합니다.
    - 테이블 양쪽 끝의 `파이프( | )`는 생략 가능합니다.
    - 헤더 셀을 구분할 때는 `3개 이상의 하이픈( - )`이 필요합니다.
    - Typora에서는 `ctrl + T` 를 통해서 쉽게 표 생성이 가능합니다.
        
        (Mac은 `option + command + t`)
        
    - 행을 늘릴 때는 `ctrl + enter` 를 누릅니다.
    - 작성
        
        ```markdown
        | 동물   | 종류   | 다리 개수 |
        | ------ | ------ | --------- |
        | 사자   | 포유류 | 4개       |
        | 닭     | 조류   | 2개       |
        | 도마뱀 | 파충류 | 4개       |
        ```

1. **수평선 (Horizontal Rule)**
    - 구분 선을 생성합니다.
    - `- * _` 을 3번 이상 연속으로 작성합니다.
    - 작성
        
        ```markdown
        ---
        ***
        ___
        ```


# 4) Git 기초

## [1] Git 초기 설정

> 최초 한 번만 설정합니다. 매번 Git을 사용할 때마다 설정할 필요가 없습니다.
> 
1. 누가 커밋 기록을 남겼는지 확인할 수 있도록 이름과 이메일을 설정합니다.
    
    작성자를 수정하고 싶을 때에는 이름, 메일 주소만 다르게 하여 동일하게 입력합니다.
    
    ```bash
    $ git config --global user.name "이름"
    $ git config --global user.email "메일 주소"
    ```
    
2. 작성자가 올바르게 설정되었는지 확인 가능합니다.
    
    ```bash
    $ git config --global -l
    
    또는
    
    $ git config --global --list
    ```
    

## [2] Git 기본 명령어

### (0) 로컬 저장소

- `Working Directory (= Working Tree)` : 사용자의 일반적인 작업이 일어나는 곳
- `Staging Area (= Index)` : 커밋을 위한 파일 및 폴더가 추가되는 곳
- `Repository` : staging area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 곳
- Git은 **Working Directory → Staging Area → Repository** 의 과정으로 버전 관리를 수행합니다.

### (1) git init

```bash
$ git init
Initialized empty Git repository in C:/Users/kyle/git-practice/.git/

kyle@KYLE MINGW64 ~/git-practice (master)
```

- 현재 작업 중인 디렉토리를 Git으로 관리한다는 명령어
- `.git` 이라는 숨김 폴더를 생성하고, 터미널에는 `(master)`라고 표기됩니다.
- Mac OS의 경우 `(master)`가 표기되지 않는데, Terminal 업그레이드를 통해 표기할 수 있습니다.

<aside>
❗ **주의 사항**

1. 이미 Git 저장소인 폴더 내에 또 다른 Git 저장소를 만들지 않습니다. (중첩 금지)
즉, 터미널에 이미 (master)가 있다면, git init을 절대 입력하면 안됩니다.

2. 절대로 홈 디렉토리에서 git init을 하지 않습니다. 터미널의 경로가 `~` 인지 확인합니다.

</aside>

### (2) git status

```bash
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

- Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어
- 어떤 작업을 시행하기 전에 수시로 status를 확인하면 좋습니다.
- 상태
    1. `Untracked` : Git이 관리하지 않는 파일 (한번도 Staging Area에 올라간 적 없는 파일)
    2. `Tracked` : Git이 관리하는 파일
        1. `Unmodified` : 최신 상태
        2. `Modified` : 수정되었지만 아직 Staging Area에는 반영하지 않은 상태
        3. `Staged` : Staging Area에 올라간 상태

### (3) git **add**

```bash
# 특정 파일
$ git add a.txt

# 특정 폴더
$ git add my_folder/

# 현재 디렉토리에 속한 파일/폴더 전부
$ git add .
```

- Working Directory에 있는 파일을 Staging Area로 올리는 명령어
- Git이 해당 파일을 추적(관리)할 수 있도록 만듭니다.
- `Untracked, Modified → Staged` 로 상태를 변경합니다.
- 예시
    
    ```bash
    $ touch a.txt b.txt
    
    $ git status
    On branch master
    
    No commits yet
    
    Untracked files: # 트래킹 되고 있지 않는 파일 목록
      (use "git add <file>..." to include in what will be committed)
            a.txt
            b.txt
    
    nothing added to commit but untracked files present (use "git add" to track)
    ```
    
    ```bash
    # a.txt만 Staging Area에 올립니다.
    
    $ git add a.txt
    ```
    
    ```bash
    $ git status
    
    On branch master
    
    No commits yet
    
    Changes to be committed: # 커밋 예정인 변경사항(Staging Area)
      (use "git rm --cached <file>..." to unstage)
            new file:   a.txt
    
    Untracked files: # 트래킹 되고 있지 않은 파일
      (use "git add <file>..." to include in what will be committed)
            b.txt
    ```
    

### (4) git **commit**

```bash
$ git commit -m "first commit"
[master (root-commit) c02659f] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
```

- Staging Area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장하는 명령어
- `커밋 메세지`는 현재 변경 사항들을 잘 나타낼 수 있도록 `의미` 있게 작성하는 것을 권장합니다.
- 각각의 커밋은 `SHA-1` 알고리즘에 의해 반환 된 고유의 해시 값을 ID로 가집니다.
- `(root-commit)` 은 해당 커밋이 최초의 커밋 일 때만 표시됩니다. 이후 커밋부터는 사라집니다.

### (5) **git log**

```bash
$ git log
commit 1870222981b4731d14ef91d401c68c0bbb2f6e7d (HEAD -> master)
Author: kyle <kyle123@hphk.kr>
Date:   Thu Dec 9 15:26:46 2021 +0900

    first commit
```

- 커밋의 내역(`ID, 작성자, 시간, 메세지 등`)을 조회할 수 있는 명령어
- 옵션
    - `--oneline` : 한 줄로 축약해서 보여줍니다.
    - `--graph` : 브랜치와 머지 내역을 그래프로 보여줍니다.
    - `--all` : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줍니다.
    - `--reverse` : 커밋 내역의 순서를 반대로 보여줍니다. (최신이 가장 아래)
    - `-p` : 파일의 변경 내용도 같이 보여줍니다.
    - `-2` : 원하는 갯수 만큼의 내역을 보여줍니다. (2 말고 임의의 숫자 사용 가능)

<aside>
💡 **옵션과 인자**

명령어를 사용하면서 `-` 혹은 `--`를 통해 옵션을 사용하는 것을 배웠습니다.
옵션과 더불어서 인자라는 개념도 존재하는데요. 옵션과 인자 무엇이 다를까요?

**옵션**은 명령어의 동작 방식을 지정하는 것입니다. 따라서 **생략 가능**합니다.
단순히 기존 기능보다 부가 적인 기능을 원할 때 사용합니다.
예를 들면 `git log --oneline`은 커밋 내역을 한 줄로 보고 싶을 때 사용합니다.
`oneline` 옵션은 말 그대로 부가 적인 기능이므로, 생략해도 `git log`는 정상 동작 합니다.

**인자**는 명령어의 동작 대상을 지정하는 것입니다. 따라서 **생략이 불가능** 합니다.
예를 들면 `git add` 라고만 작성하면 어떤 파일을 Staging Area에 올릴지 모르게 됩니다.
반드시 `git add a.txt` 와 같이 git add 명령어가 동작할 대상을 지정해야 하는데
이때 `a.txt`와 같은 대상을 인자라고 합니다.

</aside>


# 5) Github

## [1] 원격 저장소 (Remote Repository)

> 여태 까지는 내 컴퓨터라는 한정된 공간에 있는 로컬 저장소에서만 버전 관리를 진행했습니다.
이제는 Github의 원격 저장소를 이용해 내 컴퓨터의 로컬 저장소를 다른 사람과 `공유`해봅시다.
Git의 주요 목적 중 하나인 `협업`을 위해 로컬 저장소와 원격 저장소의 연동 방법을 학습합니다.
> 

### (1) Github에서 원격 저장소 생성

화면 오른쪽 상단 더하기(+) 버튼을 누르고 New repository를 클릭합니다.

저장소의 이름, 설명, 공개 여부를 선택하고 Create repository를 클릭합니다. (체크 박스는 건드리지 않습니다!)

### (2) 로컬 저장소와 원격 저장소 연결

1. 원격 저장소가 잘 생성되었는지 확인 후, 저장소의 주소를 복사합니다.
    
2. 기존에 실습 때 만들었던 홈 디렉토리의 TIL 폴더로 가서 vscode를 엽니다.

1. git init을 통해 TIL 폴더를 로컬 저장소로 만들어줍니다.
    
    ```bash
    kyle@KYLE MINGW64 ~/TIL
    $ git init
    Initialized empty Git repository in C:/Users/kyle/TIL/.git/
    ```
    
1. **git remote**
    
    로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`할 수 있는 명령어
    
    1. **등록**
        
        `git remote add <이름> <주소>` 형식으로 작성합니다.
        
        ```bash
        $ git remote add origin https://github.com/edukyle/TIL.git
        
        [풀이]
        git 명령어를 작성할건데, remote(원격 저장소)에 add(추가) 한다.
        origin이라는 이름으로 https://github.com/edukyle/TIL.git라는 주소의 원격 저장소를
        ```
        
    2. **조회**
        
        `git remote -v` 로 작성합니다.
        
        ```bash
        $ git remote -v
        origin  https://github.com/edukyle/TIL.git (fetch)
        origin  https://github.com/edukyle/TIL.git (push)
        
        add를 이용해 추가했던 원격 저장소의 이름과 주소가 출력됩니다.
        ```
        
    3. **삭제**
        
        `git remote rm <이름>` 혹은 `git remote remove <이름>` 으로 작성합니다.
        
        > 로컬과 원격 저장소의 연결을 끊는 것이지, 원격 저장소 자체를 삭제하는 게 아닙니다.
        > 
        
        ```bash
        $ git remote rm origin
        $ git remote remove origin
        
        [풀이]
        git 명령어를 작성할건데, remote(원격 저장소)와의 연결을 rm(remove, 삭제) 한다.
        그 원격 저장소의 이름은 origin이다.
        ```
        

### (3) 원격 저장소에 업로드

- 실습 때 작성했던 TIL 파일을 Github 원격 저장소에 업로드 해보겠습니다.
- **정확히 말하면, 파일을 업로드하는 게 아니라 커밋을 업로드 하는 것입니다!**
- 따라서 먼저 로컬 저장소에서 커밋을 생성해야 원격 저장소에 업로드 할 수 있습니다.

1. **로컬 저장소에서 커밋 생성**
    
    ```bash
    # 현재 상태 확인
    
    $ git status
    On branch master
    
    No commits yet
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            day1.md
    
    nothing added to commit but untracked files present (use "git add" to track)
    ```
    
    ```bash
    $ git add day1.md
    ```
    
    ```bash
    $ git commit -m "Upload TIL Day1"
    [master (root-commit) f3d6d42] Upload TIL Day1
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 day1.md
    ```
    
    ```bash
    # 커밋 확인
    
    $ git log --oneline
    f3d6d42 (HEAD -> master) Upload TIL Day1
    ```
    

1. **git push**
    - 로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어
    - `git push <저장소 이름> <브랜치 이름>` 형식으로 작성합니다.
    - `-u` 옵션을 사용하면, 두 번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능합니다.
    
    ```bash
    $ git push origin master
    
    [풀이]
    git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.
    
    ------------------------------------------------
    
    $ git push -u origin master
    이후에는 $ git push 라고만 작성해도 push가 됩니다.
    ```
    

1. **vscode 자격 증명**
    
    Sign in with your browser를 클릭합니다.
    
    Authorize GitCredentialManager를 클릭합니다.
    
    정상적으로 자격 증명이 완료 되었습니다.
    
    이후 git push 완료
    
    ```bash
    $ git push -u origin master
    info: please complete authentication in your browser...
    Enumerating objects: 3, done.
    Counting objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 218 bytes | 218.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    To https://github.com/edukyle/TIL.git
     * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.
    ```
    
2. **원격 저장소에서 정상 업로드 확인**

<aside>
❗ **(주의) Github 원격 저장소에 절대로 파일을 드래그해서 업로드 하지 않습니다!!!!**

가끔 Github를 구글 드라이브처럼 여겨서, 파일을 직접 드래그해서 올리는 경우가 있습니다.
Git 명령어를 학습했기 때문에, 반드시 git add → git commit → git push 의 단계로만
업로드 해야합니다.

그 이유는 로컬 저장소와 원격 저장소의 동기화 때문입니다.
로컬 저장소에서 변경이 먼저 일어나고, 그 변경 사항을 원격 저장소에 반영하는 형태여야 합니다. 하지만, Github에 드래그를 해서 파일을 업로드하면 원격 저장소에 변경이 먼저 일어나는 형태가 되기 때문에 이러한 행동을 지양해야 합니다.

</aside>

1. `git push`를 그림으로 이해하기

로컬 저장소의 commit 이력이 원격 저장소에 그대로 반영됩니다.

