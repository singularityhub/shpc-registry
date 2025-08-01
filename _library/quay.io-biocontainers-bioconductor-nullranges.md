---
layout: container
name:  "quay.io/biocontainers/bioconductor-nullranges"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nullranges/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nullranges/container.yaml"
updated_at: "2025-08-01 04:38:53.048295"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nullranges"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.2--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nullranges"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nullranges", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nullranges", "latest": {"1.12.0--r44hdfd78af_0": "sha256:8ab937d7638e9ba3b28ddf846ab6cd4f196c25b3d5a482fe866a283c2c7188c9"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:a0dccd4c33de075d6bc885f6b2f9befc6d6063f367c779200bc31d7d32422faa", "1.4.0--r42hdfd78af_0": "sha256:4bc87ae9234db9b90dc662fc4365794ef027c751a348f7c470207f993246cd91", "1.6.2--r43hdfd78af_0": "sha256:2ca4df22950c7ebbf611265a5c72d0365332138c97eddb2e3d2d6def6f85fc63", "1.8.0--r43hdfd78af_0": "sha256:79d3e1b462f253fb219c48802a1e9d69e02c3594faf8167ccb47c4bfe7d949fb", "1.12.0--r44hdfd78af_0": "sha256:8ab937d7638e9ba3b28ddf846ab6cd4f196c25b3d5a482fe866a283c2c7188c9"}, "docker": "quay.io/biocontainers/bioconductor-nullranges"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nullranges.
shpc-registry automated BioContainers addition for bioconductor-nullranges
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nullranges
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nullranges:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nullranges/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nullranges/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nullranges-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nullranges-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nullranges-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nullranges-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nullranges-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nullranges-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nullranges

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