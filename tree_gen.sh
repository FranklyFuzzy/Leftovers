#!/bin/bash

#=============================================================================
# Folder Tree Generator
#
# This script generates a visually appealing folder tree for a given directory.
#=============================================================================

# --- Configuration ---
# The target directory. If not provided, the script uses the current directory.
TARGET_DIR="${1:-.}"

# --- Dependencies Check ---
if ! command -v tree &>/dev/null; then
    echo "Error: 'tree' command not found. Please install it."
    echo " - On macOS: brew install tree"
    echo " - On Debian/Ubuntu: sudo apt install tree"
    echo " - On Fedora: sudo dnf install tree"
    exit 1
fi

# --- Main Logic ---

echo "Generating folder tree for: $TARGET_DIR"
echo "-------------------------------------------------"

# Use the 'tree' command to generate the folder tree
# -a: All files are listed.
# -I: Exclude patterns from the list.
# -L: Max display depth of the directory tree (optional, can be customized).
if ! tree -a -I 'git|node_modules|__pycache__' "$TARGET_DIR"; then
    echo "Error: Failed to generate folder tree for '$TARGET_DIR'."
    exit 1
fi

echo "-----------------------------------"
echo "Tree generation complete."
