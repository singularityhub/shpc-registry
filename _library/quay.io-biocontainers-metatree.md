---
layout: container
name:  "quay.io/biocontainers/metatree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metatree/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metatree/container.yaml"
updated_at: "2022-10-27 00:25:57.185652"
latest: "0.0.1--py_0"
container_url: "https://biocontainers.pro/tools/metatree"
aliases:
 - "genometreetk"
 - "metatree"
 - "phylorank"
versions:
 - "0.0.1--py_0"
description: "shpc-registry automated BioContainers addition for metatree"
config: {"url": "https://biocontainers.pro/tools/metatree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metatree", "latest": {"0.0.1--py_0": "sha256:bd67bc970e530439c7254daaf1a81a98b0da0c2ed8585a6f45dd3121671e426d"}, "tags": {"0.0.1--py_0": "sha256:bd67bc970e530439c7254daaf1a81a98b0da0c2ed8585a6f45dd3121671e426d"}, "docker": "quay.io/biocontainers/metatree", "aliases": {"genometreetk": "/usr/local/bin/genometreetk", "metatree": "/usr/local/bin/metatree", "phylorank": "/usr/local/bin/phylorank"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metatree.
shpc-registry automated BioContainers addition for metatree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metatree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metatree:0.0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metatree/0.0.1--py_0
$ module help quay.io/biocontainers/metatree/0.0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metatree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metatree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metatree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metatree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metatree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metatree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genometreetk

```bash
$ singularity exec <container> /usr/local/bin/genometreetk
$ podman run --it --rm --entrypoint /usr/local/bin/genometreetk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genometreetk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metatree

```bash
$ singularity exec <container> /usr/local/bin/metatree
$ podman run --it --rm --entrypoint /usr/local/bin/metatree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metatree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phylorank

```bash
$ singularity exec <container> /usr/local/bin/phylorank
$ podman run --it --rm --entrypoint /usr/local/bin/phylorank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylorank   -v ${PWD} -w ${PWD} <container> -c " $@"
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