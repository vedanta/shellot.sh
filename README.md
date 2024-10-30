# Shellot.sh 🐚

A powerful macOS environment backup manager that helps developers maintain consistent development environments across different machines. Shellot.sh makes it easy to backup and restore your entire development environment, including shell configurations, terminal settings, editor preferences, and development tools.

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
  - [Standard Installation](#standard-installation)
  - [Conda Installation](#conda-installation-recommended)
  - [Homebrew Installation](#homebrew-installation)
- [Usage](#-usage)
- [Backup Structure](#-backup-structure)
- [Security](#-security)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## 🌟 Features

### Shell Environment
- Shell configurations (bash, zsh)
- Environment variables
- Custom aliases and functions
- Path configurations

### Terminal Emulators
- Terminal.app settings and profiles
- iTerm2 configurations
  - Color schemes
  - Profiles
  - Key mappings
  - Scripts
  - Dynamic profiles

### Development Tools
- Vim/Neovim
  - Configuration files
  - Plugins
  - Color schemes
  - Custom mappings
- Visual Studio Code
  - User settings
  - Keybindings
  - Snippets
  - Extensions
- Git
  - Global configurations
  - Ignore patterns
  - Attributes
  - SSH keys and config

### Package Managers
- Homebrew
  - Installed formulae
  - Casks
  - Taps
  - Custom configurations
- pyenv
  - Installed versions
  - Global/local versions
  - Version files

### Shell Frameworks
- Oh My Zsh
  - Theme
  - Plugins
  - Custom scripts
  - Completions

## 🚀 Installation

### Prerequisites
- macOS 10.15 or later
- Python 3.9 or later
- Git

### Standard Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shellot.git
cd shellot
```

2. Make the script executable:
```bash
chmod +x shellot.sh
```

3. Install required Python packages:
```bash
pip3 install -r requirements.txt
```

4. (Optional) Add to your PATH:
```bash
echo 'export PATH="$PATH:$HOME/path/to/shellot"' >> ~/.zshrc  # or ~/.bashrc
source ~/.zshrc  # or source ~/.bashrc
```

### Conda Installation (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shellot.git
cd shellot
```

2. Create a new Conda environment:
```bash
# Create environment from environment.yml
conda env create -f environment.yml

# Or create manually
conda create -n shellot python=3.9
conda activate shellot
pip install -r requirements.txt
```

3. Make the script executable:
```bash
chmod +x shellot.sh
```

4. Setup the shell wrapper:
```bash
# Create a shell wrapper to auto-activate conda environment
cat > shellot << EOF
#!/bin/bash
if command -v conda &> /dev/null; then
    eval "\$(conda shell.bash hook)"
    conda activate shellot
fi
\$(dirname "\$0")/shellot.sh "\$@"
EOF

chmod +x shellot
```

5. (Optional) Add to your PATH:
```bash
# For zsh
echo 'export PATH="$PATH:$HOME/path/to/shellot"' >> ~/.zshrc
source ~/.zshrc

# For bash
echo 'export PATH="$PATH:$HOME/path/to/shellot"' >> ~/.bashrc
source ~/.bashrc
```

### Conda Environment Management

Activate the environment:
```bash
conda activate shellot
```

Update dependencies:
```bash
conda env update -f environment.yml
```

Remove the environment:
```bash
conda deactivate
conda env remove -n shellot
```

List all environments:
```bash
conda env list
```

### Homebrew Installation

```bash
brew tap yourusername/shellot
brew install shellot
```

## 📋 Usage

### Basic Commands

Export your current environment:
```bash
shellot.sh export
```

Import settings on another machine:
```bash
shellot.sh import
```

Specify custom backup location:
```bash
shellot.sh export --backup-path ~/my_backups
```

### Advanced Usage

Export specific components:
```bash
shellot.sh export --components shell,vim,vscode
```

Dry run import (shows what would be imported):
```bash
shellot.sh import --dry-run
```

Force import (overwrites existing files):
```bash
shellot.sh import --force
```

## 📂 Backup Structure

The backup will be organized in the following structure:
```
shellot_backup/
├── shellot.json          # Main settings file
├── shell_configs/        # Shell configuration files
│   ├── .zshrc
│   ├── .bashrc
│   └── .profile
├── terminal/            # Terminal.app settings
├── iterm/              # iTerm2 settings
│   ├── profiles.json
│   ├── scripts/
│   └── dynamic_profiles/
├── vim/                # Vim/Neovim settings
│   ├── .vimrc
│   └── .vim/
├── oh-my-zsh/          # Oh My Zsh settings
│   ├── custom/
│   └── themes/
├── homebrew/           # Homebrew packages
│   └── Brewfile
├── ssh/                # SSH configurations
├── git/                # Git settings
├── vscode/            # VS Code settings
│   ├── settings.json
│   ├── keybindings.json
│   └── snippets/
└── pyenv/             # pyenv settings
```

## 🔒 Security

- SSH keys and sensitive configurations are backed up with appropriate permissions
- Private keys maintain their 600 permissions during restore
- No sensitive data is transmitted outside your system
- Backup files are stored with restricted permissions
- Option to encrypt sensitive data using GPG

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Adding New Plugins

1. Create a new file in `shellot/plugins/` named `your_tool_plugin.py`
2. Extend the `BackupPlugin` class
3. Implement required methods:
   - `plugin_name`
   - `export_settings`
   - `import_settings`

Example:
```python
from base_plugin import BackupPlugin

class YourToolPlugin(BackupPlugin):
    @property
    def plugin_name(self):
        return "your_tool"
    
    def export_settings(self):
        # Implementation
        pass
    
    def import_settings(self):
        # Implementation
        pass
```

## 🔧 Troubleshooting

### Common Issues

1. Permission Errors
```bash
# Fix permissions
chmod -R u+w ~/.shellot_backup
```

2. Missing Dependencies
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

3. Conda Environment Issues
```bash
# Rebuild conda environment
conda env remove -n shellot
conda env create -f environment.yml
```

### Debug Mode

Run with debug logging:
```bash
shellot.sh export --debug
```

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🐛 Known Issues

- VSCode extension installation requires VSCode to be installed first
- Some Homebrew casks might need manual intervention during installation
- Oh My Zsh must be installed before importing its settings

## 🙏 Acknowledgments

- Oh My Zsh community
- Homebrew maintainers
- VSCode team
- iTerm2 developers

## 📮 Support

If you encounter any issues or have suggestions:
1. Check the [issues page](https://github.com/yourusername/shellot/issues)
2. Open a new issue with detailed description
3. Include your macOS version and relevant tool versions

### Version Compatibility

| macOS Version | Shellot Version | Status |
|---------------|-----------------|--------|
| 14.0+         | 1.0.0+         | ✅     |
| 13.0+         | 1.0.0+         | ✅     |
| 12.0+         | 1.0.0+         | ✅     |
| 11.0+         | 1.0.0+         | ✅     |
| 10.15         | 1.0.0+         | ✅     |
| < 10.15       | Not Supported  | ❌     |

## 📝 Release Notes

### Version 1.0.0
- Initial release
- Basic backup and restore functionality
- Support for common development tools
- Conda integration

### Version 1.1.0 (Coming Soon)
- GPG encryption support
- Cloud backup integration
- Custom plugin support
- Enhanced error handling

## 🎯 Roadmap

- [ ] Add support for additional editors (Sublime Text, JetBrains)
- [ ] Cloud sync support (Dropbox, Google Drive)
- [ ] Backup scheduling
- [ ] GUI interface
- [ ] Windows WSL support
- [ ] Linux support