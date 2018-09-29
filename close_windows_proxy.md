windows 关闭代理服务器 cmd
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" 
/v ProxyEnable /t REG_DWORD /d 0 /f 
