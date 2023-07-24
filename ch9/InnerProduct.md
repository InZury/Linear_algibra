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
> \begin{pmatrix}
> \langle u, v \rangle = u \dot v =
> u_{1}v_{1} + u_{2}v_{2} + \cdots + u_{n}v_{n}
> \end{pmatrix}
> ```

내적을 벡터 형식으로 표현하면 다음과 같다.  
> ```math
> u = 
> \begin{pmatrix}
> u_{1} \\ u_{2} \\ \vdots \\ u_{n}
> \end{pmatrix}, \ \
> v = 
> \begin{pmatrix}
> v_{1} \\ v_{2} \\ \vdots \\ v_{n}
> \end{pmatrix}, \ \
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

벡턴는 다음과 같은 결과를 갖는다.
> 내적 $ > 0$이면, 두 벡터 사이의 각도 $ < 90$  
> 내적 $ < 0$이면, 두 벡터 사이의 각도 $ > 90$  
> 내적 $ = 0$이면, 두 벡터 사이의 각도 $ = 90$

위 성질에 의하여 내적을 통해 두 벡터가 이루는 형태를 알 수 있으며,  
내적 연산 만으로 두 벡터의 수직 여부를 알 수 있다.  

<br>

내적을 이용하면 벡터의 길이를 구할 수 있으며, 벡터의 길이는 **노름**(norm)이라 하며 다음과 같이 표현한다.
> $ u = (u_{1}, u_{2}, \cdots, u_{n})$  
> $ \Vert u \Vert = \sqrt{u_{1}^{2} + u_{2}^{2} + \cdots + u_{n}^{2}}$

내적을 기하학적 관점에서 다음과 같이 정의할 수 있다.
> $ u \cdot v = \Vert u \Vert \Vert v \Vert cos \theta$  
> $ cos \theta = \dfrac{u \cdot v}{\Vert u \Vert \Vert v \Vert}$