---
layout: container
name:  "quay.io/biocontainers/mqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mqc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mqc/container.yaml"
updated_at: "2022-10-27 01:13:04.779241"
latest: "1.9--py27pl5.22.0r3.4.1_0"
container_url: "https://biocontainers.pro/tools/mqc"
aliases:
 - "counts_in_region"
 - "crossmap"
 - "cs"
 - "findjuncs"
 - "get_count_vectors"
 - "gff_parent_types"
 - "mQC.pl"
 - "make_wiggle"
 - "metagene"
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
 - "phase_by_size"
 - "psite"
 - "reformat_transcripts"
 - "replace"
 - "resolve_stack_dump"
 - "resolveip"
 - "slidejuncs"
 - "test_table_equality"
versions:
 - "1.9--py27pl5.22.0r3.4.1_0"
description: "shpc-registry automated BioContainers addition for mqc"
config: {"url": "https://biocontainers.pro/tools/mqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mqc", "latest": {"1.9--py27pl5.22.0r3.4.1_0": "sha256:110ab9a3cf3cd61822b66ef8bfdbe08220f8431032f23c3dbddc8e7d60b1f566"}, "tags": {"1.9--py27pl5.22.0r3.4.1_0": "sha256:110ab9a3cf3cd61822b66ef8bfdbe08220f8431032f23c3dbddc8e7d60b1f566"}, "docker": "quay.io/biocontainers/mqc", "aliases": {"counts_in_region": "/usr/local/bin/counts_in_region", "crossmap": "/usr/local/bin/crossmap", "cs": "/usr/local/bin/cs", "findjuncs": "/usr/local/bin/findjuncs", "get_count_vectors": "/usr/local/bin/get_count_vectors", "gff_parent_types": "/usr/local/bin/gff_parent_types", "mQC.pl": "/usr/local/bin/mQC.pl", "make_wiggle": "/usr/local/bin/make_wiggle", "metagene": "/usr/local/bin/metagene", "msql2mysql": "/usr/local/bin/msql2mysql", "mysql_client_test": "/usr/local/bin/mysql_client_test", "mysql_convert_table_format": "/usr/local/bin/mysql_convert_table_format", "mysql_find_rows": "/usr/local/bin/mysql_find_rows", "mysql_fix_extensions": "/usr/local/bin/mysql_fix_extensions", "mysql_plugin": "/usr/local/bin/mysql_plugin", "mysql_setpermission": "/usr/local/bin/mysql_setpermission", "mysql_waitpid": "/usr/local/bin/mysql_waitpid", "mysql_zap": "/usr/local/bin/mysql_zap", "mysqlaccess": "/usr/local/bin/mysqlaccess", "mysqlaccess.conf": "/usr/local/bin/mysqlaccess.conf", "mysqlbug": "/usr/local/bin/mysqlbug", "mysqlhotcopy": "/usr/local/bin/mysqlhotcopy", "mysqltest": "/usr/local/bin/mysqltest", "phase_by_size": "/usr/local/bin/phase_by_size", "psite": "/usr/local/bin/psite", "reformat_transcripts": "/usr/local/bin/reformat_transcripts", "replace": "/usr/local/bin/replace", "resolve_stack_dump": "/usr/local/bin/resolve_stack_dump", "resolveip": "/usr/local/bin/resolveip", "slidejuncs": "/usr/local/bin/slidejuncs", "test_table_equality": "/usr/local/bin/test_table_equality"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mqc.
shpc-registry automated BioContainers addition for mqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mqc:1.9--py27pl5.22.0r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mqc/1.9--py27pl5.22.0r3.4.1_0
$ module help quay.io/biocontainers/mqc/1.9--py27pl5.22.0r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### counts_in_region

```bash
$ singularity exec <container> /usr/local/bin/counts_in_region
$ podman run --it --rm --entrypoint /usr/local/bin/counts_in_region   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/counts_in_region   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossmap

```bash
$ singularity exec <container> /usr/local/bin/crossmap
$ podman run --it --rm --entrypoint /usr/local/bin/crossmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cs

```bash
$ singularity exec <container> /usr/local/bin/cs
$ podman run --it --rm --entrypoint /usr/local/bin/cs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findjuncs

```bash
$ singularity exec <container> /usr/local/bin/findjuncs
$ podman run --it --rm --entrypoint /usr/local/bin/findjuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findjuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_count_vectors

```bash
$ singularity exec <container> /usr/local/bin/get_count_vectors
$ podman run --it --rm --entrypoint /usr/local/bin/get_count_vectors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_count_vectors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff_parent_types

```bash
$ singularity exec <container> /usr/local/bin/gff_parent_types
$ podman run --it --rm --entrypoint /usr/local/bin/gff_parent_types   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff_parent_types   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mQC.pl

```bash
$ singularity exec <container> /usr/local/bin/mQC.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mQC.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mQC.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_wiggle

```bash
$ singularity exec <container> /usr/local/bin/make_wiggle
$ podman run --it --rm --entrypoint /usr/local/bin/make_wiggle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_wiggle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metagene

```bash
$ singularity exec <container> /usr/local/bin/metagene
$ podman run --it --rm --entrypoint /usr/local/bin/metagene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metagene   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### phase_by_size

```bash
$ singularity exec <container> /usr/local/bin/phase_by_size
$ podman run --it --rm --entrypoint /usr/local/bin/phase_by_size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phase_by_size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psite

```bash
$ singularity exec <container> /usr/local/bin/psite
$ podman run --it --rm --entrypoint /usr/local/bin/psite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformat_transcripts

```bash
$ singularity exec <container> /usr/local/bin/reformat_transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/reformat_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformat_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### slidejuncs

```bash
$ singularity exec <container> /usr/local/bin/slidejuncs
$ podman run --it --rm --entrypoint /usr/local/bin/slidejuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slidejuncs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_table_equality

```bash
$ singularity exec <container> /usr/local/bin/test_table_equality
$ podman run --it --rm --entrypoint /usr/local/bin/test_table_equality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_table_equality   -v ${PWD} -w ${PWD} <container> -c " $@"
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