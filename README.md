# File Encryptor 2024 v1.0.3

### 1.1 Library encoding 库编码:

- UTF-8

### 1.2 introduce 介绍

A Python library for file encryption and decryption using a simple, self-made encryption algorithm. This library supports encryption of any file type and is easy to integrate into other projects.

一个 Python 库，用于使用简单的自制加密算法进行文件加密和解密。该库支持任何文件类型的加密，并且易于集成到其他项目中。

## About updates 关于更新

### 2.1 Update type 更新类型

- .1.1 本次更新类型:
- Urgent update 紧急更新
- patch 补丁
- Minor version updates 小版本更新
- Major version updates 大版本更新
- Language packs 语言包

  



### 2.2 Updated content 更新内容

- README.md file added Chinese user manual
- Shorten the function name to make it easier to call the function

- README.md文件增加中文使用手册
- 缩短函数名称，以方便调用函数

## Features 特征

- Encrypt and decrypt any file type (e.g., `.txt`, `.jpg`, `.pdf`, `.mp4`).
- Custom encryption algorithm with simple operations (XOR and byte shifts).
- Easy-to-use API for integrating into other Python projects.
- 加密和解密任何文件类型(e.g., `.txt`, `.jpg`, `.pdf`, `.mp4`)

## Installation 安装

To install the library, simply use pip:

要安装库，只需使用 pip：
```bash
pip install file-encryptor-2024
```

## Usage 用法
Here is a basic example of how to use the CustomFileEncryptor class to encrypt and decrypt files:

下面是如何使用 CustomFileEncryptor 类来加密和解密文件的基本示例：

### English
```bash
from file_encryptor_2024.encryptor import FileEncryptor

# Initialize the encryptor with a password
encryptor = FileEncryptor(password="example_password")

# Encrypt a file
encryptor.encrypt_file("example_file", "example_file_name.enc")

# Decrypt the file back to its original form
encryptor.decrypt_file("example_file_name.enc", "example_file")

```

### 简体中文

```bash
from file_encryptor.2024.encryptor import FileEncryptor

# 使用密码初始化加密器
encryptor = FileEncryptor(password="示例密码")

# 加密文件
encryptor.encrypt_file("示例文件", "示例文件名.enc")

# 将文件解密回其原始形式
encryptor.decrypt_file("示例文件名.enc", "示例文件")
```


## Contact 联系
For any questions or inquiries, please contact the author:
- Name: LiuYuchen
- Email: liuyuchen032901@outlook.com

如有任何问题或疑问，请联系作者：

- 姓名: 刘宇晨
- 邮箱: liuyuchen032901@outlook.com
