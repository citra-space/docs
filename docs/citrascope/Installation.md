---
title: Installation
nav_order: 05
parent: CitraScope
---

# Installation

## System Requirements

CitraScope requires **Python 3.10, 3.11, or 3.12** to run properly.

### Check Your Python Version

Before installing, verify you have a compatible Python version:

```bash
python3 --version
```

If you don't have a compatible version installed, we recommend using [pyenv](https://github.com/pyenv/pyenv) to manage Python versions.

### Installing pyenv

**macOS (Homebrew):**

```bash
brew install pyenv
```

**Linux:** Follow the [pyenv installer](https://github.com/pyenv/pyenv#installation) instructions.

**Windows:** Use [pyenv-win](https://github.com/pyenv-win/pyenv-win). The quickest method is the PowerShell installer described in the [pyenv-win installation docs](https://pyenv-win.github.io/pyenv-win/docs/installation.html).

### Configuring Your Shell

pyenv needs to be initialized in your shell's startup file so that it can manage Python versions.

**Zsh (default on macOS)** -- add the following to `~/.zshrc`:

```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

**Bash** -- add the same lines to `~/.bashrc` (or `~/.bash_profile` on macOS):

```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

**Windows (pyenv-win)** -- ensure the following directories are in your PATH, *before* any other Python installations:

- `%USERPROFILE%\.pyenv\pyenv-win\bin`
- `%USERPROFILE%\.pyenv\pyenv-win\shims`

You may also need to disable the built-in Python app aliases in **Settings > Apps > App Execution Aliases**.

After making shell configuration changes, restart your terminal (or run `exec "$SHELL"` on macOS/Linux) for them to take effect.

### Installing a Python Version

```bash
pyenv install 3.12.0
pyenv local 3.12.0  # Sets Python 3.12.0 for the current directory
```

## Installing CitraScope

We recommend installing CitraScope in a virtual environment to keep dependencies isolated:

```bash
python3 -m venv citrascope-env
source citrascope-env/bin/activate  # On Windows: citrascope-env\Scripts\activate
pip install citrascope
```

### Optional Dependencies

If you're using Linux-based telescope control with INDI, install the additional INDI support:

```bash
pip install citrascope[indi]
```

This provides full integration with the INDI protocol for observatory automation.

## Running CitraScope

Once installed, CitraScope provides a command-line tool to start the daemon:

```bash
citrascope
```

By default, this starts the web interface on `http://localhost:24872` where you can configure your hardware and manage telescope tasking.

### Customizing the Web Interface Port

If you need to run the web interface on a different port:

```bash
citrascope --web-port 8080
```

### Available Commands

To see all available command-line options:

```bash
citrascope --help
```

Once the daemon is running, navigate to the web interface in your browser to complete the setup process and connect your telescope hardware.