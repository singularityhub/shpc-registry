---
layout: container
name:  "quay.io/biocontainers/bioconductor-lumi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lumi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lumi/container.yaml"
updated_at: "2024-12-21 02:51:17.481471"
latest: "2.54.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lumi"

versions:
 - "2.46.0--r41hdfd78af_1"
 - "2.50.0--r42hdfd78af_0"
 - "2.52.0--r43hdfd78af_0"
 - "2.54.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lumi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lumi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lumi", "latest": {"2.54.0--r43hdfd78af_0": "sha256:3266dfa2b6267cea22574fa0ee8e61dad7d25e7d19f078505f594b47b11ab282"}, "tags": {"2.46.0--r41hdfd78af_1": "sha256:6754316ec0fc6bc9163b4611e4b03846ffc663b2084d0352a3703963e9f0ea58", "2.50.0--r42hdfd78af_0": "sha256:4193afac50ce5849c9f7d04e1669b901b13a0b91e2d432086657c01927fdf09c", "2.52.0--r43hdfd78af_0": "sha256:5418ec8d67010435b6a6b08c9ef5cb68261b6e34a5d867854ccf17e3a632a8ef", "2.54.0--r43hdfd78af_0": "sha256:3266dfa2b6267cea22574fa0ee8e61dad7d25e7d19f078505f594b47b11ab282"}, "docker": "quay.io/biocontainers/bioconductor-lumi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lumi.
shpc-registry automated BioContainers addition for bioconductor-lumi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lumi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lumi:2.54.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lumi/2.54.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lumi/2.54.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lumi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lumi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lumi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lumi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lumi

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