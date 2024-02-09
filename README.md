
# Connect to the VM

```bash
ssh -i .ssh/ed fkhelifi-23@ssh.enst.fr
```

# Steps for Images -> Server

```bash
# 1. Git Bash (PM102)

scp -r Images_for_server/ fkhelifi-23\@ssh.enst.fr:Downloads/serveur-j4/filtre-   

# 2. VM (fkhelifi-23)

cd ../../../cal/ffa/pm102-2024/serveur-j4/filtre-

# 3. VM (Images_for_server)

cp Diracs1-s3.dat ../../../../ffa/pm102-2024/serveur-j4/filtre- 

# 4. VM (serveur-j4/filtre-)

cp Diracs1-s3.result ../../../../exterieurs/fkhelifi-23/Downloads/Images_for_server_result

# 5. Git Bash (PM102)

scp -r fkhelifi-23\@ssh.enst.fr:Downloads/Images_for_server_result/ . 
```

# Steps for Signals -> Server

```bash
# 1. Git Bash (PM102)

scp -r Signals_for_server/ fkhelifi-23\@ssh.enst.fr:Downloads/serveur-j4/filtre-   

# 2. VM (fkhelifi-23)

cd ../../../cal/ffa/pm102-2024/serveur-j2/filtre-

# 3. VM (Data_for_server)

cp diracs1-s3.dat ../../../../ffa/pm102-2024/serveur-j4/filtre- 

# 4. VM (serveur-j4/filtre-)

cp diracs1-s3.result ../../../../exterieurs/fkhelifi-23/Downloads/Data_for_server_result

# 5. Git Bash (PM102)

scp -r fkhelifi-23\@ssh.enst.fr:Downloads/Data_for_server_result/ . 
