from pathlib import Path


def _parse_scalar(value: str):
    if value in {"true", "false"}:
        return value == "true"
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def load_config(path: str | Path) -> dict:
    """Load the small YAML subset used by the CLI teaching demo."""
    config: dict = {}
    stack: list[tuple[int, dict]] = [(-1, config)]

    for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        key, _, raw_value = raw_line.strip().partition(":")
        value = raw_value.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]
        if value:
            parent[key] = _parse_scalar(value)
        else:
            parent[key] = {}
            stack.append((indent, parent[key]))

    return config
