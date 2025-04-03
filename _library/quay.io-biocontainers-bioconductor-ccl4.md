---
layout: container
name:  "quay.io/biocontainers/bioconductor-ccl4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ccl4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ccl4/container.yaml"
updated_at: "2025-04-03 03:11:14.510114"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ccl4"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ccl4"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ccl4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ccl4", "latest": {"1.44.0--r44hdfd78af_0": "sha256:71717abe32700bfc6285034d5cbd3b1391353b058bf1dc29458d35eb62b779ff"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:a9e1000eb408d4049581a6ca61e7f867263d59f06be6eec545ca0814678549f6", "1.35.0--r42hdfd78af_0": "sha256:f337424ea714693121d46aae70fd1bbd02a553308ab3b4757df5ef264d010950", "1.38.0--r43hdfd78af_0": "sha256:fadff1c85e29535773cf9d3021e67f0749088999ef502db66b5db88c51127593", "1.40.0--r43hdfd78af_0": "sha256:6827f3cb31c7a4486b64796ae8c428ca363319339a8a04f9cb47a53e400434a2", "1.44.0--r44hdfd78af_0": "sha256:71717abe32700bfc6285034d5cbd3b1391353b058bf1dc29458d35eb62b779ff"}, "docker": "quay.io/biocontainers/bioconductor-ccl4"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ccl4.
shpc-registry automated BioContainers addition for bioconductor-ccl4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ccl4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ccl4:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ccl4/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ccl4/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ccl4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccl4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccl4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ccl4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ccl4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ccl4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ccl4

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