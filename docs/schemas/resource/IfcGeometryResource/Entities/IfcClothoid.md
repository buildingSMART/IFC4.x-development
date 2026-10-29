# IfcClothoid

A clothoid is a planar curve in the form of a spiral. This curve has the property that the curvature varies linearly with the arc length.
<!-- end of short definition -->

> NOTE Definition according to ISO 10303-42:2003

Interpretation of the data shall be as follows:

```
C = SELF\IfcSpiral.Position.Location
x = SELF\IfcSpiral.Position.P[1]
y = SELF\IfcSpiral.Position.P[2]
A = ClothoidConstant
```

The clothoid is parameterized as:

$$\lambda(u)=C+A\sqrt{\pi}(\int_{0}^{u}\cos(\pi\frac{At^2}{2|A|})dt\ x+\int_{0}^{u}\sin(\pi\frac{At^2}{2|A|})dt\ y)$$

The parametric range is: -∞ < _u_ < ∞

The arc length _s_ of the curve, from the point C, is given by the formula:

$$s=Au\sqrt{\pi}$$

The curvature _κ_ and radius of the curvature _ρ_, at any point of the curve, are related to the arc length _s_ by the formulae:

$$\kappa=\frac{As}{|A^3|}, \rho=\frac{1}{\kappa}$$

The constant A, known as _flatness_ or _homothetic parameter_ of the clothoid, is specified as:

$$ A=\sqrt{LR}$$

where, L is the length measured from the inflection point; and R is the radius of the clothoid.

> NOTE Formulae adapted from **clothoid** defined in ISO 10303-42

## Attributes

### ClothoidConstant
The constant which defines the relationship between curvature and arc length for the curve.
