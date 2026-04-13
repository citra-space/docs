# Citra Space Documentation

This repository contains the documentation for [Citra Space](https://app.citra.space), a platform providing modular sensing and software solutions for detecting, tracking, and identifying orbiting objects.

## View the Documentation

Visit the live documentation site: [https://citra-space.github.io/docs](https://citra-space.github.io/docs) (or your GitHub Pages URL)

## About This Repository

This documentation site is built using Jekyll and the [just-the-docs](https://github.com/just-the-docs/just-the-docs) theme, hosted on GitHub Pages.

## Contributing

We welcome contributions to improve our documentation! If you find errors or have suggestions:

1. Fork this repository
2. Make your changes
3. Update the version in docs/_config.yml to bust the cache.
4. Submit a pull request

For questions or support, join our [Discord server](https://discord.gg/STgJQkWe9y).

## Local Development

### Prerequisites (macOS)

macOS ships with an outdated system Ruby that won't work. Install a modern version using rbenv:

```bash
# Install rbenv and certificates
brew install rbenv ca-certificates

# Add to your shell config (restart terminal or run 'source ~/.zshrc' after)
echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
echo 'export SSL_CERT_FILE=$(brew --prefix ca-certificates)/share/ca-certificates/cacert.pem' >> ~/.zshrc
source ~/.zshrc

# Install and set Ruby version
rbenv install 3.2.2
rbenv global 3.2.2

# Install bundler
gem install bundler
```

### Run locally

```bash
# Navigate to the docs directory
cd docs

# Install dependencies
bundle install

# Serve the site locally
bundle exec jekyll serve

# View at http://localhost:4000
```

## Screenshot Tool

The repo includes a Playwright-based tool for capturing screenshots of web UIs (e.g., the CitraScope dashboard) for use in documentation.

### Setup

```bash
pip install -r requirements.txt
playwright install chromium
```

### Usage

`scripts/screenshots/capture.py` captures a screenshot of a specific UI element:

```bash
python scripts/screenshots/capture.py \
  --url "http://localhost:24872/#monitoring" \
  --selector "#globalStatusBar" \
  --output "docs/citrascope/img/status-bar.png" \
  --wait-for "#globalStatusBar"
```

See `.cursor/skills/citrascope-screenshots/SKILL.md` for the full selector catalog, navigation patterns, and example invocations for CitraScope.

## Links

- **Citra Space App**: https://app.citra.space
- **API Documentation**: https://api.citra.space/docs
- **Website**: https://citra.space
- **Discord Community**: https://discord.gg/STgJQkWe9y
- **GitHub Organization**: https://github.com/citra-space
