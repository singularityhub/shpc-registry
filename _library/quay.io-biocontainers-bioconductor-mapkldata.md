---
layout: container
name:  "quay.io/biocontainers/bioconductor-mapkldata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mapkldata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mapkldata/container.yaml"
updated_at: "2024-01-26 02:48:02.238991"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mapkldata"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.29.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mapkldata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mapkldata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mapkldata", "latest": {"1.34.0--r43hdfd78af_0": "sha256:cf66765df0259774aab8794ac8a0cf73081a515971647736dddf37d05a798d94"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:1b288317b018fb75360969426a51ce6ad84576ed63d69f4a208f6dfb9d2e355a", "1.29.0--r42hdfd78af_0": "sha256:c318b089b23ce7943bc699faf5d7cb9236f84b4c1344a80fa1fa7ba86237f87b", "1.32.0--r43hdfd78af_0": "sha256:6baf71f9c722a26286b435ca39b0371cea9a281cf06738d28ff522de03378da2", "1.34.0--r43hdfd78af_0": "sha256:cf66765df0259774aab8794ac8a0cf73081a515971647736dddf37d05a798d94"}, "docker": "quay.io/biocontainers/bioconductor-mapkldata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mapkldata.
shpc-registry automated BioContainers addition for bioconductor-mapkldata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mapkldata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mapkldata:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mapkldata/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mapkldata/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mapkldata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapkldata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapkldata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mapkldata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mapkldata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mapkldata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mapkldata

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