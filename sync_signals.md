# 5G NR — PSS & SSS Summary

## SSB Basics
SSB = Synchronization Signal Block containing 4 OFDM symbols:
- Symbol 0 → PSS  
- Symbol 1 → SSS  
- Symbol 2 → PBCH  
- Symbol 3 → PBCH

SSB uses 30 kHz SCS in FR1 (n78).  
SSB bandwidth = 240 subcarriers × 30 kHz = 7.2 MHz.

Assumed receiver:
- Sampling rate fs = 15.36 MHz  
- FFT size = 512  
- FFT bin = 30 kHz  

---

## PSS (Primary Synchronization Signal)

### What is PSS?
A fixed 127-symbol Zadoff–Chu sequence used for:
- Detecting a cell  
- Finding OFDM symbol boundary  
- Getting NID2 (0,1,2)

### Key Facts
- Exactly **3 PSS sequences** exist.  
- Occupies 127 subcarriers in Symbol 0 of SSB.  
- UE correlates against 3 known sequences.  
- PSS gives timing + rough CFO + NID2.

### Processing Chain
Transmitter:
- PSS (freq domain) → map to 127 bins → IFFT → CP → transmit  

Receiver:
- Slide ~545-sample window  
- Remove CP  
- FFT 512  
- Extract 127 bins  
- Correlate with 3 sequences → detect timing & NID2  

---

## SSS (Secondary Synchronization Signal)

### What is SSS?
A 127-symbol sequence in Symbol 1 of SSB.  
Provides NID1 (0–335).  
Together with PSS → PCI = 3*NID1 + NID2 (0–1007).

### Key Facts
- **336 SSS sequences** exist.  
- UE decodes SSS only after PSS timing is known.  
- Refines timing + frequency.

### Processing Chain
- From PSS, UE knows Symbol 1 position.  
- FFT → 512 bins → extract 127 SSS bins  
- Correlate with candidate SSS sequences (pruned by NID2)  
- Get NID1 → compute PCI  

---

## OFDM Symbol & Receiver Window

### Symbol Duration @ 30 kHz SCS
- Useful symbol Tu = 1/30 kHz = 33.33 µs  
- CP ≈ 2.17–2.34 µs  
- Total ≈ 35.5 µs  

### Window Size @ fs = 15.36 MHz
- Samples per symbol ≈ 35.5 × 15.36 ≈ 545 samples  
- Window = CP (~33 samples) + useful 512 samples (FFT input)

---

## FFT Mapping
With fs = 15.36 MHz and FFT = 512:
- FFT bin width = 30 kHz  
- PSS/SSS occupy 127 bins centered inside  
- Remaining bins unused

---

## What UE Achieves After PSS+SSS
PSS gives:
- OFDM timing  
- NID2  
- Rough CFO

SSS gives:
- NID1  
- Full PCI  
- Fine timing & CFO

UE is now ready for **PBCH decoding** (next step in access).
