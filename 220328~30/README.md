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


# 6) .gitignore

## [1] .gitignore

> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것
> 

### (1) .gitignore에 작성하는 목록

- 민감한 개인 정보가 담긴 파일 (전화번호, 계좌번호, 각종 비밀번호, API KEY 등)
- OS(운영체제)에서 활용되는 파일
- IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
    - 예) pycharm -> .idea/
- 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
    - 가상 환경 : `venv/`
    - `__pycache__/`

### (2) .gitignore 작성 시 주의 사항

- 반드시 이름을 `.gitignore`로 작성합니다. 앞의 점(.)은 숨김 파일이라는 뜻입니다.
- `.gitignore` 파일은 `.git` 폴더와 동일한 위치에 생성합니다.
- **제외 하고 싶은 파일은 반드시 `git add` 전에 `.gitignore`에 작성합니다.**
    
    <aside>
    ❗ **왜 git add 전에 .gitignore에 작성해야 할까요?**
    
    `git add a.txt` 라고 작성하면, 이제 Git은 `a.txt`를 버전 관리의 대상으로 여깁니다.
    한 번 버전 관리의 대상이 된 `a.txt`는 이후에 .gitignore에 작성하더라도
    무시되지 않고 계속 버전 관리의 대상으로 인식됩니다.
    
    따라서 제외 하고 싶은 파일은 반드시 git add 전에 .gitignore에 작성해야 합니다!
    
    </aside>
    

### (3) .gitignore 쉽게 작성하기

> .gitignore의 내용을 쉽게 작성할 수 있도록 도와주는 두 개의 사이트를 소개합니다.
자신의 개발 환경에 맞는 것을 찾아서 `전체 복사, 붙여넣기`를 하면 됩니다.
> 
1. **웹사이트**

[gitignore.io](https://gitignore.io/)

1. **gitignore 저장소**

[https://github.com/github/gitignore](https://github.com/github/gitignore)

1. **Python에 대한 .gitignore 예시**
    
    [https://gitignore.io/](https://gitignore.io/) 에서 가져옴
    

## [2] 심화

> .gitignore에 대해 조금 더 알아봅니다.
> 

### (1) .gitignore 패턴 규칙

1. 아무것도 없는 라인이나, `#`로 시작하는 라인은 무시합니다.
2. `슬래시(/)`로 시작하면 하위 디렉터리에 재귀적으로 적용되지 않습니다.
3. 디렉터리는 `슬래시(/)`를 끝에 사용하는 것으로 표현합니다.
4. `느낌표(!)`로 시작하는 패턴의 파일은 ignore(무시)하지 않습니다.
5. **표준 Glob 패턴을 사용합니다.**
    - `*(asterisk)`는 문자가 하나도 없거나 하나 이상을 의미합니다.
    - `[abc]`는 중괄호 안에 있는 문자 중 하나를 의미합니다.
    - `물음표(?)`는 문자 하나를 의미합니다.
    - `[0-9]`처럼 중괄호 안에 하이픈(-)이 있는 경우 0에서 9사이의 문자 중 하나를 의미합니다.
    - `**(2개의 asterisk)`는 디렉터리 내부의 디렉터리까지 지정할 수 있습니다.
    (`a/**/z`라고 작성하면 `a/z`, `a/b/z`, `a/b/c/z` 까지 모두 영향을 끼칩니다.)

### (2) 패턴 예시

```bash
# .gitignore

# 확장자가 txt인 파일 무시
*.txt

# 현재 확장자가 txt인 파일이 무시되지만, 느낌표를 사용하여 test.txt는 무시하지 않음
!test.txt

# 현재 디렉터리에 있는 TODO 파일은 무시하고, folder/TODO 처럼 하위 디렉터리에 있는 파일은 무시하지 않음
/TODO

# build/ 디렉터리에 있는 모든 파일은 무시
build/

# folder/notes.txt 파일은 무시하고 folder/child/arch.txt 파일은 무시하지 않음
folder/*.txt

# folder 디렉터리 아래의 모든 .pdf 파일을 무시
folder/**/*.pdf
```


# 7) clone, pull

## [1] 원격 저장소 가져오기

> 지금까지는 로컬 저장소의 내용을 원격 저장소에 업로드하는 것을 학습했습니다.
이번에는 반대로, 원격 저장소의 내용을 로컬 저장소로 가져오는 것을 학습합니다.
> 

### (1) git clone

- 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어
- clone은 `"복제"`라는 뜻으로, `git clone` 명령어를 사용하면 원격 저장소를 통째로 복제해서 내 컴퓨터에 옮길 수 있습니다.
- `git clone <원격 저장소 주소>`의 형태로 작성합니다.
    
    ```bash
    $ git clone https://github.com/edukyle/TIL.git
    Cloning into 'TIL'...
    remote: Enumerating objects: 3, done.
    remote: Counting objects: 100% (3/3), done.
    remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
    Receiving objects: 100% (3/3), done.
    ```
    
    위에 작성한 대로 실행하면, `Github의 edukyle이라는 계정의 TIL 원격 저장소를 복제`하여 내 컴퓨터에 TIL이라는 이름의 로컬 저장소를 생성하게 됩니다.
    
- git clone을 통해 생성된 로컬 저장소는 `git init`과 `git remote add`가 이미 수행되어 있습니다.

### (2) git pull

- 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어
- 로컬 저장소와 원격 저장소의 내용이 완전 일치하면 git pull을 해도 변화가 일어나지 않습니다.
- `git pull <저장소 이름> <브랜치 이름>`의 형태로 작성합니다.
    
    ```bash
    $ git pull origin master
    From https://github.com/edukyle/git-practice
     * branch            master     -> FETCH_HEAD
    Updating 6570ecb..56809a9
    Fast-forward
     README.md | 1 +
     1 file changed, 1 insertion(+)
    
    [풀이]
    git 명령어를 사용할건데, origin이라는 원격 저장소의 master 브랜치의 내용을 가져온다(pull).
    ```
    

<aside>
💡 **git clone vs git pull**

clone과 pull이 모두 원격 저장소로부터 가져오는 명령어라서 조금 혼동될 수 있습니다. 

`git clone`은 git init처럼 처음에 한 번만 실행합니다. 즉 로컬 저장소를 만드는 역할이죠.
단, git init처럼 직접 로컬 저장소를 만드는 게 아니라, Github에서 저장소를 복제해서 내 컴퓨터에 똑같은 복제본을 만든다는 차이가 있습니다.

`git pull`은 git push처럼 로컬 저장소와 원격 저장소의 내용을 동기화하고 싶다면 언제든 사용합니다. 단, push는 로컬 저장소의 변경 내용을 원격 저장소에 반영하는 것이고, pull은 원격 저장소의 변경 내용을 로컬 저장소에 반영하는 것입니다. **즉 방향이 다릅니다!**

</aside>

## [2] 내 컴퓨터 ↔ Github(원격 저장소) ↔ 강의장 컴퓨터 (예시)

> 두 개 이상의 로컬 저장소에서 하나의 원격 저장소에 접근하면 어떻게 될까요?
집과 강의장을 오가면서 `clone, push, pull` 하는 과정을 살펴보겠습니다.
> 

### (1) 규칙

- 수업 때는 두 개의 폴더를 `"내 컴퓨터"`와 `"강의장 컴퓨터"` 라고 가정합니다.
- 내 컴퓨터에 있는 로컬 저장소의 이름은 `TIL-home` 입니다.
- 강의장 컴퓨터에 있는 로컬 저장소의 이름은 `TIL-class` 입니다.
- Github에 있는 원격 저장소의 이름은 `TIL-remote` 입니다.

### (2) 사전 세팅

- 홈 디렉토리 안에 `TIL-home` 폴더를 생성합니다.
- Github에서 `TIL-remote` 라는 이름의 원격 저장소를 생성합니다.
- `TIL-home` 폴더에서 vscode를 엽니다.
- 아래와 같은 절차를 진행합니다.
    
    ```bash
    # TIL-home
    
    $ git init
    $ touch day1.md
    $ git add .
    $ git commit -m "집에서 Day1 작성"
    $ git remote add origin https://github.com/edukyle/TIL-remote.git
    $ git push origin master
    ```
    
    `TIL-home` 로컬 저장소의 내용이 `TIL-remote` 원격 저장소에 그대로 반영되었습니다.
    
### (3) git clone

> 여러분은 이제 강의장에 왔습니다. 강의장 컴퓨터에는 여러분의 TIL 폴더가 없습니다.
> 
- Github에 있는 `TIL-remote`에서 `git clone`을 통해 내려 받습니다.
    
    ```bash
    # TIL-class
    
    $ git clone https://github.com/edukyle/TIL-remote.git TIL-class
    ```
    
    **원격 저장소는 `TIL-remote` 이지만, 위와 같이 작성하면 강의장 컴퓨터에는 `TIL-class`라는 이름으로 로컬 저장소가 생성됩니다. (내부 파일 내용은 똑같습니다. 단지 폴더의 이름만 바뀝니다.)**
 
### (4) git push

> 강의장 컴퓨터 → 원격 저장소
> 
- 강의장에서 새로운 파일을 만들고 원격 저장소에 업로드 합니다.
    
    ```bash
    # TIL-class
    
    $ touch day2.md
    $ git add .
    $ git commit -m "강의장에서 Day2 작성"
    $ git push origin master
    ```

### (5) git pull

> 원격 저장소 → 내 컴퓨터
> 
- 내 컴퓨터에는 day2.md가 없습니다. 왜냐하면 강의장 컴퓨터에서 day2.md를 만들어서 원격 저장소에 push 했기 때문입니다. 따라서 원격 저장소에서 day2.md에 대한 내역을 가져와야 합니다.
    
    ```bash
    # TIL-home
    
    $ git pull origin master
    ```
    
    이제 `내 컴퓨터, Github, 강의장 컴퓨터`의 내용은 동일합니다.
    
- **주의 사항 (글 만으로는 이해하기 어려우니, 직접 보여주면서 수업 합니다.)**
    
    <aside>
    ❗ **만약 TIL-home에서 pull이 아니라 commit을 먼저한 후 pull을 하면 어떻게 될까요?
    다음 세 가지의 경우가 있을 수 있습니다.**
    
    1. 내 컴퓨터와 강의장 컴퓨터에서 **서로 다른 파일을 수정**한 경우
    → 정상적으로 git pull이 됩니다.
    
    2. 내 컴퓨터와 강의장 컴퓨터에서 **같은 파일을 수정했지만, 수정한 라인이 다른** 경우
    → 정상적으로 git pull이 됩니다.
    
    3. 내 컴퓨터와 강의장 컴퓨터에서 **같은 파일의 같은 라인**을 수정한 경우
    → **충돌(conflict)**이 발생합니다. 어느 내용을 반영할지 직접 선택해야 합니다.
    
    </aside>
    
    <aside>
    ❗ **만약 TIL-home에서 pull이 아니라 commit을 먼저한 후 바로 push 하면 어떻게 될까요?**
    **아래와 같은 에러 메시지가 나타나면서 push가 실패합니다.**
    
    To https://github.com/edukyle/TIL-remote.git
    
    ! [rejected]        master -> master (non-fast-forward)
    
    error: failed to push some refs to 'https://github.com/edukyle/TIL-remote.git'
    
    원격 저장소의 내용을 먼저 받아오지 않고, 로컬 저장소에서 새로운 커밋을 생성했기 때문에 서로의 커밋 내역이 달라져서 그렇습니다.
    
    만약 로컬 저장소와 원격 저장소의 내용이 다르다면 일단 git pull을 통해 동기화를 시키고 새로운 커밋을 쌓아 나가야 합니다.
    
    </aside>
    

# 8) Branch

## [1] Branch

> Git에서 Branch라는 개념은 매우 중요합니다. 사실상 버전 관리의 꽃이라고 할 수 있습니다.
> 

### (1) Branch란?

- Branch는 `나뭇가지`라는 뜻의 영어 단어입니다.
- 즉 `브랜치`란 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 **독립적으로 작업**할 수 있도록 도와주는 Git의 도구입니다.
- **장점**
    1. 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전합니다.
    2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능합니다.
    3. 특히나 Git은 브랜치를 만드는 속도가 굉장히 빠르고, 용량도 적게 듭니다.
- **그래도 브랜치 꼭 써야하나요?**
    1. 일단 master 브랜치는 상용을 의미합니다. 그래서 언제든 세상에 공개되어 있습니다.
    2. 만약 상용에 에러가 있어서 고쳐야 한다면 어떻게 해야할까요?
    3. 고객들이 사용하고 있는데, 함부로 버전을 되돌리거나 삭제할 수 있을까요?
    4. 따라서 브랜치를 통해 별도의 작업 공간을 만들고, 그곳에서 되돌리거나 삭제를 합니다.
    5. 브랜치는 완전하게 독립이 되어있어서 어떤 작업을 해도 master에는 영향을 끼치지 못하죠.
    6. 그리고 이후에 에러를 해결했다면? 그 내용을 master에 반영할 수도 있습니다!
    7. 이러한 이유 때문에 Git에서 브랜치는 정말 강력한 기능 중의 하나라고 할 수 있습니다.

### (2) git branch

> 브랜치 `조회, 생성, 삭제 등` 브랜치와 관련된 Git 명령어
> 

```bash
# 브랜치 목록 확인
$ git branch

# 원격 저장소의 브랜치 목록 확인
$ git branch -r

# 새로운 브랜치 생성
$ git branch <브랜치 이름>

# 특정 커밋 기준으로 브랜치 생성
$ git branch <브랜치 이름> <커밋 ID>

# 특정 브랜치 삭제
$ git branch -d <브랜치 이름> # 병합된 브랜치만 삭제 가능
$ git branch -D <브랜치 이름> # (주의) 강제 삭제 (병합되지 않은 브랜치도 삭제 가능)
```

### (3) git switch

> 현재 브랜치에서 다른 브랜치로 `HEAD`를 이동시키는 명령어
`HEAD`란 현재 브랜치를 가리키는 포인터를 의미합니다.
> 

```bash
# 다른 브랜치로 이동
$ git switch <다른 브랜치 이름>

# 브랜치를 새로 생성과 동시에 이동
$ git switch -c <브랜치 이름>

# 특정 커밋 기준으로 브랜치 생성과 동시에 이동
$ git switch -c <브랜치 이름> <커밋 ID>
```

<aside>
❗ **git switch 하기 전에, 해당 브랜치의 변경 사항을 커밋 하셨나요?**

master 브랜치와 feature 브랜치가 있다고 가정해보겠습니다.
feature 브랜치에서 test.txt를 만들고 git commit 하지 않은 상황에서
master 브랜치로 이동하게 되면, test.txt 파일이 그대로 남아있습니다.

따라서 브랜치를 이동하기 전에, 꼭 커밋을 완료하고 이동하도록 합니다.

</aside>

## [2] Branch scenario

> git branch와 git switch를 통해 브랜치를 `조회, 생성, 이동`하는 실습을 진행합니다.
> 

### (1) 사전 세팅

1. 홈 디렉토리에 `git-branch-practice` 폴더를 생성하고 이동 후 vscode를 엽니다.
    
    ```bash
    
    $ mkdir git-branch-practice
    $ cd git-branch-practice
    $ code .
    ```
    
2. Git 저장소를 생성합니다.
    
    ```bash
    $ git init
    Initialized empty Git repository in C:/Users/kyle/git-branch-practice/.git/
    ```
    
3. `test.txt`를 생성하고 각각 `master-1, master-2, master-3` 이라는 내용을 순서대로 입력하여 커밋 3개를 작성합니다.
    
    ```bash
    $ touch test.txt
    
    test.txt에 master-1 작성
    $ git add .
    $ git commit -m "master-1"
    
    test.txt에 master-2 작성
    $ git add .
    $ git commit -m "master-2"
    
    test.txt에 master-3 작성
    $ git add .
    $ git commit -m "master-3"
    ```
    
4. `git log --oneline`을 입력했을 때 아래와 같이 나와야 정상입니다.
    
    총 3개의 버전이 master 브랜치에 만들어졌습니다.
    
    ```bash
    $ git log --oneline
    0604dcd (HEAD -> master) master-3
    9c22c89 master-2
    3d71510 master-1
    ```

### (2) 브랜치 생성, 조회

1. 현재 위치(master 브랜치의 최신 커밋)에서 `login`이라는 이름으로 브랜치를 생성합니다.
    
    ```bash
    $ git branch login
    ```
    
2. login브랜치가 잘 생성되었는지 확인합니다.
    
    `* master`의 의미는 현재 HEAD가 가리키는 브랜치는 `master`라는 것입니다.
    
    ```bash
    $ git branch
    	login
    * master
    ```
    
3. `git log --oneline`을 입력했을 때 아래와 같이 나와야 정상입니다.
    
    `0604dcd` 커밋 기준으로 `master`와 `login`브랜치가 위치한 것을 볼 수 있습니다.
    
    ```bash
    $ git log --oneline
    0604dcd (HEAD -> master, login) master-3
    9c22c89 master-2
    3d71510 master-1
    ```
    
4. `master` 브랜치에서 1개의 커밋을 더 작성합니다.
    
    ```bash
    test.txt에 master-4 작성
    $ git add .
    $ git commit -m "master-4"
    ```

### (3) 브랜치 이동

1. 현재 브랜치와 커밋의 상태는 다음과 같습니다.
    
    ```bash
    $ git log --oneline
    5ca7701 (HEAD -> master) master-4
    0604dcd (login) master-3
    9c22c89 master-2
    3d71510 master-1
    ```
    
2. 이때 `login`브랜치로 이동하면 어떤 일이 일어날까요?
    
    ```bash
    $ git switch login
    ```
    
    **master 브랜치의 test.txt에 작성한 master-4가 지워졌습니다!!**
    
    ```bash
    # login 브랜치의 test.txt
    
    master-1
    master-2
    master-3
    ```
    
3. 그리고 `git log --oneline`을 입력하면 아래와 같이 나타납니다.
    
    이제 `HEAD`는 `login` 브랜치를 가리키고, `master` 브랜치가 보이지 않습니다.
    
    ```bash
    $ git log --oneline
    0604dcd (HEAD -> login) master-3
    9c22c89 master-2
    3d71510 master-1
    ```
    
4. master 브랜치는 삭제된 걸까요?
    
    아닙니다! 브랜치를 조회 해보면 다음과 같이 나타납니다.
    
    HEAD가 `login` 브랜치를 가리키면서, log도 `login` 브랜치 기준으로 보이는 것이었습니다.
    
    ```bash
    $ git branch
    * login
      master
    ```
    
5. `git log --oneline --all`을 입력하면 모든 브랜치의 로그를 볼 수 있습니다.
    
    ```bash
    $ git log --oneline --all
    5ca7701 (master) master-4
    0604dcd (HEAD -> login) master-3
    9c22c89 master-2
    3d71510 master-1
    ```

<aside>
💡 즉 브랜치를 이동한다는건 HEAD가 해당 브랜치를 가리킨다는 것을 의미하고
브랜치는 최신 커밋을 가리키므로, **HEAD가 해당 브랜치의 최신 커밋을 가리키게 됩니다.

따라서 워킹 디렉토리의 내용도 HEAD가 가리키는 브랜치의 최신 커밋 상태로 변화합니다.**

</aside>

### (4) login 브랜치에서 커밋 생성

1. `test.txt` 파일에 `login-1`이라고 작성합니다.
    
    ```bash
    # login 브랜치의 test.txt
    master-1
    master-2
    master-3
    login-1
    ```
    
2. 추가적으로 `test_login.txt`도 생성하고 `login-1`이라고 작성해봅시다.
    
    ```bash
    $ touch test_login.txt
    
    # 이후 test_login.txt에 작성
    login-1
    ```
    
3. 커밋을 생성합니다.
    
    ```bash
    $ git add .
    $ git commit -m "login-1"
    ```
    
4. `git log --oneline --all --graph`를 통해 아래와 같은 내용을 확인합니다.
    
    `master` 브랜치와 `login` 브랜치가 다른 갈래로 갈라진 것을 확인할 수 있습니다.
    
    ```bash
    $ git log --oneline --graph --all
    * 3b0a091 (HEAD -> login) login-1
    | * 5ca7701 (master) master-4
    |/
    * 0604dcd master-3
    * 9c22c89 master-2
    * 3d71510 master-1
    ```


# 9) Branch-merge

## [1] Branch Merge

> 지금까지는 브랜치를 통해서 독립된 작업 공간을 만드는 것 까지 진행했습니다.
이제 각 브랜치에서의 작업이 끝나면 어떻게 할까요? 
그 작업 내용을 master에 반영해야 하지 않을까요?
지금부터는 `Merge`라고 하는 `병합`을 학습하면서 브랜치를 합치는 것을 살펴보겠습니다.
> 

### (1) git merge

- 분기된 브랜치들을 하나로 합치는 명령어
- `git merge <합칠 브랜치 이름>`의 형태로 사용합니다.
- **Merge하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야합니다.**
    
    ```bash
    # 1. 현재 branch1과 branch2가 있고, HEAD가 가리키는 곳은 branch1 입니다.
    $ git branch
    * branch1
      branch2
    
    # 2. branch2를 branch1에 합치려면?
    $ git merge branch2
    
    # 3. branch1을 branch2에 합치려면?
    $ git switch branch2
    $ git merge branch1
    ```
    

### (2) Merge의 세 종류

1. **Fast-Forward**
    - 브랜치를 병합할 때 마치 `빨리감기`처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 것
    1. 현재 master는 C2 커밋을, hotfix는 C4 커밋을 가리키고 있습니다.
        
    2. master에 hotfix를 병합하면 어떻게 될까요?
        
        ```bash
        $ git switch master
        $ git merge hotfix
        Updating s1d5f1s..1325sd4
        **Fast-forward**
         index.html | 2 ++
         1 file changed, 2 insertions(+)
        ```
        
    3. hotfix가 가리키는 C4는 C2에 기반한 커밋이므로, master가 C4에 이동하게 됩니다.
        
        이렇게 따로 merge 과정 없이 브랜치의 포인터가 이동하는 것을 `Fast-Forward`라고 합니다.
        
    4. 병합이 완료된 hotfix는 더 이상 필요 없으므로 삭제합니다.
        
        ```bash
        $ git branch -d hotfix
        Deleted branch hotfix (1325sd4).
        ```
        
2. **3-Way Merge**
    - 브랜치를 병합할 때 `각 브랜치의 커밋 두개와 공통 조상 하나`를 사용하여 병합하는 것
    - 두 브랜치에서 `다른 파일` 혹은 `같은 파일의 다른 부분`을 수정했을 때 가능합니다.
    1. 현재 master는 C4 커밋을, iss53은 C5 커밋을 가리키고 있습니다.
        
        master와 iss53의 공통 조상은 C2 커밋입니다.
        
    2. 이 상황에서 master에 iss53을 병합하면 어떻게 될까요?
        
        ```bash
        $ git switch master
        Switched to branch 'master'
        $ git merge iss53
        **Merge made by the 'ort' strategy.**
        index.html |    1 +
        1 file changed, 1 insertion(+)
        ```
        
    3. master와 iss53은 갈래가 나누어져 있기 때문에 Fast-Forward로 합쳐질 수 없습니다.
        
        따라서 공통 조상인 C2와 각자가 가리키는 커밋인 C4, C5를 비교하여 3-way merge를 진행합니다.
        
    4. 이때 생긴 C6는 master와 iss53이 병합되면서 발생한 Merge Commit입니다.
    5. 병합이 완료된 iss53은 더 이상 필요 없으므로 삭제합니다.
        
        ```bash
        $ git branch -d iss53
        Deleted branch iss53 (58sdf23).
        ```
        
3. **Merge Conflict**
    - 병합하는 두 브랜치에서 `같은 파일의 같은 부분`을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못해서 발생하는 충돌(Conflict) 현상
    - 결국은 사용자가 직접 내용을 선택해서 Conflict를 해결해야 합니다.
    1. 현재 master는 C4 커밋을, iss53은 C5 커밋을 가리키고 있습니다.
        
        master와 iss53의 공통 조상은 C2 커밋입니다. `(3-way merge에서 상황과 같습니다)`
        
    2. 3-way merge와는 달리, 만약 master와 iss53이 `같은 파일의 같은 부분`을 수정하고 병합한다면 어떤 일이 발생할까요?
        
        ```bash
        $ git merge iss53
        Auto-merging index.html
        CONFLICT (content): Merge conflict in index.html
        Automatic merge failed; fix conflicts and then commit the result.
        ```
        
    3. 충돌이 일어난 파일을 확인하기 위해 `git status`를 입력합니다.
        
        ```bash
        $ git status
        On branch master
        You have unmerged paths.
          (fix conflicts and run "git commit")
        
        Unmerged paths:
          (use "git add <file>..." to mark resolution)
        
            both modified:      index.html
        
        no changes added to commit (use "git add" and/or "git commit -a")
        ```
        
    4. `index.html`을 열어보면 아래와 같이 충돌 내역이 나옵니다.
        
        ```html
        <<<<<<< HEAD:index.html
        <div id="footer">contact : email.support@github.com</div>
        =======
        <div id="footer">
         please contact us at support@github.com
        </div>
        >>>>>>> iss53:index.html
        ```
        
    5. `=======` 를 기준으로 위는 master의 내용, 아래는 iss53의 내용입니다.
        
        이 중 하나를 선택할 수도 있고, 둘 다 선택할 수도 있고, 아예 새롭게 작성할 수도 있습니다.
        
        ```html
        <div id="footer">
        please contact us at email.support@github.com
        </div>
        ```
        
    6. 이후 git add와 git commit을 통해 병합한 내용을 커밋할 수 있습니다.
        
        ```bash
        $ git add .
        $ git commit
        ```
        
    7. Vim 편집기를 이용해서 커밋 내역을 수정할 수 있습니다.
        
        ```bash
        Merge branch 'iss53'
        
        Conflicts:
            index.html
        #
        # It looks like you may be committing a merge.
        # If this is not correct, please remove the file
        #	.git/MERGE_HEAD
        # and try again.
        
        # Please enter the commit message for your changes. Lines starting
        # with '#' will be ignored, and an empty message aborts the commit.
        # On branch master
        # All conflicts fixed but you are still merging.
        #
        # Changes to be committed:
        #	modified:   index.html
        #
        ```
        
    8. Vim 편집기를 통해 작성한 커밋이 이제 C6 커밋이 됩니다.
        
    9. 병합이 완료된 iss53은 더 이상 필요 없으므로 삭제합니다.
        
        ```bash
        $ git branch -d iss53
        Deleted branch iss53 (58sdf23).
        ```
        

## [2] Branch-merge Scenario

> 지금까지 학습했던 git merge와 세 가지 상황에 대해 다시 한 번 살펴봅니다.
> 

### (1) 사전 세팅

```bash
$ mkdir git_merge
$ cd git_merge

$ git init
$ touch test.txt

# test.txt 에 master test 1 을 입력 후 저장

$ git add .
$ git commit -m "master test 1"
```

### (2) Fast-Forward

<aside>
💡 **login 브랜치가 생성된 이후 master 브랜치에 변경 사항이 없는 상황**

즉, master 브랜치에서 login 브랜치를 merge 할 때 
login 브랜치가 master 브랜치 이후의 커밋을 가리키고 있으면 
그저 master 브랜치가 login 브랜치와 동일한 커밋을 가리키도록 이동 시킬 뿐입니다.

</aside>

1. `login` 브랜치 생성 및 이동합니다.
    
    ```bash
    $ git switch -c login
    ```
    
2. `login.txt`를 만들고 커밋합니다.
    
    ```bash
    $ touch login.txt
    $ git add .
    $ git commit -m "login test 1"
    ```
    
3. `master` 브랜치로 이동합니다.
    
    ```bash
    $ git switch master
    
    $ git log --oneline --all --graph
    * df231d0 (login) login test 1
    * 1e62b4c (HEAD -> master) master test 1
    ```
    
4. `master`에 `login`을 병합합니다.
    
    ```bash
    $ git merge login
    Updating 1e62b4c..df231d0
    **Fast-forward**
     login.txt | 0
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 login.txt
    ```
    
5. 결과를 확인합니다. (**Fast-forward**, 단순히 HEAD를 앞으로 빨리감기)
    
    ```bash
    $ git log --oneline --all --graph
    * df231d0 (HEAD -> master, login) login test 1
    * 1e62b4c master test 1
    ```
    
6. `login` 브랜치를 삭제합니다.
    
    ```bash
    $ git branch -d login
    Deleted branch login (was df231d0).
    
    $ git log --oneline --all --graph
    * df231d0 (HEAD -> master) login test 1
    * 1e62b4c master test 1
    ```
    

### (3) 3-way Merge (Merge commit)

<aside>
💡 현재 브랜치(master)가 가리키는 커밋이 Merge 할 브랜치의 조상이 아니면, git은 각 브랜치가 가리키는 커밋 2개와 공통 조상 하나를 사용하며 `3-way Merge` 합니다.

단순히 브랜치 포인터를 최신 커밋으로 옮기는 게 아니라 3-way Merge 의 결과를 별도의 커밋으로 만들고 나서 해당 브랜치가 그 커밋을 가리키도록 이동 시킵니다. 그래서 이런 커밋은 부모가 여러 개고 `Merge commit` 이라고 합니다.

</aside>

1. `signout` 브랜치를 생성 및 이동합니다.
    
    ```bash
    $ git switch -c signout
    ```
    
2. 특정 작업 완료 후 커밋합니다.
    
    ```bash
    $ touch signout.txt
    
    $ git add .
    $ git commit -m "signout test 1"
    
    $ git log --oneline
    bcade83 (HEAD -> signout) signout test 1
    df231d0 (master) login test 1
    1e62b4c master test 1
    ```
    
3. `master` 브랜치로 이동합니다.
    
    ```bash
    $ git switch master
    ```
    
4. `master`에 추가 작업 후 커밋합니다. (단 **`signout` 브랜치와 다른 파일**을 생성 혹은 수정합니다.)
    
    ```bash
    $ touch master.txt
    
    $ git add .
    $ git commit -m "master test 2"
    
    $ git log --all --oneline
    48bd5a6 (HEAD -> master) master test 2
    bcade83 (signout) signout test 1
    df231d0 login test 1
    1e62b4c master test 1
    
    ```
    
5. `master`에 `signout`을 병합합니다. (자동 merge commit 발생)
    
    ```bash
    $ git merge signout
    Merge made by the 'ort' strategy.
     signout.txt | 0
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 signout.txt
    ```
    
6. log 확인
    
    ```bash
    $ git log --oneline --all --graph
    *   ac0e971 (HEAD -> master) Merge branch 'signout'
    |\
    | * bcade83 (signout) signout test 1
    * | 48bd5a6 master test 2
    |/
    * df231d0 login test 1
    * 1e62b4c master test 1
    ```
    
7. `signout` 브랜치 삭제
    
    ```bash
    $ git branch -d signout
    Deleted branch signout (was bcade83).
    ```
    

### (4) Merge Conflict

<aside>
💡 Merge 하는 두 브랜치에서 **같은 파일의 한 부분을 동시에 수정**하고 Merge 하면 
Git은 해당 부분을 자동으로 Merge 하지 못하고 충돌이 일어납니다.
**(반면 동일 파일이더라도 서로 다른 부분을 수정했다면, Conflict 없이 자동으로 Merge Commit 됩니다!)**

</aside>

1. `hotfix` 브랜치를 생성 및 이동합니다.
    
    ```bash
    $ git switch -c hotfix
    ```
    
2. 특정 작업 완료 후 커밋합니다.
    
    ```bash
    # test.txt 수정
    
    master test 1
    **이건 hotfix에서 작성한 문장입니다.**
    ```
    
    ```bash
    $ git add .
    $ git commit -m "hotfix test 1"
    
    $ git log --oneline --graph --all
    * ad045fa (HEAD -> hotfix) hotfix test 1
    *   ac0e971 (master) Merge branch 'signout'
    |\
    | * bcade83 signout test 1
    * | 48bd5a6 master test 2
    |/
    * df231d0 login test 1
    * 1e62b4c master test 1
    ```
    
3. `master` 브랜치로 이동합니다.
    
    ```bash
    $ git switch master
    ```
    
4. 특정 작업(`hotfix` 와 동일 파일의 동일 부분 수정) 완료 후 커밋합니다.
    
    ```bash
    # text.txt 수정
    
    master test 1
    **이건 master에서 작성한 문장입니다.**
    ```
    
    ```bash
    $ git add .
    $ git commit -m "master test 3"
    
    $ git log --oneline --all --graph
    * 3170247 (HEAD -> master) master test 3
    | * ad045fa (hotfix) hotfix test 1
    |/
    *   ac0e971 Merge branch 'signout'
    |\
    | * bcade83 signout test 1
    * | 48bd5a6 master test 2
    |/
    * df231d0 login test 1
    * 1e62b4c master test 1
    ```
    
5. `master`에 `hotfix`를 병합합니다.
    
    ```bash
    $ git merge hotfix
    ```
    
6. 결과 → merge conflict 발생 (**같은 파일의 같은 문장을 수정했기 때문입니다!**)
    
7. 충돌 확인 및 해결
    - Merge Conflict가 일어났을 때 Git이 어떤 파일을 Merge 할 수 없었는지 살펴보려면 `git status` 명령을 이용합니다.
    
    ```bash
    $ git status
    On branch master
    You have unmerged paths.
      (fix conflicts and run "git commit")
      (use "git merge --abort" to abort the merge)
    
    Unmerged paths:
      (use "git add <file>..." to mark resolution)
            both modified:   test.txt
    
    no changes added to commit (use "git add" and/or "git commit -a")
    ```
    
    ```
    master test 1
    <<<<<<< HEAD
    이건 master에서 작성한 문장입니다.
    =======
    이건 hotfix에서 작성한 문장입니다.
    >>>>>>> hotfix
    ```
    
    - `=======` 위쪽의 내용은 HEAD 버전(merge 명령을 실행할 때 작업하던 `master` 브랜치)의 내용이고 아래쪽은 `hotfix` 브랜치의 내용입니다. 충돌을 해결하려면 위쪽이나 아래쪽 내용 중에서 고르거나 새로 작성하여 Merge 해야 합니다. 
    (`<<<<<<<, =======, >>>>>>>` 가 포함된 행은 삭제)
    
    ```bash
    # test.txt 최종본
    
    master test 1
    이건 충돌을 해결한 후의 문장입니다.
    ```
    
8. merge commit 진행합니다.
    
    ```bash
    $ git add .
    $ git commit
    ```
    
    - vim 편집기 등장
        
        ```bash
        Merge branch 'hotfix'
        
        # Conflicts:
        #       test.txt
        #
        # It looks like you may be committing a merge.
        # If this is not correct, please run
        #       git update-ref -d MERGE_HEAD
        # and try again.
        
        # Please enter the commit message for your changes. Lines starting
        # with '#' will be ignored, and an empty message aborts the commit.
        #
        # On branch master
        # All conflicts fixed but you are still merging.
        #
        ```
        
    - 작성된 커밋 메세지를 확인하고 `esc` 를 누른후 `:wq` 를 입력하여 저장 & 종료합니다.
        
        ```bash
        $ git commit
        [master 8ef1443] Merge branch 'hotfix'
        ```
        
9. log 확인
    
    ```bash
    $ git log --oneline --all --graph
    *   8ef1443 (HEAD -> master) Merge branch 'hotfix'
    |\
    | * ad045fa (hotfix) hotfix test 1
    * | 3170247 master test 3
    |/
    *   ac0e971 Merge branch 'signout'
    |\
    | * bcade83 signout test 1
    * | 48bd5a6 master test 2
    |/
    * df231d0 login test 1
    * 1e62b4c master test 1
    ```
    
10. `hotfix` 브랜치를 삭제합니다.


# 10) Git workflow

<aside>
💡 **Branch를 이용해 협업을 하는 두 가지 방법**에 대해 알아봅니다.
1. 원격 저장소 소유권이 있는 경우 (Shared repository model)
2. 원격 저장소 소유권이 없는 경우 (Fork & Pull model)

</aside>

## [1] 원격 저장소 소유권이 있는 경우 (Shared repository model)

### (1) 개념

- 원격 저장소가 자신의 소유이거나 collaborator로 등록되어 있는 경우에 가능합니다.
- master에 직접 개발하는 것이 아니라, `기능별로 브랜치`를 따로 만들어서 개발합니다.
- `Pull Request`를 같이 사용하여 팀원 간 변경 내용에 대한 소통을 진행합니다.

### (2) 작업 흐름

1. 소유권이 있는 원격 저장소를 로컬 저장소로 `clone` 받습니다.
    
    ```bash
    $ git clone https://github.com/edukyle/django-project.git
    ```
    

1. 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성`하고, 그 안에서 `기능을 구현`합니다.
    
    ```bash
    $ git switch -c feature/login
    ```
    

1. 기능 구현이 완료되면, 원격 저장소에 해당 브랜치를 `push` 합니다.
    
    ```bash
    $ git push origin feature/login
    ```
    

1. 원격 저장소에는 master와 각 기능의 브랜치가 반영되었습니다.

1. Pull Request를 통해 브랜치를 master에 반영해달라는 요청을 보냅니다.
(팀원들과 코드 리뷰를 통해 소통할 수 있습니다.)
    
2. 병합이 완료되면 원격 저장소에서 병합이 완료된 브랜치는 불필요하므로 삭제합니다.

1. master에 브랜치가 병합되면, 각 사용자는 로컬의 master 브랜치로 이동합니다.
    
    ```bash
    $ git switch master
    ```
    

1. 병합으로 인해 변경된 원격 저장소의 master 내용을 로컬에 받아옵니다.
    
    ```bash
    $ git pull origin master
    ```
    

1. 병합이 완료된 master의 내용을 받았으므로, 기존 로컬 브랜치는 삭제합니다. (한 사이클 종료)
    
    ```bash
    $ git branch -d feature/login
    ```
    

1. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복합니다.
    
    ```bash
    $ git switch -c feature/pay
    ```
    

## [2] 원격 저장소 소유권이 없는 경우 (Fork & Pull model)

### (1) 개념

- 오픈 소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우 사용합니다.
- 원본 원격 저장소를 그대로 내 원격 저장소에 `복제`합니다. (이 행위를 `fork`라고 합니다.)
- 기능 완성 후 `Push는 복제한 내 원격 저장소에 진행`합니다.
- 이후 `Pull Request`를 통해 원본 원격 저장소에 반영될 수 있도록 요청합니다.

### (2) 작업 흐름

1. 소유권이 없는 원격 저장소를 `fork`를 통해 내 원격 저장소로 `복제`합니다.
    
    아래와 같이 `Fork` 버튼을 누르면 자동으로 내 원격 저장소에 복제됩니다.
    

1. `fork` 후, 복제된 내 원격 저장소를 로컬 저장소에 `clone` 받습니다.
    
    ```bash
    $ git clone https://github.com/edukyle/kakao_clone.git
    ```
    

1. 이후에 로컬 저장소와 원본 원격 저장소를 동기화 하기 위해서 연결합니다.
    
    ```bash
    # 원본 원격 저장소에 대한 이름은 upstream으로 붙이는 것이 일종의 관례
    
    $ git remote add upstream https://github.com/AlexKwonPro/kakao_clone.git
    ```
    

1. 사용자는 자신이 작업할 기능에 대한 `브랜치를 생성`하고, 그 안에서 `기능을 구현`합니다.
    
    ```bash
    $ git switch -c feature/login
    ```
    
2. 기능 구현이 완료되면, `복제 원격 저장소(origin)`에 해당 브랜치를 `push` 합니다.
    
    ```bash
    $ git push origin feature/login
    ```
    
3. `복제 원격 저장소(origin)`에는 master와 브랜치가 반영되었습니다.

1. `Pull Request`를 통해 `복제 원격 저장소(origin)의 브랜치`를 `원본 원격 저장소(upstream)의 master`에 반영해달라는 요청을 보냅니다. 
(원본 원격 저장소의 관리자가 코드 리뷰를 진행하여 반영 여부를 결정합니다.)

1. `원본 원격 저장소(upstream)`의 master에 브랜치가 병합되면 `복제 원격 저장소(origin)`의 브랜치는 삭제합니다. 그리고 사용자는 로컬에서 master 브랜치로 이동합니다.
    
    ```bash
    $ git switch master
    ```
    

1. 병합으로 인해 변경된 `원본 원격 저장소(upstream)의 master` 내용을 로컬에 받아옵니다. 
그리고 기존 로컬 브랜치는 삭제합니다. (한 사이클 종료)
    
    ```bash
    $ git pull upstream master
    $ git branch -d feature/login
    ```
    

1. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복합니다.
    
    ```bash
    $ git switch -c feature/pay
    ```
    

## [3] Pull Request (PR) 자세히 알아보기

> Github 화면을 통해 Pull Request 과정을 자세히 알아봅니다.
> 

1. 브랜치를 Push 하면 `Compare & pull request` 라는 알림 버튼이 나타나는데, 이를 누르면 됩니다.
    
2. 혹은 원격 저장소 상단 바에서 `Pull requests → New pull request`을 통해서도 가능합니다.

1. `base`는 병합될 대상입니다. `master를 base로` 두면 됩니다.
`compare`는 병합할 대상입니다. 우리가 만든 `feature/login 브랜치를 compare로` 두면 됩니다.
그리고 아래쪽에서 비교 내용을 확인하고 `Create pull request`를 클릭합니다.
    
1. Pull Request에 대한 제목과 내용, 각종 담당자를 지정하는 페이지가 나옵니다.
모두 작성했다면 `Create pull request`를 눌러서 PR을 생성합니다.
    
    `Reviewers` : 현재 PR에 대해 코드 리뷰를 진행해 줄 담당자
    
    `Assignees` : 현재 PR에 대한 작업을 맡고 있는 담당자
    
2. PR이 생성되면 다음과 같은 화면이 나타납니다. 빨간 표시가 된 세 부분을 살펴보겠습니다.
    
3. `Conversation` : 아래 Write 부분에서 comment를 별도로 작성할 수도 있습니다. 그리고 `Merge pull request` 버튼을 누르면 병합이 시작됩니다. (충돌(conflict) 상황에서는 충돌을 해결하라고 나옵니다.)
    
4. `Commits` : PR을 통해 반영될 커밋들을 볼 수 있습니다.
    
5. `Files changed` : 파일의 변화 내역들을 볼 수 있습니다.
    
6. 코드리뷰를 원하는 라인에서 `+` 를 눌러서 해당 라인에 리뷰를 남길 수 있습니다.
    
    빨간 사각형으로 표시된 작은 아이콘을 클릭하면, 
    **`suggestion 기능`(코드를 이렇게 바꾸라고 추천하는 기능)**을 넣을 수도 있습니다.
    
7. 코드 리뷰를 끝내려면 `Finish your review` 버튼을 누르면 됩니다. 
그리고 옵션을 선택하고 `Submit review`를 클릭합니다.
    
    - `Comment`: 추가적인 comment를 작성할 경우 선택
    - `Approve`: merge를 승인하는 경우 선택
    - `Request change` : 수정해야 하는 사항이 있을 경우 선택

1. 다시 conversation으로 가보면 진행했던 리뷰가 이렇게 나타난 것을 확인할 수 있습니다.

1. 병합을 하게 되면 아래와 같이 보라색으로 병합이 완료되었다고 나오면 성공입니다.
    
    `Delete branch` 버튼을 통해 병합된 `feature/login` 브랜치를 지울 수 있습니다. 
    (원격 저장소에서만 지워집니다.)
    
2. `master`를 확인해보면 `feature/login`의 내용이 master에 병합된 것을 확인할 수 있습니다.
    
3. 이후 로컬 저장소의 master 브랜치에서 `git pull`을 이용해 로컬과 원격을 동기화 합니다.


# 11) Undoing

## [1] 파일 내용을 수정 전으로 되돌리기

> Working Directory에서 파일을 수정했다고 가정해봅시다.
만약 이 파일의 수정 사항을 취소하고, 원래 모습대로 돌리려면 어떻게 해야 할까요?
> 

### (1) git restore

- `git restore <파일 이름>`의 형식을 사용합니다.
- Git의 추적이 되고 있는, 즉 버전 관리가 되고 있는 파일만 되돌리기가 가능합니다.

1. 이미 버전 관리가 되고 있는 test.md 파일을 변경 후 저장(save)합니다.
    
    ```
    # test.md
    Hello
    World <- "World"라는 새로운 내용 추가
    -------------------------------------
    이후 저장
    ```
    
2. test.md는 modified 상태가 되었습니다.
    
    ```bash
    $ git status
    On branch master
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   test.md
    
    no changes added to commit (use "git add" and/or "git commit -a")
    ```
    
3. git restore를 통해 수정 전으로 되돌립니다.
    
    ```bash
    $ git restore test.md
    ```
    
    ```
    # test.md
    Hello
    -------------------------------------
    World가 삭제 되면서, 수정 전으로 되돌아감
    ```
    
- 참고사항
    
    ```bash
    # 구버전 Git(2.23.0 이전)에서는 아래와 같은 명령어 사용
    
    $ git checkout -- <파일 이름>
    ```
    

<aside>
❗ 한 번 git restore를 통해 수정을 취소하면, 해당 내용을 복원할 수 없으니 주의 바랍니다!

</aside>

## [2] 파일 상태를 Unstage로 되돌리기

> “Staging Area와 Working Directory 사이를 넘나드는 방법”

`git add`를 통해서 파일을 `Staging Area`에 올렸다고 가정해봅시다.
만약 이 파일을 다시 `Unstage` 상태로 내리려면 어떻게 해야 할까요? 
두 가지 상황으로 나누어 살펴보겠습니다.
> 

### (1) git rm --cached

1. 새 폴더에서 git 초기화 후 진행 `test.md` 파일을 생성하고 git add를 진행
    
    ```bash
    $ touch test.md
    ```
    
    ```bash
    $ git add test.md
    ```
    
    ```bash
    $ git status
    On branch master
    
    No commits yet
    
    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)
            new file:   test.md
    ```
    
2. Staging Area에 올라간 test.md를 다시 내리기(unstage)
    
    ```bash
    $ git rm --cached test.md
    rm 'test.md'
    ```
    
    ```bash
    $ git status
    On branch master
    
    No commits yet
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            test.md
    
    nothing added to commit but untracked files present (use "git add" to track)
    ```
    

### (2) git restore --staged

- 두번째 상황 전 사전 준비
    
    ```bash
    $ git add .
    $ git commit -m "first commit"
    ```
    
1. `test.md`의 내용을 변경하고 git add를 진행
    
    ```bash
    test.md 파일 변경 후
    $ git add test.md
    ```
    
    ```bash
    $ git status
    On branch master
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            modified:   test.md
    ```
    
2. Staging Area에 올라간 test.md를 다시 내리기(unstage)
    
    ```bash
    $ git restore --staged test.md
    ```
    
    ```bash
    $ git status
    On branch master
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   test.md
    
    no changes added to commit (use "git add" and/or "git commit -a")
    ```
    
- 참고사항
    
    ```bash
    구버전 Git(2.23.0 이전)에서는 아래와 같은 명령어 사용
    
    $ git reset HEAD <파일 이름>
    ```
    

<aside>
💡 **(중요) Unstage로 되돌리는 명령어가 다른 이유가 무엇인가요?**

1. `git rm --cached <file>`
    - **기존에 커밋이 없는 경우**
    - “to unstage and remove paths only from the staging area”
2. `git restore --staged <file>`
    - **기존에 커밋이 존재하는 경우**
    - “the contents are restored from HEAD”
</aside>

## [3] 바로 직전 커밋 수정하기

> 만약 `A`라는 기능을 완성하고 `"A 기능 완성"`이라는 커밋을 남겼다고 가정해봅시다.
그런데 아차! A 기능에 필요한 파일 중 1개를 빼놓고 커밋 했다는 걸 깨달아 버렸습니다.
직전 커밋을 취소하고, 모든 파일을 포함해서 다시 커밋 하려면 어떻게 해야 할까요?
> 

### (1) git commit --amend

- 2가지 역할
    1. Staging Area에 새로 올라온 내용이 없다면, 단순히 `직전 커밋의 메시지만 수정`합니다. 
    (즉, 커밋하자마자 바로 이 명령어을 실행하는 경우)
    2. Staging Area에 새로 올라온 내용이 있다면, 직전 커밋 내역에 같이 묶어서 재 커밋 됩니다.

**1-1. 커밋 메시지만 수정하는 경우**

1. A 기능을 완성하고 커밋합니다.
    
    ```bash
    $ git commit -m 'B feature completed'
    ```
    
2. 현재 커밋 해시 값 확인해두기
    
    ```bash
    $ git log
    ```
    
3. 커밋 메시지 수정을 위해 다음과 같이 입력합니다.
    
    ```bash
    $ git commit --amend
    
    hint: Waiting for your editor to close the file..[master c01f908] Add no.txt
    ...
    ```
    
4. Vim 편집기가 열리면서 직전 커밋 메시지를 수정할 수 있습니다.
    
    ```bash
    B feature completed
    
    # Please enter the commit message for your changes. Lines starting
    # with '#' will be ignored, and an empty message aborts the commit.
    #
    # Date:      Wed Jan 12 01:25:10 2022 +0900
    #
    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    #       new file:   test.txt
    ```
    
5. 커밋 메세지를 수정하고 저장하면 새로운 메세지로 변경되며 커밋 **해시 값 또한 변경됨**
    
    ```bash
    $ git log
    ```
    

**1-2. 커밋 재작성**

1. 실수로 bar.txt를 빼고 커밋 해버린 상황까지 만들어 봅시다.
    
    ```bash
    $ touch foo.txt bar.txt
    $ git add foo.txt
    ```
    
    ```bash
    $ git status
    On branch master
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   foo.txt
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            bar.txt
    ```
    
    ```bash
    $ git commit -m "foo & bar"
    
    [master 4221af6] foo & bar
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 foo.txt
    ```
    
    ```bash
    $ git status
    
    On branch master
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
            bar.txt
    ```
    
2. 누락된 파일을 staging area로 이동 시킵니다.
    
    ```bash
    $ git add bar.txt
    
    $ git status
    On branch master
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   bar.txt
    ```
    
3. `git commit --amend` 를 입력합니다
    
    ```bash
    $ git commit --amend
    ```
    
4. Vim 편집기가 열립니다. (마찬가지로 커밋 메시지도 수정가능)
    
    ```bash
    foo & bar
    
    # Please enter the commit message for your changes. Lines starting
    # with '#' will be ignored, and an empty message aborts the commit.
    #
    # Date:      Mon Jun 7 22:32:58 2021 +0900
    #
    # On branch master
    # Changes to be committed:
    #       new file:   bar.txt
    #       new file:   foo.txt
    ```
    
5. Vim 편집기를 저장 후 종료하면 직전 커밋이 덮어 씌워집니다. (커밋이 새로 추가된 것이 아님)
마찬가지로 커밋 **해시 값 또한 변경됨** 
    
    ```bash
    $ git commit --amend
    
    [master 7f6c24c] foo & bar
     Date: Mon Jun 7 22:32:58 2021 +0900
     2 files changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 bar.txt
     create mode 100644 foo.txt
    ```
    
6. `git log -p` 를 사용하여 직전 커밋의 변경 내용을 살펴봅니다.

<aside>
💡 **Vim 간단 사용법**

1. 입력 모드(`i`)
    - 문서 편집 가능
2. 명령 모드(`esc`)
    - `dd` : 해당 줄 삭제
    - `:wq` : 저장 및 종료
        - `w` : write (저장)
        - `q` : quit (종료)
    - `:q!` : 강제 종료
        - `q` : quit
        - `!` : 강제
</aside>


# 12) reset, revert

## [1] git reset

> 가끔 앱을 사용하다가 업데이트를 했는데, 오히려 예전 버전이 더 좋다고 느낄 때가 있습니다.
이처럼 만약 여러분들이 예전 버전으로 돌아가고 싶을 땐 어떻게 해야할까요?
> 

- `git reset [옵션] <커밋 ID>`의 형태로 사용합니다.
- **시계를 마치 과거로 돌리는 듯한 행위**로써, 특정 커밋 상태로 되돌아갑니다.
- 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓아 놨던 커밋들은 전부 사라집니다.

- `옵션`은 아래와 같이 세 종류가 있으며, 생략 시 `--mixed`가 기본 값입니다.
    1. `--soft` 
        - **돌아가려는 커밋으로 되돌아가고**,
        - 이후의 commit된 파일들을 `staging area`로 돌려놓음 (commit 하기 전 상태)
        - 즉, 다시 커밋할 수 있는 상태가 됨
    2. `--mixed`
        - **돌아가려는 커밋으로 되돌아가고**,
        - 이후의 commit된 파일들을 `working directory`로 돌려놓음 (add 하기 전 상태)
        - 즉, unstage 된 상태로 남아있음
        - 기본 값
    3. `--hard`
        - **돌아가려는 커밋으로 되돌아가고**,
        - 이후의 commit된 파일들(`tracked 파일들`)은 모두 working directory에서 삭제
        - 단, Untracked 파일은 Untracked로 남음
        - 혹시나 이미 삭제한 커밋으로 다시 돌아가고 싶다면? → `git reflog`를 사용합니다.
            
            ```bash
            $ git reflog
            1a410ef HEAD@{0}: reset: moving to 1a410ef
            ab1afef HEAD@{1}: commit: modified repo.rb a bit
            484a592 HEAD@{2}: commit: added repo.rb
            
            git reflog 명령어는 HEAD가 이전에 가리켰던 모든 커밋을 보여줍니다.
            따라서 --hard 옵션을 통해 지워진 커밋도, reflog로 조회하여 돌아갈 수 있습니다.
            ```
            
        - 예시
            
            ```bash
            # --hard 예시
            
            $ git log --oneline
            d56a232 (HEAD -> master) hello
            7f6c24c foo & bar
            006dc87 rename commit message
            3551584 asdasd
            71ccbf1 first
            
            $ git reset --hard 3551584
            HEAD is now at 3551584 asdasd
            
            # 3551584 커밋까지만 살아있고, 나머지 커밋은 모두 사라짐
            $ git log --oneline
            3551584 (HEAD -> master) asdasd
            71ccbf1 first
            
            $ git status
            On branch master
            nothing to commit, working tree clean
            ```
            
## [2] git revert

> git reset은 쉽게 과거로 돌아갈 수 있다는 장점이 있지만, 커밋 내역이 사라진다는 단점이 있습니다. 따라서 다른 사람과 협업할 때 커밋 내역의 차이로 인해 충돌이 발생할 수 있습니다.
> 

- `git revert <커밋 아이디>` 의 형태로 사용합니다.
- **특정 사건을 없었던 일로 만드는 행위**로써, `이전 커밋을 취소한다는 새로운 커밋`을 만듭니다.
- git reset은 커밋 내역을 삭제하는 반면, git revert는 `새로 커밋을 쌓는다`는 차이가 있습니다.
- 사용
    
    ```bash
    $ git log --oneline
    7f6c24c (HEAD -> master) foo & bar
    006dc87 rename commit message
    3551584 asdasd
    71ccbf1 first
    
    # revert commit 편집기 실행
    $ git revert 71ccbf1
    Removing foo.txt
    Removing bar.txt
    [master 3b55051] Revert "first"
     2 files changed, 0 insertions(+), 0 deletions(-)
     delete mode 100644 bar.txt
     delete mode 100644 foo.txt
    
    $ git log --oneline
    3b55051 (HEAD -> master) Revert "foo & bar" # 새로 쌓인 커밋
    7f6c24c foo & bar # 히스토리는 남아있음
    006dc87 rename commit message
    3551584 asdasd
    71ccbf1 first
    ```
    
- 기타
    
    ```bash
    # 공백을 통해 여러 커밋을 한꺼번에 되돌리기 가능
    $ git revert 7f6c24c 006dc87 3551584
    
    # 범위 지정을 통해 여러 커밋을 한꺼번에 되돌리기 가능
    $ git revert 3551584..7f6c24c
    
    # 커밋 메시지 작성을 위한 편집기를 열지 않음 (자동으로 커밋 완료)
    $ git revert --no-edit 7f6c24c
    
    # 자동으로 커밋하지 않고, Staging Area에만 올림 (이후, git commit으로 수동 커밋)
    # 이 옵션은 여러 커밋을 revert 할 때 하나의 커밋으로 묶는게 가능
    $ git revert --no-commit 7f6c24c
    ```
    

<aside>
❗ **git reset과 비슷하다는 이유로 다음 사항이 혼동될 수 있습니다.**

`git reset --hard 5sd2f42`라고 작성하면 5sd2f42라는 커밋`으로` 돌아간다는 뜻입니다.
`git revert 5sd2f42`라고 작성하면 5sd2f42라는 커밋`을` 되돌린다는 뜻입니다.

</aside>


# 13) Github pages

## [1] Github pages

- Github 원격 저장소를 이용해서 손쉽게 `웹사이트를 배포`할 수 있는 기능입니다.
- 보통 자기 소개서나 개인 블로그를 운영할 때 많이 사용합니다!
- `참고` : [https://pages.github.com/](https://pages.github.com/)

- 호스팅 업체 별 비교
    
    
    |  | 구축형 (Wordpress) | 가입형 (Tistory) | GitHub Pages |
    | --- | --- | --- | --- |
    | 비용 | 유료(서버+네트웍) | 무료 | 무료 |
    | 서버 구축 | 필요함 | 필요없음 | 필요없음 |
    | 네트워크 설정 | 필요함 | 필요없음 | 필요없음 |
    | Markdown | 가능 | 불가능(제한적) | 가능 |
    | HTML 편집 | 가능 | 불가능(제한적) | 가능 |

## [2] 실습

- 실제로 코드를 작성해도 좋고,(HTML,CSS,JavaScript) 이미 만들어진 코드를 가져와서 변경해도 좋습니다.
- `템플릿 사이트 목록`
    - [https://startbootstrap.com/](https://startbootstrap.com/)
    - [https://html5up.net/](https://html5up.net/)

### (1) 템플릿 다운 받기

> `Startbootstap → themes → portfolio & resume - CLARENCE TAYLOR - 다운 받기`
> 

### (2) 원하는 폴더에 압축 풀기

1. `git bash here`를 이용하거나 macOS의 경우 터미널을 이용해서, 파일이 있는 폴더로 이동합니다.

1. 그리고 아래의 명령어를 통해서 commit을 하고 push를 합니다.
    
    ```bash
    git init
    git add .
    git commit -m "Upload profile template"
    git remote add origin https://github.com/edukyle/profile.git
    git push -u origin master
    ```
    

1. 성공했다면 Github에 아래와 같이 출력 됩니다. (파일에 따라 다름)

### (3) `Github -> Settings -> Pages` 클릭

### (4) 브랜치 선택 후 Save로 저장

<aside>
❗ 혹시나 웹사이트를 열었는데 404 에러가 나타난다면? 아래 페이지를 확인하여
저장소에 `.nojekyll` 파일을 생성해 봅니다!

</aside>

[About GitHub Pages - GitHub Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#static-site-generators)

## [3] 추후 수정

- vscode에서 `ctrl + f` 찾기 누르고, 왼쪽 화살표 아이콘 누르신 다음에 코드 수정하시면 됩니다.
(웹 페이지는 HTML, CSS JavaScript를 활용해서 만듭니다. )

    수정 후에는 아래 순서대로 진행하면 됩니다.
    
    ```bash
    git add .
    git commit -m "커밋 메시지 작성"
    git push
    ```
    
    그리고 웹사이트 들어가서 강력 새로 고침(`ctrl + shift + r`)을 합니다.
    
    Github pages가 원래 반영이 좀 느려서, 고친 내용이 나타나기까지 조금 걸릴 수 있습니다.


# 14) Github README Profiles
# 1. 저장소 생성

- 본인의 Github 이름으로 저장소를 생성합니다.
    
    <aside>
    ✅ Public 설정 & Initialize this repository with a README 체크 해줍니다.
    
    </aside>

---

# 2. 프로필 수정

<aside>
✅ **[github-readme-stats](https://github.com/anuraghazra/github-readme-stats)**를 이용하여 가볍게 꾸며봅니다.

</aside>

- 위에서 생성한 `Github Username` 저장소로 이동합니다.
    
- 오른쪽에 위치한 `Edit README` 버튼을 클릭합니다.
    
- 간단한 인사말과 함께 stat을 추가해줍니다.
    
    `**username` 부분에 자신의 github 유저명을 적어줍니다.**
    
    **추가적으로 github pages로 생성한 블로그 주소도 적어줍니다.**
    
    ```markdown
    ### Hi, there 👋 I'm Eric.
    I love coding 💓
    
    ### About Me
    - Blog: [My Github Blog](https://Machineric.github.io.)
    
    ---
    [![Machineric's github stats](https://github-readme-stats.vercel.app/api?**username=Machineric**)](https://github.com/anuraghazra/github-readme-stats)
    ```
    
- 마지막으로 스크롤을 내려서 `Commit Changes` 버튼을 눌러줍니다.