---
layout: container
name:  "quay.io/biocontainers/bioconductor-epivizrserver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epivizrserver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epivizrserver/container.yaml"
updated_at: "2024-05-04 02:51:53.969710"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epivizrserver"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.1--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epivizrserver"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epivizrserver", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epivizrserver", "latest": {"1.30.0--r43hdfd78af_0": "sha256:8dd4c78e0337f26d486a55f28ee24f4a945bdf97f87da6542b91dd64009dfa29"}, "tags": {"1.8.1--r341_0": "sha256:0470c691b998fad83d66821d101cf7be98226879b99a9e348e22b571ebf2c42d", "1.26.0--r42hdfd78af_0": "sha256:710e37e35ddaee5912db7e8f11fd144f47e854ae6bca41187c31d59d46d094e6", "1.22.0--r41hdfd78af_0": "sha256:281e98a9381c361a228a6b94e1b7d5133a2ffa453ec3f9d92e7f26335201b6c6", "1.20.0--r41hdfd78af_0": "sha256:5807b6485c913d67228ca706c35bd0d83849f8e6d256b1ce1a27f47bf8b7879d", "1.18.0--r40hdfd78af_1": "sha256:1c17284e70a2f3b16708b4c9acf3930bb45e85159d85a26ace1b29f1183bd295", "1.16.0--r40_0": "sha256:08c79c940741b0b62392db224a8efa1f75de5f6f4891695c27179b615867f448", "1.28.0--r43hdfd78af_0": "sha256:c0e7a03313ca24f9d416fb4c91a80cd6264d05d1bf2579e2a5717d4ee000d95f", "1.30.0--r43hdfd78af_0": "sha256:8dd4c78e0337f26d486a55f28ee24f4a945bdf97f87da6542b91dd64009dfa29"}, "docker": "quay.io/biocontainers/bioconductor-epivizrserver", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epivizrserver.
shpc-registry automated BioContainers addition for bioconductor-epivizrserver
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrserver
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizrserver:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epivizrserver/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epivizrserver/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epivizrserver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrserver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizrserver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epivizrserver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epivizrserver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epivizrserver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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