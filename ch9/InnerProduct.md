# **내적 (Inner Product)**
---

## **내적**
벡터 공간 $S$에서 다음 공리를 만족하는 벡터 공간을 **내적 공간**이라 한다.  
(단, $u$, $v$, $w$는 벡터, $a$는 스칼라)
> - $\langle u, v \rangle = \langle v, u \rangle$  
> - $\langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$  
> - $\langle au, v \rangle = a\langle u, v \rangle$  
> - $\langle u, v \rangle \geq 0$

$\langle u, v\rangle$는 벡터 $u$와 $v$의 내적을 의미한다.

<br>

내적은 다른 연산과 다르게 입력 값과 출력 값의 결과 값이 다를 수 있다.  
> - $a + b = c$ (스칼라의 합)  
> - ```math
> \begin{pmatrix}
> x \\ y
> \end{pmatrix} +
> \begin{pmatrix}
> z \\ w
> \end{pmatrix} =
> \begin{pmatrix}
> u \\ v
> \end{pmatrix}
> ``` (벡터의 합)