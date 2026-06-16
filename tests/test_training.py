import unittest

from src.config import load_config
from src.data import build_eval_transforms, build_train_transforms
from src.train import simulate_validation_accuracy


class TrainingTest(unittest.TestCase):
    def test_baseline_transform_recipe(self):
        config = load_config("configs/baseline.yaml")

        self.assertEqual(build_train_transforms(config), ["resize:32", "to_tensor", "normalize:cifar10"])
        self.assertEqual(build_eval_transforms(config), ["resize:32", "to_tensor", "normalize:cifar10"])

    def test_baseline_metric_is_deterministic(self):
        config = load_config("configs/baseline.yaml")
        self.assertEqual(simulate_validation_accuracy(config), 0.842)

    def test_augmentation_branch_changes_training_recipe_only(self):
        config = load_config("configs/augmentation.yaml")

        self.assertEqual(
            build_train_transforms(config),
            [
                "horizontal_flip:p=0.5",
                "random_crop:32:padding=4",
                "resize:32",
                "to_tensor",
                "normalize:cifar10",
            ],
        )
        self.assertEqual(build_eval_transforms(config), ["resize:32", "to_tensor", "normalize:cifar10"])
        self.assertEqual(simulate_validation_accuracy(config), 0.871)


if __name__ == "__main__":
    unittest.main()
