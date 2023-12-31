# **기저와 차원 (Basis & Dimension)**
---

## **벡터 공간**
벡터의 덧셈과 스칼라의 곱이 정의되는 공간을 **벡터 공간**(vector space)이라한다.
> 벡터 공간 (vector space) $\Leftrightarrow$ 선형 공간 (linear space)

벡터 공간은 길이와 각도가 정의되지 않는다. 즉, 내적 공간으로 확장되어야 한다.  
**내적 공간** (inner product space)은 길이와 각도가 정의되어 있다.

<br>

벡터 공간의 공리는 다음과 같다. (단, $V$는 공간, &nbsp; $u$, $v$, $w$는 벡터, &nbsp; $a$, $b$는 스칼라)
> - $u$, $v$ $\in V$ &nbsp; $\rightarrow$ &nbsp; $u+v \in V$  
> - $a$, $u$ $\in V$ &nbsp; $\rightarrow$ &nbsp; $au \in V$
> - $u + v = v + u$  
> - $u + (v + w) = (u + v) + w$  
> - $u + 0 = 0 + u$  
> - $u + (-u) = (-u) + u = 0$  
> - $a(u + v) = au + av$
> - $(a + b)u = au + bu$  
> - $a(bu) = (ab)u$  
> - $1u = u$


<br>

공간을 표현하는데 $n$차원 실수 공간을 $\mathbb{R}^{n}$로 나타낸다.  
이러한 $n$차원 공간의 좌표 축의 기본 벡터를 **유닛 벡터** (unit vector)라고 한다.  
$n = 3$인 3차원 공간에 대해서 유닛 벡터 $i$, $j$, $k$는 다음과 같다.  
> $i = (1, 0, 0)$  
> $j = (0, 1, 0)$  
> $k = (0, 0, 1)$

<br>

유닛 벡터의 선형 조합으로 $n$차원 벡터를 표현 할 수 있다.  
$n = 3$인 3차원 공간에 대하여 $u$벡터는 다음과 같이 나타낼 수 있다.
> ```math
> \begin{aligned}
> u =& \ (a, b, c) \\
> =& \ (a, 0, 0) + (0, b, 0) + (0, 0, c) \\
> =& \ a(1, 0, 0) + b(0, 1, 0) + c(0, 0, 1) \\
> =& \ ai + bj + ck
> \end{aligned}
> ```

<br>

벡터 공간의 일부분은 **부분 공간** (subspace)라 한다.
> 부분 공간 $\Subset$ 벡터 공간

부분 공간을 표현하는 방법으로 **span**이라는 표현이 있다.
> $n$차원 공간에서 $n$개 이하의 기저 벡터의 집합 $S$에 속하는 $n$ 차원 이하의 부분 공간을 $W$라 할 때  
> $S$는 부분 공간 $W$를 span한다고 표현한다.  
>
> $W = span(S)$

기저 벡터는 벡터의 부분 공간을 구성하는 기본 축이다. (후위 서술)

<br><br>

## **선형 변환**
**선형 변환**(linear transformation)은 두 벡터 공간 사이의 함수를 말한다.  
벡터에 대한 신축, 회전, 반사 등을 변환이라 할 수 있다.  
행렬이라는 개념에는 선형 변환의 의미를 포함하고 있다.

<br><br>

## **선형 독립**
벡터 공간 $V$에 벡터 $w$가 존재 할 때 벡터 $w$는 다음과 같이 나타낼 수 있다.
> $w = a_{1}u_{1} + a_{2}u_{2} + \cdots + a_{n}u_{n}$

이와 같이 스칼라 집합 $A$($a_{1}$, $a_{2}$, $\dots$, $a_{n}$)과 벡터 집합 $U$($u_{1}$, $u_{2}$, $\dots$, $u_{n}$)에 대하여  
벡터 $w$를 $A$ 집합과 $U$ 집합의 조합으로 표현할 때,  
벡터 $w$는 벡터 집합 $U$의 **선형 조합**(linear combination)으로 나타낼 수 있다고 한다.

<br>

벡터 공간 $S$에 벡터 집합 $A$($a_{1}$, $a_{2}$, $\dots$, $a_{n}$)이 존재 하고, 벡터 $u$가 $A$에 속할 때
> - 벡터 $u$를 $A$에 속하는 다른 벡터의 선형 조합으로 표현 불가 $\rightarrow$ **선형 독립**(linear independent)
> - 벡터 $u$를 $A$에 속하는 다른 벡터의 선형 조합으로 표현 가능 $\rightarrow$ **선형 종속**(linear dependent)

<br><br>

## **기저**
벡터 공간 $V$가 있을 때 $V$를 생성하는 선형 독립인 벡터들을 **기저**(basis)라고 한다.  
이는 기저 벡터의 선형 조합으로 벡터 공간을 생성할 수 있다는 의미이다.

<br>

기저 벡터의 조건은 다음과 같다.
> - $\lbrace s_{1}, \ s_{2}, \ \cdots, \ s_{n}\rbrace$이 공간 $S$를 생성한다.  
> - $s_{1}, \ s_{2}, \ \cdots, \ s_{n}$은 선형 독립을 이룬다.

$n$차원 공간을 이루기 위해서는 $n$개의 기저 벡터가 필요하다.

<br>

벡터 공간 $S$의 임의의 기저 벡터들을 $\lbrace s_{1}, \ s_{2}, \ \cdots, \ s_{n}\rbrace$이라 할 때  
벡터 공간은 다음과 같은 성질을 만족한다.
> - $n$개가 넘는 벡터가 만드는 집합은 선형 종속이다.  
> - $n$개 미만의 벡터가 만드는 집합은 벡터 공간 $S$를 생성할 수 없다.  
> - 벡터 공간의 모든 기저 벡터의 개수는 동일하다.

<br><br>

## **차원**
**차원**(dimension)은 해당 벡터 공간을 구성하는 기저 벡터의 개수를 말한다.  
$n$차원 공간에서 기저 벡터의 집합 $S$의 크기가 $n$보다 크거나 작을 경우
> - $|S| < n$ 일 경우: $n$차원 공간을 생성할 수 없음  
> - $|S| > n$ 일 경우: 선형 종속 벡터가 존재함

<br><br>

## **행 공간 $\cdot$ 열 공간 $\cdot$ 영 공간**
크기가 $n \times p$인 행렬 $M$에 대하여 다음과 같이 나타낼 수 있다.
> 행 기준으로 표현: 행 벡터의 집합 행렬 $M$  
> 열 기준으로 표현: 열 벡터의 집합 행렬 $M$

아래와 같이 행렬을 행 벡터로 span할 수 있는 공간을 **행 공간**(row spaces)라 한다.
> ```math
> \begin{pmatrix}
> a_{11} & a_{12} & \cdots & a_{1p} \\
> a_{21} & a_{22} & \cdots & a_{2p} \\
> \vdots & \vdots & \ddots & \vdots \\
> a_{n1} & a_{n2} & \cdots & a_{np}
> \end{pmatrix}
> \rightarrow
> \begin{matrix}
> (a_{11}, \ a_{12}, \ \cdots, \ a_{1p}) \\
> (a_{21}, \ a_{22}, \ \cdots, \ a_{2p}) \\
> \vdots \\
> (a_{n1}, \ a_{n2}, \ \cdots, \ a_{np})
> \end{matrix}
> ```

위와 반대로 아래의 행렬을 열 벡터로 span할 수 있는 공간을 **열 공간**(column space)라 한다.
> ```math
> \begin{pmatrix}
> a_{11} & a_{12} & \cdots & a_{1p} \\
> a_{21} & a_{22} & \cdots & a_{2p} \\
> \vdots & \vdots & \ddots & \vdots \\
> a_{n1} & a_{n2} & \cdots & a_{np}
> \end{pmatrix}
> \rightarrow
> \begin{pmatrix}
> a_{11} \\ a_{21} \\ \vdots \\ a_{n1}
> \end{pmatrix},
> \begin{pmatrix}
> a_{12} \\ a_{22} \\ \vdots \\ a_{n2}
> \end{pmatrix},
> \cdots ,
> \begin{pmatrix}
> a_{1p} \\ a_{2p} \\ \vdots \\ a_{np}
> \end{pmatrix}
> ```

<br>

행렬 $M$과 벡터 $u$가 주어질 때 벡터 $u$에 선형 변환 $M$을 취할 때 기존 벡터 $u$가 벡터 0이 되게 하는 공간을 행렬 $M$의 **영 공간**(null space)이라 한다.
> $Mu = 0$

즉, 위의 식을 만족하는 모든 벡터 $u$의 집합을 행렬 $M$의 영 공간이라 한다.

<br>

행 공간, 열 공간, 영 공간은 다음과 같은 성질을 만족한다.
> - 기본 행 연산은 행렬의 영 공간을 변화시키지 않는다.  
> - 기본 행 연산은 행렬의 행 공간을 변화시키지 않는다.  
> - 행렬 $M$의 행 공간과 열 공간의 차원은 동일하다.  

<br><br>

## **랭크와 널리티**
행렬 $M$의 행 공간과 열 공간의 공통 차원을 행렬 $M$의 **랭크**(rank)라고 한다.  
이는 열 벡터에 의해 생성된 벡터 공간의 차원을 의미하고 다음과 같이 표현한다.
> $rank(M)$

위 행렬 $M$이 가질 수 있는 랭크 중에서 가장 큰 값을 $M$ 행렬의 **풀 랭크**(full rank)라고 한다.

<br>

행 공간과 열 공간의 차원을 랭크라 한다면 영 공간의 차원은 **널리티**(nullity)라고 하며 다음과 같이 표현한다.
> $nullity(M)$

<br>

랭크와 널리티는 다음과 같은 성질을 만족한다.
> - 행렬 $M$이 임의의 행렬이면 $rank(M) = rank(M^{T})$이다.  
> - 행렬 $M$이 $n$개의 열을 가진 행렬일 때, $rank(M) + nullity(M) = n$을 만족한다.

<br>
 
행렬$M$과 행렬 $M^{T}$의 rank가 동일한 이유는 다음과 같다.
> $rank(M) = dim(M$의 행 공간$) = dim(M^{T}$의 열 공간$) = rank(M^{T})$