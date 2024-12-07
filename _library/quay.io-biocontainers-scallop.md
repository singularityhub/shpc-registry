---
layout: container
name:  "quay.io/biocontainers/scallop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scallop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scallop/container.yaml"
updated_at: "2024-12-07 01:35:42.239623"
latest: "0.10.5--hdbdd923_7"
container_url: "https://biocontainers.pro/tools/scallop"

versions:
 - "0.10.5--hefd527f_4"
 - "0.10.5--h66ab1b6_5"
 - "0.10.5--h5642b88_6"
 - "0.10.5--hdbdd923_7"
description: "shpc-registry automated BioContainers addition for scallop"
config: {"url": "https://biocontainers.pro/tools/scallop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scallop", "latest": {"0.10.5--hdbdd923_7": "sha256:7a11697b5519131c477f44d2a797cb1880cb3b23ef26e0a91cc9f21dc31f4949"}, "tags": {"0.10.5--hefd527f_4": "sha256:ef2017f4248b84f089ebaa0e7d1fd276d02780494648a75dcfa4ed6c72cf8ed0", "0.10.5--h66ab1b6_5": "sha256:4aa17bddb92fbec06154e75e7a027d6e559637b1736a1528d718308adce17dc9", "0.10.5--h5642b88_6": "sha256:bae2baf00cec926f2cdb2c7cccba7245cd4273557bd111a0722aff3de8a2fcfe", "0.10.5--hdbdd923_7": "sha256:7a11697b5519131c477f44d2a797cb1880cb3b23ef26e0a91cc9f21dc31f4949"}, "docker": "quay.io/biocontainers/scallop"}
---

This module is a singularity container wrapper for quay.io/biocontainers/scallop.
shpc-registry automated BioContainers addition for scallop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scallop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scallop:0.10.5--hdbdd923_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scallop/0.10.5--hdbdd923_7
$ module help quay.io/biocontainers/scallop/0.10.5--hdbdd923_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scallop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scallop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scallop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scallop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scallop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scallop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### scallop

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