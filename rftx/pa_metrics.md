---
# Point 2: Key PA Performance Metrics — Expanded Details

## 1. Gain — What really matters

### What gain tells you
- Difference between input power and output power.  
- Typical BS PA gain: **25–32 dB**.  
- Must remain **flat** over the whole N78 band (~3.3–3.8 GHz).

### Why engineers care
- If gain droops at certain frequencies → system calibration fails.  
- If gain compresses early → DPD can’t fix it → ACLR fails.  
- Gain must be stable vs **temperature**, **supply voltage**, **device aging**.

### Key real-world notes
- Modern Doherty PAs intentionally show **soft compression** to keep efficiency high.  
- Gain ripple < 1 dB is usually targeted.

---

## 2. PAE (Power-Added Efficiency) — The king metric

### Definition
PAE = (Pout – Pin) / Pdc

### Typical numbers
- At saturation: **45–55%** for GaN Doherty PAs.  
- At 6–8 dB back-off: **30–40%**.

### Why it’s critical
- BS operating cost (power bill) depends on this.  
- Higher PAE = lower heat = smaller heat sinks = cheaper hardware.

### Tricky part
- Efficiency at **back-off** matters far more than at Psat.  
- OFDM spends most time at low average power.

---

## 3. Linearity Metrics (IMD, ACLR, EVM)

### IMD (Intermodulation Distortion)
- Nonlinearity produces 3rd, 5th, 7th order products.  
- 3rd order IMD often lands near the carrier → harmful.

### ACLR
- Adjacent channel leakage ratio.  
- 5G NR needs **ACLR better than –45 dBc** typically.  
- Bad ACLR → interference → certification failure.

### EVM
- Measures modulation accuracy.  
- Higher-order QAM (256-QAM) needs EVM < **3%**.

### Practical picture
- High IMD → poor ACLR.  
- Poor ACLR → network rejects PA.  
- DPD compensates, but only if PA is predictable.

---

## 4. Output Power Levels — The PA’s muscle

### Psat (Saturation Power)
- Max output power; extra input gives no more output.  
- N78 GaN PAs often reach **48–52 dBm**.

### P1dB
- Point where gain compresses by 1 dB.

### Back-off region
- OFDM crest factor ~10 dB → PA runs **6–10 dB below Psat**.  
- Doherty PA optimized exactly for this region.

### Why important
- Determines real usable transmit power.  
- DPD must linearize PA in the back-off region.

---

## 5. AM-AM & AM-PM Distortion

### AM-AM
- Output amplitude vs input amplitude.  
- Should be smooth for easier DPD correction.

### AM-PM
- Phase shift vs input amplitude.  
- Even small phase distortion harms EVM.

### Why important
- Nonlinear curves define the **DPD model**.  
- If AM-PM varies across frequency → wideband DPD needed.

### Typical behavior
- Doherty architecture creates strong AM-AM shaping.  
- GaN devices show memory effects → more complex DPD.

---

## 6. Bandwidth Performance — Real challenge for N78

### Why N78 is difficult
- Bandwidth is large (~400–500 MHz).  
- PA must maintain performance across entire band.

### Challenges
- Doherty load modulation is frequency-sensitive.  
- Matching networks become harder as bandwidth increases.

### Solutions used
- Broad matching (λ/4 lines, transformers).  
- Dual-input Doherty.  
- Wideband peaking PA design.

---

## 7. Stability & Ruggedness — Ensuring reliability

### Stability
- PA must avoid oscillation at any frequency.  
- Stability factors: **K > 1**, **µ > 1**.

### Ruggedness
- Must withstand antenna mismatch (VSWR).  
- Typical requirement: survive **10:1 VSWR** without failure.

### Why critical
- Real antennas reflect power due to environment.  
- Poor ruggedness → PA burnout → field failures.

---