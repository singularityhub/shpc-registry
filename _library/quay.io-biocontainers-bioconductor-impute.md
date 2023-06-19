---
layout: container
name:  "quay.io/biocontainers/bioconductor-impute"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-impute/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-impute/container.yaml"
updated_at: "2023-06-19 03:10:17.290244"
latest: "1.72.0--r42h9913872_1"
container_url: "https://biocontainers.pro/tools/bioconductor-impute"

versions:
 - "1.68.0--r41hefde4a7_2"
 - "1.72.0--r42hefde4a7_0"
 - "1.72.0--r42h9913872_1"
description: "shpc-registry automated BioContainers addition for bioconductor-impute"
config: {"url": "https://biocontainers.pro/tools/bioconductor-impute", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-impute", "latest": {"1.72.0--r42h9913872_1": "sha256:3a23196b9708d5ff54a5e354b6a4c3b27845913395ac88055ae7271d1611d752"}, "tags": {"1.68.0--r41hefde4a7_2": "sha256:12ed9015057c455610ded717c4608a1e931187d0f109bc19b2b6f72643f95fbf", "1.72.0--r42hefde4a7_0": "sha256:bd15f61cf31fe3db77e84b4c4ca914eeb9ff12ee89d9ea6f6763eb8103bdd7a1", "1.72.0--r42h9913872_1": "sha256:3a23196b9708d5ff54a5e354b6a4c3b27845913395ac88055ae7271d1611d752"}, "docker": "quay.io/biocontainers/bioconductor-impute"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-impute.
shpc-registry automated BioContainers addition for bioconductor-impute
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-impute
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-impute:1.72.0--r42h9913872_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-impute/1.72.0--r42h9913872_1
$ module help quay.io/biocontainers/bioconductor-impute/1.72.0--r42h9913872_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-impute-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-impute-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-impute-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-impute-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-impute-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-impute-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-impute

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