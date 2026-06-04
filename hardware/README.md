# hardware/

PCB exports for the ProHand control board (KiCad, V3.0).

| File | Description |
|---|---|
| `FrontSideMirroredV3.pdf` | Front copper layer, mirrored (for toner transfer / etching). |
| `BackSideNormalV3.pdf` | Back copper layer, normal orientation. |

The board carries the ESP32, the EMG module input, the motor driver, the rotary
encoder header, the OLED (I2C), and the SD card (SPI). See the PCB drawing and
circuit top-down figures in the main README for the populated layout.

## ESP32 pin map

Pins as assigned in the firmware (`src/ProHandV3.8_ESP32.cpp`). These are the
GPIO numbers, not the physical header positions.

| Function | ESP32 GPIO |
|---|---|
| EMG input (analog) | 32 |
| Motor driver: forward / backward (PWM) | 26 / 25 |
| Rotary encoder: A (interrupt) / B | 27 / 13 |
| OLED I2C: SDA / SCL | 21 / 22 |
| SD card SPI: MOSI / MISO / SCK / CS | 23 / 19 / 18 / 5 |
| Buttons: forward / backward / calibration | 2 / 4 / 3 |
| Piezo feedback (PWM) | 15 |
| Battery monitor (analog) | 34 |
| Pressure sensor / FSR (analog) | 35 |

The board also breaks out a **second motor** (forward 14 / backward 12), a
**second encoder** (A 17 / B 16), and a **second EMG input** (33). The shipped
firmware drives one motor, one encoder, and one EMG channel; the extras are wired
for future dual-actuator experiments.
