# Source Verification Notes

## Methodology

This report was compiled by seven independent research passes (one per section: Ancient India, Classical & Early Medieval India, Medieval India, Mughal Empire, Colonial Era, Independence Movement, Post-Independence India). Each pass was instructed to:

1. Prioritize official/encyclopedic sources (Britannica, World History Encyclopedia, government portals, established academic sites).
2. Cross-verify key facts — especially dates — across at least two independent sources.
3. Explicitly flag disputed or uncertain claims rather than presenting them as settled fact.

## Link Validation

After all seven sections were compiled, all reference URLs (~120 total across the report) were programmatically checked for reachability via automated HTTP requests, followed by manual spot-checks on anomalies.

**Results:**

| Outcome | Count (approx.) | Explanation |
|---|---|---|
| 200 OK | ~75 | Verified reachable |
| 403 (Britannica.com) | ~40 | Known bot-blocking behavior — **not evidence of broken/invalid pages**. Confirmed by direct browser-equivalent fetch on a sample; all Britannica citations were independently corroborated by a second working source during research. |
| 404 (genuinely broken) | 1 | `en.wikipedia.org/wiki/Railways_in_British_India` — page does not exist under that title. **Corrected** to [Rail transport in India](https://en.wikipedia.org/wiki/Rail_transport_in_India), confirmed live and covering the same colonial-era railway history. |
| Connection error (transient) | 2 | `gktoday.in` and `ddnews.gov.in` initially failed to connect via automated check but were confirmed live and functional via direct fetch — kept as-is. |
| Connection error (unresolved) | 1 | `sardarpatel.nvli.in` (Sardar Patel National Virtual Library, a government portal) — refused connection on retry. The single fact it supported (Hyderabad's "Operation Polo" annexation date) is independently corroborated by the [Annexation of Hyderabad](https://en.wikipedia.org/wiki/Annexation_of_Hyderabad) Wikipedia article, so this citation was **replaced** rather than left as an unverified reference. |

## Facts Flagged as Disputed or Uncertain

The following are genuine areas of ongoing historical debate, not gaps in research:

- Exact dating of the Indus Valley Civilization's earliest phase (3300–7000 BCE, depending on definition) and the cause(s) of its decline.
- Whether Indo-Aryan migration into India was gradual/cultural or involved conquest — an actively and politically debated question.
- Exact birth/death dates of the Buddha (c. 563–483 BCE traditional, disputed by up to a century) and Mahavira (three differing traditions, from c. 599–527 BCE to c. 490–410 BCE).
- Nalanda University's exact founding date (c. 427 CE vs. c. 450 CE).
- The magnitude and net economic effect of the colonial-era "drain of wealth" theory.
- Death toll and displacement estimates from Partition (1947) — ranging from 200,000 to 2 million deaths and 12–20+ million displaced, depending on source and methodology.
- India's exact global GDP ranking in 2025 (4th vs. 5th largest economy, depending on nominal vs. other methodology).
