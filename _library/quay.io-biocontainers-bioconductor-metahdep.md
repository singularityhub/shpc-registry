---
layout: container
name:  "quay.io/biocontainers/bioconductor-metahdep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metahdep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metahdep/container.yaml"
updated_at: "2025-12-23 04:19:08.057971"
latest: "1.64.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metahdep"

versions:
 - "1.52.0--r41hc0cfd56_2"
 - "1.56.0--r42hc0cfd56_0"
 - "1.56.0--r42ha9d7317_2"
 - "1.58.0--r43ha9d7317_0"
 - "1.60.0--r43ha9d7317_0"
 - "1.64.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metahdep"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metahdep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metahdep", "latest": {"1.64.0--r44h3df3fcb_0": "sha256:cd900081b1f821b08f580228dca4672643770dc34512add91fe925343024bb05"}, "tags": {"1.52.0--r41hc0cfd56_2": "sha256:7a582dda6071d6128d6a772acb70b9b34927477b924d75a824b38d82e84e4ad6", "1.56.0--r42hc0cfd56_0": "sha256:e5ba4efb5e29b24e0f31b47b1853af3b6b735a43e867ceb376871c58d7c74d57", "1.56.0--r42ha9d7317_2": "sha256:9bbeb7632fe1fd6e74f6edf04b5e28a6bcce2708facf9577717654a71be5f180", "1.58.0--r43ha9d7317_0": "sha256:1d6f0bc31e84d59722487b63a43be67716fd802af55a310f24cd96c0536758d4", "1.60.0--r43ha9d7317_0": "sha256:12ff5af68ad6163f208c344d323c9d533fdfff77b0614db2a92c826d9611903a", "1.64.0--r44h3df3fcb_0": "sha256:cd900081b1f821b08f580228dca4672643770dc34512add91fe925343024bb05"}, "docker": "quay.io/biocontainers/bioconductor-metahdep"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metahdep.
shpc-registry automated BioContainers addition for bioconductor-metahdep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metahdep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metahdep:1.64.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metahdep/1.64.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-metahdep/1.64.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metahdep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metahdep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metahdep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metahdep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metahdep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metahdep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metahdep

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