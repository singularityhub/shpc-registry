---
layout: container
name:  "quay.io/biocontainers/lrzip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lrzip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lrzip/container.yaml"
updated_at: "2025-01-13 03:06:18.371958"
latest: "0.651--h32784b6_1"
container_url: "https://biocontainers.pro/tools/lrzip"
aliases:
 - "lrunzip"
 - "lrzcat"
 - "lrzip"
 - "lrztar"
 - "lrzuntar"
versions:
 - "0.621--h159dde0_5"
 - "0.621--h159dde0_6"
 - "0.621--hedc9cd1_7"
 - "0.651--h5753e1d_0"
 - "0.651--h32784b6_1"
description: "shpc-registry automated BioContainers addition for lrzip"
config: {"url": "https://biocontainers.pro/tools/lrzip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lrzip", "latest": {"0.651--h32784b6_1": "sha256:ca3475fcbf349c02e7ba514841996dc1f4725296338dbf3501f6b6d538194c6e"}, "tags": {"0.621--h159dde0_5": "sha256:5e6c6973f0575878373c440924b432fe856f6e3896d467f525d41cd5f2f3a9b5", "0.621--h159dde0_6": "sha256:9fd08d86ac5359ab3769e4f6d58e7d04478aaaaa46a318a23751d4618899b76a", "0.621--hedc9cd1_7": "sha256:ed6da06f488a1f811839153e500478947618da05d6b5f4b2051afb780f117f5e", "0.651--h5753e1d_0": "sha256:5349858d767af8b2866b01ee7d1246a7c2642ace69799f91216b64c72292f8d5", "0.651--h32784b6_1": "sha256:ca3475fcbf349c02e7ba514841996dc1f4725296338dbf3501f6b6d538194c6e"}, "docker": "quay.io/biocontainers/lrzip", "aliases": {"lrunzip": "/usr/local/bin/lrunzip", "lrzcat": "/usr/local/bin/lrzcat", "lrzip": "/usr/local/bin/lrzip", "lrztar": "/usr/local/bin/lrztar", "lrzuntar": "/usr/local/bin/lrzuntar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lrzip.
shpc-registry automated BioContainers addition for lrzip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lrzip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lrzip:0.651--h32784b6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lrzip/0.651--h32784b6_1
$ module help quay.io/biocontainers/lrzip/0.651--h32784b6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lrzip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lrzip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lrzip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lrzip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lrzip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lrzip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lrunzip

```bash
$ singularity exec <container> /usr/local/bin/lrunzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzcat

```bash
$ singularity exec <container> /usr/local/bin/lrzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzip

```bash
$ singularity exec <container> /usr/local/bin/lrzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrztar

```bash
$ singularity exec <container> /usr/local/bin/lrztar
$ podman run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzuntar

```bash
$ singularity exec <container> /usr/local/bin/lrzuntar
$ podman run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
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