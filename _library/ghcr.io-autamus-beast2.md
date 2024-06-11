---
layout: container
name:  "ghcr.io/autamus/beast2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/beast2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/beast2/container.yaml"
updated_at: "2024-06-11 05:46:27.073202"
latest: "2.6.6"
container_url: "https://github.com/orgs/autamus/packages/container/package/beast2"
aliases:
 - "beast"
 - "beasti"
 - "beauti"
 - "densitree"
 - "treeannotator"
versions:
 - "2.6.3"
 - "2.6.4"
 - "2.6.6"
 - "latest"
description: "BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis of molecular sequences."
config: {"docker": "ghcr.io/autamus/beast2", "url": "https://github.com/orgs/autamus/packages/container/package/beast2", "maintainer": "@vsoch", "description": "BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis of molecular sequences.", "latest": {"2.6.6": "sha256:eafce978acb4c26a2ed3d7806a7ef7cdeba4ad94d96154ee1cdda32dce77144b"}, "tags": {"2.6.3": "sha256:5eae1eabe7b127b3847401fe69e3430f97936d7ef7198287aabe01c5e1a957cf", "2.6.4": "sha256:cc2db4b4748d750a8b62e0f6984c2c09b87815e59a8ca66ba2cfbaf33862f0db", "2.6.6": "sha256:eafce978acb4c26a2ed3d7806a7ef7cdeba4ad94d96154ee1cdda32dce77144b", "latest": "sha256:eafce978acb4c26a2ed3d7806a7ef7cdeba4ad94d96154ee1cdda32dce77144b"}, "aliases": {"beast": "/opt/view/bin/beast", "beasti": "/opt/view/bin/beasti", "beauti": "/opt/view/bin/beauti", "densitree": "/opt/view/bin/densitree", "treeannotator": "/opt/view/bin/treeannotator"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/beast2.
BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis of molecular sequences.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/beast2
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/beast2:2.6.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/beast2/2.6.6
$ module help ghcr.io/autamus/beast2/2.6.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### beast2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### beast2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### beast2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### beast2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### beast2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### beast2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beast

```bash
$ singularity exec <container> /opt/view/bin/beast
$ podman run --it --rm --entrypoint /opt/view/bin/beast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/beast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beasti

```bash
$ singularity exec <container> /opt/view/bin/beasti
$ podman run --it --rm --entrypoint /opt/view/bin/beasti   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/beasti   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beauti

```bash
$ singularity exec <container> /opt/view/bin/beauti
$ podman run --it --rm --entrypoint /opt/view/bin/beauti   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/beauti   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### densitree

```bash
$ singularity exec <container> /opt/view/bin/densitree
$ podman run --it --rm --entrypoint /opt/view/bin/densitree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/densitree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeannotator

```bash
$ singularity exec <container> /opt/view/bin/treeannotator
$ podman run --it --rm --entrypoint /opt/view/bin/treeannotator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/treeannotator   -v ${PWD} -w ${PWD} <container> -c " $@"
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