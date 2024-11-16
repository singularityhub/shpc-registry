---
layout: container
name:  "quay.io/biocontainers/bioconductor-erccdashboard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-erccdashboard/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-erccdashboard/container.yaml"
updated_at: "2024-11-16 03:42:11.581147"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-erccdashboard"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-erccdashboard"
config: {"url": "https://biocontainers.pro/tools/bioconductor-erccdashboard", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-erccdashboard", "latest": {"1.36.0--r43hdfd78af_0": "sha256:72987bfc320b17c1037e4d35b53f31a1d2ebf75c1017f4e608deb8bbc5885af4"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:f902a7038ea220e297ee7cd906833d7dd8bf184191491292bb7bc04a910ac91b", "1.32.0--r42hdfd78af_0": "sha256:01d78ab87b9d4947190d652fe0292569a4c11357909783af37299df6543cb2b9", "1.34.0--r43hdfd78af_0": "sha256:b236ad0216dab0fe71d59b871d0ff1b08dc72af9219f743b30a0c1cf75018cc6", "1.36.0--r43hdfd78af_0": "sha256:72987bfc320b17c1037e4d35b53f31a1d2ebf75c1017f4e608deb8bbc5885af4"}, "docker": "quay.io/biocontainers/bioconductor-erccdashboard"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-erccdashboard.
shpc-registry automated BioContainers addition for bioconductor-erccdashboard
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-erccdashboard
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-erccdashboard:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-erccdashboard/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-erccdashboard/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-erccdashboard-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-erccdashboard-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-erccdashboard-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-erccdashboard-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-erccdashboard-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-erccdashboard-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-erccdashboard

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