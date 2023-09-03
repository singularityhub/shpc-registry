---
layout: container
name:  "quay.io/biocontainers/bioconductor-indeed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-indeed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-indeed/container.yaml"
updated_at: "2023-09-03 03:22:33.595195"
latest: "2.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-indeed"

versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.12.0--r42hdfd78af_0"
 - "2.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-indeed"
config: {"url": "https://biocontainers.pro/tools/bioconductor-indeed", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-indeed", "latest": {"2.14.0--r43hdfd78af_0": "sha256:b58b4eff71b42c923400fce826b4198b34e48e139a34580b273025a8ffb03bda"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:242069ddbf06ff7a476c69024e2b31103a3cb08aa6e57b83e92e96dc9bf6f7dd", "2.12.0--r42hdfd78af_0": "sha256:5011969f21abba2c3aeb21a55d82840c8a167b1118f1949f0610a79ccf9009b5", "2.14.0--r43hdfd78af_0": "sha256:b58b4eff71b42c923400fce826b4198b34e48e139a34580b273025a8ffb03bda"}, "docker": "quay.io/biocontainers/bioconductor-indeed"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-indeed.
shpc-registry automated BioContainers addition for bioconductor-indeed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-indeed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-indeed:2.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-indeed/2.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-indeed/2.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-indeed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-indeed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-indeed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-indeed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-indeed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-indeed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-indeed

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