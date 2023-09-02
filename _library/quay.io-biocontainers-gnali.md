---
layout: container
name:  "quay.io/biocontainers/gnali"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gnali/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gnali/container.yaml"
updated_at: "2023-09-02 02:41:50.171103"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gnali"
aliases:
 - "bigWigToWig.pl"
 - "filter_vep"
 - "gnali"
 - "gnali_get_data"
 - "haplo"
 - "ibd2sdi"
 - "index_bigwigset.pl"
 - "innochecksum"
 - "myisam_ftdump"
 - "myisamchk"
 - "myisamlog"
 - "myisampack"
 - "mysql"
 - "mysql.server"
 - "mysql_config_editor"
 - "mysql_migrate_keyring"
 - "mysql_secure_installation"
 - "mysql_ssl_rsa_setup"
 - "mysql_tzinfo_to_sql"
 - "mysql_upgrade"
 - "mysqladmin"
 - "mysqlbinlog"
 - "mysqlcheck"
 - "mysqld"
 - "mysqld_multi"
 - "mysqld_safe"
 - "mysqldump"
 - "mysqldumpslow"
 - "mysqlimport"
 - "mysqlpump"
 - "mysqlshow"
 - "mysqlslap"
 - "variant_recoder"
 - "vep"
 - "vep_convert_cache"
 - "vep_install"
 - "wigToBigWig.pl"
 - "zlib_decompress"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for gnali"
config: {"url": "https://biocontainers.pro/tools/gnali", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gnali", "latest": {"1.1.0--pyhdfd78af_0": "sha256:5a2fd37dcdea95218667fa41b240c64da76cbdbbd54f5912c584b9d8ce483de9"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:5a2fd37dcdea95218667fa41b240c64da76cbdbbd54f5912c584b9d8ce483de9"}, "docker": "quay.io/biocontainers/gnali", "aliases": {"bigWigToWig.pl": "/usr/local/bin/bigWigToWig.pl", "filter_vep": "/usr/local/bin/filter_vep", "gnali": "/usr/local/bin/gnali", "gnali_get_data": "/usr/local/bin/gnali_get_data", "haplo": "/usr/local/bin/haplo", "ibd2sdi": "/usr/local/bin/ibd2sdi", "index_bigwigset.pl": "/usr/local/bin/index_bigwigset.pl", "innochecksum": "/usr/local/bin/innochecksum", "myisam_ftdump": "/usr/local/bin/myisam_ftdump", "myisamchk": "/usr/local/bin/myisamchk", "myisamlog": "/usr/local/bin/myisamlog", "myisampack": "/usr/local/bin/myisampack", "mysql": "/usr/local/bin/mysql", "mysql.server": "/usr/local/bin/mysql.server", "mysql_config_editor": "/usr/local/bin/mysql_config_editor", "mysql_migrate_keyring": "/usr/local/bin/mysql_migrate_keyring", "mysql_secure_installation": "/usr/local/bin/mysql_secure_installation", "mysql_ssl_rsa_setup": "/usr/local/bin/mysql_ssl_rsa_setup", "mysql_tzinfo_to_sql": "/usr/local/bin/mysql_tzinfo_to_sql", "mysql_upgrade": "/usr/local/bin/mysql_upgrade", "mysqladmin": "/usr/local/bin/mysqladmin", "mysqlbinlog": "/usr/local/bin/mysqlbinlog", "mysqlcheck": "/usr/local/bin/mysqlcheck", "mysqld": "/usr/local/bin/mysqld", "mysqld_multi": "/usr/local/bin/mysqld_multi", "mysqld_safe": "/usr/local/bin/mysqld_safe", "mysqldump": "/usr/local/bin/mysqldump", "mysqldumpslow": "/usr/local/bin/mysqldumpslow", "mysqlimport": "/usr/local/bin/mysqlimport", "mysqlpump": "/usr/local/bin/mysqlpump", "mysqlshow": "/usr/local/bin/mysqlshow", "mysqlslap": "/usr/local/bin/mysqlslap", "variant_recoder": "/usr/local/bin/variant_recoder", "vep": "/usr/local/bin/vep", "vep_convert_cache": "/usr/local/bin/vep_convert_cache", "vep_install": "/usr/local/bin/vep_install", "wigToBigWig.pl": "/usr/local/bin/wigToBigWig.pl", "zlib_decompress": "/usr/local/bin/zlib_decompress", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gnali.
shpc-registry automated BioContainers addition for gnali
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gnali
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gnali:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gnali/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/gnali/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gnali-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gnali-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gnali-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gnali-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gnali-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gnali-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigWigToWig.pl

```bash
$ singularity exec <container> /usr/local/bin/bigWigToWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_vep

```bash
$ singularity exec <container> /usr/local/bin/filter_vep
$ podman run --it --rm --entrypoint /usr/local/bin/filter_vep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_vep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnali

```bash
$ singularity exec <container> /usr/local/bin/gnali
$ podman run --it --rm --entrypoint /usr/local/bin/gnali   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnali   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnali_get_data

```bash
$ singularity exec <container> /usr/local/bin/gnali_get_data
$ podman run --it --rm --entrypoint /usr/local/bin/gnali_get_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnali_get_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplo

```bash
$ singularity exec <container> /usr/local/bin/haplo
$ podman run --it --rm --entrypoint /usr/local/bin/haplo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibd2sdi

```bash
$ singularity exec <container> /usr/local/bin/ibd2sdi
$ podman run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_bigwigset.pl

```bash
$ singularity exec <container> /usr/local/bin/index_bigwigset.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### innochecksum

```bash
$ singularity exec <container> /usr/local/bin/innochecksum
$ podman run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisam_ftdump

```bash
$ singularity exec <container> /usr/local/bin/myisam_ftdump
$ podman run --it --rm --entrypoint /usr/local/bin/myisam_ftdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisam_ftdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisamchk

```bash
$ singularity exec <container> /usr/local/bin/myisamchk
$ podman run --it --rm --entrypoint /usr/local/bin/myisamchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisamchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisamlog

```bash
$ singularity exec <container> /usr/local/bin/myisamlog
$ podman run --it --rm --entrypoint /usr/local/bin/myisamlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisamlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisampack

```bash
$ singularity exec <container> /usr/local/bin/myisampack
$ podman run --it --rm --entrypoint /usr/local/bin/myisampack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisampack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql

```bash
$ singularity exec <container> /usr/local/bin/mysql
$ podman run --it --rm --entrypoint /usr/local/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql.server

```bash
$ singularity exec <container> /usr/local/bin/mysql.server
$ podman run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config_editor

```bash
$ singularity exec <container> /usr/local/bin/mysql_config_editor
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_migrate_keyring

```bash
$ singularity exec <container> /usr/local/bin/mysql_migrate_keyring
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_migrate_keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_migrate_keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_secure_installation

```bash
$ singularity exec <container> /usr/local/bin/mysql_secure_installation
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_ssl_rsa_setup

```bash
$ singularity exec <container> /usr/local/bin/mysql_ssl_rsa_setup
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_tzinfo_to_sql

```bash
$ singularity exec <container> /usr/local/bin/mysql_tzinfo_to_sql
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_upgrade

```bash
$ singularity exec <container> /usr/local/bin/mysql_upgrade
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqladmin

```bash
$ singularity exec <container> /usr/local/bin/mysqladmin
$ podman run --it --rm --entrypoint /usr/local/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlbinlog

```bash
$ singularity exec <container> /usr/local/bin/mysqlbinlog
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlcheck

```bash
$ singularity exec <container> /usr/local/bin/mysqlcheck
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld

```bash
$ singularity exec <container> /usr/local/bin/mysqld
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_multi

```bash
$ singularity exec <container> /usr/local/bin/mysqld_multi
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_safe

```bash
$ singularity exec <container> /usr/local/bin/mysqld_safe
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldump

```bash
$ singularity exec <container> /usr/local/bin/mysqldump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldumpslow

```bash
$ singularity exec <container> /usr/local/bin/mysqldumpslow
$ podman run --it --rm --entrypoint /usr/local/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlimport

```bash
$ singularity exec <container> /usr/local/bin/mysqlimport
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlpump

```bash
$ singularity exec <container> /usr/local/bin/mysqlpump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlshow

```bash
$ singularity exec <container> /usr/local/bin/mysqlshow
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlslap

```bash
$ singularity exec <container> /usr/local/bin/mysqlslap
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variant_recoder

```bash
$ singularity exec <container> /usr/local/bin/variant_recoder
$ podman run --it --rm --entrypoint /usr/local/bin/variant_recoder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variant_recoder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep

```bash
$ singularity exec <container> /usr/local/bin/vep
$ podman run --it --rm --entrypoint /usr/local/bin/vep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_convert_cache

```bash
$ singularity exec <container> /usr/local/bin/vep_convert_cache
$ podman run --it --rm --entrypoint /usr/local/bin/vep_convert_cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_convert_cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vep_install

```bash
$ singularity exec <container> /usr/local/bin/vep_install
$ podman run --it --rm --entrypoint /usr/local/bin/vep_install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vep_install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig.pl

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zlib_decompress

```bash
$ singularity exec <container> /usr/local/bin/zlib_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git

```bash
$ singularity exec <container> /usr/local/bin/git
$ podman run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-cvsserver

```bash
$ singularity exec <container> /usr/local/bin/git-cvsserver
$ podman run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/git-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-shell

```bash
$ singularity exec <container> /usr/local/bin/git-shell
$ podman run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-archive

```bash
$ singularity exec <container> /usr/local/bin/git-upload-archive
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/git-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gitk

```bash
$ singularity exec <container> /usr/local/bin/gitk
$ podman run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)