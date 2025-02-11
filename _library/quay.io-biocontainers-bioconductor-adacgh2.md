---
layout: container
name:  "quay.io/biocontainers/bioconductor-adacgh2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adacgh2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adacgh2/container.yaml"
updated_at: "2025-02-11 03:29:11.531949"
latest: "2.42.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-adacgh2"

versions:
 - "2.34.0--r41hc0cfd56_2"
 - "2.38.0--r42hc0cfd56_0"
 - "2.38.0--r42ha9d7317_1"
 - "2.40.0--r43ha9d7317_0"
 - "2.42.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-adacgh2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adacgh2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-adacgh2", "latest": {"2.42.0--r43ha9d7317_0": "sha256:692cd27db0aedbea84a4a9678bf21b0501870dbf76bd8bf7457be7aeedcfc127"}, "tags": {"2.34.0--r41hc0cfd56_2": "sha256:367178eca470c1bcafbb75d7b03d7c22f2a5b8c07bb460aaa331c810af0891b3", "2.38.0--r42hc0cfd56_0": "sha256:7181554c55aa84f2829ace72cfe856596d2d1aa07e4f0e27737780eb910ae7cd", "2.38.0--r42ha9d7317_1": "sha256:0337828aa34ba6a65ea9c365907449a9b60714a4155d616ff0e6cc0d2b1e4b51", "2.40.0--r43ha9d7317_0": "sha256:4360cd47e3db2e712ae02903d0be1e09562d210017f1ae2085acf2074ca85c3a", "2.42.0--r43ha9d7317_0": "sha256:692cd27db0aedbea84a4a9678bf21b0501870dbf76bd8bf7457be7aeedcfc127"}, "docker": "quay.io/biocontainers/bioconductor-adacgh2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adacgh2.
shpc-registry automated BioContainers addition for bioconductor-adacgh2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adacgh2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adacgh2:2.42.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adacgh2/2.42.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-adacgh2/2.42.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adacgh2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adacgh2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adacgh2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adacgh2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adacgh2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adacgh2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-adacgh2

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