---
layout: container
name:  "quay.io/biocontainers/bioconductor-sparsesignatures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sparsesignatures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sparsesignatures/container.yaml"
updated_at: "2024-03-18 23:41:38.003095"
latest: "2.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sparsesignatures"

versions:
 - "2.4.0--r41hdfd78af_0"
 - "2.8.0--r42hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sparsesignatures"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sparsesignatures", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sparsesignatures", "latest": {"2.12.0--r43hdfd78af_0": "sha256:09d0e98d9803f498de8e750a99352507542070353b50037688dafc17a3e1d757"}, "tags": {"2.4.0--r41hdfd78af_0": "sha256:ec74d1a0ed2eb295b713e63e3ccb1128c6c72a925f1e4d66bb62b4567da6e73e", "2.8.0--r42hdfd78af_0": "sha256:3aa74dbb9bd0969b8c175c2544e218439e85c05d38a2ebd75b7d25b1bfc15f25", "2.10.0--r43hdfd78af_0": "sha256:1ba97bf5075dac69879cd85e609d0969222c1954cd426b8072089b33317006af", "2.12.0--r43hdfd78af_0": "sha256:09d0e98d9803f498de8e750a99352507542070353b50037688dafc17a3e1d757"}, "docker": "quay.io/biocontainers/bioconductor-sparsesignatures"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sparsesignatures.
shpc-registry automated BioContainers addition for bioconductor-sparsesignatures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsesignatures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sparsesignatures:2.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sparsesignatures/2.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sparsesignatures/2.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sparsesignatures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsesignatures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparsesignatures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sparsesignatures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sparsesignatures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sparsesignatures-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sparsesignatures

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