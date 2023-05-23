---
layout: container
name:  "quay.io/biocontainers/bioconductor-connectivitymap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-connectivitymap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-connectivitymap/container.yaml"
updated_at: "2023-05-23 02:45:17.139452"
latest: "1.33.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-connectivitymap"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-connectivitymap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-connectivitymap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-connectivitymap", "latest": {"1.33.0--r42hdfd78af_0": "sha256:04b50d1768febe4a251bff23327df4243dc72ebf8105f7336e2843ca50fee328"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:089856a3a1c48b2de7898fba6a4ccac48fa36cbcd5b5cb12739d3ef068f63b1d", "1.33.0--r42hdfd78af_0": "sha256:04b50d1768febe4a251bff23327df4243dc72ebf8105f7336e2843ca50fee328"}, "docker": "quay.io/biocontainers/bioconductor-connectivitymap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-connectivitymap.
shpc-registry automated BioContainers addition for bioconductor-connectivitymap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-connectivitymap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-connectivitymap:1.33.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-connectivitymap/1.33.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-connectivitymap/1.33.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-connectivitymap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-connectivitymap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-connectivitymap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-connectivitymap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-connectivitymap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-connectivitymap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-connectivitymap

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