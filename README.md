# aig-shieldsup-simulation
Demonstration of ransomware recovery using Python brute-force (ZIP password cracking). Completed as part of Forage’s AIG Shields Up Cybersecurity Simulation.
# Cybersecurity Job Simulation (Forage - AIG Shields Up)

This repository contains artifacts from the **AIG Shields Up: Cybersecurity Job Simulation** (Forage). It demonstrates a small, self-contained demonstration of recovering an encrypted file using a Python bruteforce script and includes screenshots as proof-of-work.

## 🛡️ Tasks Completed
- **Task 1 — Zero-Day Vulnerability Response**: Analysis of the Log4j exploit and internal advisory (summary).
- **Task 2 — Bypassing Ransomware**: Implemented and ran a Python brute-force script against a password-protected ZIP file (used `rockyou.txt` wordlist). Successfully recovered the sensitive file (password found in screenshots).

## 🔐 Files Included
- `bruteforce.py` — Python script used to brute-force a password-protected ZIP file.
- `ImportantFile.txt` — Decrypted file contents summary (text form).
- `screenshots/` — Proof-of-work images:
  - `script.png` — The Python script screenshot.
  - `terminal.png` — Terminal output showing the cracked password.
  - `decrypted.png` — The decrypted Word document screenshot.

## 📂 Suggested Repo Structure (already prepared in this zip)
```
cybersecurity-simulation/
├── README.md
├── bruteforce.py
├── ImportantFile.txt
└── screenshots/
    ├── script.png
    ├── terminal.png
    └── decrypted.png
```

## ⚠️ Notes
- The original `ImportantFile.docx` (binary Word document) was recovered during the simulation. For portability in this package I've included a plaintext summary `ImportantFile.txt` and screenshots as proof. If you want, replace `ImportantFile.txt` with the original `ImportantFile.docx` before pushing to GitHub.
- Do **not** upload any sensitive or real credentials to public repositories.

---
**Author:** Oppong Isaac  
**Date:** October 2025
