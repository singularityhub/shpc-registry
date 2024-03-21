---
layout: container
name:  "quay.io/biocontainers/bioconductor-compcoder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-compcoder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-compcoder/container.yaml"
updated_at: "2024-03-21 02:34:37.411268"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-compcoder"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.2--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-compcoder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-compcoder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-compcoder", "latest": {"1.38.0--r43hdfd78af_0": "sha256:454b7db3b6dc7cca1ad37aa1c5dd1664c86599734c3f5d16a237728755d3cc1e"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:b84d1af6e7b19cc865519d616fa574ffa43e8b6a1f86afa99333f4556d6b7165", "1.34.0--r42hdfd78af_0": "sha256:017ed3ce55b15f93c112ccd1debb795ab836840757c788b0b4c7664995984660", "1.36.2--r43hdfd78af_0": "sha256:a5572f48541621e8cbf6bfba09c18e47616b5614987106e84ede846c4d02a576", "1.38.0--r43hdfd78af_0": "sha256:454b7db3b6dc7cca1ad37aa1c5dd1664c86599734c3f5d16a237728755d3cc1e"}, "docker": "quay.io/biocontainers/bioconductor-compcoder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-compcoder.
shpc-registry automated BioContainers addition for bioconductor-compcoder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-compcoder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-compcoder:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-compcoder/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-compcoder/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-compcoder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compcoder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compcoder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-compcoder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-compcoder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-compcoder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-compcoder

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