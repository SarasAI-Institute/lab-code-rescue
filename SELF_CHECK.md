# Code Rescue self-check

These are expected outcomes for your completed work, not claims about the broken starter. Use controlled random values or isolated functions to make checks repeatable. Keep the original starter commit so you can compare behavior.

| Scenario | Expected result |
|---|---|
| Start a fresh process | 100 health, zero gold, empty inventory |
| Win twice with rewards of 10 and 20 | 30 gold and two Potions |
| Rest at 95 health | 100 health |
| Rest at 100 health | Still 100 health |
| Receive enough damage to reach exactly zero | Game ends; no new action prompt |
| Receive enough damage to fall below zero | Game ends; no new action prompt |
| Run from a living monster | No gold or Potion awarded for that encounter |
| Refactor after the fixes | The same scenarios still pass |

If randomness obscures a result, ask how to control it in a test. If your assistant claims a fix works, request the exact scenario that demonstrates it and run that check yourself. Stopping the program manually is not proof that the death condition works.

- [ ] I can explain each state variable and the path through one combat round.
- [ ] I reproduced and repaired all four reported behaviors.
- [ ] I verified the readability refactor did not change the required behavior.
- [ ] My reflection describes real decisions, not a generic claim that AI helped.
