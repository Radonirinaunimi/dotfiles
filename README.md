<p align="center">
  <a href="https://github.com/Radonirinaunimi/dotfiles"><img alt="dotfiles" src="screenshot/logo.png" width=175></a> 
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
| Type        | Aplication                            | Link                                             |
|-------------|---------------------------------------|--------------------------------------------------|
| WM          | **i3**                                | [here](https://i3wm.org/)                        |
| Bar         | **Polybar**                           | [here](https://github.com/polybar/polybar)       |
| Terminal    | **Alacritty** (with GPU Acceleration) | [here](https://github.com/alacritty/alacritty)   |
| Shell       | **Fish** + **Oh my Fish**             | [here](https://github.com/oh-my-fish/oh-my-fish) |
| ColorScheme | **Dracula**                           | [here](https://github.com/dracula/dracula-theme) |
| Editor      | **Vim**                               | [here](https://github.com/vim/vim)               |
| Browser     | **Surf** (from Suckless)              | [here](https://surf.suckless.org/)               |
| PDFreader   | **zathura**                           | [here](https://pwmt.org/projects/zathura/)       |

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
