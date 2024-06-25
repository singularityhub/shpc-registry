---
layout: container
name:  "quay.io/biocontainers/bioconductor-widgettools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-widgettools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-widgettools/container.yaml"
updated_at: "2024-06-25 03:05:58.851856"
latest: "1.80.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-widgettools"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
 - "1.80.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-widgettools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-widgettools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-widgettools", "latest": {"1.80.0--r43hdfd78af_0": "sha256:8050dccfc4ee02b7f1de1c13869f66ac579ca74d53ef156067e2e973e0fba073"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:fb94bdeeeaf73575444d14c630c64b524565971e86724114c41cb84d68f7242d", "1.76.0--r42hdfd78af_0": "sha256:e10d0b08bff2b824011e777b32e03864dbc47aba403e56b6e0336547b150ba3c", "1.78.0--r43hdfd78af_0": "sha256:5129ba95d47ba22e67d8bbbe7a3811fa7af96e3e280d6026beb1b35acb28a74d", "1.80.0--r43hdfd78af_0": "sha256:8050dccfc4ee02b7f1de1c13869f66ac579ca74d53ef156067e2e973e0fba073"}, "docker": "quay.io/biocontainers/bioconductor-widgettools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-widgettools.
shpc-registry automated BioContainers addition for bioconductor-widgettools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-widgettools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-widgettools:1.80.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-widgettools/1.80.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-widgettools/1.80.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-widgettools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-widgettools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-widgettools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-widgettools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-widgettools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-widgettools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-widgettools

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