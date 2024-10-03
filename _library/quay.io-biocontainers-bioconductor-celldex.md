---
layout: container
name:  "quay.io/biocontainers/bioconductor-celldex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-celldex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-celldex/container.yaml"
updated_at: "2024-10-03 03:25:18.740017"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-celldex"

versions:
 - "1.4.0--r41hdfd78af_1"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-celldex"
config: {"url": "https://biocontainers.pro/tools/bioconductor-celldex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-celldex", "latest": {"1.12.0--r43hdfd78af_0": "sha256:d7a1d39c07f00e620e2e72d4b374ddacffd1d0f5e8f89e2ebb189dd299987e62"}, "tags": {"1.4.0--r41hdfd78af_1": "sha256:5fe1ee51d6b24522dc1029d5ea2f61be1e353017bfe01988cf785a86dcf37bb3", "1.8.0--r42hdfd78af_0": "sha256:c875db3c3394ffd691bbcc93ef9527050c0440204d1c18b6297f479682ddc76c", "1.10.1--r43hdfd78af_0": "sha256:562d3eb983ec73f6cd66d97ba9f57d41e25c3e2617d270a46c1bcc6e80ab36e1", "1.12.0--r43hdfd78af_0": "sha256:d7a1d39c07f00e620e2e72d4b374ddacffd1d0f5e8f89e2ebb189dd299987e62"}, "docker": "quay.io/biocontainers/bioconductor-celldex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-celldex.
shpc-registry automated BioContainers addition for bioconductor-celldex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-celldex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-celldex:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-celldex/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-celldex/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-celldex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celldex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celldex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-celldex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-celldex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-celldex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-celldex

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