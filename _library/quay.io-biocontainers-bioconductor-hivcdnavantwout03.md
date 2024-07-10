---
layout: container
name:  "quay.io/biocontainers/bioconductor-hivcdnavantwout03"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hivcdnavantwout03/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hivcdnavantwout03/container.yaml"
updated_at: "2024-07-10 02:45:05.036802"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hivcdnavantwout03"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.37.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hivcdnavantwout03"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hivcdnavantwout03", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hivcdnavantwout03", "latest": {"1.42.0--r43hdfd78af_0": "sha256:9359687f3501441106f2906b8175db23d31a6a6e31044118dfc9a40ce42760af"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:adeabecd005cc86cdae547f012db1c0cf4ffa68eb91f0449d8e0b35c175a78b4", "1.37.0--r42hdfd78af_0": "sha256:17ec0a5be607e6adcfa38140248ac27b3d77896e219988b7780b356fa7acb98b", "1.40.0--r43hdfd78af_0": "sha256:85c9e5f6dd4502ca48c472cfce2904b66b323f19b4251e6df42c91088e9f4fd8", "1.42.0--r43hdfd78af_0": "sha256:9359687f3501441106f2906b8175db23d31a6a6e31044118dfc9a40ce42760af"}, "docker": "quay.io/biocontainers/bioconductor-hivcdnavantwout03"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hivcdnavantwout03.
shpc-registry automated BioContainers addition for bioconductor-hivcdnavantwout03
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hivcdnavantwout03
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hivcdnavantwout03:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hivcdnavantwout03/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hivcdnavantwout03/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hivcdnavantwout03-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hivcdnavantwout03-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hivcdnavantwout03-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hivcdnavantwout03-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hivcdnavantwout03-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hivcdnavantwout03-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hivcdnavantwout03

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