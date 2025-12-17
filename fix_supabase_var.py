import re
import shutil
import os

file_path = r'c:\_working\Projetos\ControleAvLockWeb\index.html'
backup_path = r'c:\_working\Projetos\ControleAvLockWeb\index_backup.html'

try:
    shutil.copy2(file_path, backup_path)
    print(f"Backup created at {backup_path}")
except Exception as e:
    print(f"Backup failed: {e}")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replacement(match):
    prefix = match.group(1)
    if prefix:
        return match.group(0) # Return unchanged
    return 'supabaseClient'

# Regex to match 'supabase' but check for specific prefixes
# Prefixes to preserve: window. @ / . " ' -
pattern = r'(window\.|@|\/|\.|"|\'|-)?\bsupabase\b'

new_content = re.sub(pattern, replacement, content)

# Verify change
if new_content == content:
    print("No changes made.")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("File updated successfully.")
