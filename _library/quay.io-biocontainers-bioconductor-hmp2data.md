---
layout: container
name:  "quay.io/biocontainers/bioconductor-hmp2data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hmp2data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hmp2data/container.yaml"
updated_at: "2023-06-15 03:29:09.986511"
latest: "1.12.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hmp2data"
aliases:
 - "pandoc-server"
 - "glpsol"
 - "pandoc"
versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hmp2data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hmp2data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hmp2data", "latest": {"1.12.0--r42hdfd78af_0": "sha256:00654c1b7b8822b2fdc48aadfa1f5416621dab96b35e8c396038f3b3039b2cb4"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:e666d9b5e01e13860a6793f8e6b20f988b27da681366b6114d3f4a8cd8512a6e", "1.12.0--r42hdfd78af_0": "sha256:00654c1b7b8822b2fdc48aadfa1f5416621dab96b35e8c396038f3b3039b2cb4"}, "docker": "quay.io/biocontainers/bioconductor-hmp2data", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "glpsol": "/usr/local/bin/glpsol", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hmp2data.
shpc-registry automated BioContainers addition for bioconductor-hmp2data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hmp2data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hmp2data:1.12.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hmp2data/1.12.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hmp2data/1.12.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hmp2data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hmp2data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hmp2data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hmp2data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hmp2data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hmp2data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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