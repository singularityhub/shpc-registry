---
layout: container
name:  "quay.io/biocontainers/cellprofiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cellprofiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cellprofiler/container.yaml"
updated_at: "2024-05-07 02:47:52.932312"
latest: "4.2.6--py39hf95cd2a_0"
container_url: "https://biocontainers.pro/tools/cellprofiler"

versions:
 - "4.2.1--py38hec16e2b_2"
 - "4.2.1--py38h031d066_3"
 - "4.2.6--py39hf95cd2a_0"
 - "4.2.6--py310h4b81fae_0"
description: "shpc-registry automated BioContainers addition for cellprofiler"
config: {"url": "https://biocontainers.pro/tools/cellprofiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cellprofiler", "latest": {"4.2.6--py39hf95cd2a_0": "sha256:3bd144c71514e6346c39843b6d4bc387e8a069f264486d5420328278a5505762"}, "tags": {"4.2.1--py38hec16e2b_2": "sha256:c4bafc812c204f5cddf7e708076c9f06e777971f0b205280f4525a83e427f733", "4.2.1--py38h031d066_3": "sha256:52b599b899a739b5742629ea45624b84168b6701857bbb4ace8c5b996e99e740", "4.2.6--py39hf95cd2a_0": "sha256:3bd144c71514e6346c39843b6d4bc387e8a069f264486d5420328278a5505762", "4.2.6--py310h4b81fae_0": "sha256:81e50f607d9c49cc7b7b8fe4867a90cc1a3cac18bfeb07f1138370fb78f45b5c"}, "docker": "quay.io/biocontainers/cellprofiler"}
---

This module is a singularity container wrapper for quay.io/biocontainers/cellprofiler.
shpc-registry automated BioContainers addition for cellprofiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cellprofiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cellprofiler:4.2.6--py39hf95cd2a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cellprofiler/4.2.6--py39hf95cd2a_0
$ module help quay.io/biocontainers/cellprofiler/4.2.6--py39hf95cd2a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cellprofiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cellprofiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cellprofiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cellprofiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cellprofiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cellprofiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cellprofiler

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