---
layout: container
name:  "quay.io/biocontainers/hgvs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hgvs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hgvs/container.yaml"
updated_at: "2022-10-27 00:51:31.033664"
latest: "1.5.2--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/hgvs"
aliases:
 - "hgvs-shell"
 - "pyppeteer-install"
 - "seqrepo"
 - "sqlformat"
 - "yoyo"
 - "yoyo-migrate"
versions:
 - "1.5.2--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for hgvs"
config: {"url": "https://biocontainers.pro/tools/hgvs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hgvs", "latest": {"1.5.2--pyh5e36f6f_0": "sha256:1b37fcaafc7259c53732b87777ec0f06dbd385a6cc99d76e62495c06d2db0554"}, "tags": {"1.5.2--pyh5e36f6f_0": "sha256:1b37fcaafc7259c53732b87777ec0f06dbd385a6cc99d76e62495c06d2db0554"}, "docker": "quay.io/biocontainers/hgvs", "aliases": {"hgvs-shell": "/usr/local/bin/hgvs-shell", "pyppeteer-install": "/usr/local/bin/pyppeteer-install", "seqrepo": "/usr/local/bin/seqrepo", "sqlformat": "/usr/local/bin/sqlformat", "yoyo": "/usr/local/bin/yoyo", "yoyo-migrate": "/usr/local/bin/yoyo-migrate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hgvs.
shpc-registry automated BioContainers addition for hgvs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hgvs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hgvs:1.5.2--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hgvs/1.5.2--pyh5e36f6f_0
$ module help quay.io/biocontainers/hgvs/1.5.2--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hgvs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hgvs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hgvs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hgvs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hgvs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hgvs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hgvs-shell

```bash
$ singularity exec <container> /usr/local/bin/hgvs-shell
$ podman run --it --rm --entrypoint /usr/local/bin/hgvs-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hgvs-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyppeteer-install

```bash
$ singularity exec <container> /usr/local/bin/pyppeteer-install
$ podman run --it --rm --entrypoint /usr/local/bin/pyppeteer-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyppeteer-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqrepo

```bash
$ singularity exec <container> /usr/local/bin/seqrepo
$ podman run --it --rm --entrypoint /usr/local/bin/seqrepo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqrepo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqlformat

```bash
$ singularity exec <container> /usr/local/bin/sqlformat
$ podman run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yoyo

```bash
$ singularity exec <container> /usr/local/bin/yoyo
$ podman run --it --rm --entrypoint /usr/local/bin/yoyo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yoyo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yoyo-migrate

```bash
$ singularity exec <container> /usr/local/bin/yoyo-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/yoyo-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yoyo-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
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