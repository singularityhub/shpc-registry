---
layout: container
name:  "quay.io/biocontainers/figtree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/figtree/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/figtree/container.yaml"
updated_at: "2022-10-27 01:14:05.604368"
latest: "1.4.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/figtree"
aliases:
 - "figtree"
versions:
 - "1.4.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for figtree"
config: {"url": "https://biocontainers.pro/tools/figtree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for figtree", "latest": {"1.4.4--hdfd78af_1": "sha256:f1c9736ebe836e37ff69078499926a6fb10df43959acf6eb4275e21b9216352e"}, "tags": {"1.4.4--hdfd78af_1": "sha256:f1c9736ebe836e37ff69078499926a6fb10df43959acf6eb4275e21b9216352e"}, "docker": "quay.io/biocontainers/figtree", "aliases": {"figtree": "/usr/local/bin/figtree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/figtree.
shpc-registry automated BioContainers addition for figtree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/figtree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/figtree:1.4.4--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/figtree/1.4.4--hdfd78af_1
$ module help quay.io/biocontainers/figtree/1.4.4--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### figtree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### figtree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### figtree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### figtree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### figtree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### figtree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### figtree

```bash
$ singularity exec <container> /usr/local/bin/figtree
$ podman run --it --rm --entrypoint /usr/local/bin/figtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/figtree   -v ${PWD} -w ${PWD} <container> -c " $@"
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