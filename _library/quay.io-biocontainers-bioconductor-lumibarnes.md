---
layout: container
name:  "quay.io/biocontainers/bioconductor-lumibarnes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lumibarnes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lumibarnes/container.yaml"
updated_at: "2024-01-19 03:03:11.552859"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lumibarnes"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lumibarnes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lumibarnes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lumibarnes", "latest": {"1.42.0--r43hdfd78af_0": "sha256:63a2b623b6a49539f1ad02538cd8c76625bef98449f6e38b1292d6afa532988f"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:6ffd789b5952c7d69b96c76826dc07b050bbf695161d42da176e08a6efc89dd4", "1.38.0--r42hdfd78af_0": "sha256:27f4a5bbbeda75ae05c2bcb5178e7a14fec03e29c4c5d9dfc8754a606706b542", "1.40.0--r43hdfd78af_0": "sha256:56477c6f15fb2d199124381a2526e309f6f4a7ce29f8c54a06bf4a1fd6c85809", "1.42.0--r43hdfd78af_0": "sha256:63a2b623b6a49539f1ad02538cd8c76625bef98449f6e38b1292d6afa532988f"}, "docker": "quay.io/biocontainers/bioconductor-lumibarnes"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lumibarnes.
shpc-registry automated BioContainers addition for bioconductor-lumibarnes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lumibarnes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lumibarnes:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lumibarnes/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lumibarnes/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lumibarnes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumibarnes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumibarnes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lumibarnes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lumibarnes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lumibarnes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lumibarnes

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