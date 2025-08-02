---
layout: container
name:  "quay.io/biocontainers/bioconductor-cbioportaldata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cbioportaldata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cbioportaldata/container.yaml"
updated_at: "2025-08-02 03:34:58.365030"
latest: "2.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cbioportaldata"

versions:
 - "2.6.0--r41hdfd78af_0"
 - "2.10.0--r42hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.14.0--r43hdfd78af_0"
 - "2.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cbioportaldata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cbioportaldata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cbioportaldata", "latest": {"2.18.0--r44hdfd78af_0": "sha256:ae57c1d3faafcf796fc74f6ab80e3457787633c71e2e466e40f502bb55854e92"}, "tags": {"2.6.0--r41hdfd78af_0": "sha256:56f3b30c2cbdf566b7708b99b3f021f9711f596851e14423091555b1499049c1", "2.10.0--r42hdfd78af_0": "sha256:9d98f19995f99ca2ae664348799429e1888da1b2fc64bc0d34451e3046f85f43", "2.12.0--r43hdfd78af_0": "sha256:5b9636aca5427a032a042658066b719ac21eb8d97fb01c9f6fe027eaa7f8646f", "2.14.0--r43hdfd78af_0": "sha256:3f8909dd6fd663f517d9557b9c52a92e102b9cff8f7d41e732f2d3b67ada7198", "2.18.0--r44hdfd78af_0": "sha256:ae57c1d3faafcf796fc74f6ab80e3457787633c71e2e466e40f502bb55854e92"}, "docker": "quay.io/biocontainers/bioconductor-cbioportaldata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cbioportaldata.
shpc-registry automated BioContainers addition for bioconductor-cbioportaldata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cbioportaldata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cbioportaldata:2.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cbioportaldata/2.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cbioportaldata/2.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cbioportaldata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cbioportaldata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cbioportaldata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cbioportaldata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cbioportaldata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cbioportaldata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cbioportaldata

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