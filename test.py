import subprocess


neovim_url = "https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage"

print("...更新本地软件仓库中...")


subprocess.call(['sudo', 'apt', 'wget'])

subprocess.call(['sudo', 'wget', neovim_url])
