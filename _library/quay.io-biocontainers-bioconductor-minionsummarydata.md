---
layout: container
name:  "quay.io/biocontainers/bioconductor-minionsummarydata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-minionsummarydata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-minionsummarydata/container.yaml"
updated_at: "2024-11-12 02:59:37.530093"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-minionsummarydata"

versions:
 - "1.24.0--r41hdfd78af_1"
 - "1.27.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-minionsummarydata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-minionsummarydata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-minionsummarydata", "latest": {"1.32.0--r43hdfd78af_0": "sha256:52bc778694259424f8021aa060f73a48d271bfdfd1247806c420794629263dea"}, "tags": {"1.24.0--r41hdfd78af_1": "sha256:4299144aa702268ac2f805f2d216d8a308d5d37917628d5e4d4317b89d3d1d84", "1.27.0--r42hdfd78af_0": "sha256:e8e757b249a8f39307760a21566f6dd38586cf36ba976722d8e0b768d55cea55", "1.30.0--r43hdfd78af_0": "sha256:8597277637c05aa750c54c4028e06f5d53c569cc43ef4268252b23ab26fba36a", "1.32.0--r43hdfd78af_0": "sha256:52bc778694259424f8021aa060f73a48d271bfdfd1247806c420794629263dea"}, "docker": "quay.io/biocontainers/bioconductor-minionsummarydata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-minionsummarydata.
shpc-registry automated BioContainers addition for bioconductor-minionsummarydata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-minionsummarydata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-minionsummarydata:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-minionsummarydata/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-minionsummarydata/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-minionsummarydata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-minionsummarydata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-minionsummarydata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-minionsummarydata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-minionsummarydata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-minionsummarydata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-minionsummarydata

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