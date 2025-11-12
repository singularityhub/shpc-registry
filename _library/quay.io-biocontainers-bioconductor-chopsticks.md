---
layout: container
name:  "quay.io/biocontainers/bioconductor-chopsticks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chopsticks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chopsticks/container.yaml"
updated_at: "2025-11-12 03:22:02.767645"
latest: "1.72.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chopsticks"

versions:
 - "1.60.0--r41hc0cfd56_2"
 - "1.64.0--r42hc0cfd56_0"
 - "1.64.0--r42hc0cfd56_1"
 - "1.64.0--r42ha9d7317_2"
 - "1.66.0--r43ha9d7317_0"
 - "1.68.0--r43ha9d7317_1"
 - "1.72.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chopsticks"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chopsticks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chopsticks", "latest": {"1.72.0--r44h3df3fcb_0": "sha256:63ad61a654a031bb40c9824e4ab6c4484144b7469baf513a237a49ded2ea93f2"}, "tags": {"1.60.0--r41hc0cfd56_2": "sha256:4f26615e2b0594ffd9b4da49d540f99e3098a9ea8a5cdda50cfefa42ed71acca", "1.64.0--r42hc0cfd56_0": "sha256:8973052869777e417b1e59d1cb0ad11fc3d2dacbfa647ee478683674196dcb35", "1.64.0--r42hc0cfd56_1": "sha256:833a8086c496a980c0cbd486aaa7cf8a65ca8f5e34271d98f0c6f4288adc722a", "1.64.0--r42ha9d7317_2": "sha256:b022a813427bb41eba47cf8036c3c53cef719488224381d9cfa4ed8b5ac96bd4", "1.66.0--r43ha9d7317_0": "sha256:aed1c3808843b16082bcded28ef1e1ff261c23d0a9e2139cd7e00debd98bceb3", "1.68.0--r43ha9d7317_1": "sha256:84188f46670b9feab74bc197b3ea57f8693bb8e1d45912b090eb918893514ca6", "1.72.0--r44h3df3fcb_0": "sha256:63ad61a654a031bb40c9824e4ab6c4484144b7469baf513a237a49ded2ea93f2"}, "docker": "quay.io/biocontainers/bioconductor-chopsticks"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chopsticks.
shpc-registry automated BioContainers addition for bioconductor-chopsticks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chopsticks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chopsticks:1.72.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chopsticks/1.72.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-chopsticks/1.72.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chopsticks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chopsticks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chopsticks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chopsticks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chopsticks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chopsticks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chopsticks

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