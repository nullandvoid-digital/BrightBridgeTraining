import tomllib
import os


def toml_to_py():
    with open("rubric.py", "w") as f:
        with open("rubric.toml", "rb") as d:
            data = tomllib.load(d)
            for k, v in data.items():
                f.write(f"# {k.upper()}\n")
                for k, v in v.items():
                    f.write(f"{k.upper()} = {v}\n")


if __name__ == "__main__":
    toml_to_py()
