---
layout: container
name:  "quay.io/biocontainers/bioconductor-isee"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-isee/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-isee/container.yaml"
updated_at: "2024-08-02 03:11:53.451038"
latest: "2.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-isee"

versions:
 - "2.6.0--r41hdfd78af_0"
 - "2.10.0--r42hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-isee"
config: {"url": "https://biocontainers.pro/tools/bioconductor-isee", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-isee", "latest": {"2.14.0--r43hdfd78af_0": "sha256:d6539dac4203b48e14940088a990b26aae9d0cc21ae3b10bf934947b40e78897"}, "tags": {"2.6.0--r41hdfd78af_0": "sha256:cc2230a6c7278f49244ca0d21c36d5ebe252ec5634644ac287465e24308e42f4", "2.10.0--r42hdfd78af_0": "sha256:a16736992115de0eefc9f0680e1cf4c1cc39437e47df4574d864a06aa12d6704", "2.12.0--r43hdfd78af_0": "sha256:fd0089405b5e7fdf08b23198b778654a42ae5424552ca48ef5845ef8570587d9", "2.14.0--r43hdfd78af_0": "sha256:d6539dac4203b48e14940088a990b26aae9d0cc21ae3b10bf934947b40e78897"}, "docker": "quay.io/biocontainers/bioconductor-isee"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-isee.
shpc-registry automated BioContainers addition for bioconductor-isee
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-isee
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-isee:2.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-isee/2.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-isee/2.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-isee-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isee-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isee-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-isee-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-isee-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-isee-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-isee

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