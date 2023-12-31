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
스칼라의 합 연산은 다음과 같다.  
> ```math
> a + b = c
> ```  

벡터의 합 연산은 다음과 같다.
> ```math
> \begin{pmatrix}
> x \\ y
> \end{pmatrix} +
> \begin{pmatrix}
> z \\ w
> \end{pmatrix} =
> \begin{pmatrix}
> u \\ v
> \end{pmatrix}
> ```

스칼라의 합과 벡터의 합은 모두 입력 값과 결과 값의 형태가 동일하다.  
하지만 벡터 $u$와 $v$에 대하여 내적은 다음과 같이 계산하며, 입력 값과 결과 값의 형태가 다를 수 있다.  
> ```math
> \langle u, v \rangle = u \cdot v =
> u_{1}v_{1} + u_{2}v_{2} + \cdots + u_{n}v_{n}
> ```

내적을 벡터 형식으로 표현하면 다음과 같다.  
> ```math
> u = 
> \begin{pmatrix}
> u_{1} \\ u_{2} \\ \vdots \\ u_{n}
> \end{pmatrix},
> \ \ v = 
> \begin{pmatrix}
> v_{1} \\ v_{2} \\ \vdots \\ v_{n}
> \end{pmatrix}
> ```
> ```math
> \langle u, v \rangle = u^{T}v =
> (u_{1}, u_{2}, \cdots, u_{n})
> \begin{pmatrix}
> v_{1} \\ v_{2} \\ \vdots \\ v_{n}
> \end{pmatrix} = 
> u_{1}v_{1} + u_{2}v_{2} + \cdots + u_{n}v_{n}
> ```
이는 대수적 관점에서의 내적을 정의한 것이다.


<br>

벡터는 다음과 같은 결과를 갖는다.
> 내적 $> 0$이면, 두 벡터 사이의 각도 $< 90$  
> 내적 $< 0$이면, 두 벡터 사이의 각도 $> 90$  
> 내적 $= 0$이면, 두 벡터 사이의 각도 $= 90$

위 성질에 의하여 내적을 통해 두 벡터가 이루는 형태를 알 수 있으며,  
내적 연산 만으로 두 벡터의 수직 여부를 알 수 있다.  

<br>

내적을 이용하면 벡터의 길이를 구할 수 있으며, 벡터의 길이는 **노름**(norm)이라 하며 다음과 같이 표현한다.
> $u = (u_{1}, u_{2}, \cdots, u_{n})$  
> $\Vert u \Vert = \sqrt{u_{1}^{2} + u_{2}^{2} + \cdots + u_{n}^{2}}$

내적을 기하학적 관점에서 다음과 같이 정의할 수 있다.
> $u \cdot v = \Vert u \Vert \Vert v \Vert cos \theta$  
> 
> $cos \theta = \dfrac{u \cdot v}{\Vert u \Vert \Vert v \Vert}$

<br>

벡터 공간 $V$에 벡터 $u$가 존재할 때, 벡터 $u$를 부분 공간으로 하여 수직으로 투영한 것을
**정사영**(projection)이라 한다.  
내적은 정사영과 비슷한 개념으로 생각할 수 있으며 다음과 같다.  
> ![proj](/resource/projection.png)  

벡터 $u$를 $v$에 정사영 시킨 벡터의 길이는 $\Vert u \Vert \vert cos\theta \vert$이며  
길이는 음수가 될 수 없으므로 $cos\theta$에 절댓값을 취한다.  
또한, 벡터 $u$를 벡터 $v$에 정사영 시킨 벡터를 다음과 같이 나타낸다.
> $\Vert proj_{v}u \Vert = \Vert u \Vert \vert cos\theta \vert$

<br>

즉, 벡터 $u$를 벡터 $v$에 정사영시킨 벡터의 길이인 $\Vert u \Vert cos\theta$와 기존 벡터 $v$의 길이인 $\Vert v \Vert$의 곱과 같다.
> ```math
> \begin{aligned}
> \langle u, v \rangle
> =& \Vert u \Vert \Vert v \Vert cos\theta \\
> =& (\Vert v \Vert) \times (\Vert u \Vert cos\theta) \\
> =& (length \ of \ vector \ v) \times (length \ of \ vector \ proj_{v}u)
> \end{aligned}
> ```

내적의 결과가 음수라면 $proj_{v}u$는 벡터 $v$에 반대 방향임을 알 수 있다.

<br><br>

## **직교 공간과 정규 직교 공간**
두 직선 또는 두 평면이 직각을 이루며 만나는 것을 **직교**(orthogonal)이라고 한다.  
벡터 공간에서는 모든 벡터가 서로 직교하면 해당 벡터 공간은 직교한다고 말한다.  
이때, 벡터의 길이가 1일 때, 이를 **정규 직교**(orthonormal)라고 한다.

<br>

벡터 공간 $S$와 벡터 $u_{1}$, $u_{2}$, $u_{3}$가 다음과 같을 때
> - $S = \lbrace {u_{1}, u_{2}, u_{3}} \rbrace$  
> - 벡터 공간 $S$에 속한 벡터 간 내적값이 모두 0 일 때

벡터 공간 $S$는 직교한다고 말한다.

<br>

직교 공간에 존재하는 직교 벡터의 길이가 모두 1인 경우, 해당 벡터를 **정규 직교 벡터**(orthonormal vector)라고 하며  
정규 직교 벡터가 만드는 공간을 **정규 직교 공간**(orthonormal space)라고 한다.

<br>

직교 벡터를 정규 직교 벡터로 변환하는 과정을 **정규화**(normalization)라고 하며 다음과 같이 변환한다. 
> $v = \dfrac{1}{\Vert u \Vert}u$  
> 
> $\Vert v \Vert = \Vert \dfrac{1}{\Vert u \Vert}u \Vert = \dfrac{1}{\cancel{\Vert u \Vert}}\cancel{\Vert u \Vert} = 1$


<br><br>

## 정규 직교 벡터의 좌표 표현
벡터 공간 $V$의 **정규 직교 기저**(orthonormal basis)를 $S = \lbrace v_{1}, v_{2}, \cdots, v_{n} \rbrace$라고 할 때  
벡터 공간 $V$에 속하는 임의의 벡터 $u$는 다음과 같이 표현한다.
> $u = \langle a, v_{1} \rangle v_{1} + \langle a, v_{2} \rangle v_{2} + \cdots + \langle a, v_{n} \rangle v_{n}$

여기서 $\langle a, v_{i} \rangle$를 $c_{i}$라 할 때 벡터 $u$는 다음과 같이 나타낼 수도 있다.
> ```math
> \begin{aligned}
> u =& \langle a, v_{1} \rangle v_{1} + \langle a, v_{2} \rangle v_{2} + \cdots + \langle a, v_{n} \rangle v_{n} \\
> =& c_{1}v_{1} + c_{2}v_{2} + \cdots + c_{n}v_{n} \\
> =& (c_{1}, c_{2}, \cdots, c_{n})
> \end{aligned}
> ```

<br>

벡터 $u$와 기저 벡터 $v_{i}$를 내적하면 다음과 같다.
> ```math
> \begin{aligned}
> \langle a, v_{i} \rangle
> =& \langle c_{1}v_{1} + c_{2}v_{2} + \cdots + c_{n}v_{n}, \ v_{i} \rangle \\
> =& \langle c_{1}v_{1}, \ v_{i} \rangle + \langle c_{2}v_{2}, \ v_{i} \rangle + \cdots + \langle c_{n}v_{n}, \ v_{i} \rangle \\
> =& \langle c_{i}v_{i}, \ v_[i] \rangle \\
> =& c_{i}v_{i}^{T}v_{i} \\
> =& c_{i}
> \end{aligned}
> ```
>  
> $$\therefore a = c_{i}$$

<br>

벡터 공간 $V$에 **직교 기저**(orthogonal basis)를 $U = \lbrace u_{1}, u_{2}, \cdots, u_{n} \rbrace$라 라 할 때, 임의의 벡터 $w$는 다음과 같이 표현할 수 있다.
> $w = \dfrac{\langle a, u_{1} \rangle}{\Vert u_{1} \Vert^{2}}u_{1} + \dfrac{\langle a, u_{2} \rangle}{\Vert u_{2} \Vert^{2}}u_{2} + \cdots + \dfrac{\langle a, u_{n} \rangle}{\Vert u_{n} \Vert^{2}}u_{n}$

이때 벡터 $u$의 좌표는 다음과 같이 나타낸다.
> ```math
> w = 
> \begin{Bmatrix}
> \dfrac{\langle a, u_{1} \rangle}{\Vert u_{1} \Vert^{2}}, &
> \dfrac{\langle a, u_{2} \rangle}{\Vert u_{2} \Vert^{2}}, &
> \cdots, &
> \dfrac{\langle a, u_{n} \rangle}{\Vert u_{n} \Vert^{2}}
> \end{Bmatrix}
> ```

<br><br>

## **그램 슈미트 과정**
정사영의 개념을 활용하는 정리는 다음과 같다.
> **정사영 정리**(projection theorem)  
> 벡터 공간 $S$의 부분 공간 $W$가 존재할 때 벡터 공간 $S$에 속하는 임의의 벡터 $u$는 다음과 같이 표현할 수 있다.
> $$ u = w_{1} + w{2} $$
> 이때, $w_{1}$은 부분 공간 $W$에 속하는 벡터이며, $w_{2}$는 부분 공간의 직교 공간인 $W^{-1}$에 속하는 벡터이다.  
> ```math
> \begin{aligned}
> w_{1} =& Proj_{_{W}}u \\
> w_{2} =& Proj_{_{W\perp}}u
> \end{aligned}
> ```

정사영 정리는 다음과 같이 위와 다르게 표현할 수 있다.
> ```math
> \begin{aligned}
> u =& w_{1} + w_{2} \\
> \Leftrightarrow& w_{2} = u - w_{1} \\
> \Leftrightarrow& u = Proj_{_{W}}u + Proj_{_{W\perp}}u \\
> \Leftrightarrow& Proj_{_{W\perp}}u = u - Proj_{_{W}}u \\
> \Leftrightarrow& u= Proj_{_{W}}u + (u - Proj_{_{W}}u)
> \end{aligned}
> ```

<br>

정사영 개념에 직교 개념이 합쳐진 것을 직교 정사영이라 한다.  
벡터 공간 $S$의 부분 공간을 $W$라 할 때, 부분 공간 $W$의 직교 기저가 $\lbrace u_{1}, u_{2}, \cdots, u_{n}\rbrace$이고 $t$가 벡터 공간 $S$의 임의의 벡터이면 $Proj_{_{W}}t$는 다음과 같다.
> ```math 
> Proj_{W}t = \dfrac{\langle t, u_{1} \rangle}{\Vert u_{1} \Vert^{2}}u_{1} +
> \dfrac{\langle t, u_{2} \rangle}{\Vert u_{2} \Vert^{2}}u_{2} + \cdots +
> \dfrac{\langle t, u_{n} \rangle}{\Vert u_{n} \Vert^{2}}u_{n}
> ```

따라서 $Proj_{_{W}}t$의 좌표는 다음과 같다.
> ```math 
> \left\{
> \dfrac{\langle t, u_{1} \rangle}{\Vert u_{1} \Vert^{2}}, \
> \dfrac{\langle t, u_{2} \rangle}{\Vert u_{2} \Vert^{2}}, \ \cdots, \
> \dfrac{\langle t, u_{n} \rangle}{\Vert u_{n} \Vert^{2}}
> \right\}
> ```

<br>

벡터 공간 $S$에 부분 공간 $W$의 정규 직교 기저가 $\lbrace v_{1}, v_{2}, \cdots, v_{n} \rbrace$일 때  
$r$이 벡터 공간 $S$의 임의의 벡터이면 $Proj_{_{W}}r$은 다음과 같다.
> ```math
> Proj_{_{W}}r = \langle a, v_{1} \rangle v_{1} +
> \langle a, v_{2} \rangle v_{2} + \cdots +
> \langle a, v_{n} \rangle v_{n}
> ```

<br>

기저 벡터 집합 $S = \lbrace s_{1}, s_{2}, \cdots, s_{n} \rbrace$을 직교 기저 벡터 집합
$U = \lbrace u_{1}, u_{2}, \cdots, u_{n} \rbrace$으로  
변환하는 과정을 **그램 슈미트 과정**(Gram-Schmidt Process)라고 한다.  
그램 슈미트 과정은 다음과 같다.
> step 1
> - $u_{1} = s_{1}$
>
> step 2
> - $u_{2} = s_{2} - \dfrac{\langle s_{2}, u_{1} \rangle}{\Vert u_{1} \Vert^{2}}u_{1}$  
> $\because s_{2} = u_{2} + Proj_{_{U_{1}}}s_{2}$
>
> step 3
> - $u_{3} = s_{3} - \dfrac{\langle s_{3}, u_{1} \rangle}{\Vert u_{1} \Vert^{2}}u_{1} - \dfrac{\langle s_{3}, u_{2} \rangle}{\Vert u_{2} \Vert^{2}}u_{2}$  
> $\because s_{3} = u_{2} + Proj_{_{U_{2}}}s_{3}$
>
> $$\vdots$$
> step $n$
> - $u_{n} = s_{n} - \dfrac{\langle s_{n}, u_{1} \rangle}{\Vert u_{1} \Vert^{2}}u_{1} - \dfrac{\langle s_{n}, u_{2} \rangle}{\Vert u_{2} \Vert^{2}}u_{2} - \cdots - \dfrac{\langle s_{n}, u_{n-1} \rangle}{\Vert u_{n-1} \Vert^{2}}u_{n-1}$

그램 슈미트 과정은 기저를 직교 기저로 바꾸기 때문에 모든 벡터가 서로 직교하게 만들어야 한다.

<br>

행렬 $M$이 $n \times p$행렬이고 풀 랭크 일 때, 행렬 $M$의 열 벡터는 모두 선형 독립이다.  
따라서 행렬 $M$의 열 벡터는 공간의 기저가 될 수 있다. 이때, 행렬 $M$을 다음과 같이 분해할 수 있다.
> $M = QR$

이때 $Q$는 $n \times p$행렬이고 정규 직교 벡터로 구성되어 있으며, $R$은 가역 상 삼각행렬이다.  
**가역 상 삼각 행렬**(invertible upper triangular matrix)은 역행렬이 존재하는 상 삼각 행렬을 말한다.

<br>

행렬 $M$의 열 벡터는 다음과 같이 표현할 수 있다.
> - 열 벡터의 표현식 (1)
> $$m_{1} = \langle m_{1}, v_{1} \rangle v_{1} + \langle m_{1}, v_{2} \rangle v_{2} + \cdots + \langle m_{1}, v_{n} \rangle v_{n}$$
> $$m_{2} = \langle m_{2}, v_{1} \rangle v_{1} + \langle m_{2}, v_{2} \rangle v_{2} + \cdots + \langle m_{2}, v_{n} \rangle v_{n}$$
> $$\vdots$$
> $$m_{n} = \langle m_{n}, v_{1} \rangle v_{1} + \langle m_{n}, v_{2} \rangle v_{2} + \cdots + \langle m_{n}, v_{n} \rangle v_{n}$$
> - 열 벡터의 표현식 (2)
> ```math
> \begin{pmatrix} m_{1} & m_{2} & \cdots & m_{n} \end{pmatrix} = 
> \begin{pmatrix} v_{1} & v_{2} & \cdots & v_{n} \end{pmatrix} \begin{pmatrix}
> \langle a_{1}v_{1} \rangle & \langle a_{2}v_{1} \rangle & \cdots & \langle a_{n}v_{1} \rangle \\
> \langle a_{1}v_{v} \rangle & \langle a_{2}v_{v} \rangle & \cdots & \langle a_{n}v_{2} \rangle \\
> \vdots & \vdots & \ddots & \vdots \\
> \langle a_{1}v_{n} \rangle & \langle a_{2}v_{n} \rangle & \cdots & \langle a_{n}v_{n} \rangle
> \end{pmatrix}
> ```

위 표현식을 통해 다음과 같이 나타낼 수 있다.
> $$ M = QR $$
> ```math
> \begin{pmatrix} v_{1} & v_{2} & \cdots & v_{n} \end{pmatrix}
> ```
> ```math
> R = 
> \begin{pmatrix}
> \langle a_{1}v_{1} \rangle & \langle a_{2}v_{1} \rangle & \cdots & \langle a_{n}v_{1} \rangle \\
> \langle a_{1}v_{v} \rangle & \langle a_{2}v_{v} \rangle & \cdots & \langle a_{n}v_{2} \rangle \\
> \vdots & \vdots & \ddots & \vdots \\
> \langle a_{1}v_{n} \rangle & \langle a_{2}v_{n} \rangle & \cdots & \langle a_{n}v_{n} \rangle
> \end{pmatrix}
> ```

이처럼 행렬 $M$을 행렬 $Q$와 행렬 $R$로 분해하는 것을 $QR$분해라고 한다.

<br>

하우스홀더 행렬을 이용하여 $QR$분해할 수도 있다.  
결론적으로 말하면 다음과 같다.
> $$M = QR$$
>
> $$Q = H_{1}H_{2}H_{3}$$
>
> $$R = H_{3}H_{2}H_{1}M$$

하우스홀더 행렬에 대한 이해는 다음 페이지를 통하여 설명한다.
> [Householder QR 분해](https://github.com/InZury/Linear_algibra/blob/main/ch9/Householder_QR.md)

