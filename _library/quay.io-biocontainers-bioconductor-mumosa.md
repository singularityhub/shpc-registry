---
layout: container
name:  "quay.io/biocontainers/bioconductor-mumosa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mumosa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mumosa/container.yaml"
updated_at: "2024-06-25 02:43:15.276115"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mumosa"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mumosa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mumosa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mumosa", "latest": {"1.10.0--r43hdfd78af_0": "sha256:243a604ba5fc3f926957e3c9d8581be87e8107fe14952ec595fcc8d489d0098f"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:ee5106abb0c336c9e6695d9b88b731d2b860c1087c926fcbf847a3057160ca46", "1.6.0--r42hdfd78af_0": "sha256:834d3793a62e557af5da5755dc14c5f3a1732c3db9e66c78342e65a03b4fd537", "1.8.0--r43hdfd78af_0": "sha256:b8ab4ff2f9f7d6f8f48c6175e7fa0dc8e9231d8a67c291632d34ba7b884ad999", "1.10.0--r43hdfd78af_0": "sha256:243a604ba5fc3f926957e3c9d8581be87e8107fe14952ec595fcc8d489d0098f"}, "docker": "quay.io/biocontainers/bioconductor-mumosa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mumosa.
shpc-registry automated BioContainers addition for bioconductor-mumosa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mumosa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mumosa:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mumosa/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mumosa/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mumosa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mumosa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mumosa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mumosa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mumosa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mumosa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mumosa

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