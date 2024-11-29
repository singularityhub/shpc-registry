---
layout: container
name:  "quay.io/biocontainers/bioconductor-vsn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vsn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vsn/container.yaml"
updated_at: "2024-11-29 03:44:52.204572"
latest: "3.70.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-vsn"

versions:
 - "3.62.0--r41hc0cfd56_2"
 - "3.66.0--r42hc0cfd56_0"
 - "3.66.0--r42ha9d7317_1"
 - "3.68.0--r43ha9d7317_0"
 - "3.70.0--r43ha9d7317_0"
 - "3.70.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-vsn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vsn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vsn", "latest": {"3.70.0--r43ha9d7317_1": "sha256:1a05247afd1e5504c20a3359a3b5261777445e307540366977a7acbc2f820f9c"}, "tags": {"3.62.0--r41hc0cfd56_2": "sha256:1b3f69b340b2b1b24aee329204bfadf740f27a70ebfb3777808136b9e4fb2adb", "3.66.0--r42hc0cfd56_0": "sha256:a4b32f949c74c4bdd85e9f7ac43e9abde1114ce474173437ea15232dcd1ef50c", "3.66.0--r42ha9d7317_1": "sha256:996205f5a822e6c59bc74effa9600c22678b4c4cb34c9eb42bb3906bf94f75a5", "3.68.0--r43ha9d7317_0": "sha256:092b864ced2ab848604426bf516a51a403a112df70e52606a8bcabe81ce2ed97", "3.70.0--r43ha9d7317_0": "sha256:b09186931094080eb1c42d661f6e10480ca8b19203050561ee25d9d33e25d48a", "3.70.0--r43ha9d7317_1": "sha256:1a05247afd1e5504c20a3359a3b5261777445e307540366977a7acbc2f820f9c"}, "docker": "quay.io/biocontainers/bioconductor-vsn"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vsn.
shpc-registry automated BioContainers addition for bioconductor-vsn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vsn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vsn:3.70.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vsn/3.70.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-vsn/3.70.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vsn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vsn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vsn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vsn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vsn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vsn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vsn

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