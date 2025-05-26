---
layout: container
name:  "quay.io/biocontainers/perl-dbd-pg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-dbd-pg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-dbd-pg/container.yaml"
updated_at: "2025-05-26 03:28:21.100970"
latest: "3.18.0--pl5321h3a0becb_2"
container_url: "https://biocontainers.pro/tools/perl-dbd-pg"
aliases:
 - "pg_verify_checksums"
 - "pg_standby"
 - "tzselect"
 - "zdump"
 - "zic"
 - "oid2name"
 - "pg_receivewal"
 - "pg_resetwal"
 - "pg_waldump"
 - "vacuumlo"
 - "clusterdb"
versions:
 - "3.8.1--pl526h14c3975_0"
 - "3.16.0--pl5321hec16e2b_0"
 - "3.15.1--pl5321hec16e2b_1"
 - "3.16.0--pl5321hd072a1e_2"
 - "3.18.0--pl5321hbeff08c_0"
 - "3.16.0--pl5321hbeff08c_3"
 - "3.18.0--pl5321h3a0becb_1"
 - "3.18.0--pl5321h3a0becb_2"
description: "shpc-registry automated BioContainers addition for perl-dbd-pg"
config: {"url": "https://biocontainers.pro/tools/perl-dbd-pg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-dbd-pg", "latest": {"3.18.0--pl5321h3a0becb_2": "sha256:b5aa06851250c7cb79184ddfebb743b6a8b11a4216c6b8dae492d81301d2bb30"}, "tags": {"3.8.1--pl526h14c3975_0": "sha256:abda6024fe48d477d0f9ee3e6e26279a4f4cd0fe316a446b706c0d9ee75aab4b", "3.16.0--pl5321hec16e2b_0": "sha256:56731792fe6c89aae9cb565b187ac55423663830e46ee0cde1935678d5e0fee1", "3.15.1--pl5321hec16e2b_1": "sha256:243891b7d78398681df315fbfb093180b7fa42e8ad8d645628612f331936bac4", "3.16.0--pl5321hd072a1e_2": "sha256:b0f51db81fcb95a7e6722c32b6231d1ac3abb049779ea59f676774de396cdffb", "3.18.0--pl5321hbeff08c_0": "sha256:ad63c51c171a19edbfa9d4abfa0a92963d0330ed90e87e57404c122fa8f3777c", "3.16.0--pl5321hbeff08c_3": "sha256:e72542431090810e9c10c88d68c93d5d92dd4c7d81e33c33ada8f181200622e6", "3.18.0--pl5321h3a0becb_1": "sha256:1a0e01c7003bbcb73901abef9a1fafb6767a969c8434020c4bb7c7f2b163a348", "3.18.0--pl5321h3a0becb_2": "sha256:b5aa06851250c7cb79184ddfebb743b6a8b11a4216c6b8dae492d81301d2bb30"}, "docker": "quay.io/biocontainers/perl-dbd-pg", "aliases": {"pg_verify_checksums": "/usr/local/bin/pg_verify_checksums", "pg_standby": "/usr/local/bin/pg_standby", "tzselect": "/usr/local/bin/tzselect", "zdump": "/usr/local/bin/zdump", "zic": "/usr/local/bin/zic", "oid2name": "/usr/local/bin/oid2name", "pg_receivewal": "/usr/local/bin/pg_receivewal", "pg_resetwal": "/usr/local/bin/pg_resetwal", "pg_waldump": "/usr/local/bin/pg_waldump", "vacuumlo": "/usr/local/bin/vacuumlo", "clusterdb": "/usr/local/bin/clusterdb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-dbd-pg.
shpc-registry automated BioContainers addition for perl-dbd-pg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-dbd-pg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-dbd-pg:3.18.0--pl5321h3a0becb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-dbd-pg/3.18.0--pl5321h3a0becb_2
$ module help quay.io/biocontainers/perl-dbd-pg/3.18.0--pl5321h3a0becb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-dbd-pg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-dbd-pg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-dbd-pg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-dbd-pg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-dbd-pg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-dbd-pg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pg_verify_checksums

```bash
$ singularity exec <container> /usr/local/bin/pg_verify_checksums
$ podman run --it --rm --entrypoint /usr/local/bin/pg_verify_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_verify_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_standby

```bash
$ singularity exec <container> /usr/local/bin/pg_standby
$ podman run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
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