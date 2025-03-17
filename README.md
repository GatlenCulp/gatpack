<h1 align="center">
  <a href="https://github.com/GatlenCulp/gatpack">
    <img src="https://raw.githubusercontent.com/GatlenCulp/gatpack/main/docs/images/logo.png" alt="Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
  <h1>GatPack</h1>

<a href="#about"><strong>Explore the docs »</strong></a>
<br />
<img src="https://raw.githubusercontent.com/GatlenCulp/gatpack/main/docs/images/gatpack-cli.png" title="Home Page" width="500px">
<br />
<a href="https://github.com/GatlenCulp/gatpack/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
·
<a href="https://github.com/GatlenCulp/gatpack/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
.
<a href="https://github.com//gatpack/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>

</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/GatlenCulp/gatpack?style=flat-square)](LICENSE) [![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/GatlenCulp/gatpack/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) [![code with love by ](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-GatlenCulp-ff1414.svg?style=flat-square)](https://github.com/GatlenCulp)

![Uses the Cookiecutter Data Science project template, GOTem style](https://img.shields.io/badge/GOTem-Project%20Instance-328F97?logo=cookiecutter) ![PyPI - Version](https://img.shields.io/pypi/v/gatpack?style=flat) [![tests](https://github.com/GatlenCulp/gatlens-opinionated-template/actions/workflows/tests.yml/badge.svg)](https://github.com/GatlenCulp/gatpack/actions/workflows/tests.yml) [![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv) ![GitHub stars](https://img.shields.io/github/stars/gatlenculp/gatpack?style=social)

<h3>⚡️ Quick Install</h3>

```bash
curl -LsSf https://raw.githubusercontent.com/GatlenCulp/gatpack/main/install.sh | sh
```

</div>

______________________________________________________________________

## About

GatPack is a CLI and Python API for automating LaTeX and PDF document generation using [Jinja templating](https://jinja.palletsprojects.com/en/stable/api/). This was originally developed for creating professional looking packets for AI safety coursework at [MIT AI Alignment](https://aialignment.mit.edu).

<details>
<summary>Screenshots</summary>
<br>

|                                                               CLI                                                                |                                                       Generated Cover Page                                                       |                                                         Pre-Rendered Cover Page                                                          |
| :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://raw.githubusercontent.com/GatlenCulp/gatpack/main/docs/images/gatpack-cli.png" title="Home Page" width="100%"> | <img src="https://raw.githubusercontent.com/GatlenCulp/gatpack/main/docs/images/cover-page.png" title="Login Page" width="100%"> | <img src="https://raw.githubusercontent.com/GatlenCulp/gatpack/main/docs/images/latex-jinja-pretty.png" title="Login Page" width="100%"> |

</details>

<details>
<summary>Built With</summary>
<br>

- Typer (For the CLI)
- LaTeX (For creating documents from text)
- Jinja (For templating and placeholders)
- Pydantic (For specifying the config file schema)

</details>

<details>
<summary>See who is using</summary>
<br>

- [MIT AI Alignment (MAIA)](https://aialignment.mit.edu/)
- [AI Safety Student Team (AISST)](https://haist.ai/) at Harvard
- [Columbia AI Alignment Club (CAIAC)](https://www.cualignment.org/)

Let us know if your team is using it an how!

</details>

<details>
<summary>Table of Contents</summary>
<br>

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [About](#about)
- [Getting Started](#getting-started)
  - [00 Requirements](#00-requirements)
  - [01 Install GatPack](#01-install-gatpack)
  - [02 Initialize your project (`gatpack init`)](#02-initialize-your-project-gatpack-init)
  - [03 Build the Example project](#03-build-the-example-project)
- [Usage](#usage)
  - [01 CLI Help](#01-cli-help)
  - [02 LaTeX-Modified Jinja](#02-latex-modified-jinja)
  - [04 Going Beyond LaTeX & PDFs](#04-going-beyond-latex--pdfs)
  - [05 Understand the Compose File (`compose.gatpack.json`)](#05-understand-the-compose-file-composegatpackjson)
    - [05.01 The `context` object](#0501-the-context-object)
    - [05.02 The `pipelines` list](#0502-the-pipelines-list)

<!-- /code_chunk_output -->

</details>

______________________________________________________________________

## Getting Started

_Note: Parts 00 and 01 can be skipped if the quick install above worked._

### 00 Requirements

- LaTeX (`pdflatex` specifically, see more instructions on installing below)
- Python 3.10+
- Text Editor (Ex: VSCode)

<details>
<summary><b>Installing Requirements</b></summary>
<br />

**00.01 installing python**

Python can be installed from the [Python downloads page](https://www.python.org/downloads/), or if you have `brew` on macOS:

```bash
brew install python
```

**00.02 pdflatex requirement**

To use `gatpack build` which will convert a LaTeX document to a PDF, you will need `pdflatex` to be available on your path. You can check for this with

```bash
pdflatex --verison
```

If this command isn't found, then you need to install a LaTeX compiler to your machine.

For mac you can install [MacTeX](https://www.tug.org/mactex/mactex-download.html). Using Homebrew:

```bash
brew install --cask mactex
```

_Note: Eventually this LaTeX requirement will be removed_

<!-- I should take a look at this: https://pypi.org/project/pdflatex/ -->

**00.03 text editor requirement**

Any text editor will do but you should probably choose something with JSON syntax highlighting such as VSCode.

<br />
</details>

### 01 Install GatPack

[Gatpack is a Python package](https://pypi.org/project/gatpack/) that can easily be installed from your favorite package manager

**Using uv (Recommended)**

[uv](https://docs.astral.sh/uv/getting-started/installation/) is a fast, reliable Python package installer and resolver:

```bash
uv tool install gatpack
```

_Note: Make sure you run `uv tool update-shell`, otherwise uv tools won't be in your PATH_

<details>
<summary><b>Alternative Installation Methods</b></summary>
<br>

**Using pipx**

Ideal for CLI applications that you want isolated from your system:

```bash
pipx install gatpack
```

**Using pip with a virtual environment**

```bash
# Create and activate a virtual environment first
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Then install within the virtual environment
pip install gatpack
```

**Using conda**

```bash
# Create a conda environment
conda create -n gatpack-env python=3.12
conda activate gatpack-env

# Install gatpack
pip install gatpack
```

</details>

You can verify the installation by running:

```bash
gatpack --help
```

### 02 Initialize your project (`gatpack init`)

cd into the directory you would like to create your example project [(source code)](https://github.com/GatlenCulp/cookiecutter-gatpack) and run:

```bash
gatpack init
```

### 03 Build the Example project

The example compose file comes with one preset pipeline called `reading-packet` which contains the instructions to build a packet with a cover, readings, and a final page with additional readings.

```bash
gatpack compose reading-packet --overwrite
```

When finished, you should have an `output/output.pdf` file.

______________________________________________________________________

## Usage

### 01 CLI Help

The CLI commands are NOT documented in any dedicated page. Instead commands are documented from within the CLI itself. `gatpack --help` will provide usage information. `gatpack COMMAND --help` will provide usage information on subcommands.

![GatPack CLI](docs/images/gatpack-cli.png)

<!-- <img src="docs/images/gatpack-cli.png" title="Home Page" width="500px"> -->

### 02 LaTeX-Modified Jinja

The [Jinja placeholders for LaTeX were modified](https://jinja.palletsprojects.com/en/stable/templates/#line-statements) to ensure compatability and a good user experience:

| Function                                                                                                             | LaTeX-Modified              | Standard                  | Usage                                    |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------- | ---------------------------------------- |
| [Expresssions & Variables](https://jinja.palletsprojects.com/en/stable/templates/#variables)                         | `\VAR{variable_name}`       | `{{ variable_name }}`     | Insert a variable value                  |
| [Statements & Control Structures](https://jinja.palletsprojects.com/en/stable/templates/#list-of-control-structures) | `\BLOCK{for item in items}` | `{% for item in items %}` | Control structures (loops, conditionals) |
| [Comments](https://jinja.palletsprojects.com/en/stable/templates/#comments)                                          | `\#{comment text}`          | `{# comment text #}`      | Add template comments                    |
| [Line Statements](https://jinja.palletsprojects.com/en/stable/templates/#comments)                                   | `%-`                        | `#`                       | Single line statements                   |
| [Line Comment](https://jinja.palletsprojects.com/en/stable/templates/#line-statements)                               | `%#`                        | `##`                      | Single line comments                     |

[See the Jinja API for more information](https://jinja.palletsprojects.com/en/stable/api/). Apart from the delimeter syntax, everything should work the same. These placeholders will be filled in with variable assignments made from your `compose.gatpack.json`'s `context` object when you run `gatpack infer` (ex: `gatpack infer --from example.jinja.tex --to example.tex`).

<details>
<summary> Why this Modification is Needed </summary>
<br />

Standard Jinja placeholders: `{{ variable_name }}`, `{% for item in items %} {% endfor %}`, etc. don't play well with LaTeX. It becomes very difficult to view your LaTeX template since you run into syntax errors and some LaTeX syntax conflicts with Jinja tags, leading to errors from both systems.

<div style="display: flex; gap: 20px; align-items: center;">
    <div>
        <p><strong>Standard Jinja:</strong></p>
        <img src="https://raw.githubusercontent.com/GatlenCulp/gatpack/main/docs/images/latex-jinja-ugly.png" title="Ugly Latex Jinja" width="300px">
    </div>
    <div>
        <p><strong>LaTeX-Adapted Jinja:</strong></p>
        <img src="https://raw.githubusercontent.com/GatlenCulp/gatpack/main/docs/images/latex-jinja-pretty.png" title="Pretty Latex Jinja" width="300px">
    </div>
</div>

The Jinja placeholders above are meant to fix this issue.

</details>

<details>

<summary>Get placeholder highlighting in your LaTeX document </summary>
</br>

```tex
% Define Jinja placeholder commands for better editor visualization
\usepackage{xcolor}
\definecolor{jinjaColor}{HTML}{7B68EE}  % Medium slate blue color for Jinja
\definecolor{jinjaVarBg}{HTML}{E6E6FA}    % Light lavender for variables
\definecolor{jinjaBlockBg}{HTML}{FFE4E1}  % Misty rose for blocks
\definecolor{jinjaCommentBg}{HTML}{E0FFFF}  % Light cyan for comments
\newcommand{\VAR}[1]{\colorbox{jinjaVarBg}{\detokenize{#1}}}
\newcommand{\BLOCK}[1]{\colorbox{jinjaBlockBg}{\detokenize{#1}}}
\newcommand{\COMMENT}[1]{\colorbox{jinjaCommentBg}{\detokenize{#1}}}
```

</details>

<!-- ### 03 Usage Examples

- You want to combine multiple files into a packet: `pdfs/document1.pdf`, `pdfs/document2.pdf`, and `pdfs/document3.pdf`. This makes printing and stapling multiple copies easier: `gatpack combine pdfs/*.pdf packet.pdf`

- You want to build and reuse a LaTeX template for an invoice: `invoice.jinja.tex`. To do this, render your template using Jinja placeholders into `invoice.tex` using the assignments from `compose.gatpack.json` then build your invoice to a pdf `invoice.pdf`:

  ```bash
  gatpack --from invoice.jinja.tex --to invoice.pdf
  ``` -->

### 04 Going Beyond LaTeX & PDFs

If you need more than just LaTeX and PDFs, it's recommended that you check out [pandoc](https://pandoc.org/index.html) -- a software that can convert most files from one format to another (Ex: LaTeX to Markdown, HTML, etc.). It of course doesn't work quite as well as natively writing the document in that language, but I generally recommend it.

### 05 Understand the Compose File (`compose.gatpack.json`)

Here is the `compose.gatpack.json` file that comes with the sample `gatpack init` project:

```json
{
  "$schema": "https://raw.githubusercontent.com/GatlenCulp/gatpack/refs/heads/feature/compose-actions/gatpack/schema/json/GatPackCompose.schema.json",
  "name": "Intro Fellowship Reading Packet",
  "description": "Packet for CAIAC's Spring 2025 Intro Fellowship",
  "version": "1.0",
  "context": {
    "program_long_name": "Intro Fellowship",
    "time_period": "Spring 2025",
    "chron_info": "WEEK 0",
    "title": "Introduction to machine learning",
    "subtitle": "READINGS",
    "primary_color": "0B0D63",
    "primary_color_faded": "789BD6",
    "core_readings": [
      {
        "title": "Neural Networks",
        "read_on_device": true,
        "subsection": "Chapters 1-6",
        "author": "3Blue1Brown",
        "year": 2024,
        "url": "https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&feature=shared",
        "thumbnail_path": ""
      }
    ],
    "further_readings": [
      {
        "title": "A short introduction to machine learning",
        "subsection": "",
        "author": "Ngo",
        "year": 2021,
        "url": "https://www.alignmentforum.org/posts/qE73pqxAZmeACsAdF/a-short-introduction-to-machine-learning",
        "thumbnail_path": ""
      },
      // ... More readings
      {
        "title": "A (long) peek into reinforcement learning",
        "subsection": "",
        "author": "Weng",
        "year": 2018,
        "url": "https://lilianweng.github.io/posts/2018-02-19-rl-overview/",
        "thumbnail_path": ""
      }
    ]
  },
  "pipelines": [
    {
      "description": "Create the full reading packet.",
      "id": "reading-packet",
      "steps": [
        {
          "name": "Render cover page",
          "from": "cover/cover.jinja.tex",
          "to": "cover/cover.pdf"
        },
        // ... More Steps ...
        {
          "name": "Combine all readings into packet.pdf",
          "combine": [
            "cover/cover.pdf",
            "device_readings/device_readings.pdf",
            "further_readings/further_readings.pdf"
          ],
          "to": "output/packet.pdf"
        }
      ]
    }
  ]
}
```

#### 05.01 The `context` object

The `context` object contains variable assignments used to fill in Jinja placeholders.

```json
"context": {
  "program_long_name": "Intro Fellowship",
  "time_period": "Spring 2025",
  "chron_info": "WEEK 0",
  "title": "Introduction to machine learning",
  "subtitle": "READINGS",
  "primary_color": "0B0D63",
  "primary_color_faded": "789BD6",
  // ...
}
```

#### 05.02 The `pipelines` list

The `pipelines` list contains sequential steps. Each `pipeline` requires and is referred to by an `id` key

```json
"pipelines": [
  {
    // Required ID to refer to the pipeline
    "id": "reading-packet",
    // Optional description
    "description": "Create the full reading packet.",
    // Steps that define the pipeline operations
    "steps": [
      {
        "name": "Render cover page",
        "from": "cover/cover.jinja.tex",
        "to": "cover/cover.pdf"
      },
      //... More pipeline steps ...,
      {
        "name": "Combine all readings into packet.pdf",
        "combine": [
          "cover/cover.pdf",
          "device_readings/device_readings.pdf",
          "further_readings/further_readings.pdf"
        ],
        "to": "output/packet.pdf"
      }
    ]
  }
]
```

Additionally, `pipelines` defines a single `pipeline`: a sequential set of steps to perform for some operation. Running `gatpack compose` in the same directory as your `compose.gatpack.json` file will show all available pipelines.

Each step in a pipeline must contain a `name` key. The only two operations supported in steps now are: `gatpack infer` and `gatpack combine`

```json
// Gatpack Infer Example Step
{
  "name": "Render cover page",
  // File to convert (*.tex or *.jinja.tex file)
  "from": "cover/cover.jinja.tex",
  // File to save to
  "to": "cover/cover.pdf"
}
```

```json
// Gatpack Combine Example Step
{
  "name": "Combine all readings into packet.pdf",
  // List of PDFs to combine
  "combine": [
    "cover/cover.pdf",
    "device_readings/device_readings.pdf",
    "further_readings/further_readings.pdf"
  ],
  // Location to save combined PDF to
  "to": "output/packet.pdf"
}
```
