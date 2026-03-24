# 🔐 Password Strength Checker

A command-line tool written in Python that analyses the strength of a password and gives instant visual feedback — right in your terminal.

---

## 📸 What it looks like

```
╔══════════════════════════════════╗
║      PASSWORD STRENGTH CHECKER   ║
╚══════════════════════════════════╝

Enter a password: MyP@ssw0rd123

  Rule Checks
  ──────────────────────────────────
  ✓  Length        At least 8 characters
  ✓  Uppercase     At least one uppercase letter
  ✓  Lowercase     At least one lowercase letter
  ✓  Digit         At least one digit (0–9)
  ✓  Symbol        At least one symbol (e.g. !@#$)

  Common Password Check
  ──────────────────────────────────
  ✓  Not found in common password list

  Strength
  ──────────────────────────────────
  ████████████████████░░░░░░░░░░  8/10  Strong
```

---

## ✨ Features

- ✅ Checks password against 5 rules (length, uppercase, lowercase, digit, symbol)
- ⚠️ Detects common weak passwords (e.g. `password`, `123456`)
- 📊 Scores your password from 0–10 with a visual progress bar
- 🎨 Colour-coded output (red / yellow / green) in the terminal
- 💡 Shows helpful hints for any rules you've failed

---

## 🚀 How to run

**Requirements:** Python 3 — no external libraries needed.

```bash
python3 password_checker.py
```

Then just type your password when prompted.

---

## 🧠 How the scoring works

| Points | Source |
|--------|--------|
| +1 per rule passed | Up to 5 points for length, uppercase, lowercase, digit, symbol |
| +1 | Password is 12+ characters |
| +2 | Password is 16+ characters |
| +1 | 10+ unique characters |
| +1 | 15+ unique characters |
| -5 | Password is in the common passwords list |

Final score is clamped between 0 and 10.

| Score | Verdict |
|-------|---------|
| 0–2   | Very Weak 🔴 |
| 3–4   | Weak 🔴 |
| 5–6   | Fair 🟡 |
| 7–8   | Strong 🟢 |
| 9–10  | Very Strong 🟢 |

---

## 📁 Project structure

```
password-checker/
│
├── password_checker.py   # Main script
└── README.md             # You're reading it!
```

---

## 🛠️ Built with

- Python 3
- ANSI escape codes for terminal colours
- Unicode block characters for the progress bar (`█`, `░`)

---

## 📌 Notes

- Colours and the progress bar work in **macOS Terminal**, **iTerm2**, and any modern terminal
- No pip installs needed — fully standard library

---

*Mini project — built to practise Python functions, string manipulation, and terminal formatting.*
