def build_train_transforms(config: dict) -> list[str]:
    dataset = config["dataset"]
    input_size = dataset["input_size"]
    transforms = [
        f"resize:{input_size}",
        "to_tensor",
        "normalize:cifar10",
    ]

    augmentation = config.get("augmentation", {})
    if augmentation.get("enabled", False):
        if augmentation.get("random_crop", False):
            transforms.insert(0, f"random_crop:{input_size}:padding={augmentation['crop_padding']}")
        if augmentation.get("horizontal_flip", False):
            transforms.insert(0, "horizontal_flip:p=0.5")

    return transforms


def build_eval_transforms(config: dict) -> list[str]:
    dataset = config["dataset"]
    input_size = dataset["input_size"]
    return [
        f"resize:{input_size}",
        "to_tensor",
        "normalize:cifar10",
    ]


def describe_dataset(config: dict) -> str:
    dataset = config["dataset"]
    train_pct = int(dataset["train_split"] * 100)
    val_pct = 100 - train_pct
    return f"{dataset['name']} {dataset['input_size']}x{dataset['input_size']} split {train_pct}/{val_pct}"
