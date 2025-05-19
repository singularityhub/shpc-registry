---
layout: container
name:  "quay.io/biocontainers/bioconductor-diggit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-diggit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-diggit/container.yaml"
updated_at: "2025-05-19 03:22:30.672045"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-diggit"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-diggit"
config: {"url": "https://biocontainers.pro/tools/bioconductor-diggit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-diggit", "latest": {"1.38.0--r44hdfd78af_0": "sha256:47e78dbc1cb7a9d2f7ba65ba87a579f762402a4276c001f89cc7673dd50238f4"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:9e7db64c71e69772e4f242c61d9d135165ee72e071655949fcc70e7a4ebe8911", "1.30.0--r42hdfd78af_0": "sha256:2001e03d72a28854fc6201217164635f6b119899e452ff2e150f3548fd799ec9", "1.32.0--r43hdfd78af_0": "sha256:ddc1ee37b3316e1d9775642b7aa76c048efe8d8f73aff28256d24db244311ad6", "1.34.0--r43hdfd78af_0": "sha256:6ae74001dc49ec3f013acaac5f54c174fc878b82f8be72778f27ed4f466e9ff0", "1.38.0--r44hdfd78af_0": "sha256:47e78dbc1cb7a9d2f7ba65ba87a579f762402a4276c001f89cc7673dd50238f4"}, "docker": "quay.io/biocontainers/bioconductor-diggit"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-diggit.
shpc-registry automated BioContainers addition for bioconductor-diggit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-diggit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-diggit:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-diggit/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-diggit/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-diggit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diggit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diggit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-diggit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-diggit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-diggit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-diggit

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