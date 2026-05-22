# IfcAlignmentHorizontalSegmentTypeEnum

The IfcAlignmentHorizontalSegmentTypeEnum indicates the type of a segment of a horizontal alignment segment (IfcAlignmentHorizontalSegment). Horizontal segments can be viewed from a geometric perspective and from a kinematic perspective. In recent times the kinematic perspective gained importance. The enumerations are detailed according to this development especially in modern track design.
<!-- end of short definition -->

**Kinematic perspective on horizontal alignment segments**

The central parameter of the kinematic perspective is lateral acceleration of the vehicle induced by change of direction while driving. In the horizontal layout this is the represented by the curvature of the segment. According to the curvature value the following categorization can be made:

| Curvature | Segmenttype    | Enumeration Values |
|:----|:------------------|:----------|
| 0 | straight line    | LINE |
| constant in the complete segment, <> 0 | Circular arc | CIRCULARARC |
| variation along the segment | Transition with linear curvature variation | CLOTHOID, CUBIC |
| variation along the segment | Transition with non-linear curvature variation | HELMERTCURVE, BLOSSCURVE, COSINECURVE, SINECURVE, VIENNESEBEND |


**Geometric perspective on horizontal alignment segments**



The traditional view is denoted by the geometric perspective in the context of the business terminology related IfcAlignment documentation. Before the availability of modern computers alignment design was performed using "traditional" drawing techniques. In the first phase of computerization this origin led to a representation in the x,y space first and a check of safety related properties in a second step. This can still be seen in regulations which have been put into effect 1980 or earlier. Of course designs which have been produced on basis of these regulations reflect the "good enough" attitude in the precision of the documentation.

In a later phase an increasing importance of the kinematic perspective can be observed. Here precise control of the lateral acceleration (horizontal and cant layout) and vertical acceleration (vertical layout) became prevalent. Designers started to use high performance transition bends especially in high speed scenarios. In the kinematic perspective precise curvature fitting between consecutive segments needs to be better than in the "good enough" approach of traditional geometric perspective. Central terms are e.g. "jerks", "theoretical cant" or "cant deficiency".

**Generic calculation of intrinsic x, y-coordinates for a given curvature**

For each horizontal alignment segment with a known curvature formula a generic method to calculate segment intrinsic coordinates exists.

$$\displaylines{ \varphi(s) = \int d \varphi = \int \kappa(s) \ d s \\\\
x(s) = \int cos \ \varphi(s) \ d s = \int cos( \int \kappa(s) \ d s \ ) d s \\\\
y(s) = \int sin \ \varphi(s) \ d s = \int \sin( \int \kappa(s) \ d s\ ) d s }$$

> NOTE While it is possible to apply the generic calculation also for trivial cases like LINE or CIRCULARARC it is much more efficient to use available formulas.

**Word of warning**

"Good enough" traditional designs have to be carefully checked before being included into a high precision 3D model. Intermediate corrections might be necessary. Fortunately the clothoid works very well with comparable documentation quality both in the classic geometric perspective and in the more recent kinematic perspective. Fortunately the vast majority of horizontal transition bends are designed and implemented as clothoids.

**Recommendation**

Check the relevant regulations for the network in question. Alignment designs as such are very stable over the lifetime of the road or track. Especially for old designs quality and precision of available documentation has to be checked very carefully. A clear understanding of limitations should be established before implementing automated data flows between high precision BIM environments and legacy documentation systems. This applies both to legacy, central databases and to legacy, individual documents.

**Used Symbols and their meaning**

| Symbol | meaning | Unit, value range |
|:----|:------------------|:----------|
| L | full length of segment    | positive length L > 0 |
| s | current position on segment    | 0 < s < L |
| ξ | = s / L (Greek "xi") standardised, dimensionless path length along the alignment / track centre line    | 0 < ξ < 1 |
| κ | (Greek "kappa") Curvature (inverse radius) of the alignment / track centre line in plan view (horizontal layout).    | 1/radius |
| κ<sub>1</sub> | Curvature (inverse radius) at beginning of the alignment / track centre line in plan view (horizontal layout).    | 1/radius |
| h | height of the gravity center line used for calculation above the track centreline in the ground plan. | length |
| ψ | (Greek "psi") Angle of cant (cross slope angle, bank angle)    | rad |
| φ | (Greek "phi") Directional angle (azimuth, bearing) | rad |
| x(s) | variable longitudinal coordinate of the projection of the alignment / track centreline into the ground plan. | length |
| y(s) | variable transverse coordinate of the projection of the alignment / track centreline into the ground plan. | length |

**Terminology**

**Intrinsic coordinate, intrinisc coordinate system of an alignment segment:**

The origin of an intrinsic coordinate system is the start of the segment. The direction of the positive x-axis is the start direction of the segments.

## Items

### LINE
In the geometry perspective it denotes a straight connection between two points. In the dynamic perspective, it denotes a segment with a curvature with a value of 0. This means that no lateral acceleration acts on the moving vehicle.

**Base formula (Curvature) **

$$ \kappa=0 $$

### CIRCULARARC
In the geometric perspective, it denotes a connection between two points that follows a circular path. In the dynamic perspective, it denotes a segment with constant lateral acceleration on the moving vehicle, i.e. constant curvature.

**Base formula (Curvature) **

$$ \kappa = const, \kappa <> 0 $$

### CLOTHOID
In the geometric perspective, a clothoid denotes a connection between two points where the radius of curvature changes along the segment at a constant rate. The clothoid was an early achievement of geometry, also known as Euler's spiral or Cornu's spiral. It became very popular in road and rail design even before the widespread availability of computers because of the availability of tabulations of the normalized clothoid. Proper application of the so called clothoid constant provided fast solutions for all relevant parameters necessary to integrate clothoid segments between two consecutive segments with constant curvature. In most cases the clothoid smooths the curvature between a straight line and a circular arc. <br/>

In the dynamic perspective, it denotes a segment with constant rate of lateral acceleration change induced by the curvature. The kinematic properties of the clothoid both reduce the exerted forces on the track by a train, improve the travel experience of train passengers and also reduce the stress of a car driver by avoiding sudden movements of the steering wheel.<br>

The kinematic advantages of the clothoid as a smoothing segment are true also for all the other transition bends currently in use.

**Base formula (Curvature)**

$$ \displaylines{ \xi = \frac{s}{L} \\\\
\kappa(s) = \kappa_{1} + \xi \Delta \kappa }$$

### CUBIC
In IFC CUBIC denotes a transition segment where x and y coordinates obey a cubic formula.

**General formula**

$$ y = a \cdot x^3 + b \cdot x^2 + c \cdot x + d $$

It was discovered very early that setting **a** to "1 / 6RL" and **b**, **c** and **d** to 0 yields a good enough approximation of the clothoid in many situations.

**Cubic formula for alignment**

$$ y = \frac{x^3}{6 \cdot R \cdot L} $$

Since the manual computation of cubics was considerable easier compared to the theoretically sound clothoid, cubic transitions became very popular as "good enough" replacement curves.

Cubic transition bends can still be found in many legacy alignments based on earlier design regulations. There also exist regulations containing cubic transitions for new designs.

It is obvious that simple approximations cannot fulfil all requirements for a kinematically correct track design. For example, the requirement of tangential continuity has often been neglected in favour of lower design costs by using sufficiently good cubic curves.

The cubic is known in two variants as **Cubic Parabola** or **Cubic Spiral** setting either the sinus or the cosinus of the deflection angle to 0.

### HELMERTCURVE
The Helmert curve or Helmert transition is an early example of a high performance transition bend. It is now widely accepted in relevant science and engineering that the linear change of the clothoid induces unwanted kinematic influences to a running train at speeds higher than 125 km/h.

In the geometry perspective the Helmert segment is the assembly of two parts of same length which mirror the same change in radius of curvature. A rough approximation is known as the biquadratic parabola.

>NOTE also referred to as Schramm curve.

**Base formula (Curvature)**

$$ \displaylines{
  \xi = \frac{s}{L} \\\\
  \text{First half: } \kappa(s) = \kappa_{1} + 2\xi^2 \Delta \kappa \\\\
  \text{Second half: } \kappa(s) = \kappa_{1} + ( 1 - 2 (1 - \xi)^2) \Delta \kappa
} $$

### BLOSSCURVE
The Bloss transition is a more recent form of a high performance transition bend. Proposed in 1936. it is now in use in several railway networks. There is no established rough geometric approximation.

>NOTE Further reading: Constantin Ciobanu, BLOSS TRANSITION – A SHORT DESIGN GUIDE

**Base formula (Curvature)**

$$ \displaylines{
  \xi = \frac{s}{L} \\\\
  \kappa(s) = \kappa_{1} + (3 - 2\xi) \  \xi^2 \ \Delta \kappa
} $$

### COSINECURVE
Cosine transition. The cosine transition was already discussed in 1868. Width the advent of high-speed rail it was applied in production designs. It is e.g. installed on Japanese high speed lines.

**Base formula (Curvature)**

$$ \displaylines{
  \xi = \frac{s}{L} \\\\
  \kappa(s) = \kappa_{1} + \frac{1}{2}(1- cos(\pi\xi) \ ) \Delta \kappa
} $$

### SINECURVE
Sine transition or sinusoidal transition was suggested 1937. The curvature function is built up of one period of a sine function. The sine curve is characterised by particularly advantageous smoothing properties at the end points. Compared to the clothoid, it is twice as long.

>NOTE also referred to as Klein curve.

**Base formula (Curvature)**

$$ \displaylines{
  \xi = \frac{s}{L} \\\\
  \kappa(s) = \kappa_{1} + ( \xi - \frac{1}{2\pi}sin(2\pi\xi) \ ) \Delta \kappa
} $$

### VIENNESEBEND
The Viennese Bend (R) is an innovative track geometry transition element. Instead of analyzing the vehicle movement at the track plane the optimization efforts target a gravity center line at a defined height above the rails.

As a consequence the path of the horizontal alignment center line is also influenced by the cant layout. The first part of the curvature formula is assembled from the basic function like the other transition bends. The additional term contains the bank angle "ψ" and the gravity center line height "h" and is unique to the Viennes Bend (R). This term causes a small movement contrary to the main direction in the x,y layout.

**Curvature formula**

$$ \displaylines{
  \xi = \frac{s}{L} \\\\
  \psi(s) = \psi_1 + \Delta\psi \cdot \xi^4 \cdot (35-84\xi + 70\xi^2-20\xi^3) \\\\
  \kappa(s) = \kappa_{1} + ( \Delta \kappa \cdot \xi^2 \cdot (35-84\xi + 70\xi^2-20\xi^3) \\\\
  \hspace{3em}  -420 \cdot \frac{h \Delta\psi}{L^2} \cdot (1 - 4\xi + 5\xi^2 - 2\xi^3)) \cdot \xi^2
} $$
