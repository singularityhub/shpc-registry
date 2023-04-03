---
layout: container
name:  "quay.io/biocontainers/bioconductor-samspectral"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-samspectral/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-samspectral/container.yaml"
updated_at: "2023-04-03 02:35:39.991905"
latest: "1.52.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-samspectral"

versions:
 - "1.48.0--r41hc0cfd56_2"
 - "1.52.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-samspectral"
config: {"url": "https://biocontainers.pro/tools/bioconductor-samspectral", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-samspectral", "latest": {"1.52.0--r42hc0cfd56_0": "sha256:77c76917c1eda0d8c273eee61291b6b668c0c03962e31a86c89e6dd0d3345069"}, "tags": {"1.48.0--r41hc0cfd56_2": "sha256:f4fd858ba58961ae7585211a5d11f2a1aa493d1252b41b73278de5011879ac35", "1.52.0--r42hc0cfd56_0": "sha256:77c76917c1eda0d8c273eee61291b6b668c0c03962e31a86c89e6dd0d3345069"}, "docker": "quay.io/biocontainers/bioconductor-samspectral"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-samspectral.
shpc-registry automated BioContainers addition for bioconductor-samspectral
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-samspectral
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-samspectral:1.52.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-samspectral/1.52.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-samspectral/1.52.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-samspectral-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-samspectral-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-samspectral-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-samspectral-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-samspectral-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-samspectral-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-samspectral

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