---
layout: container
name:  "quay.io/biocontainers/bioconductor-pwmenrich"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pwmenrich/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pwmenrich/container.yaml"
updated_at: "2026-02-07 04:17:59.930304"
latest: "4.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pwmenrich"

versions:
 - "4.30.0--r41hdfd78af_0"
 - "4.34.0--r42hdfd78af_0"
 - "4.36.0--r43hdfd78af_0"
 - "4.38.0--r43hdfd78af_0"
 - "4.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pwmenrich"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pwmenrich", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pwmenrich", "latest": {"4.42.0--r44hdfd78af_0": "sha256:600752981a1641726142c16c8d880748a912e43c699f2bfb4c5614ad050541c3"}, "tags": {"4.30.0--r41hdfd78af_0": "sha256:1b578da0c635c0e27543d413378f21f1a397db1b5b8465889c0504a15d04d383", "4.34.0--r42hdfd78af_0": "sha256:4ec5cc6cd7d04f0d34b534f2529a9b51211ee9de5c2a5227d078a89189e61398", "4.36.0--r43hdfd78af_0": "sha256:395f476258d8debfeb23ed2f083d8c201c765dd37908cd1f4495926015d5724d", "4.38.0--r43hdfd78af_0": "sha256:f1567986e773d8f518c8039c852ac6b2221680af2d4b6b0b9a3c07268ff56973", "4.42.0--r44hdfd78af_0": "sha256:600752981a1641726142c16c8d880748a912e43c699f2bfb4c5614ad050541c3"}, "docker": "quay.io/biocontainers/bioconductor-pwmenrich"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pwmenrich.
shpc-registry automated BioContainers addition for bioconductor-pwmenrich
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pwmenrich
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pwmenrich:4.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pwmenrich/4.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pwmenrich/4.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pwmenrich-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwmenrich-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwmenrich-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pwmenrich-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pwmenrich-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pwmenrich-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pwmenrich

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