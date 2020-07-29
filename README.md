<p align="center">
  <a href="https://github.com/Radonirinaunimi/dotfiles"><img alt="dotfiles" src="screenshot/new_logo.png" width=400></a> 
</p>
<p align="center">
  <a href="https://github.com/Radonirinaunimi/dotfiles/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Radonirinaunimi/dotfiles?label=license&logo=Github&style=flat-square"></a>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Radonirinaunimi/dotfiles?label=repo%20size&logo=Github&style=flat-square">
</p>

It goes without saying that if one stares at a screen for several hours a day, the experience must be as painless as possible. Such an aim would entail a workflow that seeks to maximize the productivity with a color scheme that is pleasant to look at. This repository contains some dotfiles that, while not succeding yet, aims to achieve that goal.

### Features

The following configurations have been heavily but not entirely influenced by the [dracula](https://draculatheme.com/) theme. For the time being, the window manger in which most of the features described below is [i3](https://i3wm.org/). Below are the details of such configurations.
![screenshot](screenshot/out.png)

### Configurations
As a window manager, I use [i3](https://i3wm.org/). The main apps, where the configuration files are inlcuded in this repository, are the following:
| Type        | Aplication                 |Overview                                                                                                        | Features                                                               |
|-------------|----------------------------|--------------------------------------------------------------------------------------------------------------- |------------------------------------------------------------------------|
| WM          | **i3**                     |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/refactor/screenshot/autotilling.png" width="200">    | <ul><li>Autotilling</li></ul>                                          |
| Bar         | **Polybar**                |                                                                                                                | <ul><li>Minimal</li><li>Clickable widgets</li></ul>                    |
| Terminal    | **Alacritty**              |                                                                                                                | <ul><li>GPU acceleration</li></ul>                                     |
| Shell       | **Fish** + **Oh my Fish**  |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/refactor/screenshot/fish_prompt.png" width="200">    | <ul><li>Powerline</li><li>Git status</li><li>Execution time</li></ul>  |
| App Launcher| **rofi**                   |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/refactor/screenshot/rofi.png" width="200">           | <ul><li>Dracula color scheme</li></ul>                                 |
| Editor      | **Vim**                    |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/refactor/screenshot/vim.png" width="200">            | <ul><li>Powerline status</li></ul>                                     |
| Multiplexer | **Tmux**                   |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/refactor/screenshot/tmux.png" width="200">           | <ul><li>Dracula Themed</li><li>Powerline & Git</li></ul>               |
| Browser     | **Surf/Firefox**           |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/refactor/screenshot/firefox.png" width="200">        | <ul><li>Dracula Themed</li></ul>                                       |
| PDFreader   | **zathura**                |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/refactor/screenshot/zathura.png" width="200">        | <ul><li>Dracula Themed</li></ul>                                       |

### Side Notes

##### Vim
In order to install all the `vim` plugins, first, copy the `.vimrc` in the home directory, run the folowing in the terminal
```bash
`vim`
```
and then the plugins can be updated inside `vim` as
```bash
:VimBootstrapUpdate
:PlugInstall
```

##### Tmux

To configure `tmux` based on the following [plugin](https://github.com/tmux-plugins/tpm), the [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) must be installed first. To install the plugins, just copy the `.tmux.conf` into the home directory and run the following
```bash
tmux source ~/.tmux.conf
```
then, inside a `tmux` session, press <kbd>Ctr</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>.
