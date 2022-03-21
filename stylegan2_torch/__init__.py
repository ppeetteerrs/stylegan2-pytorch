from contextlib import suppress
from importlib import metadata
from os import system as shell

from stylegan2_torch.discriminator import Discriminator
from stylegan2_torch.equalized_lr import Blur, EqualConv2d, EqualLeakyReLU, EqualLinear
from stylegan2_torch.generator import Generator
from stylegan2_torch.utils import Resolution, default_channels

__author__ = "Peter Yuen"
__email__ = "ppeetteerrsx@gmail.com"
__version__ = "test"
with suppress(Exception):
    __version__ = metadata.version("stylegan2_torch")


__all__ = [
    "Discriminator",
    "Generator",
    "Resolution",
    "default_channels",
    "Blur",
    "EqualConv2d",
    "EqualLeakyReLU",
    "EqualLinear",
]


def __test():  # pragma: no cover
    """
    Runs pytest locally and keeps only `coverage.xml` for GitHub Actions to upload to Codecov.
    """
    shell(
        "pytest --cov=simple_poetry --cov-report xml --cov-report term-missing tests \
            && rm -rf .pytest_cache && rm .coverage"
    )


def __serve():  # pragma: no cover
    """
    Serve local documentation.
    """
    print("serving")
    shell(
        "cp README.md docs/index.md && \
            mkdocs serve"
    )


def __docs():  # pragma: no cover
    """
    Build gh-pages documentation branch.
    """
    shell(
        "cp README.md docs/index.md && \
            mkdocs gh-deploy --force"
    )
