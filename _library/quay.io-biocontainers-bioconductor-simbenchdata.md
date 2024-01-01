---
layout: container
name:  "quay.io/biocontainers/bioconductor-simbenchdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simbenchdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simbenchdata/container.yaml"
updated_at: "2024-01-01 03:06:34.018903"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simbenchdata"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simbenchdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simbenchdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simbenchdata", "latest": {"1.10.0--r43hdfd78af_0": "sha256:e5629796d6d642eeee2ad1a5028f7669293426e386f7762cbe9b5dd18eb5d5c0"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:681ad4a4edb5165104ddcf4bc507a59755c70ac44039d3c9d69fc07cb7be67db", "1.6.0--r42hdfd78af_0": "sha256:946fb8c6e2ea5db41445b2b4e85fe84fe7d73b1c0e1997740ece0482dcc31c5a", "1.8.0--r43hdfd78af_0": "sha256:45d18edf70abd6303864c138d854f8d86c6b043373a994fef4e66d2783fb28dd", "1.10.0--r43hdfd78af_0": "sha256:e5629796d6d642eeee2ad1a5028f7669293426e386f7762cbe9b5dd18eb5d5c0"}, "docker": "quay.io/biocontainers/bioconductor-simbenchdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simbenchdata.
shpc-registry automated BioContainers addition for bioconductor-simbenchdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simbenchdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simbenchdata:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simbenchdata/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-simbenchdata/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simbenchdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simbenchdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simbenchdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simbenchdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simbenchdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simbenchdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-simbenchdata

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