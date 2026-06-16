# Data Augmentation Experiment

- Branch: `exp/data-augmentation`
- Source notebook: `ResNet-18-with-data-augmentation.ipynb`
- Config: `configs/augmentation.yaml`
- CLI command: `python3 -m src.train --config configs/augmentation.yaml`
- Baseline smoke-demo validation accuracy: 0.842
- Experiment smoke-demo validation accuracy: 0.871

## Change summary

- Adds `RandomCrop(32, padding=4)` to the training transform recipe.
- Adds `RandomHorizontalFlip()` to the training transform recipe.
- Keeps evaluation transforms deterministic.
- Adds tests for the augmentation recipe.

## PR review questions

- Does augmentation affect only training data?
- Are validation/test transforms still deterministic?
- Is the experiment evidence recorded?
- Is the diff small enough to review?
