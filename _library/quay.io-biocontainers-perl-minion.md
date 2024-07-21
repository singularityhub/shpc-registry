---
layout: container
name:  "quay.io/biocontainers/perl-minion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-minion/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-minion/container.yaml"
updated_at: "2024-07-21 03:20:36.612338"
latest: "10.30--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-minion"
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
 - "10.25--pl5321hdfd78af_0"
 - "10.27--pl5321hdfd78af_0"
 - "10.26--pl5321hdfd78af_0"
 - "10.28--pl5321hdfd78af_0"
 - "10.29--pl5321hdfd78af_0"
 - "10.30--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for perl-minion"
config: {"url": "https://biocontainers.pro/tools/perl-minion", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-minion", "latest": {"10.30--pl5321hdfd78af_0": "sha256:21fe71f4b8fa27b098035bbfb81b8a07c355831bce7d6e28e63f620636da1e5d"}, "tags": {"10.25--pl5321hdfd78af_0": "sha256:02209cef337b913ad90efbbced8bc9521b1e4e9601fbdaed48ab86ef78a913e2", "10.27--pl5321hdfd78af_0": "sha256:1f0a6e42472c20b0eefd114c6c118b3b18c3a9bd80cd800e71c6593a796ae5b3", "10.26--pl5321hdfd78af_0": "sha256:43035972fbd10c4ebf1c6eb8cf7ecdaf482f1fa5987c71dcc735b9ad82580170", "10.28--pl5321hdfd78af_0": "sha256:349a1c0ee336e6a28961da55039ba87f632c9d386f8cdb38863f52d52bec789e", "10.29--pl5321hdfd78af_0": "sha256:e394c5343be4dc852ae053053b8edac5311a098ccc040b80738cc40699f104df", "10.30--pl5321hdfd78af_0": "sha256:21fe71f4b8fa27b098035bbfb81b8a07c355831bce7d6e28e63f620636da1e5d"}, "docker": "quay.io/biocontainers/perl-minion", "aliases": {"hypnotoad": "/usr/local/bin/hypnotoad", "mojo": "/usr/local/bin/mojo", "morbo": "/usr/local/bin/morbo", "pg_amcheck": "/usr/local/bin/pg_amcheck", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "pg_checksums": "/usr/local/bin/pg_checksums", "tzselect": "/usr/local/bin/tzselect", "zdump": "/usr/local/bin/zdump", "zic": "/usr/local/bin/zic", "oid2name": "/usr/local/bin/oid2name", "pg_receivewal": "/usr/local/bin/pg_receivewal", "pg_resetwal": "/usr/local/bin/pg_resetwal", "pg_waldump": "/usr/local/bin/pg_waldump", "vacuumlo": "/usr/local/bin/vacuumlo", "clusterdb": "/usr/local/bin/clusterdb", "createdb": "/usr/local/bin/createdb", "createuser": "/usr/local/bin/createuser", "dropdb": "/usr/local/bin/dropdb", "dropuser": "/usr/local/bin/dropuser", "ecpg": "/usr/local/bin/ecpg", "initdb": "/usr/local/bin/initdb", "pg_archivecleanup": "/usr/local/bin/pg_archivecleanup", "pg_basebackup": "/usr/local/bin/pg_basebackup", "pg_controldata": "/usr/local/bin/pg_controldata", "pg_ctl": "/usr/local/bin/pg_ctl", "pg_dump": "/usr/local/bin/pg_dump", "pg_dumpall": "/usr/local/bin/pg_dumpall", "pg_isready": "/usr/local/bin/pg_isready"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-minion.
singularity registry hpc automated addition for perl-minion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-minion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-minion:10.30--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-minion/10.30--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-minion/10.30--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-minion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-minion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-minion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-minion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-minion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-minion-inspect-deffile:

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