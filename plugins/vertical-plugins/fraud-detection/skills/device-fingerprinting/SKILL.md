---
name: device-fingerprinting
description: |
  Device identification and fingerprinting for fraud detection and session tracking.
  Perfect for: device-based fraud signals, cross-session tracking, bot detection.
  Not ideal for: network-level threat detection, DDoS prevention.
---

# Device Fingerprinting

## Core Philosophy
**"Know the device to know the risk — a familiar device is a trusted device."**

## Fingerprint Components

### Browser-Based Signals
| Signal | Entropy | Description |
|--------|---------|-------------|
| User-Agent | Medium | Browser name, version, OS |
| Screen resolution | Low | Display dimensions |
| Timezone | Low | UTC offset |
| Language | Low | Browser language preference |
| Canvas hash | High | GPU rendering differences |
| WebGL renderer | High | GPU model identification |
| Audio context | Medium | Audio processing differences |
| Installed fonts | High | System font enumeration |
| Plugin list | Medium | Browser plugins/extensions |
| CPU cores | Low | navigator.hardwareConcurrency |
| Device memory | Low | navigator.deviceMemory |
| Touch support | Low | Touch vs mouse input |

### Network Signals
| Signal | Description |
|--------|-------------|
| IP address | Client IP (respect proxies via X-Forwarded-For) |
| IP geolocation | Country, region, city |
| ISP/ASN | Internet service provider |
| Proxy detection | VPN, Tor, datacenter, residential proxy |
| Connection type | WiFi, cellular, wired |

### Behavioral Signals
| Signal | Description |
|--------|-------------|
| Typing cadence | Keystroke timing patterns |
| Mouse movement | Movement velocity and patterns |
| Scroll behavior | Scroll speed and patterns |
| Form fill time | Time from page load to form submission |
| Copy-paste detection | Pasted vs typed input |

## Device Trust Scoring

### Trust Levels
| Level | Score | Criteria |
|-------|-------|----------|
| Trusted | 0-10 | Known device, >30 days history, no fraud |
| Familiar | 11-30 | Seen before, <30 days, no fraud |
| Neutral | 31-50 | First-time device, no negative signals |
| Suspicious | 51-75 | Proxy, spoofed signals, or linked to fraud |
| Malicious | 76-100 | Confirmed fraud device, bot, or emulator |

### Spoofing Detection
1. **User-Agent consistency**: Compare claimed UA with actual browser capabilities
2. **Timezone mismatch**: Compare JS timezone with IP geolocation timezone
3. **Canvas/WebGL anomalies**: Detect headless browsers and emulators
4. **Automation detection**: Check for `navigator.webdriver`, phantom properties
5. **Impossible configurations**: GPU that doesn't match claimed OS

## Privacy Considerations
- Comply with GDPR/CCPA — fingerprinting is personal data processing
- Provide clear privacy policy disclosure
- Implement data retention limits (90 days recommended)
- Support right-to-deletion requests
- Do not use fingerprinting for tracking/advertising — fraud prevention only
