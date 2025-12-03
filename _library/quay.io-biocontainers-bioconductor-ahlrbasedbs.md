---
layout: container
name:  "quay.io/biocontainers/bioconductor-ahlrbasedbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ahlrbasedbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ahlrbasedbs/container.yaml"
updated_at: "2025-12-03 03:56:43.943101"
latest: "1.8.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ahlrbasedbs"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.5.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.7.0--r43hdfd78af_0"
 - "1.8.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ahlrbasedbs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ahlrbasedbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ahlrbasedbs", "latest": {"1.8.0--r44hdfd78af_0": "sha256:06e802ee6a5a7e2b32f586e70887dac33b8beb9dc8764c66bb956c97d2df2199"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:7a7726285e5c83cf3e9b4af8cffaf25939285ad55d771b3fdb11bc159e263d19", "1.5.0--r42hdfd78af_0": "sha256:abe0ee191fda768c1cd88d3ebd8af1cfc9b64b2309046d11514b2c3aecb41d96", "1.6.0--r43hdfd78af_0": "sha256:6b1aa737a7dabafa193b3aeed71c7906e541163d56119af8cf5432cdda3889a8", "1.7.0--r43hdfd78af_0": "sha256:1a00866374f5f47d01ba2296191015261a47f18a7f29a0bc3f5c254d6b0f8609", "1.8.0--r44hdfd78af_0": "sha256:06e802ee6a5a7e2b32f586e70887dac33b8beb9dc8764c66bb956c97d2df2199"}, "docker": "quay.io/biocontainers/bioconductor-ahlrbasedbs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ahlrbasedbs.
shpc-registry automated BioContainers addition for bioconductor-ahlrbasedbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ahlrbasedbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ahlrbasedbs:1.8.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ahlrbasedbs/1.8.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ahlrbasedbs/1.8.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ahlrbasedbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahlrbasedbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahlrbasedbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ahlrbasedbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ahlrbasedbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ahlrbasedbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ahlrbasedbs

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