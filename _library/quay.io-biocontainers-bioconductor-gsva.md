---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsva"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsva/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsva/container.yaml"
updated_at: "2023-03-23 02:44:11.689862"
latest: "1.46.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsva"

versions:
 - "1.42.0--r41hc0cfd56_2"
 - "1.46.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsva"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsva", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsva", "latest": {"1.46.0--r42hc0cfd56_0": "sha256:8e97c964798b56090d6eb8c4c3d33ae785e4e968eb6d01278103948ff3bb0018"}, "tags": {"1.42.0--r41hc0cfd56_2": "sha256:f5a0a282e384289c54aaee024c4898ad7030c3c03ae324626097f457944984a9", "1.46.0--r42hc0cfd56_0": "sha256:8e97c964798b56090d6eb8c4c3d33ae785e4e968eb6d01278103948ff3bb0018"}, "docker": "quay.io/biocontainers/bioconductor-gsva"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsva.
shpc-registry automated BioContainers addition for bioconductor-gsva
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsva
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsva:1.46.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsva/1.46.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-gsva/1.46.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsva-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsva-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsva-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsva-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsva-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsva-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gsva

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