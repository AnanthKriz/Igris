# 🖤 IGRIS — The Shadow That Leaves No Trace

> **“Born from silence. Built for oblivion.”**  
> _Inspired by IGRIS from Solo Leveling — this tool is not a program.  
> It’s a digital ghost that executes, melts, and erases itself from reality._

---

## 👁‍🗨 What is IGRIS?

**IGRIS** is a *self-melting*, *anti-forensic*, *fileless* cyber weapon designed for advanced stealth ops, red teaming, and forensic evasion.

Once executed, IGRIS performs its task **entirely in RAM**, scrubs all traces of its existence, and then vanishes —  
> Just like the shadow soldier it’s named after.

---

## ⚔️ Why IGRIS?

In the world of defenders, scans, and forensic trails...  
IGRIS doesn’t fight.  
**It disappears.**

---

## 🧠 Core Features

| Module                  | Description                                |
|-------------------------|--------------------------------------------|
| 🧊 In-memory execution   | All payloads run from RAM (safe version for now) |
| 🔥 Melt-on-exit         | Deletes its own script after execution     |
| 🧹 Anti-forensics       | Cleans shell history, PowerShell logs      |
| 🕳️ Temp folder erasure  | Removes temp files created during run      |
| 🕒 Timed vanish option  | Self-erases after X seconds                |
| 🦠 No C2/No Network      | Fully standalone. No callback or beacon.   |

---

## 🛠️ Execution Instructions

### 🐧 On Linux/macOS:
```bash
python3 igris.py
```

### 🪟 On Windows (CMD or PowerShell):
```bash
py igris.py
```

> **Note:** Requires Python 3.  
> For EXE build: use PyInstaller  
> `pyinstaller --onefile igris.py`

---

## ⚠️ What IGRIS Does (Safe Version)

1. Spawns a fake RAM-only payload  
2. Creates and deletes a temporary directory  
3. Wipes shell history (bash, zsh, PowerShell)  
4. Deletes its own `.py` or `.exe` file — **melts itself**  
5. Leaves no trace behind

---

## 💀 What’s Coming in Future Builds?

| Feature                   | Status |
|---------------------------|--------|
| 🧬 Memory-only shellcode execution | 🔒 Phase 2 |
| 🔗 PowerShell Reflective DLL loader | 🔒 Phase 2 |
| 🔁 Filename mutation engine        | 🔒 Phase 3 |
| 👁️ Zero-log syscalls & stealth hooks | 🔒 Experimental |

---

## 🖤 Lore Mode: Why “IGRIS”?

> “He stood still. A black knight of fireless shadows.  
> His presence erased the air around him.”  
> — *Solo Leveling*

Just like the original Igris:  
- He doesn’t speak.  
- He doesn’t bleed.  
- He doesn’t *exist* until summoned.

IGRIS is your **digital summon** —  
A one-command ghost.  
**It executes. It melts. It disappears.**

---

## ☠️ Disclaimer

> This project is for **educational and research** use only.  
> Use it **only in lab environments, red teaming, or cybersec testing.**  
> The author is not responsible for misuse.

---

## 👑 Made By

**KRIZ** — “In the digital empire, Kriz stands as the Cyber King — unseen, unmatched, unstoppable.”

```bash
[ IGRIS ACTIVATED ]
>> Payload executed
>> History erased
>> IGRIS melted into silence...
```
