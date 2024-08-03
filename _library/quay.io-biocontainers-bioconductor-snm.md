---
layout: container
name:  "quay.io/biocontainers/bioconductor-snm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snm/container.yaml"
updated_at: "2024-08-03 03:10:31.341002"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snm"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snm", "latest": {"1.50.0--r43hdfd78af_0": "sha256:29b69084f15d9a987a407ead1c5efc8fb2236674d239661a228dacf4c03910ae"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:4e52013794b9f54445f95174d71194fa608395d527d607243977478164061fc7", "1.46.0--r42hdfd78af_0": "sha256:623f8080657e9d58a6090509b12c171f48a8e9e102688f2e40056544faaad222", "1.48.0--r43hdfd78af_0": "sha256:26d830fda6e8550e80b6c77c7361069bce2c10856c1cd42e1cdbea2d619184c4", "1.50.0--r43hdfd78af_0": "sha256:29b69084f15d9a987a407ead1c5efc8fb2236674d239661a228dacf4c03910ae"}, "docker": "quay.io/biocontainers/bioconductor-snm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snm.
shpc-registry automated BioContainers addition for bioconductor-snm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snm:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snm/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-snm/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-snm

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