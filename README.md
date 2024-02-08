# Git Bash (PM102)
```bash
scp -r Images_for_server/ fkhelifi-23\@ssh.enst.fr:Downloads/  
```
# VM (Images_for_server)
```bash
cp Diracs5-s5.dat ../../../../ffa/pm102-2024/serveur-j3/filtre- 
```
# VM (serveur-j3/filtre-)
```bash
cp Diracs5-s5.result ../../../../exterieurs/fkhelifi-23/Downloads/Images_for_server_result
```

# Git Bash (PM102)
```bash
scp -r fkhelifi-23\@ssh.enst.fr:Downloads/Images_for_server_result/ . Git Bash
```
