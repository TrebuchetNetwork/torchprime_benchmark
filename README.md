# Prime Number Generation Benchmark - Sieve of Atkin vs. Sieve of Eratosthenes

This repository contains a benchmark comparison of two popular prime number generation algorithms, the Sieve of Atkin and the Sieve of Eratosthenes. The code is implemented in Python using PyTorch, both on the CPU and with MPS (Metal Performance Shaders) support when available.

The benchmark measures the time taken to generate prime numbers up to a given limit, and it provides a comparison of the performance of the two algorithms, as well as a naïve MPS implementation for reference.

## Features

- Implementation of the Sieve of Atkin in PyTorch (CPU and MPS)
- Implementation of the Sieve of Eratosthenes in PyTorch (CPU and MPS)
- Naïve MPS implementation for reference
- Time measurements for each algorithm
- Code to generate safe primes

## Requirements

- Python 3.x
- PyTorch

## Usage

1. Clone the repository
2. Install the required dependencies
3. Run the benchmark script with `python benchmark.py`

The script will output the time taken for each algorithm and the ratio of generated safe primes to the limit.

## Contributing

Feel free to open issues for any bugs, suggestions, or optimizations. If you would like to contribute directly to the code, please create a pull request with a clear description of your changes.

## License

MIT License
