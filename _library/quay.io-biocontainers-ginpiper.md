---
layout: container
name:  "quay.io/biocontainers/ginpiper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ginpiper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ginpiper/container.yaml"
updated_at: "2025-12-06 03:20:19.088759"
latest: "1.0.0--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/ginpiper"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.0.0--r42hdfd78af_1"
 - "1.0.0--r43hdfd78af_2"
 - "1.0.0--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for ginpiper"
config: {"url": "https://biocontainers.pro/tools/ginpiper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ginpiper", "latest": {"1.0.0--r44hdfd78af_3": "sha256:42873af95c1c7346c2e4c1e66a9abba16404c6dcb55fc556ede8d135881e1b87"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:5a3ece21f9fc0ec60537ce2fedb0b69e387415076659dce0390187def6cd7340", "1.0.0--r42hdfd78af_1": "sha256:fbff1da8e62166fff192c036ae0a92a1aabf5c097c7129a3f31d27d06610b8db", "1.0.0--r43hdfd78af_2": "sha256:7807c8097ed40cd9947c1effaf5f6c1af4bd70a5317d6c374c1aa64e2d4a1024", "1.0.0--r44hdfd78af_3": "sha256:42873af95c1c7346c2e4c1e66a9abba16404c6dcb55fc556ede8d135881e1b87"}, "docker": "quay.io/biocontainers/ginpiper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ginpiper.
shpc-registry automated BioContainers addition for ginpiper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ginpiper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ginpiper:1.0.0--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ginpiper/1.0.0--r44hdfd78af_3
$ module help quay.io/biocontainers/ginpiper/1.0.0--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ginpiper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ginpiper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ginpiper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ginpiper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ginpiper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ginpiper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ginpiper

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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