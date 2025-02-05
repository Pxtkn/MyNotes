
## Image Matching
### Detection
#### Principal Component Analysis
- To measure uniqueness, We can use principal component analysis (PCA).
- The 1st principal component is the direction with highest variance.
- The 2nd principal component is the direction with highest variance which is orthogonal to the previous components.
- Procedures
    1. Subtract off the mean for each data point.
    2. Compute the covariance matrix.
    3. Compute eigenvectors and eigenvalues.
    4. The components are the eigenvectors ranked by the eigenvalues.

#### Corner Detection
1. Compute the covariance matrix at each point

$$
H = \sum_{(u,v)} w(u,v) 
\begin{bmatrix} I_x^2 & I_xI_y \\ I_xI_y & I_y^2 \end{bmatrix}, 
I_x = \frac{\partial f}{\partial x}, 
I_y = \frac{\partial f}{\partial x} \\
\text{w(u,v) is typically Gaussian weights}
$$

2. Compute eigenvalues

$$
H = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, 
\lambda_{\pm} = \frac{1}{2}((a  d) \pm \sqrt{4bc  (a - d)^2})
$$

3. Classify points using eigenvalues of H

#### Gradient Operators
Roberts Operator:

$\begin{bmatrix}
    1 & 0 \\ 
    0 & -1 \\ 
\end{bmatrix}, 
\begin{bmatrix}
    0 & 1 \\ 
    -1 & 0 \\ 
\end{bmatrix}$

Prewitt Operator:

$\begin{bmatrix}
    -1 & 0 & 1\\ 
    -1 & 0 & 1\\ 
    -1 & 0 & 1\\ 
\end{bmatrix}, 
\begin{bmatrix}
    1 & 1 & 1 \\ 
    0 & 0 & 0 \\ 
    -1 & -1 & -1 \\ 
\end{bmatrix}$

Sobel Operator:

$\begin{bmatrix}
    -1 & 0 & 1\\ 
    -2 & 0 & 2\\ 
    -1 & 0 & 1\\ 
\end{bmatrix}, 
\begin{bmatrix}
    1 & 2 & 1 \\ 
    0 & 0 & 0 \\ 
    -1 & -2 & -1 \\ 
\end{bmatrix}$

Laplacian Operator:

$\begin{bmatrix}
    0 & 1 & 0 \\ 
    1 & -4 & 1 \\ 
    0 & 1 & 0 \\ 
\end{bmatrix}$


#### Harris Detector

$$
f = \frac{\lambda_1\lambda_2}{\lambda_1 + \lambda_2}
= \frac{determinant(H)}{trace(H)} = \frac{ad - bc}{a  d} \\
\text{f is called corner response}
$$

1. Compute derivatives at each pixel
2. Compute covariance matrix $H$ in a Gaussian window around each pixel 
3. Compute corner response function $f$
4. Threshold $f$
5. Find local maxima of response function (nonmaximum suppression)

- Invariant to intensity shift
- Not invariant to intensity scaling
- Invariant to translation and rotation
- Not invariant to scaling
    - Find scale that gives local maximum of f
    - Instead of computing $f$ for larger and larger windows, we can implement using a fixed window size with an image pyramid

#### Blob Detector
- Laplacian is sensitive to noise
- Usually using Laplacian of Gaussian (LoG) filter
- Feature points are local maxima in both position and scale
<br>

- LoG can be approximated by Difference of two Gaussians (DoG)
- Computing DoG at different scales



### Description
#### SIFT Descriptor
**Orientation Normalization**

- Compute orientation histogram
- Select dominant orientation
- Normalize: rotate to fixed orientation 

**Lowe’s SIFT algorithm**

- Run DoG detector
    - Find maxima in location/scale space
    - Remove edge points
- Find dominate orientation
- For each (x,y,scale,orientation), create descriptor

**Other detectors and descriptors**

- HOG: Histogram of oriented gradients
- SURF: Speeded Up Robust Features 
- FAST (corner detector) 
- ORB: an efficient alternative to SIFT or SURF 
- Fast Retina Key- point (FREAK) 

### Matching
- Define distance function that compares two descriptors
- Test all the features in another image, find the one with min distance
- Simple approach: $||f1 - f2 ||$
- Can give small distances for ambiguous (incorrect) matches

**Ratio test**

- Ratio score = $||f_1 - f_2 || / || f_1 - f_2^{'} ||$
    - $f_2$ is best match to $f_1$ in $I_2$
    - $f_2^{'}$ is 2nd best match to $f_1$ in $I_2$
- Ambiguous matches have large ratio scores

**Mutual nearest neighbor**

- Find mutual nearest neighbors
- $f_2$ is the nearest neighbor of $f_1$ in $I_2$
- $f_1$ is the nearest neighbor of $f_2$ in $I_1$


