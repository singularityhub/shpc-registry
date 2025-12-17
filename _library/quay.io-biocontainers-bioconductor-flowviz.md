---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowviz/container.yaml"
updated_at: "2025-12-17 03:49:32.461795"
latest: "1.70.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowviz"

versions:
 - "1.58.0--r41hdfd78af_0"
 - "1.62.0--r42hdfd78af_0"
 - "1.64.0--r43hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
 - "1.70.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowviz", "latest": {"1.70.0--r44hdfd78af_0": "sha256:1334395d9cbc5e58cd7edab75df306312f8cb12148da2ffebce3d1c9f6c4d1b9"}, "tags": {"1.58.0--r41hdfd78af_0": "sha256:ddf4d225b40afc541e97271e02c760ac2e4beab62c6f5756d2af9240d2e64cac", "1.62.0--r42hdfd78af_0": "sha256:74ab99c7a9fabeaa50feffa1f93f3747a2e8325a71a384e99f72ecaeca704b90", "1.64.0--r43hdfd78af_0": "sha256:db46bb0cd07b6648f78703e543a5edcaf8d1d383f73505f90861b971fd494942", "1.66.0--r43hdfd78af_0": "sha256:85ad25b7cbace54dd91948cbb4dfe4e4b5fe41f38ec5dfff8a4afd2efcc79f19", "1.70.0--r44hdfd78af_0": "sha256:1334395d9cbc5e58cd7edab75df306312f8cb12148da2ffebce3d1c9f6c4d1b9"}, "docker": "quay.io/biocontainers/bioconductor-flowviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowviz.
shpc-registry automated BioContainers addition for bioconductor-flowviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowviz:1.70.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowviz/1.70.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowviz/1.70.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowviz

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