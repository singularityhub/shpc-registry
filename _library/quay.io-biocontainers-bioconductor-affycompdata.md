---
layout: container
name:  "quay.io/biocontainers/bioconductor-affycompdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affycompdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affycompdata/container.yaml"
updated_at: "2025-02-04 02:52:59.056772"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affycompdata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affycompdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affycompdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affycompdata", "latest": {"1.44.0--r44hdfd78af_0": "sha256:d1a4350950b7bb97d0bdc059eee20b559933487dd98b9807816c84cc1e092245"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:d48aec6d007037c77b97a5e4bf09074b2b1bcdc74307640999855e6d5d45bbf5", "1.36.0--r42hdfd78af_0": "sha256:2f1d9cdbec053dcea000a4fc231df42c8ce20db76ce4648343072e3ef472b91e", "1.38.0--r43hdfd78af_0": "sha256:45146f063f330b12abe61eeeb33fe58ca19fb7873e2913402e75d3b48cc3a05f", "1.40.0--r43hdfd78af_0": "sha256:5e5f9b4cd742000918c26a19df9422003ba8a3a4aca7bf272839f74eea08575d", "1.44.0--r44hdfd78af_0": "sha256:d1a4350950b7bb97d0bdc059eee20b559933487dd98b9807816c84cc1e092245"}, "docker": "quay.io/biocontainers/bioconductor-affycompdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affycompdata.
shpc-registry automated BioContainers addition for bioconductor-affycompdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affycompdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affycompdata:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affycompdata/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affycompdata/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affycompdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycompdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affycompdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affycompdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affycompdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affycompdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affycompdata

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