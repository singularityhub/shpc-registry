---
layout: container
name:  "quay.io/biocontainers/coatran"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coatran/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/coatran/container.yaml"
updated_at: "2024-12-23 03:13:04.448302"
latest: "0.0.4--h503566f_1"
container_url: "https://biocontainers.pro/tools/coatran"
aliases:
 - "coatran_constant"
 - "coatran_expgrowth"
 - "coatran_inftime"
 - "coatran_transtree"
versions:
 - "0.0.1--h9f5acd7_1"
 - "0.0.1--h4ac6f70_3"
 - "0.0.4--hdbdd923_0"
 - "0.0.4--h503566f_1"
description: "shpc-registry automated BioContainers addition for coatran"
config: {"url": "https://biocontainers.pro/tools/coatran", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for coatran", "latest": {"0.0.4--h503566f_1": "sha256:39cc10bcc01b2a39927c3d94c6afd61488652255a647ec9b17a51b1317ab3986"}, "tags": {"0.0.1--h9f5acd7_1": "sha256:a06f219fe42b1f23edd5c6718dbaf582a459bd1d5ddb86c8193e1094adc1c052", "0.0.1--h4ac6f70_3": "sha256:58f940650adaaad24e0f158dd3a274bf04fbbda343ab8f0e129944e298a35db9", "0.0.4--hdbdd923_0": "sha256:b1db3e85a3f237dddcc27410975348778ae8d1effa18cffea9d6b21bc552ef3b", "0.0.4--h503566f_1": "sha256:39cc10bcc01b2a39927c3d94c6afd61488652255a647ec9b17a51b1317ab3986"}, "docker": "quay.io/biocontainers/coatran", "aliases": {"coatran_constant": "/usr/local/bin/coatran_constant", "coatran_expgrowth": "/usr/local/bin/coatran_expgrowth", "coatran_inftime": "/usr/local/bin/coatran_inftime", "coatran_transtree": "/usr/local/bin/coatran_transtree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coatran.
shpc-registry automated BioContainers addition for coatran
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coatran
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coatran:0.0.4--h503566f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coatran/0.0.4--h503566f_1
$ module help quay.io/biocontainers/coatran/0.0.4--h503566f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coatran-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coatran-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coatran-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coatran-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coatran-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coatran-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coatran_constant

```bash
$ singularity exec <container> /usr/local/bin/coatran_constant
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_constant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_constant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coatran_expgrowth

```bash
$ singularity exec <container> /usr/local/bin/coatran_expgrowth
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_expgrowth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_expgrowth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coatran_inftime

```bash
$ singularity exec <container> /usr/local/bin/coatran_inftime
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_inftime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_inftime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coatran_transtree

```bash
$ singularity exec <container> /usr/local/bin/coatran_transtree
$ podman run --it --rm --entrypoint /usr/local/bin/coatran_transtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coatran_transtree   -v ${PWD} -w ${PWD} <container> -c " $@"
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