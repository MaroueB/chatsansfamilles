from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
PARRAINAGE_DIR = ROOT / "parrainage"
AVAILABLE_DIR = PARRAINAGE_DIR / "a-parrainer"
SPONSORED_DIR = PARRAINAGE_DIR / "parraines"
INDEX_FILE = ROOT / "index.html"
EMAIL = "chatsansfamilles@orange.fr"
START_MARKER = "<!-- SPONSORSHIP-CARDS:START -->"
END_MARKER = "<!-- SPONSORSHIP-CARDS:END -->"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def display_name(image_path: Path) -> str:
    return re.sub(r"\s+", " ", image_path.stem.replace("_", " ")).strip()


def image_files(folder: Path) -> list[Path]:
    folder.mkdir(parents=True, exist_ok=True)
    return sorted(
        (
            path
            for path in folder.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
        ),
        key=lambda path: display_name(path).casefold(),
    )


def render_card(image_path: Path, sponsored: bool) -> list[str]:
    name = display_name(image_path)
    safe_name = html.escape(name)
    image_url = quote(image_path.relative_to(ROOT).as_posix(), safe="/")
    status_class = "is-sponsored" if sponsored else "is-available"
    status = (
        "Je suis déjà parrainé ! 🩷"
        if sponsored
        else "😺 Et si vous me parrainiez ?"
    )

    lines = [
        f'<article class="sponsorship-cat {status_class}">',
        '  <div class="sponsorship-cat-content">',
        f'    <img src="{image_url}" alt="Portrait de {safe_name}">',
        f'    <span class="sponsorship-cat-name">{safe_name}</span>',
        f'    <span class="sponsorship-cat-status {status_class}">'
        f'{status}</span>',
    ]

    if not sponsored:
        subject = quote(f"Parrainage de {name}", safe="")
        lines.append(
            f'    <a class="sponsorship-cat-action" '
            f'href="mailto:{EMAIL}?subject={subject}">'
            'Écrivez-moi ! '
            '<span aria-hidden="true">→</span></a>'
        )
    lines.extend(["  </div>", "</article>"])
    return lines


def generated_cards() -> list[str]:
    available = image_files(AVAILABLE_DIR)
    sponsored = image_files(SPONSORED_DIR)
    if not available and not sponsored:
        raise ValueError(
            "Aucune photo trouvée dans les dossiers de parrainage. "
            "index.html n'a pas été modifié."
        )

    names: set[str] = set()
    cards: list[str] = []
    for image_path, is_sponsored in [
        *((path, False) for path in available),
        *((path, True) for path in sponsored),
    ]:
        name_key = display_name(image_path).casefold()
        if name_key in names:
            name = display_name(image_path)
            raise ValueError(
                f"Le nom « {name} » apparaît dans les deux dossiers. "
                "index.html n'a pas été modifié."
            )
        names.add(name_key)
        cards.extend(render_card(image_path, is_sponsored))
    return cards


def update_index(cards: list[str]) -> bool:
    with INDEX_FILE.open("r", encoding="utf-8", newline="") as index_file:
        content = index_file.read()

    if content.count(START_MARKER) != 1 or content.count(END_MARKER) != 1:
        raise ValueError(
            "Les marqueurs de la galerie sont absents ou en double dans "
            "index.html. "
            "index.html n'a pas été modifié."
        )

    lines = content.splitlines(keepends=True)
    start_index = next(
        i for i, line in enumerate(lines) if START_MARKER in line
    )
    end_index = next(
        i for i, line in enumerate(lines) if END_MARKER in line
    )
    if end_index <= start_index:
        raise ValueError(
            "L'ordre des marqueurs est incorrect. "
            "index.html n'a pas été modifié."
        )

    newline = "\r\n" if "\r\n" in content else "\n"
    start_indent = lines[start_index].partition(START_MARKER)[0]
    replacement = [f"{start_indent}{START_MARKER}{newline}"]
    replacement.extend(f"{start_indent}{line}{newline}" for line in cards)
    replacement.append(f"{start_indent}{END_MARKER}{newline}")

    updated = lines[:start_index] + replacement + lines[end_index + 1:]
    updated_content = "".join(updated)
    if updated_content == content:
        return False

    with INDEX_FILE.open("w", encoding="utf-8", newline="") as index_file:
        index_file.write(updated_content)
    return True


def main() -> int:
    try:
        cards = generated_cards()
        changed = update_index(cards)
    except (OSError, ValueError) as error:
        print(f"Erreur : {error}", file=sys.stderr)
        return 1

    count = sum('class="sponsorship-cat ' in line for line in cards)
    action = "Galerie mise à jour" if changed else "Galerie déjà à jour"
    print(f"{action} : {count} fiche(s) générée(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
