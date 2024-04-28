---
layout: container
name:  "quay.io/biocontainers/bioconductor-dmcfb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dmcfb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dmcfb/container.yaml"
updated_at: "2024-04-28 02:41:03.098861"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dmcfb"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dmcfb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dmcfb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dmcfb", "latest": {"1.14.0--r43hdfd78af_0": "sha256:19a853d9d59471e8de939a849334744d80c69da312df3a128ce2e31b039443e3"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a9fcea041ad36bb68032e544f5835f402254dec9a0f2d4f69566de77845c4ba6", "1.12.0--r42hdfd78af_0": "sha256:0d3e62fb04dfc0b0651bbbf9ea513401944cd30cb412d2a013fa53927f760340", "1.14.0--r43hdfd78af_0": "sha256:19a853d9d59471e8de939a849334744d80c69da312df3a128ce2e31b039443e3"}, "docker": "quay.io/biocontainers/bioconductor-dmcfb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dmcfb.
shpc-registry automated BioContainers addition for bioconductor-dmcfb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dmcfb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dmcfb:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dmcfb/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dmcfb/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dmcfb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmcfb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmcfb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dmcfb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dmcfb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dmcfb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dmcfb

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