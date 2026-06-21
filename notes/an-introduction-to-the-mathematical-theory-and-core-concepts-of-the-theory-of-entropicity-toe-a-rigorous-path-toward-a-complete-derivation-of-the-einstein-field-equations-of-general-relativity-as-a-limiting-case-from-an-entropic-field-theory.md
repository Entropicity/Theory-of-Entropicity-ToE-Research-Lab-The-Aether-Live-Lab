# ToE Living Review Letters Series, Letter IV — Monograph Edition
# An Introduction to the Mathematical Theory and Core Concepts of the Theory of Entropicity (ToE): A Rigorous Path Toward a Complete Derivation of the Einstein Field Equations of General Relativity as a Limiting Case from an Entropic Field Theory

# A Five-Part Definitive Reference Work

# PART I
The Revolutionary Inversion and Mathematical Prerequisites

**John Onimisi Obidi**
Research Lab, The Aether
jonimisiobidi@gmail.com
Canonical Archive: https://entropicity.github.io/Theory-of-Entropicity-ToE/

First Edition — June 2026
Written: Wednesday, 03 June 2026 

# Some Historical Footnote for Posterity — Ahead of a Preface: 
The reader already well familiar with the Theory of Entropicity (ToE) knows by now that my main aim in my endeavors has been to discover general and fundamental principles of nature, and that I am less concerned for the most part about the details of how nature works—I must leave that labor of love to others who have greater inclinations toward such matters. This serves as a crucial frontispiece for the reader, which is to enable him or her to know ahead of time about my inherent motivations; and for me, to keep me steady in my purpose.

This, then, relative to my purpose, is the first time, after over a year of my labors in the formulation of the Theory of Entropicity (ToE), that I can say I have actually made some progress; and that what I have done so far in the past one year of my turmoil and toil in the development of the Theory of Entropicity (ToE) is actually child's play compared to the present work on the subject....

...When **Albert Einstein** was invited to the University of **Göttingen** by the illustrious **David Hilbert** in June of 1915 to deliver six consequential lectures within an intense week on his emerging Theory of General Relativity, Einstein had occasion to discuss with some of the greatest mathematical minds of the 20th Century; and it was after that period of another intense effort, and with the disturbing communication that Hilbert had already discovered the mathematical action principle of General Relativity [later to be called the Einstein-Hilbert Action, in honor of Hilbert and Einstein, in recognition of their enduring and undeniable accomplishments], Einstein, one more time, in a last desperate effort, tackled with immortal brutal force the problem he had been encountering in his General Relativity (GR) prior to his momentous Göttingen visit, which namely was to arrive at the final correct form of the consistent generally covariant field equations, and which he eventually found [discovered] with great exhilaration and heavenly joy...

**So, I feel that same indescribable exhilaration and heavenly joy at this very moment over my discovery in this work you now hold in your hands.**

With that said, I here commit you to your own arduous task of reading through this monograph **[ToE LRLS Letter IV]**, which you must now begin; and **may you find in it equivalent and comparable joy.**

# Dedication

To the unnamed student who once asked,
“Why does entropy always increase?”
and was told “Because that is the second law.”
and asked again, “But why?”
and was told to stop asking.
This monograph is the beginning of an answer.

To every physicist who has stared at the Einstein field equations
and felt, beneath their mathematical beauty,
the quiet insistence that something deeper must be there.

To **Dr. Olalekan T. Owolawi** — in whose correspondence the first light of this theory was struck. [Reference the Owolawi-Obidi Correspondence (OOC) on the Foundation of the Theory of Entropicity (ToE)]

And to all who understand that the universe does not merely have entropy.
The universe is entropy, organized.

# Epigraphs

**“It is wrong to think that the task of physics is to find out how Nature is. Physics concerns what we can say about Nature.”**
— Niels Bohr

**“The most incomprehensible thing about the universe is that it is comprehensible.”**
— Albert Einstein, Physics and Reality, 1936

**“It from Bit. Otherwise put, every it — every particle, every field of force, even the spacetime continuum itself — derives its existence, its meaning, its very being from answers to yes-or-no questions.”***
— John Archibald Wheeler, It from Bit, 1990

**“The entropy of the universe tends to a maximum.”**
— Rudolf Clausius, The Mechanical Theory of Heat, 1865

**“The fundamental object of study in physics is not the particle, nor the field, nor the wave — it is the distinction. The capacity of a physical system to be in one state rather than another is the root of all measurable reality.”**
— John Onimisi Obidi, ToE Living Review Letter I (The Ontological Primacy of Entropy), 2026

**“It is a beautiful and profound fact that the equations of motion for a gravitational system can be derived from the purely thermodynamic concept of entropy on a holographic screen.”**
— Erik Verlinde, On the Origin of Gravity and the Laws of Newton, 2011

**“The Einstein equation of state: the proportionality of entropy to horizon area in all local Rindler causal horizons, together with the fundamental relation δQ = TδS, implies the Einstein field equation.”**
— Ted Jacobson, Thermodynamics of Spacetime, Physical Review Letters, 1995

**“The information-geometric structure of a statistical manifold is not merely an analogy for physics. It is the arena in which physics, properly understood, takes place. To derive gravity from entropy is not to demote gravity — it is to elevate entropy to its rightful station as the most fundamental field in nature.”**
— John Onimisi Obidi, ToE Living Review Letter III (From Information Geometry to Information Gravity), 2026

# Abstract
The Theory of Entropicity (ToE) is a programmatic, mathematically rigorous framework in theoretical and mathematical physics whose central claim is that entropy — understood not merely as a thermodynamic bookkeeping variable but as a primary, dynamical, real-valued scalar field defined over a differentiable manifold — is the most primitive physical quantity from which all other physical structure, including spacetime geometry and the matter content that curves it, can be systematically derived. This monograph constitutes the first in a five-part series intended as a definitive reference work for the ToE program. Part I lays the full mathematical and conceptual foundation. Its purpose is twofold: first, to make the central philosophical and scientific argument for the ontological inversion that places entropy at the root of the physical hierarchy, and second, to develop with complete pedagogical rigour every mathematical prerequisite — differential geometry, tensor calculus, fiber bundle theory, and the statistical foundations of kinetic theory — that the remaining four parts will require and build upon.

The standard hierarchy of contemporary theoretical physics flows from a reductionist program: matter is composed of particles, particles obey quantum field theories, thermodynamics and statistical mechanics emerge as coarse-grained approximations to the underlying quantum dynamics, and entropy is a derived, emergent concept applicable only to sufficiently complex systems. ToE inverts this hierarchy by a deliberate and carefully argued ontological declaration: the entropy field S(x), defined as a smooth function on the entropic manifold Λ, is not emergent from particle physics but is instead the ground-level physical datum from which metric geometry, particle physics, and gravitational field equations all emerge as limiting cases. This inversion is not metaphysical speculation; it is supported by a convergent body of modern physics results, including Bekenstein’s identification of black hole entropy with horizon area (Bekenstein 1973), Hawking’s derivation of thermal radiation from quantum fields in curved spacetime (Hawking 1975), Jacobson’s celebrated thermodynamic derivation of the Einstein field equations from the entropy-area law (Jacobson 1995), Verlinde’s entropic force program (Verlinde 2011), Padmanabhan’s thermodynamic structure of spacetime, and Bianconi’s recent Gravity from Entropy program (Bianconi 2023). The ToE program, developed by Obidi in the ToE Living Review Letters Series (Letters I through IV, 2025–2026), makes a stronger and more systematic claim than any of these: it provides an explicit and complete chain of mathematical maps from information-geometric structure to Lorentzian spacetime and from entropy distributions to the stress-energy tensor.

The chain of maps central to ToE may be summarized as follows. One begins with a parametric family of probability distributions {p(x|θ)} on the entropic manifold Λ, parametrized by coordinates θμ. The Fisher–Rao metric on the corresponding statistical manifold provides a natural Riemannian metric on parameter space. The Obidi Transformation, defined in Part III, deforms this metric by incorporating an entropic anisotropy tensor Σμν derived from the Kullback–Leibler divergence structure, breaking the invariance established by Čencov’s theorem and selecting a unique physical metric. This deformed metric, the Obidi Metric, is shown to be a Lorentzian metric of signature (−, +, +, +), whose curvature — expressed through the Obidi Curvature Invariant — encodes the entropic geometry of the manifold. The left-hand side of the Einstein field equations, namely the Einstein tensor Gμν, is shown to emerge from the curvature of the Obidi metric in the infrared (IR) limit of the theory, where all information-geometric microstructure has been coarse-grained away. The right-hand side, namely the stress-energy tensor Tμν, emerges from the second moment of the entropic probability distribution over momentum fiber spaces, as the fiber integral of pμpν weighted by the entropic distribution function f(ent)(x, Ω). The Einstein field equations therefore appear not as fundamental postulates but as the IR limit of the Master Entropic Equation (MEE), the fundamental field equation of ToE.

Part I of this monograph is organized as follows. Chapter 1 orients the reader with respect to the scope, purpose, and prerequisites of the full monograph. Chapter 2 presents the revolutionary inversion argument in full, including its scientific evidence base and its formal statement as the Obidi Conjecture. Chapter 3 develops the theory of smooth manifolds in full pedagogical detail, covering charts, atlases, tangent and cotangent bundles, pushforwards, and pullbacks. Chapter 4 develops tensor algebra, the metric tensor, affine connections, the Levi-Civita connection, the Riemann curvature tensor, the Ricci tensor, the Ricci scalar, the Einstein tensor, and the Bianchi identity. Chapter 5 introduces fiber bundle theory and the mathematics of coarse-graining via fiber integrals, establishing the precise mathematical model by which microscopic entropic structure gives rise to macroscopic physical fields. Chapter 6 develops the statistical and probabilistic foundations of the theory, establishing that physical tensors are moment objects of distribution functions, and connecting the maximum entropy principle to the selection of physical states. The monograph closes Part I with a summary, a notation guide, and an interim bibliography for Parts I through II.

Keywords: Theory of Entropicity, entropic gravity, information geometry, Fisher–Rao metric, Einstein field equations, statistical manifold, fiber bundle, coarse-graining, maximum entropy, Obidi Metric, Lorentzian geometry.

# Table of Contents
# PART I — The Revolutionary Inversion and Mathematical Prerequisites
# Chapter 1    Orientation and Scope — What This Monograph Does and Why It Matters
# Chapter 2    The Revolutionary Inversion — Why Entropy Must Come First
2.1   The Standard Hierarchy of Physics and Its Limitations
2.2   The Ontological Declaration of ToE: Entropy as the Primitive Field
2.3   Why the Inversion Is Not Absurd — Evidence from Modern Physics
2.4   The Three Levels of the Entropy Field: Scalar, Gradient, Vector
2.5   The Physical Meaning of Inverting the Hierarchy
2.6   Why Mass, Pressure, Radiation, and Stress Are Not Alien to Information
# Chapter 3    The Language of Smooth Manifolds
3.1   What Is a Manifold? Physical and Mathematical Definitions
3.2   Charts, Atlases, and Coordinate Systems
3.3   Smooth Maps, Diffeomorphisms, and Pullbacks
3.4   Tangent Spaces and Tangent Vectors
3.5   Cotangent Spaces and One-Forms (Covectors)
3.6   The Tangent Bundle and Cotangent Bundle
3.7   Physical Meaning of Bundles in ToE
# Chapter 4    Tensors, Metrics, and the Language of Curvature
4.1   Scalars, Vectors, Covectors — A Unified View
4.2   Tensors as Multilinear Maps — Definition and Examples
4.3   The Metric Tensor — Measuring Distance and Angle
4.4   Raising and Lowering Indices
4.5   Connections and Covariant Derivatives
4.6   The Riemann Curvature Tensor
4.7   The Ricci Tensor and Ricci Scalar
4.8   The Einstein Tensor and the Bianchi Identity
4.9   The Levi-Civita Connection — The Unique Metric Connection
# Chapter 5    Fiber Bundles, Fiber Integrals, and Coarse-Graining
5.1   What Is a Fiber Bundle?
5.2   Vector Bundles and Principal Bundles
5.3   Sections of a Bundle
5.4   Fiber Integrals — The Mathematics of Coarse-Graining
5.5   How Fiber Integrals Produce Effective Fields
5.6   Physical Interpretation in ToE — From Microstructure to Macroscopic Physics
# Chapter 6    Probability, Moments, and the Statistical Foundations
6.1   Probability Distributions and Their Role in ToE
6.2   The Zeroth Moment — Normalization
6.3   The First Moment — Mean, Center of Mass, Momentum Density
6.4   The Second Moment — Variance, Pressure, Stress
6.5   Higher Moments and Radiation
6.6   Why Physical Tensors Are Moment Objects
6.7   The Kinetic Theory Connection — Distribution Functions and Stress-Energy
# PART II — Information Geometry: The Mathematical Engine of ToE
Chapter 7    Statistical Manifolds and the Fisher–Rao Metric
Chapter 8    Kullback–Leibler Divergence, Relative Entropy, and Geometry
Chapter 9    The Fubini–Study Metric and Quantum Information Geometry
Chapter 10    The Amari–Čencov α-Connections and Dual Geometry
Chapter 11    Čencov’s Theorem and Its Fundamental Obstruction for ToE
Chapter 12    Quantum Relative Entropy — Araki–Umegaki and Bures Structures
Chapter 13    Rényi and Tsallis Entropies and the α–q Constitutive Constraint
Chapter 14    The Hybrid Metric-Affine Space (HMAS)
# PART III — The Core Architecture of the Theory of Entropicity (ToE)
Chapter 15    The Ontological Entropy Field S(Λ) — Definition and Properties
Chapter 16    The Obidi Action — ToE’s Variational Principle
Chapter 17    The Master Entropic Equation (MEE) — ToE’s Field Equation
Chapter 18    The Entropic Current, Conservation Law, and Arrow of Time
Chapter 19    The Obidi Transformation — Breaking Čencov Invariance
Chapter 20    The Obidi Metric — From Information Geometry to Lorentzian Spacetime
Chapter 21    The Obidi Curvature Invariant (OCI)
Chapter 22    The Vuli–Ndlela Integral — Entropy-Weighted Path Integral
Chapter 23    The Haller–Obidi Action and Lagrangian
Chapter 24    The No-Rush Theorem and Entropic Speed Limit
Chapter 25    The Entropic Cosmological Constant
# PART IV — From Entropic Field Theory to Einstein Gravity
Chapter 26    The Einstein–Hilbert Action and the Einstein Field Equations — A Structural Review
Chapter 27    The Obidi–Einstein Correspondence (OEC)
Chapter 28    Deriving the Left-Hand Side — The Einstein Tensor from Entropic Geometry
28.1   From the Obidi Metric to Lorentzian Curvature
28.2   The Entropic Riemann, Ricci, and Einstein Tensors
28.3   The Bianchi Identity as an Entropic Conservation Law
# Chapter 29    Deriving the Right-Hand Side — The Entropic Stress-Energy Tensor
29.1   Pressure as Entropic Response to Volume Change
29.2   Stress as Anisotropic Entropic Resistance to Deformation
29.3   Momentum as Directed Entropic Flow
29.4   Radiation as Entropic Massless Flow
29.5   Mass as Stabilized Entropic Energy Storage
29.6   The Entropic Stress-Energy Tensor T(ent)μν
29.7   The Einstein Stress-Energy Tensor as IR Limit
Chapter 30    The Einstein Field Equations as a Limiting Case of ToE
Chapter 31    The Cosmological Constant and Dark Energy from ToE
Chapter 32    Connections to Bianconi’s Gravity from Entropy
# PART V — Literature Review, Context, and Experimental Pathways
Chapter 33    Bekenstein and the Birth of Black Hole Entropy
Chapter 34    Hawking Radiation and Quantum Entropy of Horizons
Chapter 35    Jacobson’s Thermodynamic Derivation of Einstein’s Equations
Chapter 36    Verlinde’s Entropic Gravity Program
Chapter 37    Padmanabhan’s Emergent Gravity and Thermodynamic Structure of Spacetime
Chapter 38    Bianconi’s Gravity from Entropy
Chapter 39    Other Precursors — Frieden, Jaynes, Caticha, Matsueda
Chapter 40    ToE in the Landscape — What Is New, What Is Different, What Is Predicted

# Comprehensive References
# Preface
**John Onimisi Obidi** — Research Lab, The Aether — June 3, 2026

This monograph was not written because the author believed he had all the answers. It was written because he believed he had found the right question. The question — stated with the full weight it deserves — is this: is entropy a property that physical systems have, or is it a field from which physical systems emerge? The standard answer, embedded in every graduate curriculum in theoretical physics, is the former. Particles exist, fields exist. **But the Theory of Entropicity (ToE) inverts that hierarchy and declares that Entropy is a universal, fundamental Field of Nature from which all reality emerges.**
