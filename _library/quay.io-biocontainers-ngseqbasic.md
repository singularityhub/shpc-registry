---
layout: container
name:  "quay.io/biocontainers/ngseqbasic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngseqbasic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngseqbasic/container.yaml"
updated_at: "2025-07-28 04:00:01.085191"
latest: "2.0.1--pl5.22.0.1_1"
container_url: "https://biocontainers.pro/tools/ngseqbasic"
aliases:
 - "NGseqBasic"
 - "bedClip"
 - "bedGraphPack"
 - "innochecksum"
 - "msql2mysql"
 - "myisam_ftdump"
 - "myisamchk"
 - "myisamlog"
 - "myisampack"
 - "mysql"
 - "mysql_client_test"
 - "mysql_convert_table_format"
 - "mysql_find_rows"
 - "mysql_fix_extensions"
 - "mysql_plugin"
 - "mysql_secure_installation"
 - "mysql_setpermission"
 - "mysql_tzinfo_to_sql"
 - "mysql_upgrade"
 - "mysql_waitpid"
 - "mysql_zap"
 - "mysqlaccess"
 - "mysqlaccess.conf"
 - "mysqladmin"
 - "mysqlbinlog"
 - "mysqlbug"
 - "mysqlcheck"
 - "mysqld"
 - "mysqld_multi"
 - "mysqld_safe"
 - "mysqldump"
 - "mysqldumpslow"
 - "mysqlhotcopy"
 - "mysqlimport"
 - "mysqlshow"
 - "mysqlslap"
 - "mysqltest"
 - "replace"
 - "resolve_stack_dump"
 - "resolveip"
 - "testEnvironment"
 - "trim_galore"
 - "flash"
 - "bedGraphToBigWig"
 - "bedToBigBed"
 - "cutadapt"
 - "fastqc"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
 - "perl5.22.0"
 - "c2ph"
versions:
 - "2.0.1--pl5.22.0.1_1"
description: "shpc-registry automated BioContainers addition for ngseqbasic"
config: {"url": "https://biocontainers.pro/tools/ngseqbasic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngseqbasic", "latest": {"2.0.1--pl5.22.0.1_1": "sha256:4fd3e6d18e9921cba95e36563ff5203f37930a68dd6aa4aab2fd58270ef98847"}, "tags": {"2.0.1--pl5.22.0.1_1": "sha256:4fd3e6d18e9921cba95e36563ff5203f37930a68dd6aa4aab2fd58270ef98847"}, "docker": "quay.io/biocontainers/ngseqbasic", "aliases": {"NGseqBasic": "/usr/local/bin/NGseqBasic", "bedClip": "/usr/local/bin/bedClip", "bedGraphPack": "/usr/local/bin/bedGraphPack", "innochecksum": "/usr/local/bin/innochecksum", "msql2mysql": "/usr/local/bin/msql2mysql", "myisam_ftdump": "/usr/local/bin/myisam_ftdump", "myisamchk": "/usr/local/bin/myisamchk", "myisamlog": "/usr/local/bin/myisamlog", "myisampack": "/usr/local/bin/myisampack", "mysql": "/usr/local/bin/mysql", "mysql_client_test": "/usr/local/bin/mysql_client_test", "mysql_convert_table_format": "/usr/local/bin/mysql_convert_table_format", "mysql_find_rows": "/usr/local/bin/mysql_find_rows", "mysql_fix_extensions": "/usr/local/bin/mysql_fix_extensions", "mysql_plugin": "/usr/local/bin/mysql_plugin", "mysql_secure_installation": "/usr/local/bin/mysql_secure_installation", "mysql_setpermission": "/usr/local/bin/mysql_setpermission", "mysql_tzinfo_to_sql": "/usr/local/bin/mysql_tzinfo_to_sql", "mysql_upgrade": "/usr/local/bin/mysql_upgrade", "mysql_waitpid": "/usr/local/bin/mysql_waitpid", "mysql_zap": "/usr/local/bin/mysql_zap", "mysqlaccess": "/usr/local/bin/mysqlaccess", "mysqlaccess.conf": "/usr/local/bin/mysqlaccess.conf", "mysqladmin": "/usr/local/bin/mysqladmin", "mysqlbinlog": "/usr/local/bin/mysqlbinlog", "mysqlbug": "/usr/local/bin/mysqlbug", "mysqlcheck": "/usr/local/bin/mysqlcheck", "mysqld": "/usr/local/bin/mysqld", "mysqld_multi": "/usr/local/bin/mysqld_multi", "mysqld_safe": "/usr/local/bin/mysqld_safe", "mysqldump": "/usr/local/bin/mysqldump", "mysqldumpslow": "/usr/local/bin/mysqldumpslow", "mysqlhotcopy": "/usr/local/bin/mysqlhotcopy", "mysqlimport": "/usr/local/bin/mysqlimport", "mysqlshow": "/usr/local/bin/mysqlshow", "mysqlslap": "/usr/local/bin/mysqlslap", "mysqltest": "/usr/local/bin/mysqltest", "replace": "/usr/local/bin/replace", "resolve_stack_dump": "/usr/local/bin/resolve_stack_dump", "resolveip": "/usr/local/bin/resolveip", "testEnvironment": "/usr/local/bin/testEnvironment", "trim_galore": "/usr/local/bin/trim_galore", "flash": "/usr/local/bin/flash", "bedGraphToBigWig": "/usr/local/bin/bedGraphToBigWig", "bedToBigBed": "/usr/local/bin/bedToBigBed", "cutadapt": "/usr/local/bin/cutadapt", "fastqc": "/usr/local/bin/fastqc", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngseqbasic.
shpc-registry automated BioContainers addition for ngseqbasic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngseqbasic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngseqbasic:2.0.1--pl5.22.0.1_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngseqbasic/2.0.1--pl5.22.0.1_1
$ module help quay.io/biocontainers/ngseqbasic/2.0.1--pl5.22.0.1_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngseqbasic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngseqbasic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngseqbasic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngseqbasic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngseqbasic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngseqbasic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NGseqBasic

```bash
$ singularity exec <container> /usr/local/bin/NGseqBasic
$ podman run --it --rm --entrypoint /usr/local/bin/NGseqBasic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NGseqBasic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedClip

```bash
$ singularity exec <container> /usr/local/bin/bedClip
$ podman run --it --rm --entrypoint /usr/local/bin/bedClip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedClip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedGraphPack

```bash
$ singularity exec <container> /usr/local/bin/bedGraphPack
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphPack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphPack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### innochecksum

```bash
$ singularity exec <container> /usr/local/bin/innochecksum
$ podman run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msql2mysql

```bash
$ singularity exec <container> /usr/local/bin/msql2mysql
$ podman run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysql_client_test

```bash
$ singularity exec <container> /usr/local/bin/mysql_client_test
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_client_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_client_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_convert_table_format

```bash
$ singularity exec <container> /usr/local/bin/mysql_convert_table_format
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_convert_table_format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_convert_table_format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_find_rows

```bash
$ singularity exec <container> /usr/local/bin/mysql_find_rows
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_find_rows   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_find_rows   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_fix_extensions

```bash
$ singularity exec <container> /usr/local/bin/mysql_fix_extensions
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_fix_extensions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_fix_extensions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_plugin

```bash
$ singularity exec <container> /usr/local/bin/mysql_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_secure_installation

```bash
$ singularity exec <container> /usr/local/bin/mysql_secure_installation
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_setpermission

```bash
$ singularity exec <container> /usr/local/bin/mysql_setpermission
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysql_waitpid

```bash
$ singularity exec <container> /usr/local/bin/mysql_waitpid
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_waitpid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_waitpid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_zap

```bash
$ singularity exec <container> /usr/local/bin/mysql_zap
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_zap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_zap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlaccess

```bash
$ singularity exec <container> /usr/local/bin/mysqlaccess
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlaccess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlaccess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlaccess.conf

```bash
$ singularity exec <container> /usr/local/bin/mysqlaccess.conf
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlaccess.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlaccess.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysqlbug

```bash
$ singularity exec <container> /usr/local/bin/mysqlbug
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysqlhotcopy

```bash
$ singularity exec <container> /usr/local/bin/mysqlhotcopy
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlhotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlhotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysqltest

```bash
$ singularity exec <container> /usr/local/bin/mysqltest
$ podman run --it --rm --entrypoint /usr/local/bin/mysqltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqltest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### replace

```bash
$ singularity exec <container> /usr/local/bin/replace
$ podman run --it --rm --entrypoint /usr/local/bin/replace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/replace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resolve_stack_dump

```bash
$ singularity exec <container> /usr/local/bin/resolve_stack_dump
$ podman run --it --rm --entrypoint /usr/local/bin/resolve_stack_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/resolve_stack_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resolveip

```bash
$ singularity exec <container> /usr/local/bin/resolveip
$ podman run --it --rm --entrypoint /usr/local/bin/resolveip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/resolveip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testEnvironment

```bash
$ singularity exec <container> /usr/local/bin/testEnvironment
$ podman run --it --rm --entrypoint /usr/local/bin/testEnvironment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testEnvironment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_galore

```bash
$ singularity exec <container> /usr/local/bin/trim_galore
$ podman run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flash

```bash
$ singularity exec <container> /usr/local/bin/flash
$ podman run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedGraphToBigWig

```bash
$ singularity exec <container> /usr/local/bin/bedGraphToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBigBed

```bash
$ singularity exec <container> /usr/local/bin/bedToBigBed
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
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