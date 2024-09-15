---
layout: container
name:  "quay.io/biocontainers/bioconductor-cormotif"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cormotif/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cormotif/container.yaml"
updated_at: "2024-09-15 03:09:50.066843"
latest: "1.48.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cormotif"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cormotif"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cormotif", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cormotif", "latest": {"1.48.0--r43hdfd78af_0": "sha256:d356868024e59de0116be57776a6d783bf26e7666b1b67745e489502f440fd8d"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:6e567a6b3f510fb6e38c4191b7a45bdb8f033048cce236483c2788f487b7a82d", "1.44.0--r42hdfd78af_0": "sha256:ee34acdaad50d37d0b9f0114011a223a686ab62619f40c72909794cbfd50d755", "1.46.0--r43hdfd78af_0": "sha256:a46ad1e0a0e4e56643770f75751c8ec96465cb626baf8902a2b8047d7e9e8520", "1.48.0--r43hdfd78af_0": "sha256:d356868024e59de0116be57776a6d783bf26e7666b1b67745e489502f440fd8d"}, "docker": "quay.io/biocontainers/bioconductor-cormotif"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cormotif.
shpc-registry automated BioContainers addition for bioconductor-cormotif
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cormotif
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cormotif:1.48.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cormotif/1.48.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cormotif/1.48.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cormotif-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cormotif-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cormotif-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cormotif-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cormotif-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cormotif-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cormotif

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