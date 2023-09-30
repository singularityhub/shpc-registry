---
layout: container
name:  "quay.io/biocontainers/bioconductor-affycoretools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affycoretools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affycoretools/container.yaml"
updated_at: "2023-09-30 03:09:00.610168"
latest: "1.72.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affycoretools"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affycoretools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affycoretools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affycoretools", "latest": {"1.72.0--r43hdfd78af_0": "sha256:e8e1160dfd8f1b5c8e595065fdc5bbcbac82ce97893f9fb560a5b0bd6156ffc4"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:52a251ae058f236be6c33d0e6a1b2c638820e24e344bfd895d42b1d1d55a0554", "1.70.0--r42hdfd78af_0": "sha256:a7c4e04b920bf59556c25b41440dc10948c4c5de7d53c92b1ae42b5e84f59003", "1.72.0--r43hdfd78af_0": "sha256:e8e1160dfd8f1b5c8e595065fdc5bbcbac82ce97893f9fb560a5b0bd6156ffc4"}, "docker": "quay.io/biocontainers/bioconductor-affycoretools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affycoretools.
shpc-registry automated BioContainers addition for bioconductor-affycoretools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affycoretools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affycoretools:1.72.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affycoretools/1.72.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affycoretools/1.72.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affycoretools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycoretools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycoretools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affycoretools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affycoretools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affycoretools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affycoretools

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