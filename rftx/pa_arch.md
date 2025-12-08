---
# Point 4: PA Architecture Used in Sub-6 5G (Doherty Inside)

## 1. Why Doherty Is the Standard for 5G
- 5G OFDM has high PAPR → PA operates in **6–10 dB back-off**.  
- Normal PAs have poor efficiency in back-off.  
- Doherty uses **two PAs (main + peaking)** + **load modulation** to keep efficiency high.  
- Almost all N78 base-station PAs use Doherty (usually GaN).

---

## 2. The Three Big Blocks in a Doherty PA

### a) Main PA (Carrier PA)
- Class AB-ish.  
- Handles low + mid power.  
- Always ON.  
- Gives baseline gain and linearity.

### b) Peaking PA (Auxiliary PA)
- Class C-ish bias.  
- OFF at low power, turns ON only near peaks.  
- Provides extra current.  
- Enables efficiency boost during peaks.

### c) Doherty Combiner (Impedance Inverter)
- Transformer or transmission-line network.  
- Dynamically adjusts load impedance.  
- Enables **load modulation**, the core Doherty principle.

---

## 3. How Doherty Actually Works

### Low Power Region
- Only main PA active.  
- Peaking PA OFF.  
- Main PA sees high load impedance → better linearity.

### Mid Power Region
- Peaking PA begins turning ON.  
- Injects current into combiner.  
- Load impedance at main PA reduces → efficiency improves.

### High Power Region
- Both PAs active.  
- Load impedance optimized for max efficiency.  
- Reaches high output power with minimal waste.

---

## 4. Symmetric vs Asymmetric Doherty

### Symmetric
- Main and peaking PAs same size.  
- Simpler, but less optimal for wideband 5G.

### Asymmetric (5G standard)
- Peaking PA larger than main PA.  
- Better efficiency at deeper back-off (7–9 dB).  
- Matches 5G traffic patterns → used in N78.

---

## 5. Internal Design Challenges

### a) Wideband Matching
- N78 spans ~400–500 MHz.  
- Hard to maintain Doherty behavior across entire band.  
- Requires broadband matching techniques.

### b) Phase & Amplitude Alignment
- Main + peaking paths must align at combiner.  
- Phase mismatch → worse ACLR.  
- Amplitude mismatch → efficiency loss.  
- Temperature & aging cause drift → calibration needed.

### c) Device Technology
- **GaN** preferred for high power + efficiency.  
- Handles high voltage swings.  
- Good for wideband Doherty.

---

## 6. Doherty + DPD Interaction
- Doherty nonlinearities strongest near peaking transition.  
- AM-AM knee, significant AM-PM shift.  
- Memory effects increase with bandwidth.  
- DPD must:
  - Use high nonlinear order  
  - Include memory terms  
  - Model main + peaking behavior  
  - Adapt continuously

Modern Doherty is designed assuming DPD will correct distortion.

---

## 7. Where Doherty Fits in TX Chain

Baseband → CFR → DPD → DAC → RF → Driver Amp → Doherty PA → Filters → Antenna

Doherty PA is the final high-power stage.

---