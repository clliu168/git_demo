import argparse

from .config import load_config
from .data import build_eval_transforms, build_train_transforms, describe_dataset
from .model import count_parameters, describe_model


def simulate_validation_accuracy(config: dict) -> float:
    score = 0.836
    if config["dataset"]["input_size"] == 32:
        score += 0.006
    augmentation = config.get("augmentation", {})
    if augmentation.get("enabled", False):
        if augmentation.get("random_crop", False):
            score += 0.018
        if augmentation.get("horizontal_flip", False):
            score += 0.011
    return round(score, 3)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a ResNet-18 CIFAR-10 CLI smoke demo.")
    parser.add_argument("--config", default="configs/baseline.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    accuracy = simulate_validation_accuracy(config)

    print(f"project: {config['project']}")
    print(f"mode: {config['mode']}")
    print(f"seed: {config['seed']}")
    print(f"dataset: {describe_dataset(config)}")
    print(f"model: {describe_model(config)}")
    print(f"parameters: {count_parameters(config):,}")
    print(f"train_transforms: {', '.join(build_train_transforms(config))}")
    print(f"eval_transforms: {', '.join(build_eval_transforms(config))}")
    print(f"epochs: {config['training']['epochs']}")
    print(f"validation_accuracy: {accuracy:.3f}")


if __name__ == "__main__":
    main()
