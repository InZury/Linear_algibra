## **하우스홀더를 이용한 $QR$ 분해 예시**
다음과 같이 행렬 $M$이 주어질 때 $QR$분해를 할 수 있다.
> ```math
> M = 
> \begin{pmatrix}
> x_{1} & x_{2} & x_{3} //
> y_{1} & y_{2} & y_{3} //
> z_{1} & z_{2} & z_{3} //
> w_{1} & w_{2} & w_{3}
> \end{pmatrix}
> ```

이후 $M_{1}$을 구한다.
> ```math
> M_{1} = M = 
> \begin{pmatrix}
> x_{1} & x_{2} & x_{3} //
> y_{1} & y_{2} & y_{3} //
> z_{1} & z_{2} & z_{3} //
> w_{1} & w_{2} & w_{3}
> \end{pmatrix}
> ```

행렬 $M_{1}$의 1열을 $m_{1}$으로 설정한 다음 $m_{1}$의 노름을 구한다.
> ```math
> m_{1} = 
> \begin{pmatrix}
> x_{1} \\ y_{1} \\ z_{1} \\ w_{1}
> \end{pmatrix},
> \quad \quad
> e_{1} = 
> \begin{pmatrix}
> 1 \\ 0 \\ 0 \\ 0
> \end{pmatrix},
> ```
> $$ \Vert m_{1} \Vert = \sqrt{x_{1}^{2} + y_{1}^{2} + z_{1}^{2} + w_{1}^{2}} $$

여기서 $e_{1}$은 기저 벡터를 의미한다. $sign(u)$는 벡터 u의 첫 번째 원소의 부호를 따라간다.  
벡터 $v_{1}$은 다음과 같이 구할 수 있다.
> $$ v_{1} = m_{1} + sign(m_{1})\Vert m_{1} \Vert e_{1}$$

벡터 $v_{1}$을 통해 하우스홀더 행렬 $H_{1}$을 계산할 수 있다.
> $$H_{1} = I - 2\dfrac{v_{1}v_{1}^{T}}{v_{1}^{T}v_{1}} $$

이후 하우스홀더 행렬 $H_{1}$와 행렬 $M_{1}$의 행렬 곱을 톧해 계산한다.  
계산된 $H_{1}M_{1}$의 행렬곱에서 1행과 1열을 제거하고 $M_{2}$를 계산한다.
> ```math
> M_{2} \Rightarrow
> \begin{pmatrix}
> x_{4} & x_{5} & x_{6} \\
> y_{4} & y_{5} & y_{6} \\
> z_{4} & z_{5} & z_{6} \\
> w_{4} & w_{5} & w_{6}
> \end{pmatrix}
> \Rightarrow
> \begin{pmatrix}
> y_{5} & y_{6} \\
> z_{5} & z_{6} \\
> w_{5} & w_{6}
> \end{pmatrix}
> ```

이후 $2 \times 2$크기가 될 때까지 반복하여서 하우스홀더 행렬 $H_{n}$을 구한다.  
이를 통해 행렬 $Q$와 $R$행렬을 계산할 수 있다.
> $$Q = H_{1}H_{2} \cdots H_{n}$$
> 
> $$R = H_{n}H_{n-1} \cdots H_{1}M$$

이때 $H_{1}$의 행렬 크기는 $4 \times 4$크기이고, $H_{n}$의 크기는 $2 \times 2$이므로 행렬 곱을 할 수 없다.  
따라서 크기가 작은 행렬에 단위 행렬을 추가하여 형태를 변화시킨다.
> ```math
> \begin{pmatrix}
> x & y \\ z & w
> \end{pmatrix}
> \Rightarrow
> \begin{pmatrix}
> 1 & 0 & 0 & 0 \\
> 0 & 1 & 0 & 0 \\
> 0 & 0 & x & y \\
> 0 & 0 & z & w
> \end{pmatrix}
> ```

이를 통해 행렬 $M$의 $QR$분해를 하우스홀더 행렬을 통해 계산할 수 있다.
> $$ QR = M $$