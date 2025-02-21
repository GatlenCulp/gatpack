# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

## Development environment setup

> **[?]**
> Proceed to describe how to setup local development environment.
> e.g:

To set up a development environment, please follow these steps:

1. Clone the repo

   ```sh
   git clone https://github.com/GatlenCulp/gatpack
   ```

1. TODO

## Issues and feature requests

You've found a bug in the source code, a mistake in the documentation or maybe you'd like a new feature? You can help us by [submitting an issue on GitHub](https://github.com/GatlenCulp/gatpack/issues). Before you create an issue, make sure to search the issue archive -- your issue may have already been addressed!

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

**Even better: Submit a pull request with a fix or new feature!**

### How to submit a Pull Request

1. Search our repository for open or closed
   [Pull Requests](https://github.com/GatlenCulp/gatpack/pulls)
   that relate to your submission. You don't want to duplicate effort.
1. Fork the project
1. Create your feature branch (`git checkout -b feat/amazing_feature`)
1. Commit your changes (`git commit -m 'feat: add amazing_feature'`) GatPack uses [conventional commits](https://www.conventionalcommits.org), so please follow the specification in your commit messages.
1. Push to the branch (`git push origin feat/amazing_feature`)
1. [Open a Pull Request](https://github.com/GatlenCulp/gatpack/compare?expand=1)

______________________________________________________________________

## Community & Development

### Roadmap

Planned features:

- [x] Change Jinja template delimiters to be LaTeX friendly (Highest priority)

- [x] Fix the actual Jinja LaTeX templates for packet making to look nice

- [ ] Add a padding command that will make sure all PDFs have an even number of pages before merging (that way unrelated documents don't get printed on the front and back side of the same page)

- [x] Better syntax for the CLI (`--from file --to output` syntax is probably a good call. Check out Pandoc and compare)

- [x] Automatically detect `compose.gatpack.json` file and use it as input

- [x] Allow for building workflows within the `compose.gatpack.json` file

- [ ] Allow GatPack to pull from the AirTable readings database automatically to generate both compose file and

- [ ] Make it easier to chain together multiple gatpack calls

- [ ] Footers

Things which won't be implemented but which might be cool:

- [ ] Create a [Custom Pandoc Reader/Writer](https://pandoc.org/custom-readers.html)

See the [open issues](https://github.com/GatlenCulp/gatpack/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/GatlenCulp/gatpack/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)

- [Top Bugs](https://github.com/GatlenCulp/gatpack/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)

- [Newest Bugs](https://github.com/GatlenCulp/gatpack/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

### Support

Reach out to the maintainer at one of the following places:

- [GitHub issues](https://github.com/GatlenCulp/gatpack/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/GatlenCulp)

### Project assistance

If you want to say **thank you** or/and support active development of GatPack:

- Add a [GitHub Star](https://github.com/GatlenCulp/gatpack) to the project.
- Tweet about the GatPack.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make GatPack **better**!

### 04 Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

<details>

<summary>Project Organization</summary>
<br />

```
📁 .
├── ⚙️ .cursorrules                    <- LLM instructions for Cursor IDE
├── 💻 .devcontainer                   <- Devcontainer config
├── ⚙️ .gitattributes                  <- GIT-LFS Setup Configuration
├── 🧑‍💻 .github
│   ├── ⚡️ actions
│   │   └── 📁 setup-python-env       <- Automated python setup w/ uv
│   ├── 💡 ISSUE_TEMPLATE             <- Templates for Raising Issues on GH
│   ├── 💡 pull_request_template.md   <- Template for making GitHub PR
│   └── ⚡️ workflows
│       ├── 🚀 main.yml               <- Automated cross-platform testing w/ uv, precommit, deptry,
│       └── 🚀 on-release-main.yml    <- Automated mkdocs updates
├── 💻 .vscode                        <- Preconfigured extensions, debug profiles, workspaces, and tasks for VSCode/Cursor powerusers
│   ├── 🚀 launch.json
│   ├── ⚙️ settings.json
│   ├── 📋 tasks.json
│   └── ⚙️ 'gatpack.code-workspace'
├── 🐳 docker                            <- Docker configuration for reproducability
├── 📚 docs                              <- Project documentation (using mkdocs)
├── 👩‍⚖️ LICENSE                           <- Open-source license if one is chosen
├── 📋 logs                              <- Preconfigured logging directory for
├── 👷‍♂️ Makefile                          <- Makefile with convenience commands (PyPi publishing, formatting, testing, and more)
├── ⚙️ pyproject.toml                     <- Project configuration file w/ carefully selected dependency stacks
├── 📰 README.md                         <- The top-level README
├── 🔒 secrets                           <- Ignored project-level secrets directory to keep API keys and SSH keys safe and separate from your system (no setting up a new SSH-key in ~/.ssh for every project)
│   └── ⚙️ schema                         <- Clearly outline expected variables
│       ├── ⚙️ example.env
│       └── 🔑 ssh
│           ├── ⚙️ example.config.ssh
│           ├── 🔑 example.something.key
│           └── 🔑 example.something.pub
└── 🚰 'gatpack'  <- Easily publishable source code
    ├── ⚙️ config.py                     <- Store useful variables and configuration (Preset)
    ├── 🐍 dataset.py                    <- Scripts to download or generate data
    ├── 🐍 features.py                   <- Code to create features for modeling
    ├── 📁 modeling
    │   ├── 🐍 __init__.py
    │   ├── 🐍 predict.py               <- Code to run model inference with trained models
    │   └── 🐍 train.py                 <- Code to train models
    └── 🐍 plots.py                     <- Code to create visualizations
```

</details>

### Authors & contributors

The original setup of this repository is by [Gatlen Culp](https://github.com/GatlenCulp).

For a full list of all authors and contributors, see [the contributors page](https://github.com/GatlenCulp/gatpack/contributors).

### Security

GatPack follows good practices of security, but 100% security cannot be assured.
GatPack is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

### License

This project is licensed under the **MIT**.

See [LICENSE](LICENSE) for more information.

### Acknowledgements

- [Cambridge-Boston Alignment Initiative](https://www.cbai.ai/) + [MIT AI Alignment](https://aialignment.mit.edu/) for employing me to work on program logistics which lead me to develop and share this project as a consequence
- Further upstream, [Open Philanthrophy](https://www.openphilanthropy.org/) provides a lot of the funding for CBAI/MAIA
- Other AI Safety Student groups who are doing their best to keep the world safe.
- Thanks to [Samuel Roeca](https://github.com/pappasam) for developing [latexbuild](https://github.com/pappasam/latexbuild), from which some of the LaTeX templating code was borrowed.
- https://github.com/mbr/latex

<!-- TODO: Reach out to Samuel and let him know about this. -->
