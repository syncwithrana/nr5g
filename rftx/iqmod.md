# Analog IQ Modulator → RF Filtering → PA (Next steps after interpolation/shaping)

After interpolation + shaping + DAC + reconstruction filtering, the next meaningful RF block is the **analog IQ modulator**, where your shaped baseband becomes an RF signal in n78.

---

# 1️⃣ What the IQ modulator does
It takes:

- **I(t)** → multiplied by **cos(2πf_LO t)**
- **Q(t)** → multiplied by **sin(2πf_LO t)**
- Combines them into:

$begin:math:display$
RF\(t\) \= I\(t\)\\cos\(2\\pi f\_\{LO\} t\) \- Q\(t\)\\sin\(2\\pi f\_\{LO\} t\)
$end:math:display$

This yields a clean RF output at **f_LO ≈ 3.3–3.8 GHz** (n78).

---

# 2️⃣ Key problems the IQ modulator must handle
- **LO feedthrough** → DC offsets cause spike at LO  
- **Image rejection** → imperfect I/Q amplitude/phase causes unwanted mirror  
- **Quadrature error** → phase ≠ 90°, gain mismatch  
- **LO phase noise** → directly affects EVM for 64/256-QAM  

These imperfections degrade **EVM** and **ACLR**.

---

# 3️⃣ Inside the analog IQ modulator block
- Two analog mixers  
- LO quadrature generator  
- Summing stage  
- DC offset trimming  
- Calibration loops (digital-assisted)

Modern RFICs integrate these internally.

---

# 4️⃣ Output of the IQ modulator
Mixer output contains:

- Desired RF band  
- LO leakage  
- Image component  
- Mixer harmonics  

→ Must be cleaned in the next block.

---

# 👉 Next block after IQ modulator: **RF Bandpass Filter**

---

# 5️⃣ RF Bandpass Filter (n78)
### Purpose
- Suppress **image**  
- Suppress **LO feedthrough**  
- Remove mixer spurs  
- Restrict signal to **3.3–3.8 GHz**  
- Meet 3GPP **ACLR** & emission masks

### Types
- **SAW** filters (UE)  
- **BAW/FBAR** filters (better Q for 3.5 GHz)  
- **LC** filters (discrete/prototype)  
- **Cavity** filters (gNB, high performance)

### Insertion loss
- UE: **2–3 dB**  
- gNB: **0.5–1 dB**

Higher loss → PA must compensate with more gain.

---

# 👉 After RF BPF comes the **Power Amplifier (PA)**

This is the most critical block for TX performance.

---

# Summary — current point in the RF chain
```
I/Q (digital)
   → interpolation + shaping
       → DAC
           → reconstruction filter
               → IQ analog modulator (RF upconversion)
                   → RF bandpass filter   ← we are here
                       → PA
                           → coupler → DPD feedback
                               → TDD switch
                                   → antenna
```

---

If you want, we can now dive into:

- **RF bandpass filter design**  
- **PA architecture & linearity**  
- **DPD fundamentals & memory effects**  
- **TDD switching & antenna path**

Just tell me which block to zoom into next.
