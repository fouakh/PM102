
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

cp Dirac1-1s3.dat ../../../../ffa/pm102-2024/serveur-j4/filtre- 

# 4. VM (serveur-j4/filtre-)

cp Dirac1-1s3.result ../../../../exterieurs/fkhelifi-23/Downloads/Images_for_server_result

# 5. Git Bash (PM102)

scp -r fkhelifi-23\@ssh.enst.fr:Downloads/Images_for_server_result/ . 

cd Images_for_server_result/

# 6. Git Bash (PM102/Images_for_server_result)
# After checking the result, for the next filter

rm -rf *

# 7. VM (Images_for_server_result)

rm -rf *

```


# Steps for Signals -> Server

```bash
# 1. Git Bash (PM102)

scp -r Signals_for_server/ fkhelifi-23\@ssh.enst.fr:Downloads/serveur-j4/filtre-   

# 2. VM (fkhelifi-23)

cd ../../../cal/ffa/pm102-2024/serveur-j2/filtre-

# 3. VM (Data_for_server)

cp dirac-1s3.dat ../../../../ffa/pm102-2024/serveur-j4/filtre- 

# 4. VM (serveur-j4/filtre-)

cp dirac-1s3.result ../../../../exterieurs/fkhelifi-23/Downloads/Data_for_server_result

# 5. Git Bash (PM102)

scp -r fkhelifi-23\@ssh.enst.fr:Downloads/Data_for_server_result/ . 

cd Data_for_server_result/

# 6. Git Bash (PM102/Data_for_server_result)
# After checking the result, for the next filter

rm -rf *

# 7. VM (Data_for_server_result)

rm -rf *