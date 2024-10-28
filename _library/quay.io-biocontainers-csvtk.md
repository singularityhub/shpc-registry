---
layout: container
name:  "quay.io/biocontainers/csvtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/csvtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/csvtk/container.yaml"
updated_at: "2024-10-28 03:35:44.152050"
latest: "0.30.0--h9ee0642_2"
container_url: "https://biocontainers.pro/tools/csvtk"
aliases:
 - "csvtk"
versions:
 - "0.9.1--0"
 - "0.25.0--h9ee0642_0"
 - "0.24.0--h9ee0642_0"
 - "0.23.0--h9ee0642_0"
 - "0.22.0--h9ee0642_1"
 - "0.21.0--0"
 - "0.26.0--h9ee0642_0"
 - "0.27.2--h9ee0642_0"
 - "0.28.0--h9ee0642_0"
 - "0.29.0--h9ee0642_0"
 - "0.30.0--h9ee0642_1"
 - "0.30.0--h9ee0642_2"
description: "shpc-registry automated BioContainers addition for csvtk"
config: {"url": "https://biocontainers.pro/tools/csvtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for csvtk", "latest": {"0.30.0--h9ee0642_2": "sha256:823983bb6611770d91f053c1dff42e4213d7ec3e345187af96220510b5c53bc3"}, "tags": {"0.9.1--0": "sha256:f65b8de8066c7356a969fa878bc1d7594ed4a25fbf8ee8d2fd2da18d60b93271", "0.25.0--h9ee0642_0": "sha256:f07592f60d3749bfb3df81a23f57d5e709cda30b3c818ac0be699e586bff01b2", "0.24.0--h9ee0642_0": "sha256:80cddaa213cf1d67362394b41cbba51e9b9b31afeafe2383bfa8bc9c3dfa4217", "0.23.0--h9ee0642_0": "sha256:3250fe7bad2d661c1ad6a40983383ae98d29548f9df75f0830ecf1686647d2c6", "0.22.0--h9ee0642_1": "sha256:da9ce8ebf0e9f88c29317de4ce56ccc31c5845887d5ac7f7037354e2c92c25c4", "0.21.0--0": "sha256:72c9b7f9f9c17bb758dd28eb25d033d46fa0d0cbfd085ae6df28c1e3c3fa0d61", "0.26.0--h9ee0642_0": "sha256:689199471f4d63aa671a7307266ce2b75e8dc1f5a70078f6caded8d5fc5ed42d", "0.27.2--h9ee0642_0": "sha256:f90dd399ff459b1de53f4ffb43f19891ffb8f30d52ae3f40ac65a5a2a6629bae", "0.28.0--h9ee0642_0": "sha256:2bba5a84515e6242407fbb6cdd571b8a62711dfe87325dc913de11cfd3881998", "0.29.0--h9ee0642_0": "sha256:ffe51fde60ad717d1709324259c962499e2641bf35b2c0a7e09dac53f8aa9ffd", "0.30.0--h9ee0642_1": "sha256:4a854c8968a07dd908a8c640d31662e98ea2dadab89bb0a5050a0ad6e071abe2", "0.30.0--h9ee0642_2": "sha256:823983bb6611770d91f053c1dff42e4213d7ec3e345187af96220510b5c53bc3"}, "docker": "quay.io/biocontainers/csvtk", "aliases": {"csvtk": "/usr/local/bin/csvtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/csvtk.
shpc-registry automated BioContainers addition for csvtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/csvtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/csvtk:0.30.0--h9ee0642_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/csvtk/0.30.0--h9ee0642_2
$ module help quay.io/biocontainers/csvtk/0.30.0--h9ee0642_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### csvtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### csvtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### csvtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### csvtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### csvtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### csvtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csvtk

```bash
$ singularity exec <container> /usr/local/bin/csvtk
$ podman run --it --rm --entrypoint /usr/local/bin/csvtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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