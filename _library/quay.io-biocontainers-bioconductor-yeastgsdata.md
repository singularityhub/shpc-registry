---
layout: container
name:  "quay.io/biocontainers/bioconductor-yeastgsdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yeastgsdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yeastgsdata/container.yaml"
updated_at: "2024-10-24 03:32:15.619745"
latest: "0.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-yeastgsdata"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.35.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-yeastgsdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yeastgsdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yeastgsdata", "latest": {"0.40.0--r43hdfd78af_0": "sha256:f652d60d3ac172e0583ddd80be439a548e10ca0f1bd712ecf4030caccc6e8438"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:af4804fcd1fb4dae4e76bc658fa14c2e0f45d8e35ab5ab57a34a59d40e06b74e", "0.35.0--r42hdfd78af_0": "sha256:384d37eb785ce63356711a4d2bbc4fa92cc68d0ff546212bd678fc226a89e35c", "0.38.0--r43hdfd78af_0": "sha256:e9c6b26a2c45c801ad54f5c752753ed990caf1dfa3284d1fc392d78f5096dacf", "0.40.0--r43hdfd78af_0": "sha256:f652d60d3ac172e0583ddd80be439a548e10ca0f1bd712ecf4030caccc6e8438"}, "docker": "quay.io/biocontainers/bioconductor-yeastgsdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yeastgsdata.
shpc-registry automated BioContainers addition for bioconductor-yeastgsdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastgsdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastgsdata:0.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yeastgsdata/0.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-yeastgsdata/0.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yeastgsdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastgsdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastgsdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yeastgsdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yeastgsdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yeastgsdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-yeastgsdata

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