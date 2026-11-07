import shutil
import pathlib
import sys

def main():
    src = pathlib.Path("integrations/VulnClaw/vulnclaw/skills/specialized")
    if not src.exists():
        print(f"Error: {src} no existe")
        sys.exit(1)

    home = pathlib.Path.home()
    destinations = [
        home / ".agents" / "skills",
        home / ".claude" / "skills"
    ]

    for d in destinations:
        d.mkdir(parents=True, exist_ok=True)

    count = 0
    for skill_dir in src.iterdir():
        if skill_dir.is_dir():
            for d in destinations:
                dest_skill = d / skill_dir.name
                shutil.copytree(skill_dir, dest_skill, dirs_exist_ok=True)
            count += 1

    print(f"Exito: {count} skills especializadas copiadas a ~/.agents/skills y ~/.claude/skills")

if __name__ == "__main__":
    main()

