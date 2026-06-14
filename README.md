# BloomFilter-IoT

A hardware-optimized identity verification framework built in Python. Designed for secure communication networks, this engine implements a custom **Bloom Filter probabilistic bit-array** to perform instant lookup checks on incoming device connections.

## ⚡ Probabilistic Performance Metrics
* **Space Complexity:** Fixed bit-allocation size $O(M)$, bypassing the need to store raw strings.
* **Time Complexity:** Constant-time $O(K)$ lookups, where $K$ is the number of hash operations.
* **Error Margin:** Zero False Negatives; a small, predictable margin of False Positives.
