def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    pattern_count = 0
    comparison_count = 0
    match_indices = []

    while i < n:
        comparison_count += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            pattern_count += 1
            match_indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return pattern_count, comparison_count, match_indices

# Pola yang dicari
pattern = "GCAATAATTTGATATCCTATCACGATGGAAGCTACCTTAAAAAA"

# Data DNA yang diambil dari Bank Gen DNA (NCBI-USA)
# Asumsi data DNA mikro bakteri diambil dari file dna_sequence.txt
with open('DNA.txt', 'r') as file:
    text = file.read().replace('\n', '')

# Menjalankan KMP search
pattern_count, comparison_count, match_indices = kmp_search(pattern, text)

print(f"Pattern muncul sebanyak {pattern_count} kali.")
print(f"Proses pembandingan dilakukan sebanyak {comparison_count} kali.")
print(f"Indeks kecocokan: {match_indices}")
