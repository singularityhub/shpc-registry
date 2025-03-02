---
layout: container
name:  "quay.io/biocontainers/adapterremoval"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/adapterremoval/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/adapterremoval/container.yaml"
updated_at: "2025-03-02 03:22:54.212244"
latest: "2.3.4--pl5321haf24da9_1"
container_url: "https://biocontainers.pro/tools/adapterremoval"
aliases:
 - "AdapterRemoval"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.3.3--pl5321h19e8d03_0"
 - "2.3.3--pl5321h6dccd9a_2"
 - "2.3.3--pl5321h6dccd9a_3"
 - "2.3.4--pl5321h6dccd9a_0"
 - "2.3.4--pl5321haf24da9_1"
description: "shpc-registry automated BioContainers addition for adapterremoval"
config: {"url": "https://biocontainers.pro/tools/adapterremoval", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for adapterremoval", "latest": {"2.3.4--pl5321haf24da9_1": "sha256:a3f40b914f590e25dc3256b481342c91ca490bc7abda264a73dc3cc9d9808bb5"}, "tags": {"2.3.3--pl5321h19e8d03_0": "sha256:e0c9cb7d5b6f1306a8147a97a59bf5a8b68915b88a2863a4b1b8c9eb24b21fc3", "2.3.3--pl5321h6dccd9a_2": "sha256:5999669f3537e784919feaf6347efe7ad2b1924a14ee4a31398d3ce15f766dc2", "2.3.3--pl5321h6dccd9a_3": "sha256:2852c4b7caab17fc9d82e96abd305c05307fe28fe8cddb0eb81c511c28c08aa5", "2.3.4--pl5321h6dccd9a_0": "sha256:d7cfa399c45483b1992368199035df4dc829e4026ccb15296519bb2f6b79a54e", "2.3.4--pl5321haf24da9_1": "sha256:a3f40b914f590e25dc3256b481342c91ca490bc7abda264a73dc3cc9d9808bb5"}, "docker": "quay.io/biocontainers/adapterremoval", "aliases": {"AdapterRemoval": "/usr/local/bin/AdapterRemoval", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/adapterremoval.
shpc-registry automated BioContainers addition for adapterremoval
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/adapterremoval
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/adapterremoval:2.3.4--pl5321haf24da9_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/adapterremoval/2.3.4--pl5321haf24da9_1
$ module help quay.io/biocontainers/adapterremoval/2.3.4--pl5321haf24da9_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adapterremoval-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adapterremoval-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adapterremoval-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adapterremoval-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adapterremoval-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adapterremoval-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AdapterRemoval

```bash
$ singularity exec <container> /usr/local/bin/AdapterRemoval
$ podman run --it --rm --entrypoint /usr/local/bin/AdapterRemoval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AdapterRemoval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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