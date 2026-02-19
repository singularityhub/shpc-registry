---
layout: container
name:  "quay.io/biocontainers/pyhoward"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyhoward/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyhoward/container.yaml"
updated_at: "2026-02-19 07:14:03.588450"
latest: "0.13.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pyhoward"
aliases:
 - "bedToGenePred"
 - "bio"
 - "fasta_filter.py"
 - "flake8"
 - "genePredToGtf"
 - "genomepy"
 - "gff3ToGenePred"
 - "howard"
 - "ibd2sdi"
 - "markdown2"
 - "md_toc"
 - "mysql.server"
 - "mysql_config_editor"
 - "mysql_migrate_keyring"
 - "propconv"
 - "pycodestyle"
 - "pyfiglet"
 - "pyflakes"
 - "pyhoward"
 - "pynose"
 - "innochecksum"
 - "myisam_ftdump"
 - "myisamchk"
 - "myisamlog"
 - "myisampack"
 - "mysql"
 - "mysql_secure_installation"
 - "mysql_tzinfo_to_sql"
 - "mysqladmin"
 - "mysqlbinlog"
 - "mysqlcheck"
 - "mysqld"
 - "mysqld_multi"
 - "mysqld_safe"
 - "mysqldump"
 - "mysqldumpslow"
 - "mysqlimport"
 - "mysqlshow"
 - "mysqlslap"
 - "genePredToBed"
 - "gtfToGenePred"
 - "coverage"
 - "cyvcf2"
 - "protoc-25.3.0"
 - "checksum-profile"
versions:
 - "0.13.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pyhoward"
config: {"url": "https://biocontainers.pro/tools/pyhoward", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyhoward", "latest": {"0.13.0--pyhdfd78af_0": "sha256:23f61450bce94bb3242a82a152e6978fd19b3018a2aa3f9b3f33b7c207dd1905"}, "tags": {"0.13.0--pyhdfd78af_0": "sha256:23f61450bce94bb3242a82a152e6978fd19b3018a2aa3f9b3f33b7c207dd1905"}, "docker": "quay.io/biocontainers/pyhoward", "aliases": {"bedToGenePred": "/usr/local/bin/bedToGenePred", "bio": "/usr/local/bin/bio", "fasta_filter.py": "/usr/local/bin/fasta_filter.py", "flake8": "/usr/local/bin/flake8", "genePredToGtf": "/usr/local/bin/genePredToGtf", "genomepy": "/usr/local/bin/genomepy", "gff3ToGenePred": "/usr/local/bin/gff3ToGenePred", "howard": "/usr/local/bin/howard", "ibd2sdi": "/usr/local/bin/ibd2sdi", "markdown2": "/usr/local/bin/markdown2", "md_toc": "/usr/local/bin/md_toc", "mysql.server": "/usr/local/bin/mysql.server", "mysql_config_editor": "/usr/local/bin/mysql_config_editor", "mysql_migrate_keyring": "/usr/local/bin/mysql_migrate_keyring", "propconv": "/usr/local/bin/propconv", "pycodestyle": "/usr/local/bin/pycodestyle", "pyfiglet": "/usr/local/bin/pyfiglet", "pyflakes": "/usr/local/bin/pyflakes", "pyhoward": "/usr/local/bin/pyhoward", "pynose": "/usr/local/bin/pynose", "innochecksum": "/usr/local/bin/innochecksum", "myisam_ftdump": "/usr/local/bin/myisam_ftdump", "myisamchk": "/usr/local/bin/myisamchk", "myisamlog": "/usr/local/bin/myisamlog", "myisampack": "/usr/local/bin/myisampack", "mysql": "/usr/local/bin/mysql", "mysql_secure_installation": "/usr/local/bin/mysql_secure_installation", "mysql_tzinfo_to_sql": "/usr/local/bin/mysql_tzinfo_to_sql", "mysqladmin": "/usr/local/bin/mysqladmin", "mysqlbinlog": "/usr/local/bin/mysqlbinlog", "mysqlcheck": "/usr/local/bin/mysqlcheck", "mysqld": "/usr/local/bin/mysqld", "mysqld_multi": "/usr/local/bin/mysqld_multi", "mysqld_safe": "/usr/local/bin/mysqld_safe", "mysqldump": "/usr/local/bin/mysqldump", "mysqldumpslow": "/usr/local/bin/mysqldumpslow", "mysqlimport": "/usr/local/bin/mysqlimport", "mysqlshow": "/usr/local/bin/mysqlshow", "mysqlslap": "/usr/local/bin/mysqlslap", "genePredToBed": "/usr/local/bin/genePredToBed", "gtfToGenePred": "/usr/local/bin/gtfToGenePred", "coverage": "/usr/local/bin/coverage", "cyvcf2": "/usr/local/bin/cyvcf2", "protoc-25.3.0": "/usr/local/bin/protoc-25.3.0", "checksum-profile": "/usr/local/bin/checksum-profile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyhoward.
singularity registry hpc automated addition for pyhoward
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyhoward
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyhoward:0.13.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyhoward/0.13.0--pyhdfd78af_0
$ module help quay.io/biocontainers/pyhoward/0.13.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyhoward-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyhoward-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyhoward-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyhoward-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyhoward-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyhoward-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedToGenePred

```bash
$ singularity exec <container> /usr/local/bin/bedToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/bedToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bio

```bash
$ singularity exec <container> /usr/local/bin/bio
$ podman run --it --rm --entrypoint /usr/local/bin/bio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_filter.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flake8

```bash
$ singularity exec <container> /usr/local/bin/flake8
$ podman run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genePredToGtf

```bash
$ singularity exec <container> /usr/local/bin/genePredToGtf
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToGtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomepy

```bash
$ singularity exec <container> /usr/local/bin/genomepy
$ podman run --it --rm --entrypoint /usr/local/bin/genomepy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomepy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3ToGenePred

```bash
$ singularity exec <container> /usr/local/bin/gff3ToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/gff3ToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3ToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### howard

```bash
$ singularity exec <container> /usr/local/bin/howard
$ podman run --it --rm --entrypoint /usr/local/bin/howard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/howard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibd2sdi

```bash
$ singularity exec <container> /usr/local/bin/ibd2sdi
$ podman run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibd2sdi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown2

```bash
$ singularity exec <container> /usr/local/bin/markdown2
$ podman run --it --rm --entrypoint /usr/local/bin/markdown2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md_toc

```bash
$ singularity exec <container> /usr/local/bin/md_toc
$ podman run --it --rm --entrypoint /usr/local/bin/md_toc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md_toc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### propconv

```bash
$ singularity exec <container> /usr/local/bin/propconv
$ podman run --it --rm --entrypoint /usr/local/bin/propconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/propconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycodestyle

```bash
$ singularity exec <container> /usr/local/bin/pycodestyle
$ podman run --it --rm --entrypoint /usr/local/bin/pycodestyle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycodestyle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfiglet

```bash
$ singularity exec <container> /usr/local/bin/pyfiglet
$ podman run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflakes

```bash
$ singularity exec <container> /usr/local/bin/pyflakes
$ podman run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyhoward

```bash
$ singularity exec <container> /usr/local/bin/pyhoward
$ podman run --it --rm --entrypoint /usr/local/bin/pyhoward   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyhoward   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pynose

```bash
$ singularity exec <container> /usr/local/bin/pynose
$ podman run --it --rm --entrypoint /usr/local/bin/pynose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pynose   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysql_secure_installation

```bash
$ singularity exec <container> /usr/local/bin/mysql_secure_installation
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_tzinfo_to_sql

```bash
$ singularity exec <container> /usr/local/bin/mysql_tzinfo_to_sql
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### genePredToBed

```bash
$ singularity exec <container> /usr/local/bin/genePredToBed
$ podman run --it --rm --entrypoint /usr/local/bin/genePredToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genePredToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtfToGenePred

```bash
$ singularity exec <container> /usr/local/bin/gtfToGenePred
$ podman run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtfToGenePred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-25.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-25.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
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