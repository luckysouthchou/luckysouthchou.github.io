zsh自己就更新了
也不知道咋的，atom就用不上了。
一直提示flake8没有安装对路径。

后来根据一个日本人写的提示才弄对了

open ~/.bash_profile

找到conda的文件如下：（复制所有的）
# added by Anaconda3 5.3.0 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<

再打开，粘贴进去
open ~/.zshrc
再执行
source ~/.zshrc

这下conda就能在当前用了
最后再执行：
conda install flake8
问题成功解决


---------
补上oh my zsh的使用
用起来清爽多了呵呵

安装 如下：
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

还可以自己选择主题



--------
iTerm2
清爽好多啊 UI真的好看
呵呵，用了就回不去
以后要多探索
