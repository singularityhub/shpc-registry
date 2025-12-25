---
layout: container
name:  "quay.io/biocontainers/bioconductor-hmmcopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hmmcopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hmmcopy/container.yaml"
updated_at: "2025-12-25 04:20:38.883832"
latest: "1.48.0--r44h3df3fcb_1"
container_url: "https://biocontainers.pro/tools/bioconductor-hmmcopy"

versions:
 - "1.36.0--r41hc0cfd56_2"
 - "1.40.0--r42hc0cfd56_0"
 - "1.40.0--r42ha9d7317_2"
 - "1.42.0--r43ha9d7317_0"
 - "1.44.0--r43ha9d7317_1"
 - "1.48.0--r44h3df3fcb_0"
 - "1.48.0--r44h3df3fcb_1"
description: "shpc-registry automated BioContainers addition for bioconductor-hmmcopy"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hmmcopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hmmcopy", "latest": {"1.48.0--r44h3df3fcb_1": "sha256:bb4fc52bf8b028c192ab3293da819a3486b40a1ea9589013f69a55f4adaf2eb2"}, "tags": {"1.36.0--r41hc0cfd56_2": "sha256:cc8d9c0d15af0412738d16b6c0084274fe8eb2ab6a63f7f53624e29023fcb172", "1.40.0--r42hc0cfd56_0": "sha256:9a1726df08dbbf004065c203c2ef7890daa473a6ee41fd15ef64965aa08da7af", "1.40.0--r42ha9d7317_2": "sha256:4fbe085107ea1122eb98d2a7111cfeddb50dae625bcb03a2749029079070d6ce", "1.42.0--r43ha9d7317_0": "sha256:db7b42ec57957a6b3ca08239ccc20d585db2e8632939d4f1ffd923a7905af0e7", "1.44.0--r43ha9d7317_1": "sha256:5eba57fad05e44d5b67ae63a9a2531c5c83717f6ddff5608b937fdc9c0563101", "1.48.0--r44h3df3fcb_0": "sha256:d4808c78372a06dac3027e0c61a32814a6c3cc9b2e42258af46743de76c37afd", "1.48.0--r44h3df3fcb_1": "sha256:bb4fc52bf8b028c192ab3293da819a3486b40a1ea9589013f69a55f4adaf2eb2"}, "docker": "quay.io/biocontainers/bioconductor-hmmcopy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hmmcopy.
shpc-registry automated BioContainers addition for bioconductor-hmmcopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hmmcopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hmmcopy:1.48.0--r44h3df3fcb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hmmcopy/1.48.0--r44h3df3fcb_1
$ module help quay.io/biocontainers/bioconductor-hmmcopy/1.48.0--r44h3df3fcb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hmmcopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hmmcopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hmmcopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hmmcopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hmmcopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hmmcopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hmmcopy

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