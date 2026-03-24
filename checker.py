import sys

# ANSI colour codes for terminal output
RED     = "\033[31m"
YELLOW  = "\033[33m"
GREEN   = "\033[32m"
CYAN    = "\033[36m"
BOLD    = "\033[1m"
DIM     = "\033[2m"  # dimmed/greyed out text
RESET   = "\033[0m"  # resets all formatting back to default

# Maps each verdict to its corresponding colour for display
VERDICT_COLOURS = {
    "Very Weak":   RED,
    "Weak":        RED,
    "Fair":        YELLOW,
    "Strong":      GREEN,
    "Very Strong": GREEN,
}

# Function that takes a password and checks it against 5 rules
def check_rules(password):
    # Each key in the results dictionary corresponds to a specific rule
    # The value is a boolean indicating whether the password passed that rule or not
    return {
        "length":    len(password) >= 8,                                          # password must be at least 8 characters
        "uppercase": any(c.isupper() for c in password),                          # c.isupper() checks if the character is an uppercase letter
        "lowercase": any(c.islower() for c in password),                          # any() returns True if at least 1 character matches
        "digit":     any(c.isdigit() for c in password),                          # c.isdigit() checks if the character is a digit (0-9)
        "symbol":    any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password), # checks against a string of allowed symbols
    }

# Hint messages shown to the user when a rule is failed
RULE_HINTS = {
    "length":    "At least 8 characters",
    "uppercase": "At least one uppercase letter",
    "lowercase": "At least one lowercase letter",
    "digit":     "At least one digit (0–9)",
    "symbol":    "At least one symbol (e.g. !@#$)",
}

# A list of commonly used weak passwords to check against
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty",
    "abc123", "football", "monkey", "letmein", "111111", "1234"
]

# Returns True if the password (case-insensitive) is in the common passwords list
def is_common(password):
    return password.lower() in COMMON_PASSWORDS

# Strength scorer — calculates a score out of 10 and returns a verdict label
def get_score(password, rules, is_common_password):
    score = sum(rules.values())  # each passed rule adds 1 to the score (max 5)

    # Bonus points for longer passwords
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 2  # extra bonus for very long passwords

    # Bonus points for variety of unique characters
    unique_chars = len(set(password))  # set() removes duplicates, len() counts what's left
    if unique_chars >= 10:
        score += 1
    if unique_chars >= 15:
        score += 1

    # Penalise common passwords heavily
    if is_common_password:
        score -= 5

    score = max(0, min(10, score))  # clamp score between 0 and 10

    # Map score ranges to verdict labels
    if score <= 2:
        verdict = "Very Weak"
    elif score <= 4:
        verdict = "Weak"
    elif score <= 6:
        verdict = "Fair"
    elif score <= 8:
        verdict = "Strong"
    else:
        verdict = "Very Strong"

    return score, verdict

# Draws a visual progress bar using block characters, coloured by score
def draw_progress_bar(score, width=30):
    filled = int((score / 10) * width)          # how many blocks to fill based on score
    bar    = "█" * filled + "░" * (width - filled)  # filled blocks + empty blocks

    # Choose colour based on score range
    if score <= 4:
        colour = YELLOW
    elif score <= 6:
        colour = YELLOW
    else:
        colour = GREEN

    if score <= 2:
        colour = RED  # override to red for very weak passwords

    return f"{colour}{bar}{RESET}"

# Prints a decorative header using box-drawing characters
def print_header():
    print(f"\n{BOLD}{CYAN}╔══════════════════════════════════╗")
    print(f"║     PASSWORD STRENGTH CHECKER    ║")
    print(f"╚══════════════════════════════════╝{RESET}\n")

def main():
    print_header()
    password = input(f"{BOLD}Enter a password:{RESET} ")

    # Run all checks
    rules   = check_rules(password)
    common  = is_common(password)
    score, verdict = get_score(password, rules, common)

    # ── Rule checks ──────────────────────────────────────
    print(f"\n{BOLD}  Rule Checks{RESET}")
    print(f"  {'─' * 34}")
    for rule, passed in rules.items():
        if passed:
            icon  = f"{GREEN}✓{RESET}"                        # green tick for passed rules
            label = f"{rule.capitalize():<12}"
            hint  = f"{DIM}{RULE_HINTS[rule]}{RESET}"         # dimmed hint text when passed
        else:
            icon  = f"{RED}✗{RESET}"                          # red cross for failed rules
            label = f"{RED}{rule.capitalize():<12}{RESET}"
            hint  = f"{YELLOW}→ {RULE_HINTS[rule]}{RESET}"    # yellow arrow with fix suggestion
        print(f"  {icon}  {label}  {hint}")

    # ── Common password check ─────────────────────────────
    print(f"\n{BOLD}  Common Password Check{RESET}")
    print(f"  {'─' * 34}")
    if common:
        print(f"  {RED}⚠  '{password}' is a known weak password!{RESET}")
    else:
        print(f"  {GREEN}✓  Not found in common password list{RESET}")

    # ── Score & progress bar ──────────────────────────────
    verdict_colour = VERDICT_COLOURS[verdict]  # look up the colour for this verdict
    bar = draw_progress_bar(score)

    print(f"\n{BOLD}  Strength{RESET}")
    print(f"  {'─' * 34}")
    print(f"  {bar}  {BOLD}{verdict_colour}{score}/10  {verdict}{RESET}")
    print()

# Only runs main() if this file is executed directly (not imported as a module)
if __name__ == "__main__":
    main()

