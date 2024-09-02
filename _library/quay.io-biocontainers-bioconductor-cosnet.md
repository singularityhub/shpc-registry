---
layout: container
name:  "quay.io/biocontainers/bioconductor-cosnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cosnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cosnet/container.yaml"
updated_at: "2024-09-02 05:00:08.870641"
latest: "1.36.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cosnet"

versions:
 - "1.28.0--r41hc0cfd56_2"
 - "1.32.0--r42hc0cfd56_0"
 - "1.32.0--r42ha9d7317_2"
 - "1.34.0--r43ha9d7317_0"
 - "1.36.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cosnet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cosnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cosnet", "latest": {"1.36.0--r43ha9d7317_0": "sha256:f8b30b815adfed977ec54b06c6658839058b898c3893498e2243561ad346bf68"}, "tags": {"1.28.0--r41hc0cfd56_2": "sha256:0fc108595369f2deb733488ddf82fec0dbb25cfd001a112f8c6e0dff37492a44", "1.32.0--r42hc0cfd56_0": "sha256:5efe6bc543296dfd9c0ea82fe5c9fc0fe3161ddcba7d411a2720395681fdee86", "1.32.0--r42ha9d7317_2": "sha256:9d5da30c0aa5b9203a7b5e237962a2493c46f82aee2378def1423bbe21ca3e98", "1.34.0--r43ha9d7317_0": "sha256:66f9e98b5a5fb3124afe2abe3391df29c73b3261da05151f864608690719e9bc", "1.36.0--r43ha9d7317_0": "sha256:f8b30b815adfed977ec54b06c6658839058b898c3893498e2243561ad346bf68"}, "docker": "quay.io/biocontainers/bioconductor-cosnet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cosnet.
shpc-registry automated BioContainers addition for bioconductor-cosnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cosnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cosnet:1.36.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cosnet/1.36.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-cosnet/1.36.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cosnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cosnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cosnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cosnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cosnet

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