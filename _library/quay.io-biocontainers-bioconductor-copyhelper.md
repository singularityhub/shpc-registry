---
layout: container
name:  "quay.io/biocontainers/bioconductor-copyhelper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-copyhelper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-copyhelper/container.yaml"
updated_at: "2024-08-19 03:50:32.301756"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-copyhelper"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.30.0--r42hdfd78af_0"
 - "1.29.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-copyhelper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-copyhelper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-copyhelper", "latest": {"1.34.0--r43hdfd78af_0": "sha256:218232293f5871efc9333af28ba4c94d038b588200573eee1d68c9d9fa2427c5"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:0f5763cfaf27bcfd469950f45f9f33e406698ac17e38dd87ab66c44afcfcd66a", "1.30.0--r42hdfd78af_0": "sha256:574b20e16da52b0474858d9c891a3f0947a4c29b12c19659a9b3ebb306dc0448", "1.29.0--r42hdfd78af_0": "sha256:a8a3eb212f159af40fda74460752f5d59275a5544464b35d4c101afa8df4c5cd", "1.32.0--r43hdfd78af_0": "sha256:0a9860adc529a9d1c1ac7942ea2088d6f71525ce85a4b7416b0c55d020d3aeb8", "1.34.0--r43hdfd78af_0": "sha256:218232293f5871efc9333af28ba4c94d038b588200573eee1d68c9d9fa2427c5"}, "docker": "quay.io/biocontainers/bioconductor-copyhelper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-copyhelper.
shpc-registry automated BioContainers addition for bioconductor-copyhelper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-copyhelper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-copyhelper:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-copyhelper/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-copyhelper/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-copyhelper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copyhelper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copyhelper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-copyhelper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-copyhelper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-copyhelper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-copyhelper

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