---
layout: container
name:  "quay.io/biocontainers/bioconductor-netbiov"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-netbiov/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-netbiov/container.yaml"
updated_at: "2023-07-14 03:02:54.990353"
latest: "1.31.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-netbiov"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.31.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-netbiov"
config: {"url": "https://biocontainers.pro/tools/bioconductor-netbiov", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-netbiov", "latest": {"1.31.0--r42hdfd78af_0": "sha256:29ed77ceb6558e82e2505fe70df7d495d1887ff3c4247dd8cceb0e15a3da4ffb"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:d3f2e007bf57952d4cbb5e8ca6b6ec83de5fe2a0aa647307f9651d85547a3405", "1.31.0--r42hdfd78af_0": "sha256:29ed77ceb6558e82e2505fe70df7d495d1887ff3c4247dd8cceb0e15a3da4ffb"}, "docker": "quay.io/biocontainers/bioconductor-netbiov"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-netbiov.
shpc-registry automated BioContainers addition for bioconductor-netbiov
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-netbiov
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-netbiov:1.31.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-netbiov/1.31.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-netbiov/1.31.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-netbiov-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netbiov-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netbiov-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-netbiov-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-netbiov-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-netbiov-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-netbiov

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