---
layout: container
name:  "quay.io/biocontainers/bioconductor-monalisa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-monalisa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-monalisa/container.yaml"
updated_at: "2023-07-21 03:26:36.305313"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-monalisa"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-monalisa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-monalisa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-monalisa", "latest": {"1.6.0--r43hdfd78af_0": "sha256:a6c829c97067424ff53217d24cf8512bf33ea587d861bba980bb57f40ce956ad"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:ac40a7ba6919070a3266847797fbfc1b84cdbc1f7829e71caffa3a0b3d7f4205", "1.4.0--r42hdfd78af_0": "sha256:eadc39c53e300efd3b40f9bbdb401c964da67458b4cf5d4f8278358c4c2c68f2", "1.6.0--r43hdfd78af_0": "sha256:a6c829c97067424ff53217d24cf8512bf33ea587d861bba980bb57f40ce956ad"}, "docker": "quay.io/biocontainers/bioconductor-monalisa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-monalisa.
shpc-registry automated BioContainers addition for bioconductor-monalisa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-monalisa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-monalisa:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-monalisa/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-monalisa/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-monalisa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-monalisa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-monalisa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-monalisa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-monalisa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-monalisa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-monalisa

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