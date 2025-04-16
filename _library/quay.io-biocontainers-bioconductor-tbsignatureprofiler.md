---
layout: container
name:  "quay.io/biocontainers/bioconductor-tbsignatureprofiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tbsignatureprofiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tbsignatureprofiler/container.yaml"
updated_at: "2025-04-16 03:24:58.332249"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tbsignatureprofiler"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tbsignatureprofiler"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tbsignatureprofiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tbsignatureprofiler", "latest": {"1.14.0--r43hdfd78af_0": "sha256:27b4286fa191e3528a2a3132ca150950da183aa35d736fc4178a3b841c7570c3"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:fe4e2a987e315f46c1c4892a11fb3bd7f147d69a3c90f340ab67115756a0d5f2", "1.10.0--r42hdfd78af_0": "sha256:7de2d4f9219303bdc1660c2985ee0fd5015254b51e824236e34525564e596f12", "1.12.0--r43hdfd78af_0": "sha256:ae1c54477829e915db8ad5d8e0154793128ec4b48036ce2fb822fd1d66ff94a4", "1.14.0--r43hdfd78af_0": "sha256:27b4286fa191e3528a2a3132ca150950da183aa35d736fc4178a3b841c7570c3"}, "docker": "quay.io/biocontainers/bioconductor-tbsignatureprofiler"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tbsignatureprofiler.
shpc-registry automated BioContainers addition for bioconductor-tbsignatureprofiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tbsignatureprofiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tbsignatureprofiler:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tbsignatureprofiler/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tbsignatureprofiler/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tbsignatureprofiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tbsignatureprofiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tbsignatureprofiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tbsignatureprofiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tbsignatureprofiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tbsignatureprofiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tbsignatureprofiler

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