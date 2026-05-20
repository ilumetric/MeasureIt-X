import zipfile
import os
import re
import datetime

# --- Пути: скрипт лежит в корне аддона ---
script_dir = os.path.dirname(os.path.realpath(__file__))
addon_root = script_dir
init_path = os.path.join(addon_root, "__init__.py")
manifest_path = os.path.join(addon_root, "blender_manifest.toml")

# --- Инкремент версии в __init__.py (bl_info) ---
def increment_version_in_init():
    with open(init_path, "r", encoding="utf-8") as f:
        content = f.read()
    version_match = re.search(r"(['\"]version['\"]\s*:\s*\()(.*?)(\))", content, re.DOTALL)
    if not version_match:
        raise ValueError("Не найдена версия в bl_info.")
    version_tuple = version_match.group(2)
    parts = [x.strip() for x in version_tuple.split(",")]
    try:
        last = int(parts[-1]) + 1
        parts[-1] = str(last)
    except Exception as e:
        raise ValueError(f"Ошибка при увеличении версии: {e}")
    new_version = ", ".join(parts)
    new_content = content[:version_match.start(2)] + new_version + content[version_match.end(2):]
    with open(init_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return tuple(parts)

# --- Синхронизация версии в blender_manifest.toml ---
def sync_version_in_manifest(version_parts):
    if not os.path.exists(manifest_path):
        return
    with open(manifest_path, "r", encoding="utf-8") as f:
        content = f.read()
    new_version = ".".join(version_parts)
    new_content, count = re.subn(
        r'(^\s*version\s*=\s*")[^"]*(")',
        lambda m: m.group(1) + new_version + m.group(2),
        content,
        count=1,
        flags=re.MULTILINE,
    )
    if count == 0:
        raise ValueError("Не найдена version в blender_manifest.toml.")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(new_content)

version_parts = increment_version_in_init()
sync_version_in_manifest(version_parts)

def get_addon_name():
    with open(init_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"['\"]name['\"]\s*:\s*['\"]([^'\"]+)['\"]", content)
    if match:
        return match.group(1).replace(' ', '_')
    raise ValueError("Не найдено имя аддона в bl_info.")

# Сборка строки версии: поддержка как 3-кортежа, так и расширенного формата со стадией
stage_letter_map = {'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd'}
if len(version_parts) >= 5:
    stage_letter = stage_letter_map.get(version_parts[3], version_parts[3])
    version_str = f"{version_parts[0]}{version_parts[1]}{version_parts[2]}{stage_letter}{version_parts[4]}"
elif len(version_parts) == 4:
    stage_letter = stage_letter_map.get(version_parts[3], version_parts[3])
    version_str = f"{version_parts[0]}{version_parts[1]}{version_parts[2]}{stage_letter}"
else:
    version_str = f"{version_parts[0]}_{version_parts[1]}_{version_parts[2]}"

addon_name = get_addon_name()

# Формат даты: ДДММГГ
build_date = datetime.datetime.now().strftime("%d%m%y")

zip_name = f"{addon_name}_{version_str}_{build_date}.zip"

exclude_dirs = {
    ".git", ".vscode", "__pycache__", ".mypy_cache",
    "dist", "build", ".idea",
}
exclude_files = {
    "build_zip.py", zip_name,
    ".gitattributes", ".gitignore", ".pylintrc",
    "pyproject.toml",
}
exclude_ext = {".pyc", ".pyo"}

# Имя папки внутри zip = id из манифеста (важно для extension-платформы Blender)
project_dir = "measureit"
parent_dir = os.path.dirname(addon_root)
zip_path = os.path.join(parent_dir, zip_name)

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file in exclude_files:
                continue
            if os.path.splitext(file)[1] in exclude_ext:
                continue
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, path)
            ziph.write(full_path, os.path.join(project_dir, relative_path))

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(addon_root, zipf)

print(f"Создан архив: {zip_path}")
print(f"Версия: {'.'.join(version_parts)}")
