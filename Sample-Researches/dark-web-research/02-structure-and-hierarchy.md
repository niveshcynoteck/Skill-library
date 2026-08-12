# Structure & Hierarchy

There isn't one single "dark web" — it's really a collection of separate anonymity networks, each with its own internal architecture:

- **Tor** — Uses circuit-based onion routing with volunteer relays and centralized directory authorities to build fast, low-latency 3-hop circuits. It's the largest and most widely used network, and can also act as a gateway to/from the regular internet via exit nodes.
- **I2P (Invisible Internet Project)** — Uses "garlic routing" (a variant of onion routing that bundles multiple messages together) and asymmetric inbound/outbound tunnels. It has a documented **three-layer hierarchical structure**, with active I2P router endpoints forming Layer 1 of the network graph. Unlike Tor, it has no central directory authority and mostly keeps traffic inside its own network of internal sites ("eepsites").
- **Freenet** — A fully decentralized peer-to-peer datastore. Content is distributed and cached probabilistically across participating nodes rather than served from fixed servers, trading speed for resilience and censorship-resistance.

These three are often described as "the three pillars of the dark web."

## Marketplace Hierarchy

Beyond the network layer, within Tor specifically there's also a rough market hierarchy: large centralized marketplaces (historically Silk Road, AlphaBay) sit at the top, feeding into smaller vendor shops, forums, and now — since the major 2017–2019 takedowns — an increasingly **fragmented, decentralized ecosystem** of many smaller platforms rather than one dominant marketplace.

## Sources
- [Unveiling the I2P web structure: a connectivity analysis](https://arxiv.org/pdf/2101.03212)
- [Freenet, I2P and TOR: the three pillars of the dark web — Aleph Networks](https://www.aleph-networks.eu/en/what-is-the-dark-web/)
- [Dark Web Browsers 2026 | Tor vs I2P vs Freenet | Kahana](https://kahana.co/blog/dark-web-browsers-tor-i2p-freenet-2026)
- [Dark Web Marketplaces: Major Global Takedowns Explained 2025 | DeepStrike](https://deepstrike.io/blog/dark-web-marketplaces-takedowns)
