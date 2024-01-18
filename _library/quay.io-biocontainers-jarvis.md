---
layout: container
name:  "quay.io/biocontainers/jarvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jarvis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jarvis/container.yaml"
updated_at: "2024-01-18 03:18:58.531861"
latest: "1.1--h031d066_4"
container_url: "https://biocontainers.pro/tools/jarvis"
aliases:
 - "JARVIS"
versions:
 - "1.1--hec16e2b_2"
 - "1.1--h031d066_4"
description: "shpc-registry automated BioContainers addition for jarvis"
config: {"url": "https://biocontainers.pro/tools/jarvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jarvis", "latest": {"1.1--h031d066_4": "sha256:117b2e8a7aef1adbd82e04e038237761c5034f411cc4637c989c2ecc43bf57b9"}, "tags": {"1.1--hec16e2b_2": "sha256:f8f4754f154a2e1e85c90c9ba39c782f1e15256969e2db64694f34e17dad1d3b", "1.1--h031d066_4": "sha256:117b2e8a7aef1adbd82e04e038237761c5034f411cc4637c989c2ecc43bf57b9"}, "docker": "quay.io/biocontainers/jarvis", "aliases": {"JARVIS": "/usr/local/bin/JARVIS"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jarvis.
shpc-registry automated BioContainers addition for jarvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jarvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jarvis:1.1--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jarvis/1.1--h031d066_4
$ module help quay.io/biocontainers/jarvis/1.1--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jarvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jarvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jarvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jarvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jarvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jarvis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### JARVIS

```bash
$ singularity exec <container> /usr/local/bin/JARVIS
$ podman run --it --rm --entrypoint /usr/local/bin/JARVIS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JARVIS   -v ${PWD} -w ${PWD} <container> -c " $@"
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