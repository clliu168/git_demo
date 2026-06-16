import argparse

from .config import load_config
from .train import simulate_validation_accuracy


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the CLI smoke-demo recipe.")
    parser.add_argument("--config", default="configs/baseline.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    accuracy = simulate_validation_accuracy(config)
    print(f"accuracy: {accuracy:.3f}")
    print(f"error_rate: {1 - accuracy:.3f}")


if __name__ == "__main__":
    main()
