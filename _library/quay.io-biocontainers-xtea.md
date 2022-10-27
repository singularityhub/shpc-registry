---
layout: container
name:  "quay.io/biocontainers/xtea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xtea/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/xtea/container.yaml"
updated_at: "2022-10-27 01:02:08.696318"
latest: "0.1.9--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/xtea"
aliases:
 - "wtdbg-cns"
 - "wtdbg2"
 - "wtpoa-cns"
 - "xtea"
 - "xtea_hg19"
 - "xtea_long"
versions:
 - "0.1.9--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for xtea"
config: {"url": "https://biocontainers.pro/tools/xtea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xtea", "latest": {"0.1.9--hdfd78af_0": "sha256:0855c844a4e6298aacbbdef1d538507c33ab1683215b22b2b20aa0077af9bd42"}, "tags": {"0.1.9--hdfd78af_0": "sha256:0855c844a4e6298aacbbdef1d538507c33ab1683215b22b2b20aa0077af9bd42"}, "docker": "quay.io/biocontainers/xtea", "aliases": {"wtdbg-cns": "/usr/local/bin/wtdbg-cns", "wtdbg2": "/usr/local/bin/wtdbg2", "wtpoa-cns": "/usr/local/bin/wtpoa-cns", "xtea": "/usr/local/bin/xtea", "xtea_hg19": "/usr/local/bin/xtea_hg19", "xtea_long": "/usr/local/bin/xtea_long"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xtea.
shpc-registry automated BioContainers addition for xtea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xtea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xtea:0.1.9--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xtea/0.1.9--hdfd78af_0
$ module help quay.io/biocontainers/xtea/0.1.9--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xtea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xtea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xtea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xtea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xtea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xtea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wtdbg-cns

```bash
$ singularity exec <container> /usr/local/bin/wtdbg-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg2

```bash
$ singularity exec <container> /usr/local/bin/wtdbg2
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpoa-cns

```bash
$ singularity exec <container> /usr/local/bin/wtpoa-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtea

```bash
$ singularity exec <container> /usr/local/bin/xtea
$ podman run --it --rm --entrypoint /usr/local/bin/xtea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtea   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtea_hg19

```bash
$ singularity exec <container> /usr/local/bin/xtea_hg19
$ podman run --it --rm --entrypoint /usr/local/bin/xtea_hg19   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtea_hg19   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtea_long

```bash
$ singularity exec <container> /usr/local/bin/xtea_long
$ podman run --it --rm --entrypoint /usr/local/bin/xtea_long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtea_long   -v ${PWD} -w ${PWD} <container> -c " $@"
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