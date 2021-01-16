# Check

An Interactive, Proximity Based Spell Checker

## Development Goal

- Develop a spell checker that makes suggestions purely based on the assumption that the user mistyped a key close to the intended key
- Define proximity as the distance from the mistyped key to a potential nearby key
- Create a recursive user interface
- Rebuild data files only when needed

## Specifications

- Distill modules into four different files: main file, class building file, file manager, and UI helpers
- Center class development around a pickle/jar design format
- Ensure spell checking engine to be flexible and offer domain-specific (proximity based) suggestions
