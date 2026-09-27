# Module 2 mini-lab — Code Rescue

Investigate a small unfamiliar Python game, verify its behavior and make focused repairs. This practices the context, debugging and review techniques from Module 2 before you apply them to PromptLab.

## Your starting point

`legacy_game.py` runs a small text RPG. It contains unclear names and four intentional behavior defects. There are no external dependencies or supplied solution tests. The code is short enough to investigate without introducing a new framework.

## Local setup

Download **Code → Download ZIP** from this repository and extract it into a new folder, or clone it if you already use Git. Open that folder in your editor. Use Python 3.12 and Git, with the Codex or Claude Code setup you established in Module 1. No Codespaces, devcontainer or shared API key is needed.

From the lab folder, create and activate a virtual environment:

| Platform | Create | Activate |
|---|---|---|
| macOS / Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |
| Windows PowerShell | `py -3.12 -m venv .venv` | `.venv\Scripts\Activate.ps1` |

All subsequent Python commands use `python` in that active environment. If you downloaded a ZIP, initialize a local Git repository and commit the supplied starter before working. If you cloned it, retain the starter commit. Commit small changes as you go.

## Run and observe

```sh
python legacy_game.py
```

Use `f` to fight, `a` to attack, `r` to run during combat, or `r` to rest outside combat. Ctrl+C stops the program. Start a new process for a fresh game. Random combat makes some cases hard to reproduce; use controlled random values in your own checks rather than playing until a rare case happens.

## Required game behavior

- Start with 100 health, zero gold and an empty inventory. Maximum health is 100.
- Each victory awards 10–30 gold **in addition** to existing gold and adds one Potion to inventory.
- A monster attacks only if still alive after your attack. Running away earns no victory reward.
- Resting adds ten health up to the maximum.
- Health at or below zero ends the game without another action prompt or a chance to revive through rest.
- Potion use, saving games and additional game mechanics are outside this lab's scope.

## Tasks

1. **Explain before editing.** Map the state variables and game loop. Ask your assistant for a source-grounded explanation; verify its claims. An unused variable is not proof of a missing feature.
2. **Reproduce the reports.** Investigate gold not accumulating, missing inventory items, actions after fatal damage, and resting above maximum health. Capture an observed result or a small controlled check for each.
3. **Repair in small steps.** Predict the change, inspect the proposed diff and recheck behavior. Keep each fix narrow and rerun prior checks.
4. **Improve readability.** Rename unclear variables and extract one useful function. Preserve the verified game behavior; avoid adding classes or unrelated features solely because the assistant proposes them.
5. **Explain your result.** Complete the self-check and a brief reflection with actual prompts, decisions and checks.

Useful first prompt: “Map the game state and control flow from the source. Identify what is known versus uncertain. Do not change code yet.”

## Finish

Use [SELF_CHECK.md](SELF_CHECK.md) for concrete scenarios. You are finished when the agreed behavior works, the code is easier to follow, and you can explain the repairs yourself. Optional: turn the controlled checks into a small standard-library unittest suite.

## Working with your coding assistant

Use either taught tool; this lab does not require two independent builds. Read the task yourself, supply relevant context, ask for one bounded step, inspect the diff and verify the result. Record a few real decisions in [REFLECTION.md](REFLECTION.md). Try an explanation or hypothesis before requesting implementation. Prompt examples are starting points to adapt, not answers to paste blindly.

This is **ungraded practice**. Keep your work and reflection; there is no submission, mandatory time limit or capstone credit. Apply the method separately to your ongoing PromptLab project. A working mini-lab does not replace capstone evidence.
