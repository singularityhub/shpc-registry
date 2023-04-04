---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicranges"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicranges/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicranges/container.yaml"
updated_at: "2023-04-04 03:08:43.486069"
latest: "1.50.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicranges"

versions:
 - "1.46.1--r41hc0cfd56_1"
 - "1.50.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicranges"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicranges", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicranges", "latest": {"1.50.0--r42hc0cfd56_0": "sha256:93201e43ecc91803249436d1e67428700e8c280bfc528292653affe3f98f40a5"}, "tags": {"1.46.1--r41hc0cfd56_1": "sha256:8d8da7fb85a221e37b90faacdc11ae7a8c8c01decc9d0d2c1cb05dbc1583cf08", "1.50.0--r42hc0cfd56_0": "sha256:93201e43ecc91803249436d1e67428700e8c280bfc528292653affe3f98f40a5"}, "docker": "quay.io/biocontainers/bioconductor-genomicranges"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicranges.
shpc-registry automated BioContainers addition for bioconductor-genomicranges
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicranges
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicranges:1.50.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicranges/1.50.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-genomicranges/1.50.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicranges-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicranges-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicranges-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicranges-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicranges-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicranges-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomicranges

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