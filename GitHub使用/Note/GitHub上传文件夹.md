### GitHub上传文件夹

##### 1.输入自己的用户名和邮箱

为注册GitHub账号时所用的用户名和邮箱;我的用户名为“1997ST2016”，邮箱为“1324971964@qq.com ”.

```
$  git config --global user.name "1997ST2016"
$  git config --global user.email "1324971964@qq.com"
```

![](D:\MyUniversity\Leetcode\GitHub使用\pictures\Name and Email.png)

##### 2.设置SSH key

首先检验本机是否生成秘钥，执行命令：

```
$ cd ~/.ssh
$ ls
```

若结果如下，则说明秘钥已存在。

![](D:\MyUniversity\Leetcode\GitHub使用\pictures\SSH.png)

如果没有秘钥，则执行以下命令来生成秘钥：

```
$  ssh-keygen -t rsa -b 4096 -C“ 1324971964@qq.com ”
```

生成过程中按3次回车键就好（默认路径，默认没有密码登录），生成成功后，用记事本打开id_rsa.pub，得到ssh key公钥。

id_rsa.pub所在位置，一般为默认路径。

![](D:\MyUniversity\Leetcode\GitHub使用\pictures\.ssh.png)

##### 3.为GitHub账号配置SSH key

登录Github账号，点击右上角用户头像右侧的倒三角，找到“setting”，点击；然后在左侧菜单栏中找到“SSH and GPG keys”，选择“new SSH key" ,输入title，下面key的内容就是本机SSH key公钥（直接将id_rsa.pub中的内容粘贴过来就可以），然后点击下面的”Add SSH key“即可完成。

#### 4.上传本地文件夹或者文件

**4.1 创建一个本地文件**

![](D:\MyUniversity\Leetcode\GitHub使用\pictures\localfile.png)

**4.2  建立本地仓库**

​	4.2.1 首先进入上述文件夹

​	4.2.2 执行指令进行初始化，会在原始文件夹中生成一个隐藏的文件夹“.git" :

```
$  git init
```

​	4.2.3 执行指令将问价添加到本地仓库

```
$ git add .         //添加当前文件夹下的所有文件
$ git add **.cpp    //添加当前文件夹下的**.cpp这个文件
```

​	4.2.4 输入本次的提交说明，单引号内为说明内容：

```
$ git commit -m "new"  //引号中的内容为对该文件的描述
```

![](D:\MyUniversity\Leetcode\GitHub使用\pictures\commit.png)

在写commit说明的时候最好能讲清楚提交的内容是啥含义，便于日后查看。这一点我还有待改进！！！

**4.3  关联GitHub仓库**

在GitHub中新建一个repository，复制该仓库的地址：

执行命令：

```
$ git remote add origin https://github.com/1997ST2016/LeetCode.git
```

如果**出现错误**：fatal: remote origin already exists，则执行以下语句：

    $ git remote rm origin
再重新执行：

```
$ git remote add origin https://github.com/1997ST2016/LeetCode.git
```

**4.4  上传文件**

执行命令：

```
$ git push origin master
```

如果**出现错误**：failed to push som refs to…….，则执行以下语句，先把远程服务器github上面的文件拉先来，再push 上去。：

```
   $ git pull origin master
```

刷新GitHub即可看到上传的文件夹和文件。