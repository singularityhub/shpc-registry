---
layout: container
name:  "quay.io/biocontainers/bioconductor-rrho"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rrho/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rrho/container.yaml"
updated_at: "2024-01-29 02:44:48.942749"
latest: "1.42.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rrho"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rrho"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rrho", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rrho", "latest": {"1.42.0--r43hdfd78af_1": "sha256:3e39d2a97bd9b36c3971f9217aea5414d5f284226eaa8491198590b849d402e5"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:ed197765ec6f2bbc4d27014e0e453c55e80e3a8c6df0639f5037ea687ee73b17", "1.38.0--r42hdfd78af_0": "sha256:0ca8b5a8aeea9d46a6f7e48516e0d27a4b6ed9e615aa315e80237297b3405106", "1.40.0--r43hdfd78af_0": "sha256:66c8f4edcf8f23a6cce2f080d57cffa248f98f105f423b4eca1662e236770ce4", "1.42.0--r43hdfd78af_1": "sha256:3e39d2a97bd9b36c3971f9217aea5414d5f284226eaa8491198590b849d402e5"}, "docker": "quay.io/biocontainers/bioconductor-rrho"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rrho.
shpc-registry automated BioContainers addition for bioconductor-rrho
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rrho
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rrho:1.42.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rrho/1.42.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-rrho/1.42.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rrho-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rrho-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rrho-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rrho-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rrho-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rrho-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rrho

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