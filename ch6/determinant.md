# **행렬식 (Determinant)**

---

## **행렬식**
행렬의 특성을 하나의 숫자로 표현하는 방법이며,  
다른 의미로 정사각 행렬을 스칼라로 변환하는 함수를 말한다.

행렬식을 기하학적으로 생각하면, 이는 해당 행렬이 나타내는 **부피**를 계산 할 수 있음을 의미한다.

<br><br>

## **행렬식의 계산**

(행렬식) $=$ (정사각 행렬을 스칼라로 변환하는 함수)이므로  
가장 기초적인 형태인 $2 \times 2$ 크기의 정사각 행렬의 행렬식은 다음과 같다.
> ```math
> det(A) = |A| =
> \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix}
> = a_{11}a_{22} \, - \, a_{12}a_{21}
> ```

$2 \times 2$ 정사각 행렬은 2개의 벡터로 구성되어 있기 때문에 부피가 아닌 넓이로 생각한다.  

<br>

$2 \times 2$ 정사각 행렬 이외의 $3 \times 3$ 정사각 행렬부터는 다음과 같이 계산한다.
> ```math
> |A| =
> \begin{vmatrix}
> a_{11} & a_{12} & a_{13} \\
> a_{21} & a_{22} & a_{23} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> \, = \, a_{11}
> \begin{vmatrix}
> a_{22} & a_{23} \\
> a_{32} & a_{33}
> \end{vmatrix}
> \, - \, a_{12}
> \begin{vmatrix}
> a_{21} & a_{23} \\
> a_{31} & a_{33}
> \end{vmatrix}
> \, + \, a_{13}
> \begin{vmatrix}
> a_{21} & a_{22} \\
> a_{31} & a_{32}
> \end{vmatrix}
>```

위와 같이 $3 \times 3$ 이상 크기의 행렬식은 전체 행렬을 부분 행렬로 나누어 작은 부분 행렬로 계산한다.

<br>

여기서 행렬 $A$의 원소 $a_{ij}$에 대하여 행렬 의 $i$행과 $j$열을 제외하고 구성된 부분 행렬의 행렬식 $M_{ij}$를  
**$a_{ij}$의 소행렬식(minor of entry $a_{ij}$)** 이라 한다.

<br>

또한, 원소 $a_{ij}$에 대하여 다음을  **$a_{ij}$의 여인수(cofactor of entey $_a{ij}$)** 라 한다.
> $C_{ij} \ = \ (-1)^{i + j}M_{ij}$

<br>

여인수와 소행렬식의 차이점은 부호의 차이가 있으며, 여인수의 부호는 다음과 같은 패턴을 갖는다.
> ```math
> \begin{pmatrix}
> + & - & + & - & \cdots \\
> - & + & - & + & \cdots \\
> + & - & + & - & \cdots \\
> - & + & - & + & \cdots \\
> \vdots & \vdots & \vdots & \vdots & \ddots
> \end{pmatrix}
>```

소행렬식을 이용한 계산을 여인수로 표현하면 다음과 같다.
> ```math
>\begin{aligned}det(A) \, =& \, a_{11}M_{11} \, + \, a_{12}(-M_{12}) \, + \,  \cdots \, + \,
> a_{1n-1}(-M_{1n -1}) \, + \, a_{1n}M_{1n} \\
> \, =& \, a_{11}C_{11} \, + \, a_{11}C_{11} \, + \, \cdots \, + \,
> a_{1n}C_{1n} \, + \, a_{1n}C_{1n} \end{aligned}
> ```

<br><br>

## **행렬식의 성질**

다양한 행렬에 대하여 행렬식은 다음과 같은 성질을 갖는다.

삼각 행렬의 행렬식은 다음과 같다.
> ```math
> A = 
> \begin{pmatrix}
> a_{11} & a_{12} & a_{13} \\
> 0 & a_{22} & a_{23} \\
> 0 & 0 & a_{33}
> \end{pmatrix}
> ```

위와 같은 삼각 행렬의 행렬식은

> $det(A) = a_{11}a_{22}a_{33}$

로 계산이 된다.

<br>

대각 행렬의 행렬식은 다음과 같다.
> ```math
> A = 
> \begin{pmatrix}
> a_{11} & 0 & 0 \\
> 0 & a_{22} & 0 \\
> 0 & 0 & a_{33}
> \end{pmatrix}
> ```

위와 같은 대각 행렬의 행렬식은

> $det(A) = a_{11}a_{22}a_{33}$

로 삼각 행렬의 행렬식과 같다.  
따라서 단위 행렬 $I$는 대각 행렬이므로 단위 행렬의 행렬식은 항상 1임을 알 수 있다.

<br>

전치 행렬의 행렬식은 다음과 같다.

> $det(A) = det(A^T)$

행렬 $A$가 정사각 행렬이면 행렬 $A$와 전치 행렬 $A^T$의 행렬식은 동일하다.

<br>

정사각 행렬 $A$에 대하여 다음과 같이 모든 원소가 0인 행 또는 열이 존재하는 경우
> ```math
> A = 
> \begin{pmatrix}
> x & y & 0 \\
> z & w & 0 \\
> p & r & 0
> \end{pmatrix}
> ```

위의 행렬의 행렬식은 다음과 같다. (행렬 $A$의 3열을 기준으로 행렬식 계산)
> ```math
> \begin{aligned} det(A) \, =& \, a_{13}C_{13} \, + \, a_{23}C_{23} \, + \, a_{33}C_{33} \\
> =& \, 0 \times C_{13} \, + \, 0 \times C_{23} \, + \, 0 \times C_{33} \\
> =& \, 0 \end{aligned}
> ```

따라서 특정 행과 열의 원소가 모두 0일 경우, 행렬식은 0이다.

<br>

행렬식도 첨가 행렬의 계산과 마찬가지로 기본 행 연산을 이용하여 나타낼 수 있다.
> **기본 행 연산**
> - 한 행에 0이 아닌 상수를 모두 곱한다.
> - 두 행을 교환한다.
> - 한 행의 배수를 다른 행에 더한다.


정사각 행렬  $A$에 대하여,

 - **한 행에 영이 아닌 상수를 모두 곱한다.**

> $$ k \ det(A) = det(B)$$

> ```math
> k \,
> \begin{vmatrix}
> a_{11} & a_{12} & a_{13} \\
> a_{21} & a_{22} & a_{23} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> \, = \,
> \begin{vmatrix}
> ka_{11} & ka_{12} & ka_{13} \\
> a_{21} & a_{22} & a_{23} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> ```

$A$행렬의 특정 행 또는 열을 $k$배 하면 전체 행렬식의 크기는 $k$배 늘어난다.


> $$det(kA) = k^n det(A)$$

> ```math
> \begin{vmatrix}
> ka_{11} & ka_{12} & ka_{13} \\
> ka_{21} & ka_{22} & ka_{23} \\
> ka_{31} & ka_{32} & ka_{33}
> \end{vmatrix}
> \, = \,
> k^{3} \,
> \begin{vmatrix}
> a_{11} & a_{12} & a_{13} \\
> a_{21} & a_{22} & a_{23} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> ```

$A$행렬의 모든 구성 원소를 $k$배 하면 전체 행렬식은 $k^n$배가 된다. ($n =$ 행렬의 크기)

 - **두 행을 교환한다**

> $$-det(A) = det(B)$$

> ```math
> -
> \begin{vmatrix}
> a_{11} & a_{12} & a_{13} \\
> a_{31} & a_{22} & a_{23} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> \, = \,
> \begin{vmatrix}
> a_{21} & a_{22} & a_{23} \\
> a_{11} & a_{12} & a_{13} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> ```

행렬 $A$의 두 행 또는 두 열을 교환하면 기존 행렬식에서 부호를 바꾼 값과 동일하다.

 - **한 행의 배수를 다른 행에 더한다.**

> $$det(A) = det(B)$$

> ```math
> -
> \begin{vmatrix}
> a_{11} & a_{12} & a_{13} \\
> a_{31} & a_{22} & a_{23} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> \, = \,
> \begin{vmatrix}
> a_{21} & a_{22} & a_{23} \\
> a_{11} & a_{12} & a_{13} \\
> a_{31} + ka_{11} & a_{32} + ka_{12} & a_{33} + ka_{13}
> \end{vmatrix}
> ```

행렬 $A$의 하나의 행 또는 열의 배수를 다른 행에 더해도 기존 행렬식과 값이 동일하다.

<br>

행렬 $A$에 서로 비례하는 두 행 또는 두 열이 존재할 경우 행렬식은 0이다.

> ```math
> A = 
> \begin{pmatrix}
> 1 & 2 & 3 \\
> 2 & 4 & 6 \\
> x & y & z
> \end{pmatrix}
> , \ \ \
> B = 
> \begin{pmatrix}
> 1 & 2 & x \\
> 2 & 4 & y \\
> 3 & 6 & z
> \end{pmatrix}
> ```

행렬 $A$와 행렬 $B$는 각각 행의 비례와 열의 비례하기 때문에 행렬식은 0이다.

<br>

정사각 행렬 $A$와 $B$에 대하여 다음과 같은 관계가 성립한다.
> $det(AB) = det(A) \ det(B)$