---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqvartools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqvartools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqvartools/container.yaml"
updated_at: "2025-05-05 04:02:07.999696"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqvartools"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqvartools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqvartools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqvartools", "latest": {"1.44.0--r44hdfd78af_0": "sha256:ca0c2ae111be97831ea0c5b064cb53ebff71c484ec28b225e9a470aa4366eeca"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:4d9ef357f5c5fa712a59ed434495dec4d450e4c4db7fc3d6cdb3011e645996a1", "1.36.0--r42hdfd78af_0": "sha256:41fa6f1713e818ba9f4dedc288d6c016fb39d1129e23bbe8df46aa92470ceb3d", "1.38.0--r43hdfd78af_0": "sha256:5442f9cf8aec4f81b3bac64e95e92af3ead2f148fcee61f3b14ef49ab3c9739f", "1.40.0--r43hdfd78af_0": "sha256:c7978dec2f63730cd520b7b923e59ac356d8dedfee25c0d576634dbf44eb3698", "1.44.0--r44hdfd78af_0": "sha256:ca0c2ae111be97831ea0c5b064cb53ebff71c484ec28b225e9a470aa4366eeca"}, "docker": "quay.io/biocontainers/bioconductor-seqvartools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqvartools.
shpc-registry automated BioContainers addition for bioconductor-seqvartools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqvartools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqvartools:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqvartools/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqvartools/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqvartools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqvartools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqvartools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqvartools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqvartools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqvartools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqvartools

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