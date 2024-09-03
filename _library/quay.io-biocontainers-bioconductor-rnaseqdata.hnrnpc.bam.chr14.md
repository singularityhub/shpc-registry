---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14/container.yaml"
updated_at: "2024-09-03 03:05:25.905930"
latest: "0.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaseqdata.hnrnpc.bam.chr14"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.35.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaseqdata.hnrnpc.bam.chr14"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaseqdata.hnrnpc.bam.chr14", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaseqdata.hnrnpc.bam.chr14", "latest": {"0.40.0--r43hdfd78af_0": "sha256:3f1c8153e4fb72ee4b0441f54e46ce88e6f9d425b6538fc1396919730336fbec"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:1c6f6e5c2657229810f1ed8e5da4ddfa95747bf39e867fd755b358062478e74d", "0.35.0--r42hdfd78af_0": "sha256:0e2c5a2a5094de8be31c23c468539755df04befa2238fd598f9b3bccf32ba0b3", "0.38.0--r43hdfd78af_0": "sha256:ba5bcbd20cd7ec6e0ceb092730e5c3e2e4d7a1c25c1acc2f58d7d4dde0a2371e", "0.40.0--r43hdfd78af_0": "sha256:3f1c8153e4fb72ee4b0441f54e46ce88e6f9d425b6538fc1396919730336fbec"}, "docker": "quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14.
shpc-registry automated BioContainers addition for bioconductor-rnaseqdata.hnrnpc.bam.chr14
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14:0.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14/0.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnaseqdata.hnrnpc.bam.chr14/0.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaseqdata.hnrnpc.bam.chr14-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqdata.hnrnpc.bam.chr14-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqdata.hnrnpc.bam.chr14-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaseqdata.hnrnpc.bam.chr14-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaseqdata.hnrnpc.bam.chr14-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaseqdata.hnrnpc.bam.chr14-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnaseqdata.hnrnpc.bam.chr14

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