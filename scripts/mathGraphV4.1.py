import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.Symbol('t')
Pitch = 2   
RPM = 75

l1 =    14.705414728254 
l2 =    24.029450337781 
lR =    63.152554229221 

l3 =    14.097086155592 
l4 =    23.188182836153 
lL =    84.022070509429 

theta1_deg = 35.21168843
theta2_deg = 22.78463207
theta3_deg = 34.66960268
theta4_deg = 1.12516753
theta5_deg = 35.79477021

###################################################
theta1_rad = np.deg2rad(theta1_deg)
theta2_rad = np.deg2rad(theta2_deg)
theta3_rad = np.deg2rad(theta3_deg)
theta4_rad = np.deg2rad(theta4_deg)
theta5_rad = np.deg2rad(theta5_deg)

Vs = (Pitch*RPM)/60

fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.50)) 
t_values = np.linspace(0, 2.5, 100)

##INDEX THUMB
lx = sp.sqrt(((Vs*t)**2)+((l2)**2)-2*Vs*t*l2*sp.cos(theta1_rad + theta2_rad))

arcCosFor_rad_Fi = (1 - ((lx)**2)/(2*(l1**2)))
rad_Fi = sp.acos(arcCosFor_rad_Fi)

rad_Tau = (np.pi-rad_Fi)/2

arcCosFor_rad_gamma = (((lx**2)+(l2**2)-(Vs*t)**2)/(2*lx*l2))
rad_gamma = sp.acos(arcCosFor_rad_gamma)

rad_beta =  (rad_Tau + rad_gamma - theta1_rad) * lR

linearVelocity_thumb = sp.diff(rad_beta, t)

V_func_thumb = sp.lambdify(t, linearVelocity_thumb, modules=['numpy'])
V_values_thumb = V_func_thumb(t_values)


##INDEX MID
ly = sp.sqrt(((Vs*t)**2)+((l4)**2)-2*Vs*t*l4*sp.cos(theta3_rad + theta4_rad))

arcCosFor_rad_a = ((ly**2)+(l4**2)-((Vs*t)**2))/(2*ly*l4)
rad_a = sp.acos(arcCosFor_rad_a)

arcCosFor_rad_b = (ly**2)/(2*l3*ly)
rad_b = sp.acos(arcCosFor_rad_b)

rad_c = (rad_a + rad_b - theta3_rad) * lL

linearVelocity_IndexMid = sp.diff(rad_c, t)

V_func_midIndex = sp.lambdify(t, linearVelocity_IndexMid, modules=['numpy'])
V_values_midIndex = V_func_midIndex(t_values)

##PLOT THUMB
axs[0].plot(t_values, V_values_thumb, label='V(t)')
axs[0].set_xlabel('t')
axs[0].set_ylabel('V')
axs[0].set_title('Baş Parmak Açılması V(t)')
axs[0].grid(True)
axs[0].legend()

##PLOT INDEXMID
axs[1].plot(t_values, V_values_midIndex, label='V(t)')
axs[1].set_xlabel('t')
axs[1].set_ylabel('V')
axs[1].set_title('İşaret Parmak Açılması V(t)')
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()



