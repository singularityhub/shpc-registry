---
layout: container
name:  "quay.io/biocontainers/bioconductor-ecoliasv2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ecoliasv2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ecoliasv2cdf/container.yaml"
updated_at: "2023-08-20 03:09:17.417058"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-ecoliasv2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-ecoliasv2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ecoliasv2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ecoliasv2cdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:b5680a3b3dbbe472389997eef1fdf536e4aabecba8442173e5d35c7cfba3622c"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d1d0d7be1e4044727b064fc23d0f7cd1d2ef549a1128c49da2462f091849e60e", "2.18.0--r42hdfd78af_10": "sha256:e6d7c0a5485b69dff50f0d497afdf3727e057682b88749fb5f00a5bee1f6c736", "2.18.0--r43hdfd78af_11": "sha256:b5680a3b3dbbe472389997eef1fdf536e4aabecba8442173e5d35c7cfba3622c"}, "docker": "quay.io/biocontainers/bioconductor-ecoliasv2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ecoliasv2cdf.
shpc-registry automated BioContainers addition for bioconductor-ecoliasv2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoliasv2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoliasv2cdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ecoliasv2cdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-ecoliasv2cdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ecoliasv2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoliasv2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoliasv2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ecoliasv2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ecoliasv2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ecoliasv2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ecoliasv2cdf

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