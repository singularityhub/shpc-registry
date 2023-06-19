---
layout: container
name:  "quay.io/biocontainers/bioconductor-circrnaprofiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-circrnaprofiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-circrnaprofiler/container.yaml"
updated_at: "2023-06-19 02:53:12.886114"
latest: "1.12.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-circrnaprofiler"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-circrnaprofiler"
config: {"url": "https://biocontainers.pro/tools/bioconductor-circrnaprofiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-circrnaprofiler", "latest": {"1.12.0--r42hdfd78af_0": "sha256:3c5c1784ed87617733119be536537372fa7999f9f865652974c0c36588f7e9f0"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:09c7371712c325fd4d102e02ea23a82202b99f7c07c8120b595127c2836c8936", "1.12.0--r42hdfd78af_0": "sha256:3c5c1784ed87617733119be536537372fa7999f9f865652974c0c36588f7e9f0"}, "docker": "quay.io/biocontainers/bioconductor-circrnaprofiler"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-circrnaprofiler.
shpc-registry automated BioContainers addition for bioconductor-circrnaprofiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-circrnaprofiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-circrnaprofiler:1.12.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-circrnaprofiler/1.12.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-circrnaprofiler/1.12.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-circrnaprofiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-circrnaprofiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-circrnaprofiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-circrnaprofiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-circrnaprofiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-circrnaprofiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-circrnaprofiler

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