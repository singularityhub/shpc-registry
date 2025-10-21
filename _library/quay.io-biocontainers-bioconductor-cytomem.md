---
layout: container
name:  "quay.io/biocontainers/bioconductor-cytomem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cytomem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cytomem/container.yaml"
updated_at: "2025-10-21 03:50:04.316890"
latest: "1.10.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cytomem"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.10.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-cytomem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cytomem", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-cytomem", "latest": {"1.10.0--r44hdfd78af_0": "sha256:9bbb30842dbf71b709397fca1ffaf517f435b0462f3c59ddb624c6f3e43f4ebc"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:654b50f73222bc0ff6e75ff2cd9e97077f79f6ce1310e9c3900c6c2d3ef52876", "1.4.0--r43hdfd78af_0": "sha256:44e6f8532458c463e816ab9dca8afa3b6cf3413cd4e3e376fe1976f7f8f39f89", "1.6.0--r43hdfd78af_0": "sha256:3209540c03c70f06843bae8852634c6bc7608d1c07cc2a6de2ff35d5d71735ca", "1.10.0--r44hdfd78af_0": "sha256:9bbb30842dbf71b709397fca1ffaf517f435b0462f3c59ddb624c6f3e43f4ebc"}, "docker": "quay.io/biocontainers/bioconductor-cytomem"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cytomem.
singularity registry hpc automated addition for bioconductor-cytomem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cytomem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cytomem:1.10.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cytomem/1.10.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cytomem/1.10.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cytomem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytomem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cytomem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cytomem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cytomem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cytomem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cytomem

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