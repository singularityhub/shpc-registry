---
layout: container
name:  "quay.io/biocontainers/bioconductor-paircompviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-paircompviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-paircompviz/container.yaml"
updated_at: "2023-10-05 03:22:46.075611"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-paircompviz"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-paircompviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-paircompviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-paircompviz", "latest": {"1.38.0--r43hdfd78af_0": "sha256:48821f979b8980d616773bf36cebefa69f23a88e97f58ebe2045a77e568abc3d"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:6fbc26b645a1d0c47241bd06a0ea03577ed91693b1288bf0169c7324a764f1c5", "1.36.0--r42hdfd78af_0": "sha256:6d7b311972ddd0f1c40033b6d4699468eb2efa5d790e803b28bcb53d3d2e11c8", "1.38.0--r43hdfd78af_0": "sha256:48821f979b8980d616773bf36cebefa69f23a88e97f58ebe2045a77e568abc3d"}, "docker": "quay.io/biocontainers/bioconductor-paircompviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-paircompviz.
shpc-registry automated BioContainers addition for bioconductor-paircompviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-paircompviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-paircompviz:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-paircompviz/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-paircompviz/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-paircompviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paircompviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paircompviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-paircompviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-paircompviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-paircompviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-paircompviz

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