---
# PA Classes & Operating Modes — Detailed but Clean

## 1. Class AB — Inside View

### What it really is
- The transistor conducts **slightly more than half** of the RF cycle.  
- Reduces distortion vs. Class B, improves efficiency vs. Class A.  
- Bias point sits between cutoff and full conduction.

### Why it’s used
- Simple, stable, predictable.  
- Good linearity for moderate-modulation signals.  
- Common baseline PA architecture.

### Limits
- For 5G OFDM (high PAPR), Class AB alone becomes **inefficient at back-off**.  
- Leads to evolution into Doherty structures.

---

## 2. Doherty PA — Inside View

### Core idea
Two PAs working together:
- **Main PA (carrier)** → Class AB-ish, active at low/mid power.  
- **Aux PA (peaking)** → Class C-ish, turns on at high power.

### Why this is powerful
- Low power → only main PA works → decent efficiency.  
- High power → aux enters → **load modulation** occurs.  
- Maintains high efficiency even when **backed-off by 6–10 dB**.

### Why 5G needs it
- OFDM peaks require back-off → normal PAs waste power.  
- Doherty keeps efficiency high exactly in that region.

### Variants
- Symmetric / asymmetric Doherty.  
- Wideband/Dual-band versions for N78.

---

## 3. Envelope Tracking — Inside View

### What happens
- PA supply voltage dynamically follows the **signal envelope**.  
- Gives PA just enough voltage at every moment.

### Why it's useful
- Higher efficiency at average power.  
- Maintains PAE over varying amplitude levels.

### Where it's used
- Mostly **handsets** (Sub-6 smartphones).  
- Base-stations rarely use ET for wideband N78 due to complexity.

### Key challenge
- Supply modulator must be **fast and accurate** to avoid distortion.

---

## 4. Why these modes matter — Inside Explanation

### Problem: OFDM hurts PAs
- High **PAPR** → big peaks.  
- PA must operate in **back-off** to avoid clipping.  
- Back-off kills efficiency for normal PAs.

### Solution: smarter PA modes
- **Doherty** → holds efficiency at back-off.  
- **Envelope Tracking** → adjusts supply voltage.  
- **DPD** → fixes nonlinearities introduced by PA behavior.

### Effective combo for 5G
**Doherty PA + DPD + CFR = 5G-ready transmitter.**

---