---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtca/container.yaml"
updated_at: "2024-12-12 04:06:06.455817"
latest: "1.54.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtca"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtca", "latest": {"1.54.0--r43hdfd78af_0": "sha256:da036d7dadf664e2de8087751a35ef0aaedc9cf8f35e6e3f015e437de2d7ca8d"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:b354b00948b66c2830bb96f34930aa87cdb170a731dbc4695e9713a5311e125c", "1.50.0--r42hdfd78af_0": "sha256:ebd2d30660d468f8b81ad5415f8e528aa9e02f44656509a05899d82dc1f7ea48", "1.52.0--r43hdfd78af_0": "sha256:4e094798b8c58fe15dfb92911bff2d3ff6d7a86b9bc6df017299ead6e0a05006", "1.54.0--r43hdfd78af_0": "sha256:da036d7dadf664e2de8087751a35ef0aaedc9cf8f35e6e3f015e437de2d7ca8d"}, "docker": "quay.io/biocontainers/bioconductor-rtca"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtca.
shpc-registry automated BioContainers addition for bioconductor-rtca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtca:1.54.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtca/1.54.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtca/1.54.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtca

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