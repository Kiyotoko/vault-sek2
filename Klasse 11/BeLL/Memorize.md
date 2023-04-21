---
author: karlz
tags:
- Bell
- FGB
---

Vergleich von privaten Kommunikationsnetzen Tor, Mixnet und VPN anhand einer Simulationsumgebung.

# Recherche

## Systeme^[https://www.inforsec.org/wp/?p=960]

- Mixes
- DC-Net
- Anonymizer
- Crowds
- Onion Routing
- Mixminion
- Tor

### Tor^[https://www.researchgate.net/publication/320663877_Anonymous_Communication_on_the_Internet#pf9]

Onion Routing

## Strategien

- Blacklisting
- Whitelisting

## Simulation^[https://www.twi-global.com/technical-knowledge/faqs/faq-what-is-simulation]

- Diskrete Simulation: Modelling a system as it progresses through time,
- Dynamik Simulation: Modelling a system as it progresses through space
- Process Simulation: Modelling physical interactions between two or more systems

### AnoA^[https://eprint.iacr.org/2014/087.pdf]

Framework for anonymous communication protocols

# Diagramme

## Schlüssel

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

## Tor

```mermaid
graph LR
A(Alice)-->1[Guard]-->2-->3--> B(Bob)
```

## Mixnet

```mermaid
graph LR;
A(Alice)
B(Bob)
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
