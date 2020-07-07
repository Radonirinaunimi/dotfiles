<p align="center">
  <a href="https://github.com/Radonirinaunimi/dotfiles"><img alt="dotfiles" src="screenshot/logo.png" width=215></a> 
</p>
<p align="center">
  <a href="https://github.com/Radonirinaunimi/dotfiles/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Radonirinaunimi/dotfiles?label=license&logo=Github&style=flat-square"></a>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Radonirinaunimi/dotfiles?label=repo%20size&logo=Github&style=flat-square">
</p>

### Features
The following respository contains the `dotfiles` of my personal desktop configuration. It is heavily but not entirely influenced by the [Dracula](https://github.com/dracula/dracula-theme) color scheme. If you are using the dotfiles, please take into that the configurations were mainly designed to optimize my personal workflow. Below is a screenshot of my desktop.
![screenshot](screenshot/out.png)

### Configurations
As a window manager, I use [i3](https://i3wm.org/). The main apps, where the configuration files are inlcuded in this repository, are the following:
| Type        | Aplication                            |Overview                                                                                                        | Features                               |
|-------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------- |----------------------------------------|
| WM          | **i3**                                |                                                                                                                | [here]                                 |
| Bar         | **Polybar**                           |                                                                                                                | [here]                                 |
| Terminal    | **Alacritty** (with GPU Acceleration) |                                                                                                                | [here]                                 |
| Shell       | **Fish** + **Oh my Fish**             |<img src="https://github.com/Radonirinaunimi/dotfiles/blob/master/screenshot/fish_prompt.png" width="200">      | <ul><li>item1</li><li>item2</li></ul>  |
| ColorScheme | **Dracula**                           |                                                                                                                | [here]                                 |
| Editor      | **Vim**                               |                                                                                                                | [here]                                 |
| Browser     | **Surf** (from Suckless)              |                                                                                                                | [here]                                 |
| PDFreader   | **zathura**                           |                                                                                                                | [here]                                 |

### Side Notes
* In order to install all the `vim` plugins, after copying the `.vimrc` in the home directory, first run the folowing in the terminal
```bash
`vim`
```
and then the plugins can be updated inside vim as
```bash
:VimBootstrapUpdate
:PlugInstall
```
