---
layout: container
name:  "quay.io/biocontainers/perl-minion-backend-sqlite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-minion-backend-sqlite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-minion-backend-sqlite/container.yaml"
updated_at: "2024-12-05 03:31:18.228072"
latest: "5.0.7--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-minion-backend-sqlite"
aliases:
 - "hypnotoad"
 - "mojo"
 - "morbo"
 - "pg_amcheck"
 - "pg_verifybackup"
 - "pg_checksums"
 - "tzselect"
 - "zdump"
 - "zic"
 - "oid2name"
 - "pg_receivewal"
 - "pg_resetwal"
 - "pg_waldump"
 - "vacuumlo"
 - "clusterdb"
 - "createdb"
 - "createuser"
 - "dropdb"
 - "dropuser"
 - "ecpg"
 - "initdb"
 - "pg_archivecleanup"
 - "pg_basebackup"
 - "pg_controldata"
 - "pg_ctl"
 - "pg_dump"
 - "pg_dumpall"
 - "pg_isready"
versions:
 - "5.0.7--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for perl-minion-backend-sqlite"
config: {"url": "https://biocontainers.pro/tools/perl-minion-backend-sqlite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-minion-backend-sqlite", "latest": {"5.0.7--pl5321hdfd78af_0": "sha256:124f029d01bb90064afb60bb4d646d9482105bda49c241cb0113261405a3370b"}, "tags": {"5.0.7--pl5321hdfd78af_0": "sha256:124f029d01bb90064afb60bb4d646d9482105bda49c241cb0113261405a3370b"}, "docker": "quay.io/biocontainers/perl-minion-backend-sqlite", "aliases": {"hypnotoad": "/usr/local/bin/hypnotoad", "mojo": "/usr/local/bin/mojo", "morbo": "/usr/local/bin/morbo", "pg_amcheck": "/usr/local/bin/pg_amcheck", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "pg_checksums": "/usr/local/bin/pg_checksums", "tzselect": "/usr/local/bin/tzselect", "zdump": "/usr/local/bin/zdump", "zic": "/usr/local/bin/zic", "oid2name": "/usr/local/bin/oid2name", "pg_receivewal": "/usr/local/bin/pg_receivewal", "pg_resetwal": "/usr/local/bin/pg_resetwal", "pg_waldump": "/usr/local/bin/pg_waldump", "vacuumlo": "/usr/local/bin/vacuumlo", "clusterdb": "/usr/local/bin/clusterdb", "createdb": "/usr/local/bin/createdb", "createuser": "/usr/local/bin/createuser", "dropdb": "/usr/local/bin/dropdb", "dropuser": "/usr/local/bin/dropuser", "ecpg": "/usr/local/bin/ecpg", "initdb": "/usr/local/bin/initdb", "pg_archivecleanup": "/usr/local/bin/pg_archivecleanup", "pg_basebackup": "/usr/local/bin/pg_basebackup", "pg_controldata": "/usr/local/bin/pg_controldata", "pg_ctl": "/usr/local/bin/pg_ctl", "pg_dump": "/usr/local/bin/pg_dump", "pg_dumpall": "/usr/local/bin/pg_dumpall", "pg_isready": "/usr/local/bin/pg_isready"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-minion-backend-sqlite.
singularity registry hpc automated addition for perl-minion-backend-sqlite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-minion-backend-sqlite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-minion-backend-sqlite:5.0.7--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-minion-backend-sqlite/5.0.7--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-minion-backend-sqlite/5.0.7--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-minion-backend-sqlite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-minion-backend-sqlite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-minion-backend-sqlite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-minion-backend-sqlite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-minion-backend-sqlite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-minion-backend-sqlite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hypnotoad

```bash
$ singularity exec <container> /usr/local/bin/hypnotoad
$ podman run --it --rm --entrypoint /usr/local/bin/hypnotoad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypnotoad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mojo

```bash
$ singularity exec <container> /usr/local/bin/mojo
$ podman run --it --rm --entrypoint /usr/local/bin/mojo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mojo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### morbo

```bash
$ singularity exec <container> /usr/local/bin/morbo
$ podman run --it --rm --entrypoint /usr/local/bin/morbo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/morbo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_amcheck

```bash
$ singularity exec <container> /usr/local/bin/pg_amcheck
$ podman run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_verifybackup

```bash
$ singularity exec <container> /usr/local/bin/pg_verifybackup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_checksums

```bash
$ singularity exec <container> /usr/local/bin/pg_checksums
$ podman run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tzselect

```bash
$ singularity exec <container> /usr/local/bin/tzselect
$ podman run --it --rm --entrypoint /usr/local/bin/tzselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tzselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdump

```bash
$ singularity exec <container> /usr/local/bin/zdump
$ podman run --it --rm --entrypoint /usr/local/bin/zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zic

```bash
$ singularity exec <container> /usr/local/bin/zic
$ podman run --it --rm --entrypoint /usr/local/bin/zic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oid2name

```bash
$ singularity exec <container> /usr/local/bin/oid2name
$ podman run --it --rm --entrypoint /usr/local/bin/oid2name   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oid2name   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_receivewal

```bash
$ singularity exec <container> /usr/local/bin/pg_receivewal
$ podman run --it --rm --entrypoint /usr/local/bin/pg_receivewal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_receivewal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_resetwal

```bash
$ singularity exec <container> /usr/local/bin/pg_resetwal
$ podman run --it --rm --entrypoint /usr/local/bin/pg_resetwal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_resetwal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_waldump

```bash
$ singularity exec <container> /usr/local/bin/pg_waldump
$ podman run --it --rm --entrypoint /usr/local/bin/pg_waldump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_waldump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vacuumlo

```bash
$ singularity exec <container> /usr/local/bin/vacuumlo
$ podman run --it --rm --entrypoint /usr/local/bin/vacuumlo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vacuumlo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterdb

```bash
$ singularity exec <container> /usr/local/bin/clusterdb
$ podman run --it --rm --entrypoint /usr/local/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createdb

```bash
$ singularity exec <container> /usr/local/bin/createdb
$ podman run --it --rm --entrypoint /usr/local/bin/createdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createuser

```bash
$ singularity exec <container> /usr/local/bin/createuser
$ podman run --it --rm --entrypoint /usr/local/bin/createuser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createuser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropdb

```bash
$ singularity exec <container> /usr/local/bin/dropdb
$ podman run --it --rm --entrypoint /usr/local/bin/dropdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropuser

```bash
$ singularity exec <container> /usr/local/bin/dropuser
$ podman run --it --rm --entrypoint /usr/local/bin/dropuser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropuser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecpg

```bash
$ singularity exec <container> /usr/local/bin/ecpg
$ podman run --it --rm --entrypoint /usr/local/bin/ecpg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecpg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### initdb

```bash
$ singularity exec <container> /usr/local/bin/initdb
$ podman run --it --rm --entrypoint /usr/local/bin/initdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/initdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_archivecleanup

```bash
$ singularity exec <container> /usr/local/bin/pg_archivecleanup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_archivecleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_archivecleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_basebackup

```bash
$ singularity exec <container> /usr/local/bin/pg_basebackup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_basebackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_basebackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_controldata

```bash
$ singularity exec <container> /usr/local/bin/pg_controldata
$ podman run --it --rm --entrypoint /usr/local/bin/pg_controldata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_controldata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_ctl

```bash
$ singularity exec <container> /usr/local/bin/pg_ctl
$ podman run --it --rm --entrypoint /usr/local/bin/pg_ctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_ctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dump

```bash
$ singularity exec <container> /usr/local/bin/pg_dump
$ podman run --it --rm --entrypoint /usr/local/bin/pg_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dumpall

```bash
$ singularity exec <container> /usr/local/bin/pg_dumpall
$ podman run --it --rm --entrypoint /usr/local/bin/pg_dumpall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_dumpall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_isready

```bash
$ singularity exec <container> /usr/local/bin/pg_isready
$ podman run --it --rm --entrypoint /usr/local/bin/pg_isready   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_isready   -v ${PWD} -w ${PWD} <container> -c " $@"
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