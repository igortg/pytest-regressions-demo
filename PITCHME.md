@title[Cover]

## Testes de Regressão
### para modelos numéricos e ORMs

<span style="font-size: 0.5em">[ Igor T. Ghisi, Flask-Conf, 2019-09-08 ]</span>

---
@title[Who Am I]

<div class="left">
![img](./assets/image/esss-white.png)<br>
![img](./assets/image/fpolis.gif)<br>

</div>

<div class="right">
<p>![img](./assets/image/me.jpg)</p>
<p>@fa[github] igortg</p>
<p>@fa[twitter] figortg</p>
</div>

---
@title[Abrindo o apetite]

## Abrindo o apetite...

---?code=src/flask_conf_tutorial/player_char.py&lang=python
@title[Abrindo o apetite]

@[23-37]
@[38-52]

---?code=src/flask_conf_tutorial/test_player_char.py&lang=python
@title[Abrindo o apetite]

@[22-37](antes)
@[40-47](depois)

---?code=src/flask_conf_tutorial/test_sklearn_tutorial.py&lang=python
@title[Abrindo o apetite]

@[6-13]
@[6-19](antes)
@[22-30](depois)

---
@title[JetBrains Survey]

![img](assets/jetbrains-2018-tests.png)

16% não tem testes nos projetos que trabalham. Percentual baixa para 8% considerando só
profissionais senior.

---
@title[Pytest Quick Intro]

# Pytest

---
@title[Pytest Quick Intro]

![img](assets/trends-pytest-unittest.png)

Pytest tornou-se o framework de testes padrão _de facto_ para Python

---
@title[Pytest Quick Intro]

`roman7.py`

```python
def to_roman(n):
    '''convert integer to Roman numeral'''
    ...

def from_roman(s):
    '''convert Roman numeral to integer'''
    ...
```

---
@title[Pytest Quick Intro]

`test_roman7.py`

```python
from roman7 import to_roman, from_roman

def test_roman_conversion():
    assert to_roman(3) == 'III'
    assert from_roman('IV') == 4
```

---
@title[Fixtures]

# Pytest fixtures

---
@title[Fixtures - definition]

O que são _fixtures_?

> provide a fixed baseline upon which tests can reliably and repeatedly
execute. - pytest docs

---
@title[Fixtures - definition]

O que são _fixtures_?

> resolve problemas reais que ocorrem na criação de testes
unitários - Ghisi, 2018

---
@title[Fixtures - example]

```python
def test_naive_roman_writer():
    text = "In the Book 3 Chapter 7 of the 2 Collection"
    output_file = 'roman.txt'
    write_to_roman(text, output_file)
    with open(output_file) as output:
        assert output.read() == "In the Book III Chapter VII of the II Collection"
```

@[4]
@[5-6]

---
@title[Fixtures - example]

```python
def test_roman_writer3(tmpdir):
    text = "In the Book 3 Chapter 7 of the 2 Collection"
    output_file = tmpdir.mkdir('test_romans').join('roman.txt')
    write_to_roman(text, str(output_file))
    assert output_file.read() == "In the Book III Chapter VII of the II Collection"
```

@[1]
@[3]

---
@title[Plugins]

Plugins: bibliotecas python que disponibilizam uma ou mais fixtures

---
@title[pytest-datadir]

`pip install pytest-datadir`

---


---
@title[People]

### It's About People

<div class="left">
<ul>
<li>Bruno Oliveira</li>
<li>@fa[twitter]@fa[github] nicoddemus</li>
<li>[pytest for unittest users](https://gitpitch.com/nicoddemus/pytest-for-unittest-users)</li>
</ul>
 
</div>

<div class="right">
![img](assets/image/neco.jpg)
</div>

---
@title[People]

### It's About People

![img](assets/image/pastore.jpg)
<img src="./assets/memes/cafeeeee.gif" height="200"></img>
<ul>
    <li>André Pastore</li>
    <li>@fa[github] apast</li>
    <li>Do nada, tudo se constrói. Testes & Web</li>
    <li>Dom. 13:30h</li>
</ul>

---

![img](assets/memes/santos-fuel-tank-fire.jpg)

<pre class="attr-error">AttributeError: 'FireSystem' object has no attribute 'alamr'</pre> 

Note:
Para quem desenvolve com testes, ou com TDD.
Dar um improvement no seu framework de testes é como melhorar a sua IDE
O desenvolverdor acaba criando mais testes, fazendo testes de melhor qualidade,
e entregando um produto melhor, menos sucetível a falhas

---

### That's all

![img](assets/image/queen.gif)

---


---