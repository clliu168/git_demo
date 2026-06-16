def build_train_transforms(config: dict) -> list[str]:
    dataset = config["dataset"]
    input_size = dataset["input_size"]
    return [
        f"resize:{input_size}",
        "to_tensor",
        "normalize:cifar10",
    ]


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
