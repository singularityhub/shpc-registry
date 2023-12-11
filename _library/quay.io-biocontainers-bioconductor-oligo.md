---
layout: container
name:  "quay.io/biocontainers/bioconductor-oligo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oligo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oligo/container.yaml"
updated_at: "2023-12-11 02:37:45.470970"
latest: "1.64.1--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-oligo"

versions:
 - "1.58.0--r41hc0cfd56_2"
 - "1.62.0--r42hc0cfd56_0"
 - "1.62.0--r42ha9d7317_1"
 - "1.64.1--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-oligo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oligo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oligo", "latest": {"1.64.1--r43ha9d7317_0": "sha256:e1925e75e0bd19393acfa8caedecc39b91cdfefcce14ab3c8bdf7093857debfb"}, "tags": {"1.58.0--r41hc0cfd56_2": "sha256:16cbc6cd7914d0b9e33c3de46e849cd37a6d1fe28f7f563d87ea7e211170be40", "1.62.0--r42hc0cfd56_0": "sha256:2f368d7d2c8c62ca2442be07f61ca9fa5aa346a8757799fe9abe0a5f451ddb76", "1.62.0--r42ha9d7317_1": "sha256:beabac364a6fb0994141f72db4e4ee129ebece1526ea8af646046ee2690d9413", "1.64.1--r43ha9d7317_0": "sha256:e1925e75e0bd19393acfa8caedecc39b91cdfefcce14ab3c8bdf7093857debfb"}, "docker": "quay.io/biocontainers/bioconductor-oligo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oligo.
shpc-registry automated BioContainers addition for bioconductor-oligo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oligo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oligo:1.64.1--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oligo/1.64.1--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-oligo/1.64.1--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oligo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oligo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oligo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oligo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oligo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oligo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-oligo

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