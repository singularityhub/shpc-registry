---
layout: container
name:  "quay.io/biocontainers/pout2mzid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pout2mzid/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pout2mzid/container.yaml"
updated_at: "2022-10-27 00:19:53.659689"
latest: "0.3.03--boost1.62_2"
container_url: "https://biocontainers.pro/tools/pout2mzid"
aliases:
 - "pout2mzid"
versions:
 - "0.3.03--boost1.62_2"
description: "shpc-registry automated BioContainers addition for pout2mzid"
config: {"url": "https://biocontainers.pro/tools/pout2mzid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pout2mzid", "latest": {"0.3.03--boost1.62_2": "sha256:7843a3c3ad9fb9b50919fa8cc873d5c0c2ae110c273febd845e65bf66e663c25"}, "tags": {"0.3.03--boost1.62_2": "sha256:7843a3c3ad9fb9b50919fa8cc873d5c0c2ae110c273febd845e65bf66e663c25"}, "docker": "quay.io/biocontainers/pout2mzid", "aliases": {"pout2mzid": "/usr/local/bin/pout2mzid"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pout2mzid.
shpc-registry automated BioContainers addition for pout2mzid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pout2mzid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pout2mzid:0.3.03--boost1.62_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pout2mzid/0.3.03--boost1.62_2
$ module help quay.io/biocontainers/pout2mzid/0.3.03--boost1.62_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pout2mzid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pout2mzid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pout2mzid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pout2mzid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pout2mzid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pout2mzid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pout2mzid

```bash
$ singularity exec <container> /usr/local/bin/pout2mzid
$ podman run --it --rm --entrypoint /usr/local/bin/pout2mzid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pout2mzid   -v ${PWD} -w ${PWD} <container> -c " $@"
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