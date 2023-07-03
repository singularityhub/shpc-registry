---
layout: container
name:  "quay.io/biocontainers/bioconductor-sctreeviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sctreeviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sctreeviz/container.yaml"
updated_at: "2023-07-03 03:36:27.427628"
latest: "1.4.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sctreeviz"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sctreeviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sctreeviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sctreeviz", "latest": {"1.4.0--r42hdfd78af_0": "sha256:8b477667be4f0e9c402ba1f76c0c957b0021501840fc26976d7b72fbc4b26f0c"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:d27334f3c5a3099ae21b70a222023eff52b7dc62ba0704241f90b905fb263a79", "1.4.0--r42hdfd78af_0": "sha256:8b477667be4f0e9c402ba1f76c0c957b0021501840fc26976d7b72fbc4b26f0c"}, "docker": "quay.io/biocontainers/bioconductor-sctreeviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sctreeviz.
shpc-registry automated BioContainers addition for bioconductor-sctreeviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sctreeviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sctreeviz:1.4.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sctreeviz/1.4.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sctreeviz/1.4.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sctreeviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sctreeviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sctreeviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sctreeviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sctreeviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sctreeviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sctreeviz

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