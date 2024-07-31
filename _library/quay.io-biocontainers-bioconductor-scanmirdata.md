---
layout: container
name:  "quay.io/biocontainers/bioconductor-scanmirdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scanmirdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scanmirdata/container.yaml"
updated_at: "2024-07-31 03:00:28.238759"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scanmirdata"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scanmirdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scanmirdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scanmirdata", "latest": {"1.8.0--r43hdfd78af_0": "sha256:b2e789db909380248e552d93c0dc46ac1df73ba2687ca56e035a5aec2e537e71"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:5c94f71e4580aed50e3f58f8f2093d85567a83e377759776da6ac3455272bc43", "1.4.0--r42hdfd78af_0": "sha256:0ccc3b91e5ba9d67ac1df9b8eeae09a4f915ca76026eb9e3da8c277ee31c9ab2", "1.6.0--r43hdfd78af_0": "sha256:52a13438972aa2b982a4d1d55f067528326c2614ae49817c2f1d14f409b3e35d", "1.8.0--r43hdfd78af_0": "sha256:b2e789db909380248e552d93c0dc46ac1df73ba2687ca56e035a5aec2e537e71"}, "docker": "quay.io/biocontainers/bioconductor-scanmirdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scanmirdata.
shpc-registry automated BioContainers addition for bioconductor-scanmirdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scanmirdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scanmirdata:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scanmirdata/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scanmirdata/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scanmirdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scanmirdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scanmirdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scanmirdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scanmirdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scanmirdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scanmirdata

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