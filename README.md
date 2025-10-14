# R3 Package  
**State:** not finished  
**Version:** v0.2-alpha

> R3 Package is a portable, easy-to-use suite of ethical hacking tools aimed at beginners.  
> The package includes `goblin_wizard.py`, a helpful interactive manual for newcomers with notes and extensive help for each r3-pkg script.

---

## Source composition
Each script is identified by an id (`r3XXX`): the first two digits denote the category (`r31`–`r39`), and the last two digits are the script index within that category (`01`–`99`). Scripts in the `r30` category are framework scripts. Anything outside these categories is likely not intended for direct use.

---

## Categories

### _proto  
Miscellaneous scripts under rework — candidates to be refactored or integrated into R3 Package.

### r31_enum  
Information gathering. Tools to enumerate and fingerprint targets, discover services and potential vulnerabilities.

### r32_exploit  
Exploitation tools. Use after enumeration to attempt known exploits (XSS, SQLi, SSRF, etc.) and attack outdated or misconfigured services.

### r33_privilege  
Privilege escalation and lateral movement. Tools and helpers to escalate privileges and pivot through a target network.

### r34_post  
Post-exploitation. Automation and techniques for persistence, data collection, and cleanup once access is obtained.

### r35_wireless  
Wireless security tools. Attacks and auditing utilities targeting Wi‑Fi and other wireless protocols.

### r36_crypto  
Cryptography and encoding tools. Analysis, simple crypto utilities and codification helpers for puzzles, crypto analysis or obfuscated data.

### r37_fish
Phishing and social engineering tooling. Automation and templates for phishing campaigns and human-targeted vectors.

### r38_malware  
Payloads and delivery helpers intended to run on target hosts once compiled. These are aimed at exploitation, privilege escalation or post-exploit stages.

### r39_report  
Report generation and automation to speed up post-engagement documentation.

---

**Author:** R3DG0BL1N  
**License:** MIT (see LICENSE)
**Disclaimer:** Use only with explicit permission from the system owner. The author is not responsible for misuse. Unauthorized access, damage or legal consequences are your responsibility.
