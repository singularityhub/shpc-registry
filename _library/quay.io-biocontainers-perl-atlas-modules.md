---
layout: container
name:  "quay.io/biocontainers/perl-atlas-modules"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-atlas-modules/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-atlas-modules/container.yaml"
updated_at: "2024-01-13 02:37:58.934739"
latest: "0.3.1--pl5262hdbdd923_5"
container_url: "https://biocontainers.pro/tools/perl-atlas-modules"
aliases:
 - "crc32"
 - "dm_date"
 - "dm_zdump"
 - "validjson"
 - "pg_amcheck"
 - "pod_cover"
 - "pg_verifybackup"
 - "pg_checksums"
 - "findrule"
 - "tzselect"
 - "zdump"
 - "zic"
 - "oid2name"
 - "pg_receivewal"
versions:
 - "0.3.1--pl5262h87f3376_3"
 - "0.3.1--pl5262h87f3376_4"
 - "0.3.1--pl5262hdbdd923_5"
description: "shpc-registry automated BioContainers addition for perl-atlas-modules"
config: {"url": "https://biocontainers.pro/tools/perl-atlas-modules", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-atlas-modules", "latest": {"0.3.1--pl5262hdbdd923_5": "sha256:86bfbf5b3f506692d934fa2e4b2e9f76a874162722f699378580a7c40661fb54"}, "tags": {"0.3.1--pl5262h87f3376_3": "sha256:36423ff98bcd6b1ee25252f3fc42c7d2312cbadc8629ecd5045120ac1eceb5de", "0.3.1--pl5262h87f3376_4": "sha256:a2a9a002f32ff63ba959b5399e63552c53e5a8faf854af2eba3f0e0dcac27338", "0.3.1--pl5262hdbdd923_5": "sha256:86bfbf5b3f506692d934fa2e4b2e9f76a874162722f699378580a7c40661fb54"}, "docker": "quay.io/biocontainers/perl-atlas-modules", "aliases": {"crc32": "/usr/local/bin/crc32", "dm_date": "/usr/local/bin/dm_date", "dm_zdump": "/usr/local/bin/dm_zdump", "validjson": "/usr/local/bin/validjson", "pg_amcheck": "/usr/local/bin/pg_amcheck", "pod_cover": "/usr/local/bin/pod_cover", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "pg_checksums": "/usr/local/bin/pg_checksums", "findrule": "/usr/local/bin/findrule", "tzselect": "/usr/local/bin/tzselect", "zdump": "/usr/local/bin/zdump", "zic": "/usr/local/bin/zic", "oid2name": "/usr/local/bin/oid2name", "pg_receivewal": "/usr/local/bin/pg_receivewal"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-atlas-modules.
shpc-registry automated BioContainers addition for perl-atlas-modules
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-atlas-modules
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-atlas-modules:0.3.1--pl5262hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-atlas-modules/0.3.1--pl5262hdbdd923_5
$ module help quay.io/biocontainers/perl-atlas-modules/0.3.1--pl5262hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-atlas-modules-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-atlas-modules-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-atlas-modules-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-atlas-modules-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-atlas-modules-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-atlas-modules-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dm_date

```bash
$ singularity exec <container> /usr/local/bin/dm_date
$ podman run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dm_zdump

```bash
$ singularity exec <container> /usr/local/bin/dm_zdump
$ podman run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validjson

```bash
$ singularity exec <container> /usr/local/bin/validjson
$ podman run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validjson   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_amcheck

```bash
$ singularity exec <container> /usr/local/bin/pg_amcheck
$ podman run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pod_cover

```bash
$ singularity exec <container> /usr/local/bin/pod_cover
$ podman run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
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