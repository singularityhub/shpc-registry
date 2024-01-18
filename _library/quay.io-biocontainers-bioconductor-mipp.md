---
layout: container
name:  "quay.io/biocontainers/bioconductor-mipp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mipp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mipp/container.yaml"
updated_at: "2024-01-18 03:02:55.831648"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mipp"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mipp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mipp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mipp", "latest": {"1.74.0--r43hdfd78af_0": "sha256:08985674f3a7ea71bff308db60527a814e287d69aa685d6fdcf8e305c4ade8c0"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:ae855691fbcbf91c170ebb3a705c342960e4c39f7adce4bb71643f8d4368dd8a", "1.70.0--r42hdfd78af_0": "sha256:813b29d48ff1fb1d017f331a8872bb11d0dfc9a6a6337d4e581810b94467d615", "1.72.0--r43hdfd78af_0": "sha256:94e6f4a28652860dab92b8eff8a769fcbb5971d906e2cb47486e91756f9d4b40", "1.74.0--r43hdfd78af_0": "sha256:08985674f3a7ea71bff308db60527a814e287d69aa685d6fdcf8e305c4ade8c0"}, "docker": "quay.io/biocontainers/bioconductor-mipp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mipp.
shpc-registry automated BioContainers addition for bioconductor-mipp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mipp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mipp:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mipp/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mipp/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mipp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mipp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mipp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mipp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mipp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mipp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mipp

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