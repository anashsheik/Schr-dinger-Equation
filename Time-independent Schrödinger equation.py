#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:06:15 2024

@author: sheikhomeister
"""

import numpy as np
import matplotlib.pyplot as plt

#R = 1.0: Establishes the radius of the circular domain as 1.0.
R = 1.0
# theta_max = 2 * np.pi: Specifies the maximum angle, encompassing the entire circle (ranging from 0 to 2π).
theta_max = 2 * np.pi
# N = 100: Indicates the total number of grid points or discrete points for the angle θ.
N = 100
# h = theta_max / N: Determines the interval size between the discrete points on the grid.
h = theta_max / N

# The function U(theta) is to represent the potential energy as a function of the variable θ. 
# The potential energy is expressed as the cosine of θ, specifically modeled as cos(θ).
def U(theta):
    return np.cos(theta)

# The function A(theta) is established to denote the vector potential.
# It is assigned a constant value of 0.6, indicating that it remains independent of the variable θ.
def A(theta):
    return 0.6

# The function Hamiltonian(U, A) is defined to construct the Hamiltonian matrix utilizing the given potential U(θ) and vector potential A(θ).
# The matrix H is initialized as an N×N array filled with complex zeros, as it will incorporate complex terms.
# A loop will iterate through each grid point, indexed by i.
def Hamiltonian(U, A):
    H = np.zeros((N, N), dtype=complex)
    for i in range(N):
# For each grid point, the value of θ is computed as i multiplied by h.
        theta = i * h
# The diagonal elements of the Hamiltonian matrix are assigned values, which encompass the kinetic energy term (1/2 R² h²), the potential energy U(θ), and the contribution from the vector potential A(θ).
        H[i, i] = (1 / (2 * R**2 * h**2)) + U(theta) + (A(theta)**2) / (2 * R**2)
# The off-diagonal element corresponding to the left neighbor is set, incorporating a kinetic term along with a vector potential term that adds a complex component.
        H[i, (i-1) % N] = -1 / (2 * R**2 * h**2) + 1j * A(theta) / (2 * R * h)
# Similarly, the off-diagonal element for the right neighbor is established, but with an opposite sign for the complex term.
        H[i, (i+1) % N] = -1 / (2 * R**2 * h**2) - 1j * A(theta) / (2 * R * h)
# Finally, the Hamiltonian matrix H is returned.
    return H

# H_mat = Hamiltonian(U, A): This line invokes the Hamiltonian function to generate the matrix.
H_mat = Hamiltonian(U, A)
# The statement under calculates the eigenvalues and eigenvectors of the Hamiltonian matrix by utilizing NumPy's linalg.eig function.
# The eigenvalues indicate the energy levels, while the eigenvectors correspond to the associated wave functions.
eigenvalues, eigenvectors = np.linalg.eig(H_mat)

# This function arranges the indices of the eigenvalues in a non-decreasing sequence.
idx = eigenvalues.argsort()
# This line under organizes the eigenvalues according to the sorted indices and retains only the real components, eliminating any imaginary parts that may arise from numerical inaccuracies.
eigenvalues = eigenvalues[idx].real
# This line under rearranges the eigenvectors in accordance with the new order.
eigenvectors = eigenvectors[:, idx]

# Then a visualization of the ground state, which corresponds to the lowest energy level is generated
# It illustrates the squared magnitude of the ground state wave function, which indicates the probability density and depicts the potential function U(θ) as a dashed line.
# Annotations such as labels, legends, and a title enhance the understanding of the plot is also generated.
plt.figure(figsize=(10, 5))
plt.plot(np.linspace(0, theta_max, N), np.abs(eigenvectors[:, 0])**2, label='Ground State')
plt.plot(np.linspace(0, theta_max, N), U(np.linspace(0, theta_max, N)), label='Potential U (cos(theta))', linestyle='--')
plt.xlabel('θ')
plt.ylabel('|ψ|²')
plt.legend()
plt.title(f'Ground State: E = {eigenvalues[0]:.4f}')
plt.show()

# A similar plot for the First and Second Excited States, corresponding to the eigenvectors at indices 1 and 2 is established.
plt.figure(figsize=(10, 5))
plt.plot(np.linspace(0, theta_max, N), np.abs(eigenvectors[:, 1])**2, label='First Excited State')
plt.plot(np.linspace(0, theta_max, N), np.abs(eigenvectors[:, 2])**2, label='Second Excited State')
plt.xlabel('θ')
plt.ylabel('|ψ|²')
plt.legend()
plt.title(f'First and Second Excited States: E1 = {eigenvalues[1]:.4f}, E2 = {eigenvalues[2]:.4f}')
plt.show()

# Lastly, numerical values for the energy levels of the Ground State, First Excited State and Second Excited State. 
print('Eigenvalues (Energy Levels):')
print(f'Ground State: {eigenvalues[0]:.4f}')
print(f'First Excited State: {eigenvalues[1]:.4f}')
print(f'Second Excited State: {eigenvalues[2]:.4f}')





