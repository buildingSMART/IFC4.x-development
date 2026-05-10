# IfcSineSpiral

*IfcSineSpiral* is a type of spiral curve for which the curvature change is dependent on the sine function.
<!-- end of short definition -->
The sine spiral curve is parameterized by its curve length and for a given parameter \\(s\\), the heading angle \\(\theta(s)\\) and the curvature \\(\kappa(s)\\) are defined as follows. Here, \\(A_0\\) corresponds to the *ConstantTerm*, \\(A_1\\) to the *LinearTerm*, and \\(A_2\\) to the *SineTerm*.

**Heading Angle:**

The *Heading Angle* \\(\theta(s)\\) represents the orientation of the tangent to the curve at a given arc length. It indicates the direction in which the curve is "pointing" at that point. By following changes in \\(\theta(s)\\) along the curve, one can understand how the curve rotates and changes direction as it progresses.


$$\theta(s) = \frac{1}{A_0} s + \frac{1}{2}\left(\frac{A_1}{|A_1|}\right)\left(\frac{s}{A_1}\right)^2 - \frac{L}{2\pi A_2}\biggl(\cos\bigl(\frac{2\pi}{L}s\bigr)-1\biggr)$$

**Curvature:**

The *Curvature* \\(\kappa(s)\\) describes how quickly the heading angle changes with respect to the arc length. In other words, curvature indicates how "tight" a curve is turning at any point. A larger curvature corresponds to a sharper bend, while a smaller curvature corresponds to a straighter segment of the curve.

$$  \kappa(s) = \frac{1}{A_0} + \frac{A_1}{|A_1|}\left(\frac{L}{A_1}\right)^2  s + \frac{L}{A_2}\sin\left(\frac{2\pi}{L}s\right) $$
  
## Attributes

### SineTerm

### LinearTerm

### ConstantTerm
