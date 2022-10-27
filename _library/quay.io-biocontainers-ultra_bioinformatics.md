---
layout: container
name:  "quay.io/biocontainers/ultra_bioinformatics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ultra_bioinformatics/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ultra_bioinformatics/container.yaml"
updated_at: "2022-10-27 00:36:01.528319"
latest: "0.0.4.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/ultra_bioinformatics"
aliases:
 - "StrobeMap"
 - "edlib-aligner"
 - "slaMEM"
 - "uLTRA"
versions:
 - "0.0.4.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for ultra_bioinformatics"
config: {"url": "https://biocontainers.pro/tools/ultra_bioinformatics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ultra_bioinformatics", "latest": {"0.0.4.1--pyh5e36f6f_0": "sha256:efe193ed72700788e40ed41cb75aaa1ec23be83438068eb052b2b5f37748ed51"}, "tags": {"0.0.4.1--pyh5e36f6f_0": "sha256:efe193ed72700788e40ed41cb75aaa1ec23be83438068eb052b2b5f37748ed51"}, "docker": "quay.io/biocontainers/ultra_bioinformatics", "aliases": {"StrobeMap": "/usr/local/bin/StrobeMap", "edlib-aligner": "/usr/local/bin/edlib-aligner", "slaMEM": "/usr/local/bin/slaMEM", "uLTRA": "/usr/local/bin/uLTRA"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ultra_bioinformatics.
shpc-registry automated BioContainers addition for ultra_bioinformatics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ultra_bioinformatics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ultra_bioinformatics:0.0.4.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ultra_bioinformatics/0.0.4.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/ultra_bioinformatics/0.0.4.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ultra_bioinformatics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ultra_bioinformatics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ultra_bioinformatics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ultra_bioinformatics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ultra_bioinformatics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ultra_bioinformatics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### StrobeMap

```bash
$ singularity exec <container> /usr/local/bin/StrobeMap
$ podman run --it --rm --entrypoint /usr/local/bin/StrobeMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/StrobeMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edlib-aligner

```bash
$ singularity exec <container> /usr/local/bin/edlib-aligner
$ podman run --it --rm --entrypoint /usr/local/bin/edlib-aligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edlib-aligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slaMEM

```bash
$ singularity exec <container> /usr/local/bin/slaMEM
$ podman run --it --rm --entrypoint /usr/local/bin/slaMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slaMEM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uLTRA

```bash
$ singularity exec <container> /usr/local/bin/uLTRA
$ podman run --it --rm --entrypoint /usr/local/bin/uLTRA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uLTRA   -v ${PWD} -w ${PWD} <container> -c " $@"
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