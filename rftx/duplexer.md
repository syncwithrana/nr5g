---
# Duplexer / TDD Switch / Antenna Path (Final TX Front-End Block)

## 1. Why This Block Exists
This block manages:
- **Isolation** between TX and RX  
- **Routing** of high-power TX signal to antenna  
- **Protection** of RX LNA during receive mode  
- **Filtering** to meet emission masks  
- **Antenna sharing** for TDD operation  

It is the guardian between the PA and the antenna.

---

## 2. TDD Switch (Transmit/Receive Switch)
N78 uses **TDD**, so TX and RX share the same antenna but operate at different times.

### What the TDD Switch Must Handle
- High TX power (tens of watts)  
- Very low-loss RX path  
- Fast switching (microsecond-level)  
- High isolation between TX ↔ RX  

### Key Metrics
- **Insertion loss** (lower is better)  
- **Isolation** (50–60 dB or more)  
- **Power handling capacity**  
- **Switching speed**

### Typical Technologies
- PIN diode switches (common in base stations)  
- GaN/GaAs FET switches  

---

## 3. Antenna Sharing Architecture
After the switch:
- TX → Antenna  
- RX → LNA  

System ensures:
- Stable impedance for PA  
- Minimal loss for RX path  
- Monitoring of antenna VSWR  
- Protection from reflections

---

## 4. Band-Select Filters (Post-Switch Filtering)
Sometimes placed **after** the TDD switch.

### Purpose
- Define N78 transmit band  
- Reject out-of-band signals  
- Meet emission mask requirements  
- Suppress residual harmonics  

Low insertion loss is critical to preserve PA output efficiency.

---

## 5. VSWR / Reflected Power Protection

### Monitoring Elements
- Couplers  
- Directional detectors  
- Forward/reflected power sensors  

### Purpose
- Detect antenna mismatch  
- Protect PA from reflected energy  
- Trigger power back-off when VSWR is high  
- Shut down TX during severe mismatch  

Helps ensure reliability and prevent PA damage.

---

## 6. Antenna Path Challenges

### Insertion Loss
- Directly reduces radiated power  
- Impacts coverage range  
- Reduces overall efficiency  

### Isolation
- TX leakage to RX port must be extremely low  
- Prevents RX LNA from saturating  

### Switching Transients
- Fast TDD switching can cause spikes and noise  
- Requires timing control and gating circuits

---

## 7. What This Block Provides to the System
- Clean, routed TX signal  
- Proper protection for RX chain  
- Stable impedance environment for PA  
- Emission mask compliance  
- Robustness under antenna VSWR variation  
- Compatibility with multi-antenna / Massive MIMO structures  

This block is the TX front-end’s **control + protection + filtration** layer.

---