---
layout: container
name:  "quay.io/biocontainers/bioconductor-cpvsnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cpvsnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cpvsnp/container.yaml"
updated_at: "2024-02-20 03:02:22.088166"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cpvsnp"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cpvsnp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cpvsnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cpvsnp", "latest": {"1.34.0--r43hdfd78af_0": "sha256:3bd5c7bfe3cf75a09bb7653587e4024cdabaff1c20327b066674187ad8e31302"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:0abc741f95d1983c8993dcc13e961b22305f9e496c611481d025fcee6e73e505", "1.30.0--r42hdfd78af_0": "sha256:133c1750b426758d2abd0b37b01ac06077d0d9950f466637d8604533f6d00a83", "1.32.0--r43hdfd78af_0": "sha256:59ee4f4361583bcfc2f5e2c39e6dd878c213f2e4607b03b8d1559f2e4a98deb0", "1.34.0--r43hdfd78af_0": "sha256:3bd5c7bfe3cf75a09bb7653587e4024cdabaff1c20327b066674187ad8e31302"}, "docker": "quay.io/biocontainers/bioconductor-cpvsnp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cpvsnp.
shpc-registry automated BioContainers addition for bioconductor-cpvsnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cpvsnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cpvsnp:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cpvsnp/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cpvsnp/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cpvsnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cpvsnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cpvsnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cpvsnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cpvsnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cpvsnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cpvsnp

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