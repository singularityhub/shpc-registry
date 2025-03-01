---
layout: container
name:  "quay.io/biocontainers/perl-db-file"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-db-file/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-db-file/container.yaml"
updated_at: "2025-03-01 03:33:27.354588"
latest: "1.855--pl5321h779adbc_1"
container_url: "https://biocontainers.pro/tools/perl-db-file"
aliases:
 - "db_convert"
 - "db_archive"
 - "db_checkpoint"
 - "db_deadlock"
 - "db_dump"
 - "db_hotbackup"
 - "db_load"
 - "db_log_verify"
 - "db_printlog"
 - "db_recover"
versions:
 - "1.855--pl5321h779adbc_1"
description: "shpc-registry automated BioContainers addition for perl-db-file"
config: {"url": "https://biocontainers.pro/tools/perl-db-file", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-db-file", "latest": {"1.855--pl5321h779adbc_1": "sha256:30ddaf79506f3237e0d95f5db673a3d89baeb932801da71dbe8ed3782f851d7c"}, "tags": {"1.855--pl5321h779adbc_1": "sha256:30ddaf79506f3237e0d95f5db673a3d89baeb932801da71dbe8ed3782f851d7c"}, "docker": "quay.io/biocontainers/perl-db-file", "aliases": {"db_convert": "/usr/local/bin/db_convert", "db_archive": "/usr/local/bin/db_archive", "db_checkpoint": "/usr/local/bin/db_checkpoint", "db_deadlock": "/usr/local/bin/db_deadlock", "db_dump": "/usr/local/bin/db_dump", "db_hotbackup": "/usr/local/bin/db_hotbackup", "db_load": "/usr/local/bin/db_load", "db_log_verify": "/usr/local/bin/db_log_verify", "db_printlog": "/usr/local/bin/db_printlog", "db_recover": "/usr/local/bin/db_recover"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-db-file.
shpc-registry automated BioContainers addition for perl-db-file
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-db-file
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-db-file:1.855--pl5321h779adbc_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-db-file/1.855--pl5321h779adbc_1
$ module help quay.io/biocontainers/perl-db-file/1.855--pl5321h779adbc_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-db-file-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-db-file-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-db-file-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-db-file-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-db-file-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-db-file-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### db_convert

```bash
$ singularity exec <container> /usr/local/bin/db_convert
$ podman run --it --rm --entrypoint /usr/local/bin/db_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_archive

```bash
$ singularity exec <container> /usr/local/bin/db_archive
$ podman run --it --rm --entrypoint /usr/local/bin/db_archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_checkpoint

```bash
$ singularity exec <container> /usr/local/bin/db_checkpoint
$ podman run --it --rm --entrypoint /usr/local/bin/db_checkpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_checkpoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_deadlock

```bash
$ singularity exec <container> /usr/local/bin/db_deadlock
$ podman run --it --rm --entrypoint /usr/local/bin/db_deadlock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_deadlock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_dump

```bash
$ singularity exec <container> /usr/local/bin/db_dump
$ podman run --it --rm --entrypoint /usr/local/bin/db_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_hotbackup

```bash
$ singularity exec <container> /usr/local/bin/db_hotbackup
$ podman run --it --rm --entrypoint /usr/local/bin/db_hotbackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_hotbackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_load

```bash
$ singularity exec <container> /usr/local/bin/db_load
$ podman run --it --rm --entrypoint /usr/local/bin/db_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_log_verify

```bash
$ singularity exec <container> /usr/local/bin/db_log_verify
$ podman run --it --rm --entrypoint /usr/local/bin/db_log_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_log_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_printlog

```bash
$ singularity exec <container> /usr/local/bin/db_printlog
$ podman run --it --rm --entrypoint /usr/local/bin/db_printlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_printlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_recover

```bash
$ singularity exec <container> /usr/local/bin/db_recover
$ podman run --it --rm --entrypoint /usr/local/bin/db_recover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_recover   -v ${PWD} -w ${PWD} <container> -c " $@"
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