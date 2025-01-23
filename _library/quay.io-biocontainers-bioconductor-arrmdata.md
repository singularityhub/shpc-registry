---
layout: container
name:  "quay.io/biocontainers/bioconductor-arrmdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-arrmdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-arrmdata/container.yaml"
updated_at: "2025-01-23 04:05:42.947299"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-arrmdata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-arrmdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-arrmdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-arrmdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:f56fe7010caf3dd16731f92752a7549a61b4cc6d30d9599b7f9e8e8e5dcad4c5"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:d439ab215ae781076d0af48839816e5f655b3c51f75d7ea45c99db5c1bb42bde", "1.33.0--r42hdfd78af_0": "sha256:2bd9e679bebdb09dfc7d06c5eef136946a3060b7759bf046aeb41b9a34de21f9", "1.36.0--r43hdfd78af_0": "sha256:18342c4edb5c9e8191334e22452bfa7184dd55f308173cd64a7f4754ca858a84", "1.38.0--r43hdfd78af_0": "sha256:f56fe7010caf3dd16731f92752a7549a61b4cc6d30d9599b7f9e8e8e5dcad4c5"}, "docker": "quay.io/biocontainers/bioconductor-arrmdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-arrmdata.
shpc-registry automated BioContainers addition for bioconductor-arrmdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-arrmdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-arrmdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-arrmdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-arrmdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-arrmdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrmdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-arrmdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-arrmdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-arrmdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-arrmdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-arrmdata

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