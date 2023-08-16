---
layout: container
name:  "quay.io/biocontainers/bioconductor-plogo2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plogo2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plogo2/container.yaml"
updated_at: "2023-08-16 03:00:19.961847"
latest: "1.10.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-plogo2"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-plogo2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plogo2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plogo2", "latest": {"1.10.0--r42hdfd78af_0": "sha256:fa2a56103c954d7cda2295c1ac470d7c54f0d671f5fbd6ca94e838c321c902e1"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:3e7cfcad2577b53ddd7d282434d08fde294bb43e1e37ee445656333dc1bcd60c", "1.10.0--r42hdfd78af_0": "sha256:fa2a56103c954d7cda2295c1ac470d7c54f0d671f5fbd6ca94e838c321c902e1"}, "docker": "quay.io/biocontainers/bioconductor-plogo2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plogo2.
shpc-registry automated BioContainers addition for bioconductor-plogo2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plogo2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plogo2:1.10.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plogo2/1.10.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-plogo2/1.10.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plogo2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plogo2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plogo2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plogo2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plogo2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plogo2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-plogo2

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