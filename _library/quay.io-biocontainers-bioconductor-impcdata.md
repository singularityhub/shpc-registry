---
layout: container
name:  "quay.io/biocontainers/bioconductor-impcdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-impcdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-impcdata/container.yaml"
updated_at: "2024-04-10 02:39:21.086987"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-impcdata"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-impcdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-impcdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-impcdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:8106895c615eca9e399a5883bd39190016aee420cfe3eac7efda06cbd2a61099"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:93dafe57cd084ea431e54187ffcd9d3b26257bd439fae2b89470a4b12964b4da", "1.34.0--r42hdfd78af_0": "sha256:98b7c75c935f89bca61180c648183b88991dbc1d2671cbdf6ef61207ed23ea19", "1.36.0--r43hdfd78af_0": "sha256:4c8e83bdd79f1010e915effafca8b0e7de626c4191187c1d03e41588684b5d7a", "1.38.0--r43hdfd78af_0": "sha256:8106895c615eca9e399a5883bd39190016aee420cfe3eac7efda06cbd2a61099"}, "docker": "quay.io/biocontainers/bioconductor-impcdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-impcdata.
shpc-registry automated BioContainers addition for bioconductor-impcdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-impcdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-impcdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-impcdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-impcdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-impcdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-impcdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-impcdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-impcdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-impcdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-impcdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-impcdata

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