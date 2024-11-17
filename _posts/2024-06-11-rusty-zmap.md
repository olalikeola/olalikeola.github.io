---
layout: post
author: Olayinka Adekola
tags: [overview, network scanning]
---

# Rusty ZMap: High-Performance Network Scanning in Rust

[Read the project paper](/assets/files/Rusty_Zmap.pdf)

[Check out the repo here!](https://code.stanford.edu/cs340r-team-zmap/zmap-rs)

## Overview

**Rusty ZMap** is a reimplementation of the high-speed network scanner **ZMap** in **Rust**. ZMap has been a revolutionary tool in the field of network security and research, allowing researchers to scan the entire IPv4 address space for open ports in under an hour. While ZMap is known for its performance, its C-based implementation has significant challenges in terms of safety, concurrency, and maintainability. This project, **ZMap-rs**, addresses these issues by leveraging Rust's modern systems programming features, such as memory safety, concurrency handling, and performance optimizations, to create a more reliable and maintainable version of the original tool.

## Problem Statement

Network scanning is a core technique for identifying vulnerabilities and discovering active hosts and services in large address spaces. The original ZMap tool made significant strides in high-performance scanning, but its implementation in C posed challenges with memory safety, concurrency management, and code complexity. These issues made ZMap harder to maintain and extend.

**Rusty ZMap** (ZMap-rs) was developed to overcome these challenges while maintaining ZMap's performance. By re-implementing ZMap in **Rust**, we aimed to achieve:

- **Memory Safety:** Ensuring that the code is free from issues like null pointer dereferencing, data races, and memory leaks.
- **Concurrency Management:** Using Rust's ownership model to safely manage concurrency and eliminate the need for manual memory management.
- **Maintainability:** Making the codebase more understandable and easier to extend by using Rust’s modern tooling and type system.

## How Rusty ZMap Works

### Key Design Goals

Rusty ZMap was designed to retain the performance characteristics of the original ZMap while providing additional safety and maintainability benefits. To achieve this, we:

- Used Rust’s **ownership model** and **borrow checker** to prevent memory-related bugs like data races and dangling pointers.
- Took advantage of Rust’s **type system** to ensure thread safety and efficient handling of network packet data.
- Utilized the **etherparse crate** to handle Ethernet packet serialization safely without resorting to unsafe Rust code.

### Packet Serialization Challenges

One of the primary challenges in re-implementing ZMap was handling packet serialization, which in the original ZMap was done using **unsafe C code**. In Rust, serialization requires careful attention to memory safety and ownership constraints, which are enforced by the borrow checker.

We initially used the **etherparse** crate for packet building, which allowed us to avoid unsafe code but resulted in slower performance. We then optimized packet serialization by implementing a caching mechanism that allowed us to reuse portions of the Ethernet packet while only updating fields that changed between probes (e.g., IP destination address, TCP source port). This strategy closely mimics the original ZMap implementation but without the need for unsafe Rust.

### Concurrency and State Management

Rust’s concurrency model, while safer, posed challenges with global state management across threads. The borrow checker makes it difficult to mutate global variables across multiple threads without violating Rust’s ownership rules. Despite this, we were able to design thread-safe data structures that managed concurrent state efficiently, avoiding the bugs typically seen in C-based implementations of similar tools.

## Performance Evaluation

To assess the performance of **Rusty ZMap**, we conducted a series of tests comparing it to the original ZMap. The primary metrics for comparison were:

- **Scan Completion Time**
- **Hit Rate** (fraction of successful responses)
- **Scan Rate** (probes per second)

### Test Setup

We conducted the following tests:

1. **Port 443 Scan**: Scanned 1% of the IPv4 address space for open port 443.
2. **Full IPv4 Scan**: A full scan of the entire IPv4 space targeting port 443.

Both tests were performed using **four threads** to maintain consistency across trials. For each test, the **scan rate** was varied from 250K to 1.5M packets per second.

### Results

- **Full Scan of Port 443**:
  - **Rusty ZMap (ZMap-rs)**: Completed the scan in approximately 42 minutes with a hit rate of 1.444%.
  - **Original ZMap**: Completed the scan in a similar timeframe with a hit rate of 1.442%.

Our results showed that **Rusty ZMap** matches the performance of the original ZMap, with slightly higher variability at higher scan rates but still achieving comparable or even faster scan times in some instances.

## Key Takeaways

### Benefits of Rust for Systems Programming

- **Memory Safety**: Rust's strict memory management model prevented many common bugs encountered in C, such as buffer overflows and memory leaks, without sacrificing performance.
- **Concurrency**: Rust's approach to handling concurrency through ownership and borrowing ensures thread safety, eliminating the need for complex locking mechanisms used in C.
- **Maintainability**: The Rust codebase is more maintainable and easier to extend compared to ZMap’s C code, which can be difficult to understand and contribute to due to its reliance on low-level, unsafe operations.

### Challenges and Solutions

- **Serialization**: Handling packet serialization in Rust was more complex than in C due to the ownership and borrowing rules. However, we managed to overcome this using safe Rust patterns, such as caching and the `copy_from_slice` method, to avoid unsafe code while maintaining high performance.
- **Concurrency and Global State**: Managing global state across threads was challenging due to Rust’s strict ownership model. However, we used Rust’s type system and concurrency features to design a thread-safe architecture that allowed us to scale the scanner without introducing data races.

## Future Work

Looking ahead, there are several ways **Rusty ZMap** can be improved:

1. **Performance Optimization**: Incorporating more advanced networking features, such as kernel bypass and asynchronous I/O, could help Rusty ZMap achieve even faster scan speeds.
2. **Asynchronous Scanning**: By leveraging Rust's asynchronous programming capabilities, we could further reduce I/O bottlenecks and improve throughput.
3. **Integration with Advanced Features**: Future developments could integrate more advanced tools and libraries from the Rust ecosystem, such as zero-copy networking or optimized data serialization methods.

## Ethical Scanning Practices

Similar to the original ZMap, ethical considerations were prioritized during the development and testing of Rusty ZMap. Key steps taken include:

- **Randomized Scanning**: We implemented a cyclic scanning protocol to ensure each scan has a different order of IP addresses, minimizing the risk of repeatedly targeting the same hosts.
- **Blocklist Compliance**: We maintained and verified a blocklist to ensure that IP addresses that had opted out of being scanned were not included in our scans.
- **Dry Runs**: We conducted dry runs to simulate scans without sending actual packets, verifying our ethical practices before real-world testing.
- **Monitoring and Compliance**: During real-world tests, we monitored traffic using **tcpdump** to ensure that no blacklisted IP addresses were targeted.

## Conclusion

**Rusty ZMap** (ZMap-rs) demonstrates that **Rust** can be a viable alternative for high-performance network scanning tools. With its focus on memory safety, concurrency, and performance, Rust offers significant advantages in terms of maintainability and reliability without compromising on speed. Our performance evaluation shows that Rusty ZMap matches the original ZMap's scanning capabilities while addressing key challenges in memory safety and concurrency.

Rusty ZMap highlights the potential of Rust for developing high-performance systems software that is both safe and maintainable, paving the way for future innovations in network scanning tools.

---

_Project by Olayinka Adekola._
