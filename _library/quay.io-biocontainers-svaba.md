---
layout: container
name:  "quay.io/biocontainers/svaba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svaba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svaba/container.yaml"
updated_at: "2024-03-31 03:05:50.001103"
latest: "1.1.0--hf5e1c6e_5"
container_url: "https://biocontainers.pro/tools/svaba"
aliases:
 - "svaba"
versions:
 - "1.1.0--h468198e_3"
 - "1.1.0--hf5e1c6e_5"
description: "shpc-registry automated BioContainers addition for svaba"
config: {"url": "https://biocontainers.pro/tools/svaba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svaba", "latest": {"1.1.0--hf5e1c6e_5": "sha256:4a4b1553b8a866da753a38c9ed67c9755c781be40d556ef6bc534f8feb869525"}, "tags": {"1.1.0--h468198e_3": "sha256:d28106577442ab2bb1153208eadd7af371a54e8238ab2d62cf3295419b77018b", "1.1.0--hf5e1c6e_5": "sha256:4a4b1553b8a866da753a38c9ed67c9755c781be40d556ef6bc534f8feb869525"}, "docker": "quay.io/biocontainers/svaba", "aliases": {"svaba": "/usr/local/bin/svaba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svaba.
shpc-registry automated BioContainers addition for svaba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svaba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svaba:1.1.0--hf5e1c6e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svaba/1.1.0--hf5e1c6e_5
$ module help quay.io/biocontainers/svaba/1.1.0--hf5e1c6e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svaba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svaba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svaba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svaba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svaba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svaba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### svaba

```bash
$ singularity exec <container> /usr/local/bin/svaba
$ podman run --it --rm --entrypoint /usr/local/bin/svaba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svaba   -v ${PWD} -w ${PWD} <container> -c " $@"
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