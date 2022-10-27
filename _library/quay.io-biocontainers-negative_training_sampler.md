---
layout: container
name:  "quay.io/biocontainers/negative_training_sampler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/negative_training_sampler/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/negative_training_sampler/container.yaml"
updated_at: "2022-10-27 00:24:24.146779"
latest: "0.3.1--py_0"
container_url: "https://biocontainers.pro/tools/negative_training_sampler"
aliases:
 - "negative_training_sampler"
versions:
 - "0.3.1--py_0"
description: "shpc-registry automated BioContainers addition for negative_training_sampler"
config: {"url": "https://biocontainers.pro/tools/negative_training_sampler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for negative_training_sampler", "latest": {"0.3.1--py_0": "sha256:47b6ea9fe250d7c44a9c52a7a465fb5efac9586105645bb674f203f87e41f7a8"}, "tags": {"0.3.1--py_0": "sha256:47b6ea9fe250d7c44a9c52a7a465fb5efac9586105645bb674f203f87e41f7a8"}, "docker": "quay.io/biocontainers/negative_training_sampler", "aliases": {"negative_training_sampler": "/usr/local/bin/negative_training_sampler"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/negative_training_sampler.
shpc-registry automated BioContainers addition for negative_training_sampler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/negative_training_sampler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/negative_training_sampler:0.3.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/negative_training_sampler/0.3.1--py_0
$ module help quay.io/biocontainers/negative_training_sampler/0.3.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### negative_training_sampler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### negative_training_sampler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### negative_training_sampler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### negative_training_sampler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### negative_training_sampler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### negative_training_sampler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### negative_training_sampler

```bash
$ singularity exec <container> /usr/local/bin/negative_training_sampler
$ podman run --it --rm --entrypoint /usr/local/bin/negative_training_sampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/negative_training_sampler   -v ${PWD} -w ${PWD} <container> -c " $@"
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