---
layout: container
name:  "quay.io/biocontainers/flexserv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flexserv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flexserv/container.yaml"
updated_at: "2024-01-09 02:39:37.101843"
latest: "1.0.2--h8537716_2"
container_url: "https://biocontainers.pro/tools/flexserv"
aliases:
 - "bd"
 - "diaghess"
 - "dmdgoopt"
 - "lorellnma"
 - "mc-eigen-mdweb.pl"
 - "mc-eigen.pl"
 - "nmanu.pl"
 - "pca_anim_mc.pl"
versions:
 - "1.0.2--h1aed7a7_0"
 - "1.0.2--h8537716_2"
description: "singularity registry hpc automated addition for flexserv"
config: {"url": "https://biocontainers.pro/tools/flexserv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for flexserv", "latest": {"1.0.2--h8537716_2": "sha256:d6699809506f464a707acb27d48c5145f59dd3dc27c9abafc16a9f77f7d3be91"}, "tags": {"1.0.2--h1aed7a7_0": "sha256:986a5db952a3b1073feab9cb9caf857d438292b417eff9f3334d61e91222c5d8", "1.0.2--h8537716_2": "sha256:d6699809506f464a707acb27d48c5145f59dd3dc27c9abafc16a9f77f7d3be91"}, "docker": "quay.io/biocontainers/flexserv", "aliases": {"bd": "/usr/local/bin/bd", "diaghess": "/usr/local/bin/diaghess", "dmdgoopt": "/usr/local/bin/dmdgoopt", "lorellnma": "/usr/local/bin/lorellnma", "mc-eigen-mdweb.pl": "/usr/local/bin/mc-eigen-mdweb.pl", "mc-eigen.pl": "/usr/local/bin/mc-eigen.pl", "nmanu.pl": "/usr/local/bin/nmanu.pl", "pca_anim_mc.pl": "/usr/local/bin/pca_anim_mc.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flexserv.
singularity registry hpc automated addition for flexserv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flexserv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flexserv:1.0.2--h8537716_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flexserv/1.0.2--h8537716_2
$ module help quay.io/biocontainers/flexserv/1.0.2--h8537716_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flexserv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flexserv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flexserv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flexserv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flexserv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flexserv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bd

```bash
$ singularity exec <container> /usr/local/bin/bd
$ podman run --it --rm --entrypoint /usr/local/bin/bd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diaghess

```bash
$ singularity exec <container> /usr/local/bin/diaghess
$ podman run --it --rm --entrypoint /usr/local/bin/diaghess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diaghess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmdgoopt

```bash
$ singularity exec <container> /usr/local/bin/dmdgoopt
$ podman run --it --rm --entrypoint /usr/local/bin/dmdgoopt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmdgoopt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lorellnma

```bash
$ singularity exec <container> /usr/local/bin/lorellnma
$ podman run --it --rm --entrypoint /usr/local/bin/lorellnma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lorellnma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mc-eigen-mdweb.pl

```bash
$ singularity exec <container> /usr/local/bin/mc-eigen-mdweb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mc-eigen-mdweb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mc-eigen-mdweb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mc-eigen.pl

```bash
$ singularity exec <container> /usr/local/bin/mc-eigen.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mc-eigen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mc-eigen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nmanu.pl

```bash
$ singularity exec <container> /usr/local/bin/nmanu.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nmanu.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nmanu.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pca_anim_mc.pl

```bash
$ singularity exec <container> /usr/local/bin/pca_anim_mc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pca_anim_mc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pca_anim_mc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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