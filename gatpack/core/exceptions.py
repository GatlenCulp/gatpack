"""Custom exceptions for the gatpack module."""

from __future__ import annotations


class GatPackError(Exception):
    """Base exception for all gatpack errors."""


class ComposeFileNotFoundError(GatPackError):
    """Raised when a compose file cannot be found in the search directories."""


class FileTypeInferenceError(GatPackError):
    """Raised when unable to infer the file type from a file path."""


class UnsupportedConversionError(GatPackError):
    """Raised when trying to convert between unsupported file types."""


class MultipleComposeFilesError(GatPackError):
    """Raised when multiple compose files are found and no selection is made."""
