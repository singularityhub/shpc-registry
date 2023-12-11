---
layout: container
name:  "quay.io/biocontainers/bioconductor-a4core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-a4core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-a4core/container.yaml"
updated_at: "2023-12-11 02:46:18.976338"
latest: "1.48.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-a4core"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-a4core"
config: {"url": "https://biocontainers.pro/tools/bioconductor-a4core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-a4core", "latest": {"1.48.0--r43hdfd78af_0": "sha256:6651717ccd6eb121e3d84555db6159c22164c947c8547b348ce187a0b630f02c"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:9c3b5e579a009402bea0905e801688fbe3b181ae43afa3a591c28bb82f5b0534", "1.46.0--r42hdfd78af_0": "sha256:82f1cdd4aa4df5e917b3fa5be053510c0ff205fca1a971051f9841931ec66c44", "1.48.0--r43hdfd78af_0": "sha256:6651717ccd6eb121e3d84555db6159c22164c947c8547b348ce187a0b630f02c"}, "docker": "quay.io/biocontainers/bioconductor-a4core"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-a4core.
shpc-registry automated BioContainers addition for bioconductor-a4core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-a4core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-a4core:1.48.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-a4core/1.48.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-a4core/1.48.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-a4core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-a4core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-a4core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-a4core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-a4core

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