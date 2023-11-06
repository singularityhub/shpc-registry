---
layout: container
name:  "quay.io/biocontainers/bioconductor-affycomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affycomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affycomp/container.yaml"
updated_at: "2023-11-06 02:55:33.757197"
latest: "1.76.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affycomp"

versions:
 - "1.70.0--r41hdfd78af_0"
 - "1.74.0--r42hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affycomp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affycomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affycomp", "latest": {"1.76.0--r43hdfd78af_0": "sha256:06c5823c9bf80f3232e49a4b8bcb06c428e65c5b3701bbaaf7a1b2ce24c574f6"}, "tags": {"1.70.0--r41hdfd78af_0": "sha256:f3569863a269f5ccd7196695cf7c93d8df7e92e4c2dc32ba00d80d13dadca3ab", "1.74.0--r42hdfd78af_0": "sha256:432a72b90cb733c3c10f2be9c7d7a79f979ca2eeee5f5fb5af282c120d56b7ba", "1.76.0--r43hdfd78af_0": "sha256:06c5823c9bf80f3232e49a4b8bcb06c428e65c5b3701bbaaf7a1b2ce24c574f6"}, "docker": "quay.io/biocontainers/bioconductor-affycomp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affycomp.
shpc-registry automated BioContainers addition for bioconductor-affycomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affycomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affycomp:1.76.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affycomp/1.76.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affycomp/1.76.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affycomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affycomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affycomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affycomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affycomp

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