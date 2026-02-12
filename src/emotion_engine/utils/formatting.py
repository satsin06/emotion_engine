def format_probs(probs: dict, precision: int = 2) -> str:
    return (
        "{"
        + ", ".join(
            f"'{k}':{round(v, precision)}"
            for k, v in sorted(probs.items(), key=lambda x: -x[1])
        )
        + "}"
    )
