---
layout: container
name:  "quay.io/biocontainers/bioconductor-gwena"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gwena/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gwena/container.yaml"
updated_at: "2024-08-16 02:55:48.778716"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gwena"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gwena"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gwena", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gwena", "latest": {"1.12.0--r43hdfd78af_0": "sha256:eaf2a7f133c0087c381aec9bfcd27c3e3307216a86c8d08d967bef6bc7562ca8"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:249a767dc6af9e54046d0c0476e069aab59e6c0644aea996f9edaaec77eef71a", "1.8.0--r42hdfd78af_0": "sha256:456e370526d5d8e659ae76a0665ba506f3bac8aed6b63619c047a6d060ece7bd", "1.10.0--r43hdfd78af_0": "sha256:477273ed934a042d4782c62784154fe4acc76df3c0e01ad001a81099b16dfd5e", "1.12.0--r43hdfd78af_0": "sha256:eaf2a7f133c0087c381aec9bfcd27c3e3307216a86c8d08d967bef6bc7562ca8"}, "docker": "quay.io/biocontainers/bioconductor-gwena"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gwena.
shpc-registry automated BioContainers addition for bioconductor-gwena
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gwena
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gwena:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gwena/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gwena/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gwena-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gwena-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gwena-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gwena-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gwena-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gwena-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gwena

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