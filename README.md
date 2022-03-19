# Dot Files for Rituraj's Linux Machines

- Dotfiles are being handled by GNU `stow`.
- Run following commands to:
  - Preview the changes `stow` will implement:
    `stow -nvt ~ *`
  - Simulation Mode:
    `stow --adopt -nvt ~ *`
  - Implement the changes:
    `stow --adopt -vt ~ *`

