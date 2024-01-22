---
layout: container
name:  "quay.io/biocontainers/bioconductor-biomvrcns"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biomvrcns/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biomvrcns/container.yaml"
updated_at: "2024-01-22 03:31:14.322874"
latest: "1.42.1--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biomvrcns"

versions:
 - "1.34.0--r41hc0cfd56_2"
 - "1.38.0--r42hc0cfd56_0"
 - "1.38.0--r42ha9d7317_1"
 - "1.42.1--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biomvrcns"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biomvrcns", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biomvrcns", "latest": {"1.42.1--r43ha9d7317_0": "sha256:f1ff048fe44fed3a2d080e2e228cee5e53fcf6bda79d71512f1eea6982ee5606"}, "tags": {"1.34.0--r41hc0cfd56_2": "sha256:fa962454b053dc5c904a6c7f95ff245daec7c75f4a414ed910cd2f55916dbafd", "1.38.0--r42hc0cfd56_0": "sha256:7de521923747ad93c66eeae608b9f118144cd925bb7a4e1ec3e32117d0100ce8", "1.38.0--r42ha9d7317_1": "sha256:dc7630126e86419d50a2cad7dafc6e9e2eda6acb8cf84f5779ded7cd66b911b8", "1.42.1--r43ha9d7317_0": "sha256:f1ff048fe44fed3a2d080e2e228cee5e53fcf6bda79d71512f1eea6982ee5606"}, "docker": "quay.io/biocontainers/bioconductor-biomvrcns"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biomvrcns.
shpc-registry automated BioContainers addition for bioconductor-biomvrcns
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biomvrcns
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biomvrcns:1.42.1--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biomvrcns/1.42.1--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-biomvrcns/1.42.1--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biomvrcns-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biomvrcns-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biomvrcns-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biomvrcns-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biomvrcns-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biomvrcns-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biomvrcns

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