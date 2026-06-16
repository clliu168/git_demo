import unittest

from src.config import load_config


class ConfigTest(unittest.TestCase):
    def test_loads_baseline_config(self):
        config = load_config("configs/baseline.yaml")

        self.assertEqual(config["project"], "resnet18-cifar10-cli-demo")
        self.assertEqual(config["dataset"]["name"], "CIFAR-10")
        self.assertEqual(config["model"]["name"], "ResNet-18")
        self.assertFalse(config["augmentation"]["enabled"])


if __name__ == "__main__":
    unittest.main()
