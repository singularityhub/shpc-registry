---
layout: container
name:  "quay.io/biocontainers/hgvs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hgvs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hgvs/container.yaml"
updated_at: "2025-05-26 12:34:26.364935"
latest: "1.5.4--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/hgvs"
aliases:
 - "hgvs-shell"
 - "pyppeteer-install"
 - "seqrepo"
 - "sqlformat"
 - "yoyo"
 - "yoyo-migrate"
 - "iptest3"
 - "coloredlogs"
 - "iptest"
 - "humanfriendly"
 - "ipython3"
 - "tabulate"
 - "ipython"
 - "pg_config"
 - "pygmentize"
 - "normalizer"
versions:
 - "1.5.2--pyh5e36f6f_0"
 - "1.5.4--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for hgvs"
config: {"url": "https://biocontainers.pro/tools/hgvs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hgvs", "latest": {"1.5.4--pyh7cba7a3_0": "sha256:9dccfe14484409af1eeaeb82a0fdeb0986eadc7b4520afdb0db7c0f3af66245e"}, "tags": {"1.5.2--pyh5e36f6f_0": "sha256:1b37fcaafc7259c53732b87777ec0f06dbd385a6cc99d76e62495c06d2db0554", "1.5.4--pyh7cba7a3_0": "sha256:9dccfe14484409af1eeaeb82a0fdeb0986eadc7b4520afdb0db7c0f3af66245e"}, "docker": "quay.io/biocontainers/hgvs", "aliases": {"hgvs-shell": "/usr/local/bin/hgvs-shell", "pyppeteer-install": "/usr/local/bin/pyppeteer-install", "seqrepo": "/usr/local/bin/seqrepo", "sqlformat": "/usr/local/bin/sqlformat", "yoyo": "/usr/local/bin/yoyo", "yoyo-migrate": "/usr/local/bin/yoyo-migrate", "iptest3": "/usr/local/bin/iptest3", "coloredlogs": "/usr/local/bin/coloredlogs", "iptest": "/usr/local/bin/iptest", "humanfriendly": "/usr/local/bin/humanfriendly", "ipython3": "/usr/local/bin/ipython3", "tabulate": "/usr/local/bin/tabulate", "ipython": "/usr/local/bin/ipython", "pg_config": "/usr/local/bin/pg_config", "pygmentize": "/usr/local/bin/pygmentize", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hgvs.
shpc-registry automated BioContainers addition for hgvs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hgvs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hgvs:1.5.4--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hgvs/1.5.4--pyh7cba7a3_0
$ module help quay.io/biocontainers/hgvs/1.5.4--pyh7cba7a3_0
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


#### iptest3

```bash
$ singularity exec <container> /usr/local/bin/iptest3
$ podman run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config

```bash
$ singularity exec <container> /usr/local/bin/pg_config
$ podman run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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