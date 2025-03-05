---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs/container.yaml"
updated_at: "2025-03-05 03:06:03.425344"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133plus2barcodevecs"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2barcodevecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133plus2barcodevecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2barcodevecs", "latest": {"1.44.0--r44hdfd78af_0": "sha256:55c587e93ddb4c1999f475d10b1f397d72a19dbbf4a4b9b83f2363a759e3f148"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:ee9121ad1e5c78383cd2a95a1ecbcd25c7e3f2e3faf511aed9b575289e90e0c0", "1.35.0--r42hdfd78af_0": "sha256:187872d8309b3f05d450baf14cdb8acea344c6da296cf7a135102a0bdec56475", "1.38.0--r43hdfd78af_0": "sha256:40dde3b2e91b705aa60e1678bef86c775ea4e362645bfde6f8ca5b478f1c4ee7", "1.40.0--r43hdfd78af_0": "sha256:ec43d3bea01083c709e564b8b15ff729a8edcd46b170e7ce0d9be330895d0574", "1.44.0--r44hdfd78af_0": "sha256:55c587e93ddb4c1999f475d10b1f397d72a19dbbf4a4b9b83f2363a759e3f148"}, "docker": "quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs.
shpc-registry automated BioContainers addition for bioconductor-hgu133plus2barcodevecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hgu133plus2barcodevecs/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133plus2barcodevecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2barcodevecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2barcodevecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133plus2barcodevecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133plus2barcodevecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133plus2barcodevecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133plus2barcodevecs

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