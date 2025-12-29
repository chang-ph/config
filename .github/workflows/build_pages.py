import json
import os
from pathlib import Path

import yaml

BUILD_OUTPUT_FOLDER = os.environ["BUILD_OUTPUT_FOLDER"]
project_root = Path(__file__).parent.parent.parent


def main():
    os.makedirs(project_root / BUILD_OUTPUT_FOLDER)
    for file in Path(project_root).glob("*-coinfer-ai.yaml"):
        if not file.is_file():
            continue
        config = yaml.safe_load(file.read_text())
        json_str = json.dumps(config)
        (Path(BUILD_OUTPUT_FOLDER) / file.with_suffix(".json").name).write_text(
            json_str
        )


if __name__ == "__main__":
    main()
