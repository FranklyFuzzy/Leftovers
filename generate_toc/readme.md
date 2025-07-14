# Markdown TOC Generator

A Python script to automatically generate a Table of Contents (TOC) from the headers of a Markdown (`.md`) file. The TOC follows GitHub/Obsidian-style anchor link formatting and supports headers from `#` to `#####`.

## Features

- Parses headers up to level 5 (`#####`)
- Outputs properly indented TOC with anchor links
- Compatible with GitHub and Obsidian Markdown rendering
- Outputs a new file named `<original>_TOC.md` in the same directory

## Example

Given the following Markdown content:

```markdown
# Introduction
## Getting Started
### Installation
```
