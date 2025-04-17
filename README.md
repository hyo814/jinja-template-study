# jinja-template-study

공식 문서 : https://jinja.palletsprojects.com/en/stable/templates/

---

## Jinja 템플릿이란?

- **Jinja**는 HTML, XML, CSV 등 텍스트 기반 파일을 **동적으로 생성**할 수 있게 도와주는 템플릿 엔진.
- 주로 **웹 페이지의 HTML**을 생성할 때 자주 사용.

**기본 구조 예시**

```
<!DOCTYPE html>
<html lang="ko">
<head>
    <title>{{ title }}</title>
</head>
<body>
    {% for user in users %}
        <p>{{ user.name }}</p>
    {% endfor %}
</body>
</html>

```

| 구분자 | 용도 |
| --- | --- |
| `{{ ... }}` | 변수 또는 표현식을 출력 |
| `{% ... %}` | 조건문, 반복문 등 로직 처리 |
| `{# ... #}` | 주석 (출력되지 않음) |

---

## **기본 문법**

| 문법 | 설명 | 예시 |
| --- | --- | --- |
| `{{ 변수 }}` | 변수 출력 | `{{ user.username }}` |
| `{% if %}` | 조건문 처리 | `{% if user.is_authenticated %}` |
| `{% for %}` | 반복문 처리 | `{% for item in items %}` |
| `{# 주석 #}` | 주석 처리 | `{# 이 부분은 출력되지 않습니다. #}` |

**예시**

```
{% if user.is_admin %}
  관리자입니다.
{% else %}
  일반 사용자입니다.
{% endif %}

```

```
{% for post in posts %}
  <li>{{ post.title }}</li>
{% else %}
  게시물이 없습니다.
{% endfor %}

```

---

## **심화 문법**

| 문법 | 설명 | 예시 |
| --- | --- | --- |
| `{% set %}` | 변수 생성 | `{% set total = price * count %}` |
| `{% include %}` | 템플릿 포함 | `{% include 'header.html' %}` |
| `{% extends %}` | 부모 템플릿 상속 | `{% extends 'base.html' %}` |
| `{% block %}` | 재정의 가능한 영역 설정 | `{% block content %}내용{% endblock %}` |
| `{% macro %}` | 재사용 가능한 함수 정의 | `{% macro input(name) %}<input>{{ name }}{% endmacro %}` |
| `{% call %}` | 매크로에 블록 전달 | `{% call box() %}내용{% endcall %}` |
| `{% import %}` | 매크로 불러오기 | `{% import 'macros.html' as m %}` |
| `{% from import %}` | 특정 매크로만 불러오기 | `{% from 'macros.html' import input %}` |
| `{% with %}` | 지역 변수 설정 | `{% with total = sum %}{{ total }}{% endwith %}` |
| `{% raw %}` | Jinja 구문 그대로 출력 | `{% raw %}{{ 출력안됨 }}{% endraw %}` |
| `{% autoescape %}` | 자동 이스케이프 설정 | `{% autoescape true %}내용{% endautoescape %}` |
| `{% do %}` | 출력 없는 표현식 실행 | `{% do mylist.append(3) %}` |

---

## **자주 쓰이는 필터 (Filters)**

| 필터 | 설명 | 예시 |
| --- | --- | --- |
| `length` | 길이 출력 | `{{ list |
| `upper`, `lower` | 대문자/소문자 변환 | `{{ name |
| `replace` | 문자열 치환 | `{{ text |
| `default` | 기본값 지정 | `{{ name |
| `safe` | HTML 그대로 출력 | `{{ html_code |
| `truncate` | 문자열 자르기 | `{{ content |
| `int`, `float` | 타입 변환 | `{{ price |
| `join` | 리스트 결합 | `{{ items |
| `striptags` | HTML 태그 제거 | `{{ html |

**필터 예시**

```
{{ user.name|default('이름 없음') }}
{{ html_code|safe }}
{{ text|truncate(30) }}

```

---

## **템플릿 상속 (Inheritance)**

**부모 템플릿** (`base.html`)

```
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}기본 제목{% endblock %}</title>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>

```

**자식 템플릿**

```
{% extends 'base.html' %}

{% block title %}홈페이지{% endblock %}

{% block content %}
  <h1>환영합니다!</h1>
{% endblock %}

```

---

## **Include와 Import**

**Include 사용법**

```
{% include 'partials/header.html' %}

```

**Import 사용법 (매크로 활용)**

```
{% import 'forms.html' as forms %}
{{ forms.input('username') }}

```

---

## **매크로 (Macro)**

```
{% macro input(name, type='text') %}
<input name="{{ name }}" type="{{ type }}">
{% endmacro %}

{{ input('email', 'email') }}

```

---

## **자동 이스케이프 (Autoescape)**

XSS 공격 방지를 위해 자동으로 HTML을 안전하게 처리.

```
{% autoescape true %}
  {{ user_input }}
{% endautoescape %}

```

신뢰할 수 있는 HTML은 필터 `|safe`를 사용하여 출력.

```
{{ trusted_html|safe }}

```

---

## **공백 제어**

출력물에서 불필요한 공백을 제거.

```
<ul>
{%- for item in items -%}
  <li>{{ item }}</li>
{%- endfor -%}
</ul>

```

---

# 놓치기 쉽지만 중요한 Jinja 문법과 활용법(추가)

### 1. 루프 내 특수 변수 (`loop`)

- 반복문에서 제공하는 `loop` 변수는 생각보다 매우 유용.
- 목록 번호 매기기, 첫 번째 요소나 마지막 요소에 별도 처리 등이 가능.

| 루프 변수 | 설명 | 예시 |
| --- | --- | --- |
| `loop.index` | 1부터 시작하는 인덱스 | `1, 2, 3, ...` |
| `loop.index0` | 0부터 시작하는 인덱스 | `0, 1, 2, ...` |
| `loop.first` | 첫 번째 아이템 여부 | `True, False` |
| `loop.last` | 마지막 아이템 여부 | `True, False` |
| `loop.revindex` | 뒤에서부터 카운트 (1부터 시작) | `5, 4, 3, ...` |
| `loop.length` | 전체 반복 횟수 | `3, 5, 10, ...` |
| `loop.cycle(...)` | 순환값 출력 | 홀짝 표현 등에 유용 |

**예시**

```
<ul>
{% for user in users %}
  <li class="{{ loop.cycle('odd', 'even') }}">
    {{ loop.index }}. {{ user.name }}
    {% if loop.first %}(첫 번째 사용자!){% endif %}
    {% if loop.last %}(마지막 사용자!){% endif %}
  </li>
{% endfor %}
</ul>

```

---

### 2. inline-if (인라인 조건문)

- 간단한 조건식 처리를 더 짧고 간편.

```
{{ user.nickname if user.nickname else '이름 없음' }}

```

---

### 3. 공백 제어의 세부 옵션 (trim_blocks, lstrip_blocks)

- 환경 설정에서 템플릿 전체 공백을 제어.
- 실무에서는 자주 설정하여 사용.

**환경 설정 예시 (Python 코드)**

```python
env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True,       # 블록 뒤의 첫 번째 줄바꿈 제거
    lstrip_blocks=True      # 블록 시작 지점 앞의 공백 제거
)

```

---

### 4. 필터 체이닝 (Filter chaining)

- 여러 필터를 연달아 사용하면 간결한 코드 작성이 가능.

```
{{ content|striptags|truncate(100)|default('내용 없음') }}

```

---

### 5. 여러 조건의 반복문 필터링

- 반복문에 바로 조건을 걸어 필터링.

```
{% for user in users if user.active %}
  <li>{{ user.name }}</li>
{% else %}
  <li>활성화된 사용자가 없습니다.</li>
{% endfor %}

```

---

### 6. `else` 문법의 활용성

- 반복문에 쓰이는 `else`는 항목이 없을 때 실행.
- 조건문에도 `else`는 필수.

**반복문 예시**

```
{% for post in posts %}
  <li>{{ post.title }}</li>
{% else %}
  <li>게시물이 없습니다.</li>
{% endfor %}

```

---

### 7. 디버깅 및 개발용 기능 (`{% debug %}`)

- 템플릿 내에서 변수와 상태를 쉽게 확인.

```
<pre>{% debug %}</pre>

```

---

### 8. 템플릿 내 할당(scope)과 한계점

- Jinja에서 `{% set %}`을 사용할 때 **scope가 제한적**. 블록 바깥에서는 보이지 X .
- 범위 제한을 피하려면 `{% with %}` 또는 네임스페이스 객체 사용이 필요.

**Namespace 사용 예시**

```
{% set ns = namespace(total=0) %}
{% for price in prices %}
  {% set ns.total = ns.total + price %}
{% endfor %}
총 합계: {{ ns.total }}

```

---

### 9. raw 블록 활용법

- Jinja 구문을 그대로 보여줘야 하는 경우. 이때 `{% raw %}`를 사용

```
{% raw %}
이렇게 사용하세요: {{ 변수 }}
{% endraw %}

```
