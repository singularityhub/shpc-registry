---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu2beta7"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu2beta7/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu2beta7/container.yaml"
updated_at: "2025-02-21 03:30:34.908525"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu2beta7"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.37.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu2beta7"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu2beta7", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu2beta7", "latest": {"1.46.0--r44hdfd78af_0": "sha256:39fb282cec99f4c9d6f656adda9355c7f24ccc725f19ed3e631c43a7fd51bb18"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:c7de83acbcbbecd7a11eba58710d25c8d3445d50c0580d1bd838e6d92e810e2b", "1.37.0--r42hdfd78af_0": "sha256:7a21dadb851ca301375b9045ef93282073641b458e21b33a755d2c04dd6e9a0c", "1.40.0--r43hdfd78af_0": "sha256:5c1a030222933820258ee5316f840d46e2a6d011da24462003b5341dd825afd1", "1.42.0--r43hdfd78af_0": "sha256:454f0e7e876758c6493283c37f60dddff50a8e57c4013d1a500a7fd09a4f37db", "1.46.0--r44hdfd78af_0": "sha256:39fb282cec99f4c9d6f656adda9355c7f24ccc725f19ed3e631c43a7fd51bb18"}, "docker": "quay.io/biocontainers/bioconductor-hgu2beta7"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu2beta7.
shpc-registry automated BioContainers addition for bioconductor-hgu2beta7
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu2beta7
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu2beta7:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu2beta7/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hgu2beta7/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu2beta7-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu2beta7-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu2beta7-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu2beta7-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu2beta7-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu2beta7-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu2beta7

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