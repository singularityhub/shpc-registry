---
layout: container
name:  "quay.io/biocontainers/bioconductor-copa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-copa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-copa/container.yaml"
updated_at: "2024-09-20 03:17:59.222694"
latest: "1.70.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-copa"

versions:
 - "1.62.0--r41hc0cfd56_2"
 - "1.66.0--r42hc0cfd56_0"
 - "1.66.0--r42ha9d7317_1"
 - "1.68.0--r43ha9d7317_0"
 - "1.70.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-copa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-copa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-copa", "latest": {"1.70.0--r43ha9d7317_0": "sha256:1716cc79968c612c68b79fdb3f5ce0e3f9d42810c399309b90f49a77d6ef75cf"}, "tags": {"1.62.0--r41hc0cfd56_2": "sha256:962fbbcbcf0dfd15fec6a7e7cc7698cb6244e950af65f2d81696e8485bbc0456", "1.66.0--r42hc0cfd56_0": "sha256:ae707f2e0edbedd35e2aa9e4c6a2f64e24554cc43d02fd1d674bada619186175", "1.66.0--r42ha9d7317_1": "sha256:98cc724625719a0fca86900531fa65d1cbf0d609f24e3afe4ec1b7588335692f", "1.68.0--r43ha9d7317_0": "sha256:bd6529244a0edbb7776530921954cb95ab6e505c9dabada446eb6566ffeb15b5", "1.70.0--r43ha9d7317_0": "sha256:1716cc79968c612c68b79fdb3f5ce0e3f9d42810c399309b90f49a77d6ef75cf"}, "docker": "quay.io/biocontainers/bioconductor-copa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-copa.
shpc-registry automated BioContainers addition for bioconductor-copa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-copa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-copa:1.70.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-copa/1.70.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-copa/1.70.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-copa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-copa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-copa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-copa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-copa

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