---
layout: container
name:  "quay.io/biocontainers/rnasnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnasnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnasnp/container.yaml"
updated_at: "2025-03-19 03:02:17.235859"
latest: "1.2--h503566f_10"
container_url: "https://biocontainers.pro/tools/rnasnp"
aliases:
 - "RNAsnp"
versions:
 - "1.2--h1b792b2_6"
 - "1.2--h87f3376_7"
 - "1.2--hdbdd923_9"
 - "1.2--h503566f_10"
description: "shpc-registry automated BioContainers addition for rnasnp"
config: {"url": "https://biocontainers.pro/tools/rnasnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnasnp", "latest": {"1.2--h503566f_10": "sha256:75488437f5ace2cae92c41b1ba2b238422d5ad31b60259c2fa6a68c083425da5"}, "tags": {"1.2--h1b792b2_6": "sha256:213f29bc7bf7bbaa4e2dc929bddac209e1b452867bf63662435dc5090a999362", "1.2--h87f3376_7": "sha256:8ad8e65d4b7d43f3c7732744eae1dbfd2cf3f1ad671f53a9c9a8a2002fc8eabe", "1.2--hdbdd923_9": "sha256:cf18049aa0e33387f7ed234b66760d61ebd9a3e30e7001dc62b810c73aa2487b", "1.2--h503566f_10": "sha256:75488437f5ace2cae92c41b1ba2b238422d5ad31b60259c2fa6a68c083425da5"}, "docker": "quay.io/biocontainers/rnasnp", "aliases": {"RNAsnp": "/usr/local/bin/RNAsnp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnasnp.
shpc-registry automated BioContainers addition for rnasnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnasnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnasnp:1.2--h503566f_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnasnp/1.2--h503566f_10
$ module help quay.io/biocontainers/rnasnp/1.2--h503566f_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnasnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnasnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnasnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnasnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnasnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnasnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAsnp

```bash
$ singularity exec <container> /usr/local/bin/RNAsnp
$ podman run --it --rm --entrypoint /usr/local/bin/RNAsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
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