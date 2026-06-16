# ResNet-18 CIFAR-10 CLI Demo

This repository is the CLI companion for the Git/GitHub lecture deck.

It is derived from the notebook:

`/Users/jacky/project/Deep-Learning-with-PyTorch/Materials/Week6_Modern_CNN_Models/ResNet-18-with-data-augmentation.ipynb`

The notebook remains useful for model teaching and visualization. This repository is for Git/GitHub teaching: clean diffs, focused commits, CLI commands, and reviewable pull requests.

## Repository idea

- `main` contains a ResNet-18/CIFAR-10 baseline recipe.
- `exp/data-augmentation` adds a data augmentation experiment.
- The CLI prints deterministic smoke-demo metrics, so the Git demo does not depend on GPU availability or a long training run.

## Baseline CLI

```bash
python3 -m src.train --config configs/baseline.yaml
python3 -m src.evaluate --config configs/baseline.yaml
python3 -m unittest discover -s tests
```

## Git workflow demo

Start from `main`:

```bash
git status
git log --oneline --graph --decorate --all
python3 -m src.train --config configs/baseline.yaml
```

Inspect the experiment branch:

```bash
git branch -a
git switch exp/data-augmentation
git diff main..HEAD
python3 -m src.train --config configs/augmentation.yaml
cat experiments/data-augmentation.md
```

Return to the stable baseline:

```bash
git switch main
```

## Teaching point

The PR is easy to review because the important changes are split across:

- `configs/augmentation.yaml`
- `src/data.py`
- `src/train.py`
- `tests/test_training.py`
- `experiments/data-augmentation.md`

That is much cleaner than reviewing a full notebook JSON diff.
