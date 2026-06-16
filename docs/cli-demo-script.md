# CLI Demo Script

This script is aligned with the Beamer deck.

## 1. Start on main

```bash
cd /Users/jacky/project/git_and_github/resnet18-cifar10-cli-demo
git switch main
git status
git log --oneline --graph --decorate --all
python3 -m src.train --config configs/baseline.yaml
python3 -m unittest discover -s tests
```

Teaching point: `main` is the stable baseline recipe.

## 2. Inspect the experiment branch

```bash
git branch -a
git switch exp/data-augmentation
git diff main..HEAD -- configs/augmentation.yaml src/data.py src/train.py tests/test_training.py
python3 -m src.train --config configs/augmentation.yaml
cat experiments/data-augmentation.md
```

Teaching point: a PR should be a focused, reviewable change.

## 3. Return to main

```bash
git switch main
```
