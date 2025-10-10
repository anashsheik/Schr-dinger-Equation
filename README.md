# Numerical Solution of the Schrödinger Equation for a Particle on a Ring

This project provides a numerical solution to the time-independent Schrödinger equation for a quantum particle confined to a ring. The goal is to compute the energy eigenvalues and visualize the probability densities for the ground state, the first excited state, and the second excited state of the system.

The analysis involves discretizing the Hamiltonian operator and solving the resulting eigenvalue problem using Python.

---

### Table of Contents
1.  [Prerequisites](#prerequisites)
2.  [Theoretical Background](#theoretical-background)
3.  [Methodology](#methodology)
4.  [Results](#results)
5.  [Conclusion](#conclusion)

---

### Prerequisites
To run the Python script (`Assignment MAMO2100.py`) and reproduce the results, the following libraries must be installed:

- `numpy`
- `matplotlib`

You can install them using `pip`:
```bash pip install numpy matplotlib```
### Theoretical Background
The project solves the eigenvalue problem for a quantum particle on a ring of radius $R=1$. The particle is subject to an external scalar potential $U(\theta) = \cos(\theta)$ and a constant vector potential $A(\theta) = 0.6$.

The Hamiltonian for this system is given by:
$$
\hat{H}(U,A) = \frac{1}{2}\left(-\frac{i}{R}\frac{d}{d\theta}+A(\theta)\right)^{2}+U(\theta)
$$

Solving the time-independent Schrödinger equation, $\hat{H}\psi = E\psi$, provides the energy eigenvalues ($E$) and the corresponding eigenfunctions ($\psi$) of the system.

---

### Methodology

The numerical solution was implemented in Python following these steps:

1.  **Discretization**: The continuous angular coordinate $\theta \in [0, 2\pi]$ was discretized into a grid of `N=100` points. This transforms the differential equation into a matrix eigenvalue problem.

2.  **Hamiltonian Matrix Construction**: An $N \times N$ Hamiltonian matrix `H` was constructed:
    * The kinetic energy term was represented as a tridiagonal matrix, with periodic boundary conditions applied to simulate the ring topology.
    * The scalar potential $U(\theta)$ contributes to the diagonal elements of the matrix.
    * The vector potential $A(\theta)$ adds terms to both the diagonal and off-diagonal elements, introducing complex components to the Hamiltonian.

3.  **Solving the Eigenvalue Problem**: The `numpy.linalg.eig` function was used to compute the eigenvalues (energy levels) and eigenvectors (wavefunctions) of the Hamiltonian matrix `H`. The resulting eigenvalues were sorted to identify the ground and excited states.

4.  **Visualization**: The probability densities, $|\psi(\theta)|^2$, for the ground state, first excited state, and second excited state were plotted against the potential $U(\theta)$ using `matplotlib` to visualize the particle's spatial distribution.

---

### Results

The numerical computation yielded the energy eigenvalues for the three lowest states of the system.

* **Energy Eigenvalues**:
    * **Ground State ($E_0$)**: -0.5351
    * **First Excited State ($E_1$)**: 0.3434
    * **Second Excited State ($E_2$)**: 0.8536

* **Probability Densities**:
    * The **ground state** wavefunction is localized in the potential well (around $\theta = \pi$), where the potential energy is lowest, which is expected for the lowest energy state.
    * The **first and second excited states** show more complex distributions with multiple peaks, indicating higher kinetic energy and nodes where the probability of finding the particle is zero.
    * The plots confirm that the probability densities $|\psi(\theta)|^2$ are symmetric, reflecting the symmetry of the $U(\theta) = \cos(\theta)$ potential.

---

### Conclusion

This project successfully implemented a numerical method to solve the time-independent Schrödinger equation for a particle on a ring. The calculated energy levels and the visualized wavefunctions for the ground and first two excited states are consistent with the principles of quantum mechanics for a confined system.

The negative ground-state energy confirms that the particle is bound by the potential, and the increasing spacing between energy levels is characteristic of such quantum systems. The visualizations provide a clear and intuitive understanding of how the potential landscape shapes the probability distribution of the particle.
