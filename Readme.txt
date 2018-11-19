 1) Install the software.

 2) Copy the binary of the license server to a permanent
    directory, such as C:\dvt-jb-lic-server\ or 
    /opt/dvt-jb-lic-server/

 3) Windows:
    - Start a command prommpt as an Administrator.
    - Go to the directory, where you put the license
      server, using "cd".
    - Install the license server:

      x86: dvt-jb_licsrv.386.exe -mode install
      x64: dvt-jb_licsrv.amd64.exe -mode install

      This will install the license server as a 
      windows service. If you want to remove it
      again, use "-mode uninstall".

    - Open services.msc and start the service.
      Alternatively, use "net start" or reboot
      your pc/server.

  4) Start the application and point it to the license server.
     If you are running the license server on the same host,
     you can point it to "http://127.0.0.1:1337". Otherwise, 
     use the ip or hostname of your license server.

