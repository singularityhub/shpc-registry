---
layout: container
name:  "quay.io/biocontainers/bioconductor-compass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-compass/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-compass/container.yaml"
updated_at: "2023-09-01 02:45:35.933311"
latest: "1.38.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-compass"
aliases:
 - "pandoc-server"
 - "pandoc"
versions:
 - "1.32.0--r41hc247a5b_2"
 - "1.36.0--r42hc247a5b_0"
 - "1.36.0--r42hf17093f_1"
 - "1.38.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-compass"
config: {"url": "https://biocontainers.pro/tools/bioconductor-compass", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-compass", "latest": {"1.38.1--r43hf17093f_0": "sha256:797c58f6f70c52958d008fc0536f43d7ea59e6a8c6bbc9d2b9cde2daa45800f0"}, "tags": {"1.32.0--r41hc247a5b_2": "sha256:e50c8ace23b8dc4056ffe80c8b706784de8475fe2a528a99c0b57adfccf46127", "1.36.0--r42hc247a5b_0": "sha256:a1ff830040ecfe4c41a5c976e9cba62eb9548c5870682e04d366d2df2bb0d81f", "1.36.0--r42hf17093f_1": "sha256:1e9b7d297ae6b05a1c4699c50691eaddc53b738b3f26768cfb0a9e710d2f9887", "1.38.1--r43hf17093f_0": "sha256:797c58f6f70c52958d008fc0536f43d7ea59e6a8c6bbc9d2b9cde2daa45800f0"}, "docker": "quay.io/biocontainers/bioconductor-compass", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-compass.
shpc-registry automated BioContainers addition for bioconductor-compass
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-compass
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-compass:1.38.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-compass/1.38.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-compass/1.38.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-compass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-compass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-compass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-compass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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