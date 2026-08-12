# How It Works: Onion Routing & .onion Addresses

- **Onion routing**: Data is wrapped in multiple layers of encryption — like an onion — and passed through a chain of relays (typically 3: guard, middle, exit). Each relay only knows the previous and next hop, never the full path. The final (exit) node is the only one that sees the destination; the first (guard) node is the only one that sees the origin.
- **.onion addresses**: These are self-certifying addresses derived from a site's cryptographic public key (plus a version byte and checksum) — so simply reaching the address cryptographically verifies you're talking to the right service, with no external certificate authority needed.
- **Hidden services**: For .onion-to-.onion connections, there's no exit node at all — both sides build circuits that meet at a shared "rendezvous point" inside the Tor network, so traffic never touches the open internet.

## Sources
- [What is onion routing and how does it work? | NordVPN](https://nordvpn.com/blog/onion-routing/)
- [Demystifying the Dark Web: An Introduction to Tor and Onion Routing – ITP NYU](https://itp.nyu.edu/networks/explanations/demystifying-the-dark-web-an-introduction-to-tor-and-onion-routing/)
- [What is Tor and How Does Onion Routing Work? | IdentityIQ](https://www.identityiq.com/articles/what-is-tor-and-how-does-onion-routing-work)
