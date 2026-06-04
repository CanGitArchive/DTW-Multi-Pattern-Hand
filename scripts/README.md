# scripts/

Helper Python scripts used during development. These are prototyping and analysis
tools and are not required to build or flash the firmware (the DTW matcher itself
runs on the ESP32, in `src/`).

| File | Purpose |
|---|---|
| `DTW.py` | Reference implementation of the Dynamic Time Warping distance and similarity used on-device. Computes a similarity value between two short EMG sequences, the same comparison the ESP32 runs live. |
| `mathGraphV4.1.py` | Kinematic plotter for the finger mechanism. Uses the worm gear pitch, motor RPM, and link lengths to compute and plot fingertip velocity over time (thumb and index). |
| `motor_control.py` | Manual DC motor jog over serial (Pygame window): up arrow drives forward, down arrow drives backward. Used for bench testing the drive without EMG input. |

Run with Python 3. `DTW.py` needs `numpy`; `mathGraphV4.1.py` needs
`numpy`, `sympy`, and `matplotlib`; `motor_control.py` needs `pyserial` and `pygame`.
