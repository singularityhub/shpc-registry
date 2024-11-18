---
layout: container
name:  "quay.io/biocontainers/bioconductor-sigpathway"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sigpathway/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sigpathway/container.yaml"
updated_at: "2024-11-18 03:40:19.039040"
latest: "1.66.0--r42ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-sigpathway"

versions:
 - "1.62.0--r41hc0cfd56_2"
 - "1.66.0--r42hc0cfd56_0"
 - "1.66.0--r42ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-sigpathway"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sigpathway", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sigpathway", "latest": {"1.66.0--r42ha9d7317_1": "sha256:5d622f99a133b4cff4de6f2d4962852e8c8975d6dbae2208f884564004714463"}, "tags": {"1.62.0--r41hc0cfd56_2": "sha256:6c2307b8a8c449027f5cfa81adde84b1efa353c408327f19439f562c091e2b33", "1.66.0--r42hc0cfd56_0": "sha256:d094d2f17564163e02c20a0e8f5bce7ed893029f3b48c742bfa7be77b941f977", "1.66.0--r42ha9d7317_1": "sha256:5d622f99a133b4cff4de6f2d4962852e8c8975d6dbae2208f884564004714463"}, "docker": "quay.io/biocontainers/bioconductor-sigpathway"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sigpathway.
shpc-registry automated BioContainers addition for bioconductor-sigpathway
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sigpathway
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sigpathway:1.66.0--r42ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sigpathway/1.66.0--r42ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-sigpathway/1.66.0--r42ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sigpathway-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigpathway-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigpathway-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sigpathway-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sigpathway-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sigpathway-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sigpathway

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