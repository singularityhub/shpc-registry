---
layout: container
name:  "quay.io/biocontainers/bioconductor-oligoclasses"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oligoclasses/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oligoclasses/container.yaml"
updated_at: "2024-04-24 03:06:13.285470"
latest: "1.64.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-oligoclasses"

versions:
 - "1.56.0--r41hdfd78af_0"
 - "1.60.0--r42hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.64.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-oligoclasses"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oligoclasses", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oligoclasses", "latest": {"1.64.0--r43hdfd78af_0": "sha256:76c3512ecfb2f1e2f1b1b5269dd4d9e248db5e421a45275ecd47f6562e38f3ec"}, "tags": {"1.56.0--r41hdfd78af_0": "sha256:4234faac6dde4903be27ee1bb645853a12bb8a9bcbb22c54c077c1eaa3c98c5a", "1.60.0--r42hdfd78af_0": "sha256:d5800b1124e9983639f41880a8108353229cdd1a7c1051e0db0cde098bc4fd2b", "1.62.0--r43hdfd78af_0": "sha256:cc02e3bc0d788bf007eb13bbd59b0b5117fc60899615ed1cfcca5ba3d578c0b5", "1.64.0--r43hdfd78af_0": "sha256:76c3512ecfb2f1e2f1b1b5269dd4d9e248db5e421a45275ecd47f6562e38f3ec"}, "docker": "quay.io/biocontainers/bioconductor-oligoclasses"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oligoclasses.
shpc-registry automated BioContainers addition for bioconductor-oligoclasses
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oligoclasses
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oligoclasses:1.64.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oligoclasses/1.64.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-oligoclasses/1.64.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oligoclasses-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oligoclasses-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oligoclasses-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oligoclasses-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oligoclasses-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oligoclasses-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-oligoclasses

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