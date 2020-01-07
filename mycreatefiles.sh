# -*- coding:utf-8 -*-
#!/bin/zsh



function sayhello() {
  echo "hell,my nama is 波波的朋友！"
  echo "我准备按照你输入的文件名，开始创建文件夹"
  date
}

function getDirectory() ￿{
  printf "please Input file name: "
  read file_name
  # vared -p 'What would you like to do?: ' -c tmp
  echo "file name is ${file_name}"


}

function sayBye() {
    echo "Bye! 波波"
}


创建目录
function createdirectory() {
mkdir "${file_name}"
    
}


#删除文件
function delfiles() {


}

#调用函数


sayhello
getDirectory
sayBye
createdirectory
ls


