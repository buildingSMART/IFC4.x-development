# IfcCosineSpiral

*IfcCosineSpiral* is a type of spiral curve for which the curvature change is dependent on the cosine function.
<!-- end of short definition -->
The cosine spiral curve is parameterized by its curve length and for a given parameter \\(s\\), the heading angle \\(\theta(s)\\) and the curvature \\(\kappa(s)\\) are defined as follows. Here, \\(A_0\\) corresponds to the *ConstantTerm* and \\(A_1\\) to the *CosineTerm*.

**Heading Angle:**

The *Heading Angle* \\(\theta(s)\\) represents the orientation of the tangent to the curve at a given arc length. It indicates the direction in which the curve is "pointing" at that point. As you move along the curve, \\(\theta(s)\\) changes, showing how the curve’s direction evolves.

$$\theta(s) = \frac{1}{A_0} s + \frac{L}{\pi A_1} \sin\biggl(\frac{\pi}{L}s\biggr)$$

**Curvature:**

The *Curvature* \\(\kappa(s)\\) describes how quickly the heading angle changes with respect to the arc length \\(s\\). It reflects the "tightness" of the curve. Higher curvature values correspond to sharper bends, and lower curvature values correspond to straighter segments.

$$\kappa(s) = \frac{1}{A_0} + \frac{1}{A_1}\cos\biggl(\frac{\pi}{L}s\biggr)$$

## Attributes

### CosineTerm

### ConstantTerm

