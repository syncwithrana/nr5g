# 🚀 Carrier Aggregation (CA) — Deep Dive

CA = combining multiple Component Carriers (CCs) so the UE sees them as one fat pipe.

## 1️⃣ Why CA exists
- Higher throughput without needing one wide block  
- Spectrum fragmentation compensation  
- Works in FR1, FR2, DL and UL (UL optional)  
- Typical smartphone: 3–8 DL CCs, 1–3 UL CCs

## 2️⃣ Component Carrier (CC) Structure
Each CC has:  
- Numerology  
- Bandwidth  
- SSB & sync  
- CORESET/PDCCH  
- DMRS/CSI-RS  
- HARQ timeline  

PCell = anchor for RRC, UL.  
SCells = extra bandwidth, can be DL-only or DL/UL.  
SCells can be activated/deactivated dynamically.

## 3️⃣ CA Types
### Intra-band contiguous  
- Adjacent CCs  
- Easiest RF design  

### Intra-band non-contiguous  
- Frequency gap within same band  
- More filtering challenges  

### Inter-band  
- Different bands  
- Requires multiple Rx/Tx chains  
- More heat + battery usage

## 4️⃣ DL vs UL CA
### DL CA  
- 3–5 CCs typical  
- Scheduler distributes PDSCH across CCs  

### UL CA  
- Optional  
- Typically 1–2 CCs  
- PA linearity + ACLR constraints make it harder

## 5️⃣ Cross-Carrier Scheduling (CCS)
- PDCCH in CC#1 can schedule PDSCH/PUSCH in CC#2  
- Reduces control overhead  
- Requires CORESET support for CCS  

## 6️⃣ HARQ in CA
Each CC has independent HARQ processes:  
- Separate buffers  
- Separate RV mapping  
- Separate timelines  

## 7️⃣ Measurement Aspects
UE measures each CC independently:  
- DL: RSRP/RSRQ/SINR, CSI-RS, beams  
- UL: Timing alignment per CC group, power control, SRS per CC  

## 8️⃣ Mobility with CA
- Handover anchors on PCell  
- SCells reconfigured after HO  
- PCell measurements dominate mobility  
- CA doesn’t directly drive mobility decisions

## 9️⃣ BWP Interaction
Each CC can have multiple BWPs:  
- PCell has its active BWP  
- Each SCell has its own active BWP  
- UE monitors only active BWP’s PDCCH  
- Saves UE power  
- BWP switching only affects that CC

## 🔟 RF Design Impacts
UE needs:  
- Multiple LNAs  
- Multiple PAs for UL CA  
- Wideband duplexers  
- High isolation  
- Multi-carrier linearity  
- Emission mask compliance  

More CCs = more heat + more power drain.  
FR2 CA exists but beam coordination is required.

## 1️⃣1️⃣ Throughput in CA
Total throughput ≈ sum of CC throughputs, depending on:  
- MIMO layers per CC  
- Numerology  
- Scheduler efficiency  
- HARQ success  
- RF conditions  

## 1️⃣2️⃣ CA in EN-DC (LTE+NR)
- LTE PCell anchor  
- NR SCell(s)  
- LTE CA + NR CA simultaneously  
- UE runs LTE + NR PHY/MAC together  

## 1️⃣3️⃣ CA Capability Signaling
UE advertises:  
- Supported NR bands  
- Band combinations  
- CC combinations  
- MIMO layers per CC  
- Max bandwidth per CC  
- UL MIMO + power class  

This is why smartphones vary in CA combos.

## 1️⃣4️⃣ CA Scheduler Logic
gNB does:  
- PRB balancing  
- Primary CC prioritization  
- Load balancing  
- SINR-based CC allocation  
- QoS-aware scheduling  
- Semi-persistent scheduling  

Treats CCs like “multiple pipes with different pressures.”

## 1️⃣5️⃣ Debugging CA in Logs
Look for:  
- PCell + SCell identity  
- SCell activation/deactivation CE  
- crossCarrierIndicator  
- DL/UL mapping  
- BWP switches  
- CSI-RS per CC  
- CC-wise throughput  