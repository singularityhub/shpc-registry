---
layout: container
name:  "quay.io/biocontainers/trumicount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trumicount/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trumicount/container.yaml"
updated_at: "2025-04-21 04:52:13.489384"
latest: "0.9.14--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/trumicount"
aliases:
 - "gawk-4.1.3"
 - "igawk"
 - "trumicount"
 - "awk"
 - "gawk"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "0.9.9.3--r3.4.1_0"
 - "0.9.14--r41hdfd78af_0"
 - "0.9.14--r42hdfd78af_1"
 - "0.9.14--r43hdfd78af_2"
 - "0.9.14--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for trumicount"
config: {"url": "https://biocontainers.pro/tools/trumicount", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trumicount", "latest": {"0.9.14--r44hdfd78af_3": "sha256:22a75994f23ddb7469cfc0995bfb99df7750cdd2e44e7f5a221ac8c3be1bde94"}, "tags": {"0.9.9.3--r3.4.1_0": "sha256:4a3c3b312b5623ff9ac8bf739eb3bf82ee81dd9373c4a1dd2b19664e905c0dbb", "0.9.14--r41hdfd78af_0": "sha256:e25a7b0191e9df6032236faad48a130595cc3a3ba1d74402e2f69ea7d3046309", "0.9.14--r42hdfd78af_1": "sha256:da14ff3a3fd368a08ea48a637b75409a5681858a66a011c4509d09ca4b116e64", "0.9.14--r43hdfd78af_2": "sha256:fe95f1478e4fccd59e5b3fecba48da2708e1f74ed3317b622aae47de569a3af7", "0.9.14--r44hdfd78af_3": "sha256:22a75994f23ddb7469cfc0995bfb99df7750cdd2e44e7f5a221ac8c3be1bde94"}, "docker": "quay.io/biocontainers/trumicount", "aliases": {"gawk-4.1.3": "/usr/local/bin/gawk-4.1.3", "igawk": "/usr/local/bin/igawk", "trumicount": "/usr/local/bin/trumicount", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trumicount.
shpc-registry automated BioContainers addition for trumicount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trumicount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trumicount:0.9.14--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trumicount/0.9.14--r44hdfd78af_3
$ module help quay.io/biocontainers/trumicount/0.9.14--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trumicount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trumicount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trumicount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trumicount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trumicount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trumicount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk-4.1.3

```bash
$ singularity exec <container> /usr/local/bin/gawk-4.1.3
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-4.1.3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-4.1.3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igawk

```bash
$ singularity exec <container> /usr/local/bin/igawk
$ podman run --it --rm --entrypoint /usr/local/bin/igawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trumicount

```bash
$ singularity exec <container> /usr/local/bin/trumicount
$ podman run --it --rm --entrypoint /usr/local/bin/trumicount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trumicount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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