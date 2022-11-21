---
layout: container
name:  "quay.io/biocontainers/bioconductor-sc3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sc3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sc3/container.yaml"
updated_at: "2022-11-21 13:45:58.067720"
latest: "1.22.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-sc3"

versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.16.0--r40h5f743cb_0"
 - "1.14.0--r36he1b5a44_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sc3"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sc3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sc3", "latest": {"1.22.0--r41hc247a5b_2": "sha256:4bb50eaefc15a90c33b2a65ee0d8636d63897a7032db8bac7a8496e68422fb55"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:0497316480637c02d04e33c439f662e6cd00b812e5703e16f6d3e9255847963c", "1.22.0--r41hc247a5b_2": "sha256:4bb50eaefc15a90c33b2a65ee0d8636d63897a7032db8bac7a8496e68422fb55", "1.20.0--r41h399db7b_0": "sha256:fd0884ecbb56a93615070033e6851d9f8bbd164fff7020b424e1ccbbb59ceb10", "1.18.0--r40h399db7b_1": "sha256:703e12fb4561f8c614fcd106624f06ababf386fd12284553d68025844f42eac6", "1.16.0--r40h5f743cb_0": "sha256:2f7756554fa69a521f918b4f0b532bf91a79562a148c5ee5458a48a5d3c3f771", "1.14.0--r36he1b5a44_0": "sha256:40fb1b93cdfad0b302e40301efa0482002b8568a1643f0c9536e391aae9a70d5"}, "docker": "quay.io/biocontainers/bioconductor-sc3"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sc3.
shpc-registry automated BioContainers addition for bioconductor-sc3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sc3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sc3:1.22.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sc3/1.22.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-sc3/1.22.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sc3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sc3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sc3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sc3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sc3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sc3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sc3

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