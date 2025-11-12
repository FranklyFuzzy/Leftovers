import os
import re
import sys

def slugify(text):
    """Convert header text to GitHub/Obsidian-style anchor link."""
    anchor = text.strip().lower()
    anchor = re.sub(r'[^\w\- ]+', '', anchor)  # Remove non-word characters
    anchor = anchor.replace(' ', '-')          # Replace spaces with dashes
    return anchor

def generate_toc(md_lines, max_level=5):
    toc_lines = []
    for line in md_lines:
        match = re.match(r'^(#{1,5})\s+(.*)', line)
        if match:
            level = len(match.group(1))
            if level > max_level:
                continue
            title = match.group(2).strip()
            anchor = slugify(title)
            indent = '    ' * (level - 1)
            toc_lines.append(f"{indent}- [{title}](#{anchor})")
    return toc_lines

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_toc.py <markdown_file>")
        return

    input_path = sys.argv[1]
    if not input_path.endswith(".md"):
        print("Error: File must have a .md extension")
        return

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        toc = generate_toc(lines)

        output_path = os.path.splitext(input_path)[0] + "_TOC.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(toc))

        print(f"TOC written to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
