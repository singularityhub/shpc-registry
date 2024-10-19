---
layout: container
name:  "quay.io/biocontainers/bioconductor-splicingfactory"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-splicingfactory/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-splicingfactory/container.yaml"
updated_at: "2024-10-19 03:29:17.188647"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-splicingfactory"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-splicingfactory"
config: {"url": "https://biocontainers.pro/tools/bioconductor-splicingfactory", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-splicingfactory", "latest": {"1.10.0--r43hdfd78af_0": "sha256:0cdf9d443933cf95b522454dff55f8f349f95487f0000e1c66111f7134e4d22b"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:22d5b3e37ad08070b1bb355dd341198ccdbe151ef4a676524ad0bd951662a97c", "1.6.0--r42hdfd78af_0": "sha256:bcc0747e6f194d742201253642ae5f1fa9d90751d019e1a8f3aeb9bbcf0cf564", "1.8.0--r43hdfd78af_0": "sha256:c13baf7fc33a2758466b8729b567085eeac8d5ddb89b3d193832cac9937eb9c2", "1.10.0--r43hdfd78af_0": "sha256:0cdf9d443933cf95b522454dff55f8f349f95487f0000e1c66111f7134e4d22b"}, "docker": "quay.io/biocontainers/bioconductor-splicingfactory"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-splicingfactory.
shpc-registry automated BioContainers addition for bioconductor-splicingfactory
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-splicingfactory
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-splicingfactory:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-splicingfactory/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-splicingfactory/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-splicingfactory-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splicingfactory-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splicingfactory-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-splicingfactory-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-splicingfactory-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-splicingfactory-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-splicingfactory

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