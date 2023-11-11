import subprocess

# 旧的源信息和新的源信息
old_source = "bionic"
new_source = "focal"

# 读取源文件内容
# source_file = '/etc/apt/sources.list'
source_file = '/home/nico/Desktop/linuxCoder/sources.list'
with open(source_file, 'r') as f:
    source_lines = f.readlines()

# 替换源信息
new_source_lines = [line.replace(old_source, new_source) for line in source_lines]

# 将新内容写回源文件
with open(source_file, 'w') as f:
    f.writelines(new_source_lines)

# 更新软件包列表
# 更新
print("...更新本地软件仓库中...")
subprocess.call(['sudo', 'apt', 'update'])
print("...更新软件中....")
subprocess.call(['sudo', 'apt', 'upgrade'])
print("...自动清理弃用依赖...")
subprocess.call(['sudo', 'apt', 'autoremove'])
print("...安装软件: ...")
subprocess.call(['sudo', 'apt', 'install', 'git'])
subprocess.call(['sudo', 'apt', 'install', 'vim'])

subprocess.call(['sudo', 'apt', 'install', 'vim'])
subprocess.call(['sudo', 'apt', 'install', 'tree'])
subprocess.call(['sudo', 'apt', 'install', 'ranger'])
subprocess.call(['sudo', 'apt', 'install', 'htop'])
subprocess.call(['sudo', 'apt', 'install', 'neofetch'])
subprocess.call(['sudo', 'apt', 'install', 'dconf-editor'])
subprocess.call(['sudo', 'apt', 'install', 'gnome-tweaks'])
# 用于按键映射等gnome设置
# subprocess.call(['sudo', 'apt', 'install', 'ubuntu-restricted-extras'])
# 防火墙
subprocess.call(['sudo', 'apt', 'install', 'ufw'])
# 安装pg连接github
subprocess.call(['sudo', 'apt', 'install', 'gh'])
subprocess.call(['gh', 'auth', 'login'])


# 用安装包安装
# neovim 
# spark-store

