import numpy as np

def generate_prach_preamble(
    preamble_index,
    root_sequence_index,
    N_ZC,
    zero_correlation_zone,
):
    """
    Generate 5G NR PRACH preamble using Zadoff-Chu sequences.

    Args:
        preamble_index (int): preamble number 0–63
        root_sequence_index (int): prach-RootSequenceIndex (u)
        N_ZC (int): Zadoff-Chu sequence length (e.g., 839 or 139)
        zero_correlation_zone (int): defines cyclic shift spacing (N_CS)

    Returns:
        np.array: complex PRACH baseband samples (no CP)
    """

    # -------------------------
    # Step 1: Base Zadoff-Chu root sequence (x_u(n))
    # -------------------------
    n = np.arange(N_ZC)
    xu = np.exp(-1j * np.pi * root_sequence_index * n * (n + 1) / N_ZC)

    # -------------------------
    # Step 2: Compute cyclic shift for preamble index
    # N_CS = ZCZ config → determines the shift increment
    # -------------------------
    N_CS = zero_correlation_zone  # normally derived via table in 38.211
    
    cyclic_shift = (preamble_index * N_CS) % N_ZC

    # -------------------------
    # Step 3: Apply cyclic shift
    # PRACH preamble = shifted ZC sequence
    # -------------------------
    preamble = np.roll(xu, cyclic_shift)

    return preamble


# -------------------------
# Example usage
# -------------------------

preamble_index = 17                # UE-chosen preamble (0-63)
root_sequence_index = 129          # gNB configured (SIB1)
N_ZC = 839                         # typical for long PRACH (FR1)
zero_correlation_zone = 13         # example N_CS derived from config

preamble = generate_prach_preamble(
    preamble_index,
    root_sequence_index,
    N_ZC,
    zero_correlation_zone
)

print("Generated PRACH preamble samples:")
print(preamble[:20])  # print first 20 samples
print("Total samples:", len(preamble))
