---
layout: container
name:  "quay.io/biocontainers/cgat-scripts-nosetests"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgat-scripts-nosetests/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cgat-scripts-nosetests/container.yaml"
updated_at: "2022-10-27 00:40:49.844415"
latest: "0.0.4--py35r3.3.1_0"
container_url: "https://biocontainers.pro/tools/cgat-scripts-nosetests"
aliases:
 - "msql2mysql"
 - "mysql_client_test"
 - "mysql_convert_table_format"
 - "mysql_find_rows"
 - "mysql_fix_extensions"
 - "mysql_plugin"
 - "mysql_setpermission"
 - "mysql_waitpid"
 - "mysql_zap"
 - "mysqlaccess"
 - "mysqlaccess.conf"
 - "mysqlbug"
 - "mysqlhotcopy"
 - "mysqltest"
 - "pep8"
 - "replace"
 - "resolve_stack_dump"
 - "resolveip"
versions:
 - "0.0.4--py35r3.3.1_0"
description: "shpc-registry automated BioContainers addition for cgat-scripts-nosetests"
config: {"url": "https://biocontainers.pro/tools/cgat-scripts-nosetests", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgat-scripts-nosetests", "latest": {"0.0.4--py35r3.3.1_0": "sha256:8e2712379781fe7ed58fe0032cd8d94d941c90f79b58b57abb7c30ee2b6cbd68"}, "tags": {"0.0.4--py35r3.3.1_0": "sha256:8e2712379781fe7ed58fe0032cd8d94d941c90f79b58b57abb7c30ee2b6cbd68"}, "docker": "quay.io/biocontainers/cgat-scripts-nosetests", "aliases": {"msql2mysql": "/usr/local/bin/msql2mysql", "mysql_client_test": "/usr/local/bin/mysql_client_test", "mysql_convert_table_format": "/usr/local/bin/mysql_convert_table_format", "mysql_find_rows": "/usr/local/bin/mysql_find_rows", "mysql_fix_extensions": "/usr/local/bin/mysql_fix_extensions", "mysql_plugin": "/usr/local/bin/mysql_plugin", "mysql_setpermission": "/usr/local/bin/mysql_setpermission", "mysql_waitpid": "/usr/local/bin/mysql_waitpid", "mysql_zap": "/usr/local/bin/mysql_zap", "mysqlaccess": "/usr/local/bin/mysqlaccess", "mysqlaccess.conf": "/usr/local/bin/mysqlaccess.conf", "mysqlbug": "/usr/local/bin/mysqlbug", "mysqlhotcopy": "/usr/local/bin/mysqlhotcopy", "mysqltest": "/usr/local/bin/mysqltest", "pep8": "/usr/local/bin/pep8", "replace": "/usr/local/bin/replace", "resolve_stack_dump": "/usr/local/bin/resolve_stack_dump", "resolveip": "/usr/local/bin/resolveip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgat-scripts-nosetests.
shpc-registry automated BioContainers addition for cgat-scripts-nosetests
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgat-scripts-nosetests
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgat-scripts-nosetests:0.0.4--py35r3.3.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgat-scripts-nosetests/0.0.4--py35r3.3.1_0
$ module help quay.io/biocontainers/cgat-scripts-nosetests/0.0.4--py35r3.3.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgat-scripts-nosetests-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgat-scripts-nosetests-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgat-scripts-nosetests-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgat-scripts-nosetests-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgat-scripts-nosetests-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgat-scripts-nosetests-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### msql2mysql

```bash
$ singularity exec <container> /usr/local/bin/msql2mysql
$ podman run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msql2mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mysqltest

```bash
$ singularity exec <container> /usr/local/bin/mysqltest
$ podman run --it --rm --entrypoint /usr/local/bin/mysqltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqltest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pep8

```bash
$ singularity exec <container> /usr/local/bin/pep8
$ podman run --it --rm --entrypoint /usr/local/bin/pep8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pep8   -v ${PWD} -w ${PWD} <container> -c " $@"
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