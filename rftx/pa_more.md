---
# Point 5, 6, 7 — Detailed Combined View  
*(Matching Networks, Thermal/Biasing, Integration)*

# POINT 5 — MATCHING NETWORKS (IMN & OMN)

## 1. Why Matching Networks Matter
- Transistor impedance ≠ 50 Ω.  
- RF systems expect **50 Ω**.  
- Matching networks:  
  1. Transform device impedance → 50 Ω  
  2. Optimize gain, bandwidth, linearity, efficiency

---

## 2. Input Matching Network (IMN)

### Goals
- Provide proper drive power  
- Ensure stability  
- Shape gain and bandwidth  
- Maintain phase accuracy

### Impact
- Gain flatness  
- EVM  
- PA linearity  
- DPD predictability  
- Stability margins

### Typical Structures
- Microstrip lines  
- Series/shunt L/C  
- Stubs  
- Bond-wire inductances

---

## 3. Output Matching Network (OMN)

### Goals
- Convert device optimum load → 50 Ω  
- Maximize power, efficiency, and linearity  
- Maintain performance across wide N78 band

### Impact
- Psat  
- P1dB  
- PAE  
- ACLR  
- AM-AM / AM-PM  
- Doherty load modulation

### Typical Components
- Quarter-wave lines  
- Multi-section LC networks  
- Transformers  
- Baluns  
- Hybrid combiners

---

## 4. Challenges for N78 Wideband PA
- ~400–500 MHz bandwidth is large  
- Device parasitics hurt matching  
- Load modulation consistency is hard  
- Frequency-dependent peaking behavior  
- Temperature drift affects match

---

## 5. Matching in Doherty PAs

### Main PA Matching
- Optimized for linear low/mid-power region  
- Smooth AM-AM response

### Peaking PA Matching
- Optimized for high-power operation  
- Strong dynamic current capability

### Combiner Interactions
- Impedance inverter affects matching  
- Load seen by main PA changes dynamically  
- Must maintain behavior across bandwidth

---

## 6. Matching + DPD Interaction

### Good matching:
- Smooth distortion curves  
- Less memory effect  
- Easier DPD convergence  
- Better ACLR/EVM

### Bad matching:
- Unstable DPD  
- High spectral regrowth  
- Efficiency drop  
- Oscillation risks

---

# POINT 6 — THERMAL DESIGN & BIASING

## 1. Why Thermal Design Is Critical
Heat affects:
- Gain  
- AM-AM / AM-PM  
- Efficiency  
- Reliability  
- DPD stability

PAs (especially GaN) run very hot → thermal design is essential.

---

## 2. Key Thermal Components
- **Heat spreaders**  
- **Copper slugs / metal-core PCB**  
- **Heatsinks + airflow**  
- **Thermal interface materials (TIMs)**  

---

## 3. Biasing System

### Goals
- Maintain consistent gain  
- Avoid thermal runaway  
- Improve linearity  
- Keep AM-AM / AM-PM predictable

### Common Bias Types
- Fixed gate bias  
- Temperature-compensated bias  
- Adaptive bias (advanced)

Bias drift → PA drift → ACLR/EVM degrade.

---

## 4. Thermal & Bias Interactions
- Heat shifts transistor threshold voltages  
- This alters quiescent currents → changes linearity  
- DPD must constantly chase these changes  
- Some radios dynamically adjust bias & DPD

---

## 5. Ruggedness
PA must withstand:
- High VSWR  
- Temperature extremes  
- Sudden power surges

GaN is preferred due to high ruggedness.

---

# POINT 7 — INTEGRATION ASPECTS (How PA fits in TX chain)

## 1. System-Level Placement

Baseband → CFR → DPD → DAC → RF → Driver Amp → Doherty PA → Filter/Duplexer → Antenna

PA must integrate cleanly with:
- Driver stage  
- Filters / duplexer  
- Feedback receiver path  
- Thermal system

---

## 2. Driver Amplifier → PA Interface
Driver amplifier must:
- Supply correct power  
- Maintain stable phase  
- Avoid adding distortion  
- Match PA bandwidth

---

## 3. PA → Filter/Duplexer Interface

Filters remove:
- Harmonics  
- Out-of-band emissions  
- Spectral regrowth residue

But filters also:
- Add insertion loss  
- Change load seen by the PA  
- Affect linearity & ruggedness

---

## 4. Feedback Loop Integration
For DPD:
- Must sample PA output cleanly  
- Must have wide bandwidth  
- Must maintain time-alignment  
- Delay must be small for stable adaptation

Feedback quality = DPD performance.

---

## 5. Digital + RF Co-Design
Modern radios treat:
- PA  
- DPD  
- CFR  
- Biasing  
- Matching  

as **one integrated system**.  
This co-design enables high efficiency + excellent ACLR/EVM in 5G NR.

---