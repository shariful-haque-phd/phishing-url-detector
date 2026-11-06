# Packaging-level fixes (transparent change log)

These source changes were made while preparing public GitHub demonstration packages. No independent benchmark or security review was conducted.

- The training CLI creates its output directory before serializing the trained model.
- This avoids a `FileNotFoundError` when running the bundled README command on a fresh checkout.
- A small locally executed smoke test was captured under `demo/`.

The original README is preserved at `docs/ORIGINAL_README.md`. The original implementation can be compared with the user-provided source archive.
