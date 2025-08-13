import os

def generate_vault_tree(vault_path, ignore_folders=None, indent_char='|------ '):
    """
    Generates a visual tree structure of an Obsidian vault.

    Args:
        vault_path (str): The absolute path to the root of your Obsidian vault.
        ignore_folders (list, optional): A list of folder names to ignore.
                                         Defaults to ['.obsidian'].
        indent_char (str, optional): The character string used for indentation.
                                     Defaults to '|------ '.

    Returns:
        str: A string representing the vault's directory tree.
    """
    if ignore_folders is None:
        ignore_folders = ['.obsidian'] # Common Obsidian hidden folder

    tree_lines = [] # Stores lines of the tree output

    # Recursive helper function to traverse directories
    def build_tree(current_path, current_indent=''):
        # Get all entries (files and directories) in the current path
        entries = os.listdir(current_path)

        # Separate directories and files for custom sorting
        dirs = []
        files = []
        for entry in entries:
            # Ignore specified folders
            if os.path.isdir(os.path.join(current_path, entry)):
                if entry not in ignore_folders:
                    dirs.append(entry)
            else:
                files.append(entry)

        # Custom sorting:
        # Prioritize entries starting with '_' to appear at the top.
        # Then sort alphabetically.
        def custom_sort_key(item):
            if item.startswith('_'):
                return (0, item.lower()) # Sorts these first
            return (1, item.lower())     # Then sorts others

        dirs.sort(key=custom_sort_key)
        files.sort(key=custom_sort_key)

        # Add files to the tree lines
        for f_name in files:
            tree_lines.append(f"{current_indent}{indent_char}{f_name}")

        # Recursively call for subdirectories
        for d_name in dirs:
            tree_lines.append(f"{current_indent}{indent_char}{d_name}/")
            # Calculate new indent for subdirectories
            new_indent = current_indent + '|      '
            build_tree(os.path.join(current_path, d_name), new_indent)

    # Start the tree building from the vault root
    tree_lines.append(f"{os.path.basename(vault_path)}/") # Add root folder name
    build_tree(vault_path, '') # Start recursion with empty indent

    return "\n".join(tree_lines)

# --- How to use the script ---
if __name__ == "__main__":
    # IMPORTANT: Replace this with the actual path to your Obsidian vault!
    # Example: C:\\Users\\YourUser\\Documents\\MyObsidianVault
    # Example: /Users/YourUser/Documents/MyObsidianVault
    vault_root_directory = "/Users/name/Documents/folder" # <--- EDIT THIS LINE

    # Check if the path exists
    if not os.path.isdir(vault_root_directory):
        print(f"Error: Vault path '{vault_root_directory}' does not exist or is not a directory.")
        print("Please edit the 'vault_root_directory' variable in the script to your actual vault path.")
    else:
        print(f"Generating tree for vault: {vault_root_directory}\n")
        vault_tree = generate_vault_tree(vault_root_directory)
        print(vault_tree)
        print("\n--- Tree generation complete ---")
        print("Copy and paste the output into a Markdown file in your vault!")
