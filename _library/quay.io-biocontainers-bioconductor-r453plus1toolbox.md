---
layout: container
name:  "quay.io/biocontainers/bioconductor-r453plus1toolbox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-r453plus1toolbox/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-r453plus1toolbox/container.yaml"
updated_at: "2025-11-02 03:23:30.737172"
latest: "1.56.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-r453plus1toolbox"

versions:
 - "1.44.0--r41hc0cfd56_2"
 - "1.48.0--r42hc0cfd56_0"
 - "1.48.0--r42ha9d7317_1"
 - "1.50.0--r43ha9d7317_0"
 - "1.52.0--r43ha9d7317_0"
 - "1.56.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-r453plus1toolbox"
config: {"url": "https://biocontainers.pro/tools/bioconductor-r453plus1toolbox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-r453plus1toolbox", "latest": {"1.56.0--r44h3df3fcb_0": "sha256:ad1cf5178e15bc8416b008cd44f67094f256f356bda19b2937e9715680d1188d"}, "tags": {"1.44.0--r41hc0cfd56_2": "sha256:c5a8f6d1e71182c2862f977fd5a65f0d8cba6c8d780ae961334990b29a022f4b", "1.48.0--r42hc0cfd56_0": "sha256:db5521265b04722ca925c81abbe8aaa314139d04ecfec900e763075af864798a", "1.48.0--r42ha9d7317_1": "sha256:c2ff7cfc329fccb71d7b20a6741847af5c115ecc0fb17e977e818aa5c2b7975b", "1.50.0--r43ha9d7317_0": "sha256:848fd6b2ea72477f1c46a945b8bf2f7c18407b07508749bad3356446c4734a86", "1.52.0--r43ha9d7317_0": "sha256:1a418f44c28388febae5abc3cda2dd723f1c63a7191fb7c51a31a80dfff5290b", "1.56.0--r44h3df3fcb_0": "sha256:ad1cf5178e15bc8416b008cd44f67094f256f356bda19b2937e9715680d1188d"}, "docker": "quay.io/biocontainers/bioconductor-r453plus1toolbox"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-r453plus1toolbox.
shpc-registry automated BioContainers addition for bioconductor-r453plus1toolbox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-r453plus1toolbox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-r453plus1toolbox:1.56.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-r453plus1toolbox/1.56.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-r453plus1toolbox/1.56.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-r453plus1toolbox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r453plus1toolbox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r453plus1toolbox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-r453plus1toolbox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-r453plus1toolbox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-r453plus1toolbox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-r453plus1toolbox

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