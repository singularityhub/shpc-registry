---
layout: container
name:  "quay.io/biocontainers/sourmash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sourmash/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sourmash/container.yaml"
updated_at: "2022-10-27 00:30:40.093483"
latest: "2.0.0a9--py35hfc679d8_0"
container_url: "https://biocontainers.pro/tools/sourmash"
aliases:
 - "sourmash"
versions:
 - "2.0.0a9--py35hfc679d8_0"
description: "shpc-registry automated BioContainers addition for sourmash"
config: {"url": "https://biocontainers.pro/tools/sourmash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sourmash", "latest": {"2.0.0a9--py35hfc679d8_0": "sha256:3b1431a5ef4d7a71ecb85bde2147c400dfc89529a8b06fc8e59a8c8073e11874"}, "tags": {"2.0.0a9--py35hfc679d8_0": "sha256:3b1431a5ef4d7a71ecb85bde2147c400dfc89529a8b06fc8e59a8c8073e11874"}, "docker": "quay.io/biocontainers/sourmash", "aliases": {"sourmash": "/usr/local/bin/sourmash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sourmash.
shpc-registry automated BioContainers addition for sourmash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sourmash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sourmash:2.0.0a9--py35hfc679d8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sourmash/2.0.0a9--py35hfc679d8_0
$ module help quay.io/biocontainers/sourmash/2.0.0a9--py35hfc679d8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sourmash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sourmash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sourmash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sourmash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sourmash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sourmash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sourmash

```bash
$ singularity exec <container> /usr/local/bin/sourmash
$ podman run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sourmash   -v ${PWD} -w ${PWD} <container> -c " $@"
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