---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnbeads.hg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnbeads.hg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnbeads.hg19/container.yaml"
updated_at: "2023-07-30 03:14:27.649494"
latest: "1.30.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnbeads.hg19"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.30.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnbeads.hg19"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnbeads.hg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnbeads.hg19", "latest": {"1.30.0--r42hdfd78af_0": "sha256:100a40bb6d7ab804e4fe77ba931addf0391fd36417d86d4b320765cac19240a6"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:366ee2b2ed6a983b5633ba95f90f70f9a3c285e016bd09f2426b905c3c197891", "1.30.0--r42hdfd78af_0": "sha256:100a40bb6d7ab804e4fe77ba931addf0391fd36417d86d4b320765cac19240a6"}, "docker": "quay.io/biocontainers/bioconductor-rnbeads.hg19"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnbeads.hg19.
shpc-registry automated BioContainers addition for bioconductor-rnbeads.hg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnbeads.hg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnbeads.hg19:1.30.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnbeads.hg19/1.30.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnbeads.hg19/1.30.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnbeads.hg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnbeads.hg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnbeads.hg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnbeads.hg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnbeads.hg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnbeads.hg19-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnbeads.hg19

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