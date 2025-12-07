# 5G NR — Full SIB1 Breakdown

SIB1 (System Information Block Type 1) is the first major system information message the UE reads after decoding the MIB. It provides all essential parameters required for cell selection, registration, RACH, paging, mobility, and access control.

---

## 1. Cell Access Related Information

### 1.1 PLMN-IdentityList
- List of supported PLMNs.
- Each PLMN contains:
  - MCC (Mobile Country Code)
  - MNC (Mobile Network Code)
  - Optional: emergency services support

### 1.2 Tracking Area Code (TAC)
- Identifies the TA for mobility management.

### 1.3 CellIdentity
- 28-bit 5G NR Cell ID.

### 1.4 Cell Barred / Cell Reserved info
- Indicates whether the UE can camp on the cell.
- Used for access restrictions or maintenance modes.

---

## 2. Cell Selection and Reselection Information

### 2.1 q-RxLevMin
- Minimum required received signal level to camp.

### 2.2 q-RxLevMinOffset
- Offset under specific conditions.

### 2.3 q-QualMin (Optional)
- Minimum quality threshold (RSRQ based).

### 2.4 Cell reselection priority
- Inter-frequency and intra-frequency priorities.

---

## 3. ServingCellConfigCommon

Basic DL/UL configuration needed before RRC Connection Setup.

Includes:
- Downlink frequency info (ARFCN, band)
- Uplink frequency info
- SSB Subcarrier Spacing
- PDCCH and CORESET#0 information
- PDSCH configuration for SI messages
- PRACH Configuration Index
- UL power control common parameters
- Timing advance parameters

---

## 4. RACH-ConfigCommon

Defines initial access procedure:

- PRACH configuration index
- Preamble formats
- RACH occasions (time/frequency)
- Random access response window
- Total number of RA preambles
- Contention-based vs contention-free options

UE uses this to perform Random Access (Msg1 → Msg4).

---

## 5. SchedulingInfoList

Indicates other SIBs present in the cell.

Each entry contains:
- SIB type (e.g., SIB2, SIB3…)
- Periodicity (typically 20–160 ms)
- Mapping of SI messages to PDSCH
- Number of repetitions

This prevents blind scanning by the UE.

---

## 6. Paging Configuration

Parameters for UE’s idle mode behavior:

- Default paging cycle
- nB parameter (paging narrowband settings)
- PF (Paging Frame) and PO (Paging Occasion)
- Paging DRX cycle

UE uses these to conserve battery by waking only on configured paging occasions.

---

## 7. NSSAI (Network Slice Information)

Configured NSSAI list:

- SST (Slice/Service Type)
- SD (Slice Differentiator)

UE uses this for slice-aware registration (5G SA only).

---

## 8. SI-Request and SI-Window Configurations

Defines how UE may request additional system info (rare in SA deployments):

- si-RequestConfig
- si-WindowLength
- si-RepetitionPeriod

---

## 9. Uplink and Downlink Power Control Defaults

Includes:
- deltaPreambleMessage3
- p0 nominal values
- ssb-Positions

Used before dedicated RRC parameters are assigned.

---

## 10. Cell Options

Optional parameters:
- Aggregated transmission power offsets
- Cell-level access restrictions
- Unlicensed operation info (NR-U)
- TDD UL/DL pattern (if needed at early stage)

---

# Purpose of SIB1

SIB1 enables the UE to:
1. Camp on a cell  
2. Know PLMN and TAC for registration  
3. Perform RACH (initial access)  
4. Decode further SIBs  
5. Understand paging behavior  
6. Register with the correct network slice  
7. Proceed to RRC Connection Request  

Without SIB1, the UE cannot start the attach/registration process in 5G NR.




