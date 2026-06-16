# Baseline Run

- Source notebook: `ResNet-18-with-data-augmentation.ipynb`
- Config: `configs/baseline.yaml`
- CLI command: `python3 -m src.train --config configs/baseline.yaml`
- Seed: 42
- Dataset: CIFAR-10
- Transform recipe: resize, tensor conversion, normalization
- Smoke-demo validation accuracy: 0.842

This is a deterministic teaching result. The goal is to practice Git/GitHub workflow, not to benchmark the model.
