# Metric Spaces

This section introduces metric spaces, neighborhoods, convergence, boundedness, and related concepts.

```{tableofcontents}

```


```{prf:definition}
设 $X$ 为一个非空集合。若对任意的 $x,y \in X$，都存在 $\rho(x,y)\in\mathbb{R}$ 与 $x,y$ 对应，且满足以下三个条件：

1. 非负性：$\rho(x,y)\geqslant0$，等号成立当且仅当 $x=y$。
2. 对称性：$\rho(x,y)=\rho(y,x)$。
3. 三角不等式：$\rho(x,y)\leqslant\rho(x,z)+\rho(z,y),\forall z\in X$。

则称 $\rho$ 是 $X$ 上的一个距离，$X$ 是以 $\rho$ 为距离的 MetricSpace，记为 $(X,\rho)$。度量空间中的元素又称之为点。
```

---

```{prf:definition}
度量空间 $(X,\rho)$ 中的点集：

$$
\{P\in X:\rho(P,P_0)<\delta\}\qquad (\delta>0)
$$

被称为点 $P_0$ 的  或开邻域，记为 $U(P_0,\delta)$。
若取 $\le$ 则为闭邻域 $\bar{U}(P_0,\delta)$。
```

---

```{prf:proposition}
设 $(X,\rho)$ 是度量空间，$P\in X$，则：

1. $\forall \delta>0,\;P\in U(P,\delta)$
2. $\forall \delta_1,\delta_2>0,\exists \delta_3>0$ 使 $U(P,\delta_3)\subseteq U(P,\delta_1)\cap U(P,\delta_2)$
3. 若 $P\ne P_0$，则存在不相交邻域
```

---

```{proof}
(1)显然  
(2)取 $\delta_3=\min(\delta_1,\delta_2)$  
(3)取 $\delta<\rho(P,P_0)/2$
```

---

```{prf:definition}
设 $(X,\rho)$ 是度量空间，$E\subseteq X$：
$$
\delta_E=\sup_{x,y\in E}\rho(x,y)
$$
称为 diameter。
```

---

```{prf:definition}
若 $\delta_E<+\infty$ 或 $E$ 包含于某邻域中，则称 $E$ 为 bounded set。
```

---

## 收敛点列

```{prf:definition}
设 $\{x_n\}\subset X$，若存在 $x\in X$：
$$
\forall\varepsilon>0,\exists N,\;n>N\Rightarrow \rho(x_n,x)<\varepsilon
$$
则 $x_n\to x$。
```

---

```{prf:proposition}
若 $x_n\to x$：

1. 极限唯一  
2. $\rho(x_n,y)$ 有界  
3. $\{x_n\}$ 有界  
4. 子列同极限  
5. 比较收敛成立
```

---

```{proof}
(1) 三角不等式  
(2) $\rho(x_n,y)\le\rho(x_n,x)+\rho(x,y)$  
(3) 由 (2)  
(4) 显然  
(5) 直接比较
```

---

## 引用模块

```{include} analysis/metric-space/def-pset.md
```

```{include} analysis/metric-space/mapping.md
```

```{include} analysis/metric-space/normedLS.md
```
