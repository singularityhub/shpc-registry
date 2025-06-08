---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylseqdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylseqdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylseqdata/container.yaml"
updated_at: "2025-06-08 05:56:50.509752"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylseqdata"

versions:
 - "1.4.0--r41hdfd78af_1"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylseqdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylseqdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylseqdata", "latest": {"1.16.0--r44hdfd78af_0": "sha256:b7dd05b6b7d6fefd7824c16a2c61a61bf1f26f476304029e5cab856625a7919f"}, "tags": {"1.4.0--r41hdfd78af_1": "sha256:f8217659ae2f4a02126f93fa43be515f9fa3c77dbbf926d465cc5783008aca76", "1.8.0--r42hdfd78af_0": "sha256:0d560c73780e20ee854ee683509dc85fa86258a96dcba284e6bbea91a49e8bdf", "1.10.0--r43hdfd78af_0": "sha256:dbac78298b9303e0322bce485db7057b1c7d9eb02db076ac7cfe0097ce0afd70", "1.12.0--r43hdfd78af_0": "sha256:16de0dec21eebf362dd9b9cdcbe0a0e5b8a5b9b109f62d793aa2fc41e02d0ad2", "1.16.0--r44hdfd78af_0": "sha256:b7dd05b6b7d6fefd7824c16a2c61a61bf1f26f476304029e5cab856625a7919f"}, "docker": "quay.io/biocontainers/bioconductor-methylseqdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylseqdata.
shpc-registry automated BioContainers addition for bioconductor-methylseqdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylseqdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylseqdata:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylseqdata/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylseqdata/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylseqdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylseqdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylseqdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylseqdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylseqdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylseqdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylseqdata

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