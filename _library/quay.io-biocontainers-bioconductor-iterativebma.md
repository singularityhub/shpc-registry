---
layout: container
name:  "quay.io/biocontainers/bioconductor-iterativebma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iterativebma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iterativebma/container.yaml"
updated_at: "2025-04-17 03:29:17.931686"
latest: "1.60.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-iterativebma"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-iterativebma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iterativebma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iterativebma", "latest": {"1.60.0--r43hdfd78af_0": "sha256:2d7bb137d8c691313e9ada0ed35591ee816ac349ff889f8510e0bf505d6adcd1"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:d132341a61f38467eee342ac2c095a21f5a595fa452f0eacd79b836324c1e5ea", "1.56.0--r42hdfd78af_0": "sha256:915c4657d4a3d978b0ae6553d50b67d8b8738330d4ff58e16b3b1f530b8f061c", "1.58.0--r43hdfd78af_0": "sha256:24f84ca3e9d6b6b680d9d45bd14b54230d62efd9e15234c3f6abd4f40a8f48dc", "1.60.0--r43hdfd78af_0": "sha256:2d7bb137d8c691313e9ada0ed35591ee816ac349ff889f8510e0bf505d6adcd1"}, "docker": "quay.io/biocontainers/bioconductor-iterativebma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iterativebma.
shpc-registry automated BioContainers addition for bioconductor-iterativebma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iterativebma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iterativebma:1.60.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iterativebma/1.60.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-iterativebma/1.60.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iterativebma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iterativebma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iterativebma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iterativebma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iterativebma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iterativebma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-iterativebma

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