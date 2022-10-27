---
layout: container
name:  "quay.io/biocontainers/flux-simulator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flux-simulator/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/flux-simulator/container.yaml"
updated_at: "2022-10-27 00:33:18.683169"
latest: "1.2.1--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/flux-simulator"
aliases:
 - "flux-simulator"
versions:
 - "1.2.1--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for flux-simulator"
config: {"url": "https://biocontainers.pro/tools/flux-simulator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flux-simulator", "latest": {"1.2.1--hdfd78af_3": "sha256:eaad8c268d387052f3c23ce08b7959dace127abb85b0b0d31463697b5b08e7c5"}, "tags": {"1.2.1--hdfd78af_3": "sha256:eaad8c268d387052f3c23ce08b7959dace127abb85b0b0d31463697b5b08e7c5"}, "docker": "quay.io/biocontainers/flux-simulator", "aliases": {"flux-simulator": "/usr/local/bin/flux-simulator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flux-simulator.
shpc-registry automated BioContainers addition for flux-simulator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flux-simulator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flux-simulator:1.2.1--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flux-simulator/1.2.1--hdfd78af_3
$ module help quay.io/biocontainers/flux-simulator/1.2.1--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flux-simulator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flux-simulator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flux-simulator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flux-simulator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flux-simulator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flux-simulator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flux-simulator

```bash
$ singularity exec <container> /usr/local/bin/flux-simulator
$ podman run --it --rm --entrypoint /usr/local/bin/flux-simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flux-simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
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