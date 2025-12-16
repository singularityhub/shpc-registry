---
layout: container
name:  "quay.io/biocontainers/bioconductor-rlassocox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rlassocox/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rlassocox/container.yaml"
updated_at: "2025-12-16 04:13:53.756426"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rlassocox"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rlassocox"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rlassocox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rlassocox", "latest": {"1.14.0--r44hdfd78af_0": "sha256:91c921690a8b36b3bedae9a50b023651bb8e137c2161787462afca1bd3db4d5e"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:3b3691a76faffe0d6ed7189c9aa3f59db22571b272246c787f6beae322d226ff", "1.6.0--r42hdfd78af_0": "sha256:31aeff723653220e8a884388eb1885971621a323ab961c129b15d1373aa5734e", "1.8.0--r43hdfd78af_0": "sha256:7bd7e61771a177ce28d94b626d8f15d7f4534ad94e5d2c3c6c7c76ced388b0f4", "1.10.0--r43hdfd78af_0": "sha256:349a8d85b3f709580b6c4444236df18131394c520ea214a94cad51995f5bb4d6", "1.14.0--r44hdfd78af_0": "sha256:91c921690a8b36b3bedae9a50b023651bb8e137c2161787462afca1bd3db4d5e"}, "docker": "quay.io/biocontainers/bioconductor-rlassocox"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rlassocox.
shpc-registry automated BioContainers addition for bioconductor-rlassocox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rlassocox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rlassocox:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rlassocox/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rlassocox/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rlassocox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rlassocox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rlassocox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rlassocox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rlassocox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rlassocox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rlassocox

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