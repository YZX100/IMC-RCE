# IMC-RCE
批量检测IMC智能管理中心命令执行的脚本工具

![image](https://github.com/user-attachments/assets/2e7087ab-9c48-4e87-a9d1-148720396a2a)

```shell
想要检测该漏洞所使用的FOFA语句：
(title="用户自助服务" && body="/selfservice/javax.faces.resource/") || body="/selfservice/index.xhtml"

使用方法：
-u 域名/IP地址
-f 文本文件
注意：使用时所检测的域名或IP地址需要http或https协议
该脚本是使用的python解析器是python3
```
