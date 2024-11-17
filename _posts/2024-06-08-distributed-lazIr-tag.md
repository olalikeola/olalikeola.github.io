---
layout: post
author: Olayinka Adekola
tags: [overview, distributed-systems, gaming]
---

# Distributed LazIR Tag: A Decentralized Multiplayer Game

[Read the project paper](/assets/files/Distributed_LazIR_Tag.pdf)

[Watch the working demo video here!](https://drive.google.com/file/d/1gKY8r-WHq2IKce9A64gaHr1w11lVu6mk/view?usp=drive_link)

[Check out the repo here!](https://github.com/olalikeola/lazIR_tag)

## Overview

The **Distributed LazIR Tag** project creates a multiplayer laser tag game where players earn and lose points based on signals sent to IR receivers on the Raspberry Pi Zero W boards. Our system leverages the Raft consensus protocol to ensure the consistency of game actions, even in a distributed environment. Players interact via IR remotes, and a decentralized log tracks actions such as who shot whom.

The core feature of this project is the ability to maintain gameplay even when some nodes fail, thanks to the fault tolerance provided by Raft. This design allows for a highly scalable and engaging multiplayer experience that operates smoothly on low-cost embedded hardware.

## Key Features

- **Decentralized Multiplayer System**: Each Raspberry Pi node acts as both a server and a client, ensuring no single point of failure.
- **Raft Consensus Protocol**: Ensures consistency across all nodes, even during node failures.
- **Real-time Communication**: Nodes communicate using the gRPC protocol, providing low-latency, real-time game updates.
- **Fault Tolerance**: Gameplay continues uninterrupted even when some nodes fail or disconnect.
- **Scalability**: The system scales with the number of players, ensuring minimal latency impact.

## Design

### 1. System Architecture

The system architecture is based on a network of **Raspberry Pi Zero W** devices. Each Raspberry Pi acts as both a server and a client, allowing for peer-to-peer communication. This decentralized architecture helps mitigate issues related to centralized game servers, such as single points of failure.

- **Communication Protocol**: We use **gRPC** for efficient and scalable communication between nodes.
- **Consensus Mechanism**: The **Raft consensus protocol** ensures that game events are consistent across all nodes.
- **Distributed Log**: A distributed log records game actions like hits and score updates, ensuring all nodes agree on the game state.
- **Fault Tolerance**: Thanks to Raft's heartbeat monitoring, node failures are detected promptly, and disconnected nodes can rejoin with minimal disruption.

### 2. IR Remote and Receiver Setup

Each player is equipped with an IR remote, which sends signals to the **IR receivers** connected to the Raspberry Pi boards. These signals are then mapped to specific actions in the game, such as scoring points or tagging other players.

### 3. Game Flow

1. Players interact by shooting each other with IR remotes, sending signals to the Raspberry Pi nodes.
2. Each node processes these signals and updates the distributed log accordingly.
3. The Raft protocol ensures that all nodes maintain the same game state by achieving consensus on the actions taken.
4. If a node fails, Raft’s heartbeat mechanism allows the system to detect the failure and reintegrate the node when it comes back online.

![System Architecture](/assets/images/infra.png)

_Figure 1: The overall system architecture. Raspberry Pi nodes (green) are connected to IR receivers that track game events in real-time._

## Performance Analysis

Our system demonstrates the feasibility of running a distributed multiplayer game on low-cost embedded hardware. We also analyze the impact of increasing the number of players on system latency. The simulation results show that the system maintains low latency, even as more players are added, proving the scalability of the distributed design.

## Conclusion

This project showcases a robust and scalable **distributed laser tag game** that leverages the **Raft consensus protocol** for high availability, fault tolerance, and consistency. By using cost-effective embedded hardware, we overcome the limitations of traditional centralized servers, creating a multiplayer gaming experience that is both resilient and engaging.

### Check Out the Demo

[Watch the working demo video here!](https://drive.google.com/file/d/1gKY8r-WHq2IKce9A64gaHr1w11lVu6mk/view?usp=drive_link)

[Read the project paper (PDF)](/assets/files/Distributed_LazIR_Tag.pdf)

[Check out the repo here!](https://github.com/olalikeola/lazIR_tag)

<!-- ## Future Work

Future enhancements could include:

- Adding more advanced game features (e.g., power-ups, player zones).
- Improving the system's performance with additional optimizations.
- Expanding the network to support even more players without sacrificing performance. -->

---

_Project by Olayinka Adekola._
