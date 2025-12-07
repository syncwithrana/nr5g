# 5G NR MIB Detailed Breakdown

## 1. systemFrameNumber (6 bits)
- PBCH carries only the lower 6 bits of the system frame number.
- Full SFN (0–1023) is recovered later using SIB1.
- Reason: SSB bursts repeat, making higher bits ambiguous.

---

## 2. subCarrierSpacingCommon (1 bit)
Indicates the subcarrier spacing used for common channels (CORESET#0 + SIB1):

- 0 → 15 kHz  
- 1 → 30 kHz  

UE needs this to properly decode SIB1 scheduling.

---

## 3. ssb-SubcarrierOffset (5–12 bits)
Defines the frequency offset of the SSB from the carrier’s reference grid.

Used by UE to align the downlink resource grid with SSB placement.

---

## 4. dmrs-TypeA-Position (1 bit)
Defines DMRS mapping start symbol:

- 0 → Symbol 2  
- 1 → Symbol 3  

UE needs this for decoding control channels.

---

## 5. pdcch-ConfigSIB1 (8 bits)
Contains configuration for locating CORESET#0 and search spaces used for PDCCH carrying SIB1.

This is crucial for finding SIB1.

---

## 6. cellBarred (1 bit)
Controls cell accessibility:

- 0 → UE may camp  
- 1 → UE must NOT camp  

---

## 7. intraFreqReselection (1 bit)
Controls UE mobility before RRC connection:

- 0 → Stay on this cell  
- 1 → Allowed to search for better cells on same frequency  

---

## 8. spare bits
Reserved for future specifications.


---

# Visual Summary of MIB Fields


MIB:
- systemFrameNumber          (6 bits)
- subCarrierSpacingCommon    (1 bit)
- ssb-SubcarrierOffset       (5-12 bits)
- dmrs-TypeA-Position        (1 bit)
- pdcchConfigSIB1            (8 bits)
- cellBarred                 (1 bit)
- intraFreqReselection       (1 bit)
- spare                      (remaining bits)










