# GatPack Cookie Cutter Repo

This sample project is created by [GatPack](<>), a Python templating tool.

## Setup

```bash
brew install pango
brew install libffi
brew install cairo
brew install gobject-introspection

brew install weasyprint
```

To install GatPack, you will need python installed, then you can run

```bash
pip install gatpack --global
```

Once you are in this directory, run

```bash
gatpack
```

And you will receive a list of print options. You can run the example project with

```bash
gatpack build example-packet
```

## Architecture

There are a few directories:

`{{ cookiecutter.project_name }}`

- `.git`
- `config.gatpack.yaml` -- Define your high-level variables (URLs, workflows, etc.)

```yaml
workflows:
    example-packet:
        inputs:
            - qr-code:
```

<!-- Potentially use Hydra for hierarchical settings? -->

<!-- Should this be JSON to use some kind of schema? -->

<!-- Maybe have some schema be specified per template to be modular. Optionally that is. -->

- `00_assets` -- Define your pre-existing or view rendered PDFs, images, etc.
- `01_templates` -- Define/view your HTML templates with Jinja
- `02_web` -- Your rendered webpages
- `03_pdf` -- Your final resulting packets
