---
layout: container
name:  "quay.io/biocontainers/bioconductor-cctutorial"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cctutorial/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cctutorial/container.yaml"
updated_at: "2024-08-24 03:13:25.064669"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cctutorial"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cctutorial"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cctutorial", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cctutorial", "latest": {"1.40.0--r43hdfd78af_0": "sha256:94fbe19e8e4e2194438a12b1f23f8a5f043ab8a1008b37bd965883b9e7bb2cd8"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:ed76e9748f7659dcb732416e1c4fd0ff5ff32b4f76aa364cc11f15955e758554", "1.36.0--r42hdfd78af_0": "sha256:0c458abcb5ec5dc626551caccef4167e259a85ee2add8b1c0ed2cb43186cce59", "1.38.0--r43hdfd78af_0": "sha256:232c2821760e0a017acf88bd4be95d43a0ab96fff6300645aeb44a5e5a0234d3", "1.40.0--r43hdfd78af_0": "sha256:94fbe19e8e4e2194438a12b1f23f8a5f043ab8a1008b37bd965883b9e7bb2cd8"}, "docker": "quay.io/biocontainers/bioconductor-cctutorial"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cctutorial.
shpc-registry automated BioContainers addition for bioconductor-cctutorial
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cctutorial
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cctutorial:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cctutorial/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cctutorial/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cctutorial-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cctutorial-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cctutorial-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cctutorial-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cctutorial-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cctutorial-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cctutorial

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