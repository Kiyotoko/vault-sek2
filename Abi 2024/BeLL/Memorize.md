# BeLL
**Thema** Vergleich von privaten Kommunikationsnetzen Tor, Mixnet und VPN anhand einer Simulationsumgebung.
## Literaturrecherche
- https://www.primafelicitas.com/Insights/is-there-a-need-for-network-level-privacy-p2p-tor-and-mixnet/
- https://blog.torproject.org/new-foundations-tor-network-experimentation/
- https://research.torproject.org/tools/
- https://github.com/shadow/tornettools
- https://nymtech.net/
- https://www.researchgate.net/figure/VPN-Simulation-in-Packet-Tracer_fig5_271405994
## Links
- https://cryptpad.fr/code/#/2/code/edit/iVMDOCSEFVWj-Xzb1ALCcDhx/
## Aufbau
### Schlüssel
```mermaid
sequenceDiagram
    critical Share Public Key
        A->>B: Ask for Public Key
        B->>A: Send Public Key
    end
    loop Send Messages
        A->>B: Decode Message with Public Key
        B->>B: Encode Message with Private Key
    end
```
### Tor
```mermaid
graph LR;
  classDef default fill:#00AAAA,stroke:#333,stroke-width:4px;
  A(Alice) --> 1[Guard] --> 2 --> 3 --> B(Bob)
```
### Mixnet
```mermaid
graph LR;
  A(Alice)
  B(Bob)
  classDef default fill:#00AAAA,stroke:#333,stroke-width:4px;
  A --> 1
  A --> 2
  subgraph 1.Layer
    1
    2
  end
  1 --> 3
  1 --> 4
  2 --> 3
  2 --> 4
  subgraph 2. Layer
    3
    4
  end
  3 --> B
  4 --> B
```
## Simulation
### Diskrete Simulation
https://users.cs.northwestern.edu/~agupta/_projects/networking/QueueSimulation/mm1.html 