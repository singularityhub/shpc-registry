---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodbexpasy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodbexpasy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodbexpasy/container.yaml"
updated_at: "2025-12-12 03:33:03.054095"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodbexpasy"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-biodbexpasy"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodbexpasy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-biodbexpasy", "latest": {"1.6.0--r43hdfd78af_0": "sha256:02d42b773088a7895b12da39a215bcf915d29477a3e82a9897678fabd6295a73"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:1594710c2aef7cacce168a5f92df6c3c1f229a8c965d94ae2810977dd0f3b5ad", "1.4.0--r43hdfd78af_0": "sha256:04746c2f44b6dcb0e45f23680b7d9f388a57555cacaff777ce2dc22b9a38fd76", "1.6.0--r43hdfd78af_0": "sha256:02d42b773088a7895b12da39a215bcf915d29477a3e82a9897678fabd6295a73"}, "docker": "quay.io/biocontainers/bioconductor-biodbexpasy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodbexpasy.
singularity registry hpc automated addition for bioconductor-biodbexpasy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbexpasy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbexpasy:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodbexpasy/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biodbexpasy/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodbexpasy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbexpasy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbexpasy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodbexpasy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodbexpasy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodbexpasy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodbexpasy

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