# data/

Sample EMG output captured from the device during calibration.

| File | Description |
|---|---|
| `Sample10Datapoints.txt` | Five calibration records. Each record logs the resting-muscle MIN/MAX/AVRG, then ten EMG voltage points sampled at ~20 ms intervals while the user holds a contraction. These are the short sequences the DTW matcher compares against the recorded templates. |

Values are in volts (the ESP32 reads the filtered EMG between 0 V and 3.3 V).
The resting muscle sits near 1.55 V here; a contraction pushes the points
higher, which is what shifts the DTW similarity toward a detection.
