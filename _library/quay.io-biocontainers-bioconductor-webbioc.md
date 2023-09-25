---
layout: container
name:  "quay.io/biocontainers/bioconductor-webbioc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-webbioc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-webbioc/container.yaml"
updated_at: "2023-09-25 02:35:09.939357"
latest: "1.72.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-webbioc"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-webbioc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-webbioc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-webbioc", "latest": {"1.72.0--r43hdfd78af_0": "sha256:9e37fb406bb6f0dcd38e99e0490e89a383b29ac481279dcfe73508c169cca242"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:bb5b14f4311149a50dfe6fddcd18951aada34cf62d52e14b21b27dff45690401", "1.70.0--r42hdfd78af_0": "sha256:53fbd5c2c355a87f10ab4a248a4885f6082e265ffc32cca2847b165f9cd069bb", "1.72.0--r43hdfd78af_0": "sha256:9e37fb406bb6f0dcd38e99e0490e89a383b29ac481279dcfe73508c169cca242"}, "docker": "quay.io/biocontainers/bioconductor-webbioc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-webbioc.
shpc-registry automated BioContainers addition for bioconductor-webbioc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-webbioc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-webbioc:1.72.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-webbioc/1.72.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-webbioc/1.72.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-webbioc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-webbioc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-webbioc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-webbioc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-webbioc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-webbioc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-webbioc

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