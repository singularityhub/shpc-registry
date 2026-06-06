---
layout: container
name:  "quay.io/biocontainers/grit-genomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grit-genomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grit-genomics/container.yaml"
updated_at: "2026-06-06 06:23:58.324681"
latest: "0.1.1--h79ce301_0"
container_url: "https://biocontainers.pro/tools/grit-genomics"
aliases:
 - "grit"
versions:
 - "0.1.1--h79ce301_0"
description: "singularity registry hpc automated addition for grit-genomics"
config: {"url": "https://biocontainers.pro/tools/grit-genomics", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grit-genomics", "latest": {"0.1.1--h79ce301_0": "sha256:bf5df0db36c16f32dbb6558fd04a4f0f4a3ebc867a8986bf0fb9149e0dd037a5"}, "tags": {"0.1.1--h79ce301_0": "sha256:bf5df0db36c16f32dbb6558fd04a4f0f4a3ebc867a8986bf0fb9149e0dd037a5"}, "docker": "quay.io/biocontainers/grit-genomics", "aliases": {"grit": "/usr/local/bin/grit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grit-genomics.
singularity registry hpc automated addition for grit-genomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grit-genomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grit-genomics:0.1.1--h79ce301_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grit-genomics/0.1.1--h79ce301_0
$ module help quay.io/biocontainers/grit-genomics/0.1.1--h79ce301_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grit-genomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grit-genomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grit-genomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grit-genomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grit-genomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grit-genomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grit

```bash
$ singularity exec <container> /usr/local/bin/grit
$ podman run --it --rm --entrypoint /usr/local/bin/grit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grit   -v ${PWD} -w ${PWD} <container> -c " $@"
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