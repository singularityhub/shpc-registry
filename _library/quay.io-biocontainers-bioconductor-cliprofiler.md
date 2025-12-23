---
layout: container
name:  "quay.io/biocontainers/bioconductor-cliprofiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cliprofiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cliprofiler/container.yaml"
updated_at: "2025-12-23 04:19:10.447334"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cliprofiler"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cliprofiler"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cliprofiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cliprofiler", "latest": {"1.12.0--r44hdfd78af_0": "sha256:ecc371d782976673f0e231df82a9c433f4387a1b7a194123420b6d980f48eba8"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:0cc4a207d3a707227079d9f0dfdf44aa7e6af714f48124d3234502af05aa7d56", "1.4.0--r42hdfd78af_0": "sha256:203926549368371b87417d009bff623b93fb5dcab41dec68b9eec2eb81d51338", "1.6.0--r43hdfd78af_0": "sha256:e37e8ba717db5ab5dc46766f233cca4a9c6b56c01f5565d6a3d272a0f200b6b7", "1.8.0--r43hdfd78af_0": "sha256:ffee792e263681684bb0f53d4efe6aeb11f05c77b599ef2590f6d25caa9636ca", "1.12.0--r44hdfd78af_0": "sha256:ecc371d782976673f0e231df82a9c433f4387a1b7a194123420b6d980f48eba8"}, "docker": "quay.io/biocontainers/bioconductor-cliprofiler"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cliprofiler.
shpc-registry automated BioContainers addition for bioconductor-cliprofiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cliprofiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cliprofiler:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cliprofiler/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cliprofiler/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cliprofiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cliprofiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cliprofiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cliprofiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cliprofiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cliprofiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cliprofiler

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