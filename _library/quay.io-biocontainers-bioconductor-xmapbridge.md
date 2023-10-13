---
layout: container
name:  "quay.io/biocontainers/bioconductor-xmapbridge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xmapbridge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xmapbridge/container.yaml"
updated_at: "2023-10-13 03:06:47.280112"
latest: "1.58.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xmapbridge"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xmapbridge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xmapbridge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xmapbridge", "latest": {"1.58.0--r43hdfd78af_0": "sha256:60e39dea7ccf33e18bc4bea8f6fc232f1a9bb588acb39db3d2068b722d3db72f"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:38b24f3bc130a05fa96a0ac6781dcb144c3a12779cb36206404eadd54d302e01", "1.56.0--r42hdfd78af_0": "sha256:cd6e4918555a9f8cb10621f3639e1768b53989bdde01d147ca021edcbe951716", "1.58.0--r43hdfd78af_0": "sha256:60e39dea7ccf33e18bc4bea8f6fc232f1a9bb588acb39db3d2068b722d3db72f"}, "docker": "quay.io/biocontainers/bioconductor-xmapbridge"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xmapbridge.
shpc-registry automated BioContainers addition for bioconductor-xmapbridge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xmapbridge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xmapbridge:1.58.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xmapbridge/1.58.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-xmapbridge/1.58.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xmapbridge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xmapbridge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xmapbridge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xmapbridge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xmapbridge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xmapbridge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-xmapbridge

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