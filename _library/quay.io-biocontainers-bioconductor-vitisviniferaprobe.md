---
layout: container
name:  "quay.io/biocontainers/bioconductor-vitisviniferaprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vitisviniferaprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vitisviniferaprobe/container.yaml"
updated_at: "2023-08-11 02:57:45.675275"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-vitisviniferaprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-vitisviniferaprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vitisviniferaprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vitisviniferaprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:13d8294eb6bda7efb84fb5bb2aafe62bfb642e5cd6dc40efea34befd60e48d67"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5e58ba129c86d370398090c7518d74317173ccfdf89989d237842c3f21d3e499", "2.18.0--r42hdfd78af_10": "sha256:667649795e28da17e651475c5fbfdc4b6402fde7ef60ca4501843ea5dce00350", "2.18.0--r43hdfd78af_11": "sha256:13d8294eb6bda7efb84fb5bb2aafe62bfb642e5cd6dc40efea34befd60e48d67"}, "docker": "quay.io/biocontainers/bioconductor-vitisviniferaprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vitisviniferaprobe.
shpc-registry automated BioContainers addition for bioconductor-vitisviniferaprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vitisviniferaprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vitisviniferaprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vitisviniferaprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-vitisviniferaprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vitisviniferaprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vitisviniferaprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vitisviniferaprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vitisviniferaprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vitisviniferaprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vitisviniferaprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vitisviniferaprobe

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