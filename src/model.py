def describe_model(config: dict) -> str:
    model = config["model"]
    return f"{model['name']} stem={model['stem']} blocks={model['blocks']}"


def count_parameters(config: dict) -> int:
    # A compact teaching approximation for ResNet-18 on CIFAR-10.
    return 11_180_000 if config["model"]["stem"] == "cifar10" else 11_690_000
