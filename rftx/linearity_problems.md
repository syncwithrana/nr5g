---
# Point 3: Linearity Problems & Why DPD Exists — Inside View

## 1. Why PAs Become Nonlinear (Real Reason)
- When output power increases, the transistor’s gain compresses and phase shifts.  
- Heating changes device behavior dynamically.  
- Impedance varies with voltage/current.  
- Result: amplitude and phase are no longer proportional → **nonlinear distortion**.

---

## 2. OFDM Makes It Worse (PAPR Problem)
- OFDM has high PAPR (**8–12 dB**).  
- PA must handle rare high peaks → so average power is run in **deep back-off**.  
- Back-off = lower efficiency + unpredictable behavior.  
- This greatly increases distortion (IMD, ACLR).

---

## 3. Types of Distortion PAs Produce

### AM-AM Distortion
- Output amplitude no longer scales linearly with input.  
- Causes compression/expansion → generates IMD.

### AM-PM Distortion
- Phase response depends on input amplitude.  
- Hurts EVM and constellation quality.

### Memory Effects
- PA response depends on previous inputs due to:  
  - Thermal dynamics  
  - Bias circuits  
  - Trapping effects (GaN)  
- Creates frequency-dependent distortion → harder for DPD to correct.

---

## 4. What This Distortion Causes on Air

### Spectral Regrowth
- Adjacent channels get polluted.  
- Fails ACLR requirements.  
- Causes interference to neighbors.

### EVM Degradation
- Modulation accuracy drops.  
- Limits QAM order and overall throughput.

---

## 5. Why DPD Is Required (Not Optional)
DPD pre-distorts the signal so that after PA distortion, the output becomes linear.

### DPD Corrects:
- AM-AM distortion  
- AM-PM distortion  
- Memory effects  
- Frequency-dependent behavior  
- Doherty-specific nonlinear regions

### Without DPD:
- ACLR fails  
- EVM fails  
- PA must run at very low power → horrible efficiency  
- Hardware becomes bigger, hotter, and more expensive

---

## 6. PA + DPD Relationship (Very Important)
- PA nonlinearities are **intentional** in Doherty to improve efficiency.  
- DPD is designed to linearize this intentional distortion.  
- Think: **PA = power, DPD = steering**.

---

## 7. Real-World Loop: PA → Feedback → DPD Update
- A feedback receiver samples PA output.  
- DPD coefficients adapt continuously due to:  
  - Temperature variation  
  - Supply fluctuations  
  - Device aging  
  - Antenna VSWR changes  
- DPD is a **dynamic**, not static, block.

---