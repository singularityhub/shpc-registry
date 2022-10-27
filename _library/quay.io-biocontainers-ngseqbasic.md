---
layout: container
name:  "quay.io/biocontainers/ngseqbasic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngseqbasic/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ngseqbasic/container.yaml"
updated_at: "2022-10-27 01:11:06.764340"
latest: "2.0.1--pl5.22.0.1_1"
container_url: "https://biocontainers.pro/tools/ngseqbasic"
aliases:
 - "NGseqBasic"
 - "bedClip"
 - "bedGraphPack"
 - "msql2mysql"
 - "mysql_convert_table_format"
 - "mysql_find_rows"
 - "mysql_fix_extensions"
 - "mysql_setpermission"
 - "mysql_waitpid"
 - "mysql_zap"
 - "mysqlaccess"
 - "mysqlaccess.conf"
 - "mysqlbug"
 - "mysqlhotcopy"
 - "testEnvironment"
versions:
 - "2.0.1--pl5.22.0.1_1"
description: "shpc-registry automated BioContainers addition for ngseqbasic"
config: {"url": "https://biocontainers.pro/tools/ngseqbasic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngseqbasic", "latest": {"2.0.1--pl5.22.0.1_1": "sha256:727bb15c8bc37d98c87046a6eeda207a86c0d5fe574cbc54c51e345710402331"}, "tags": {"2.0.1--pl5.22.0.1_1": "sha256:727bb15c8bc37d98c87046a6eeda207a86c0d5fe574cbc54c51e345710402331"}, "docker": "quay.io/biocontainers/ngseqbasic", "aliases": {"NGseqBasic": "/usr/local/bin/NGseqBasic", "bedClip": "/usr/local/bin/bedClip", "bedGraphPack": "/usr/local/bin/bedGraphPack", "msql2mysql": "/usr/local/bin/msql2mysql", "mysql_convert_table_format": "/usr/local/bin/mysql_convert_table_format", "mysql_find_rows": "/usr/local/bin/mysql_find_rows", "mysql_fix_extensions": "/usr/local/bin/mysql_fix_extensions", "mysql_setpermission": "/usr/local/bin/mysql_setpermission", "mysql_waitpid": "/usr/local/bin/mysql_waitpid", "mysql_zap": "/usr/local/bin/mysql_zap", "mysqlaccess": "/usr/local/bin/mysqlaccess", "mysqlaccess.conf": "/usr/local/bin/mysqlaccess.conf", "mysqlbug": "/usr/local/bin/mysqlbug", "mysqlhotcopy": "/usr/local/bin/mysqlhotcopy", "testEnvironment": "/usr/local/bin/testEnvironment"}}
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


#### msql2mysql

```bash
$ singularity exec <container> /usr/local/bin/msql2mysql
$ podman run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysql_setpermission

```bash
$ singularity exec <container> /usr/local/bin/mysql_setpermission
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysqlbug

```bash
$ singularity exec <container> /usr/local/bin/mysqlbug
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlhotcopy

```bash
$ singularity exec <container> /usr/local/bin/mysqlhotcopy
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlhotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlhotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testEnvironment

```bash
$ singularity exec <container> /usr/local/bin/testEnvironment
$ podman run --it --rm --entrypoint /usr/local/bin/testEnvironment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testEnvironment   -v ${PWD} -w ${PWD} <container> -c " $@"
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