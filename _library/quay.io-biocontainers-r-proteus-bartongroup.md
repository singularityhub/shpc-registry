---
layout: container
name:  "quay.io/biocontainers/r-proteus-bartongroup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-proteus-bartongroup/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-proteus-bartongroup/container.yaml"
updated_at: "2025-02-16 03:18:13.012109"
latest: "0.2.16--r44hdfd78af_2"
container_url: "https://biocontainers.pro/tools/r-proteus-bartongroup"
aliases:
 - "hb-info"
 - "tjbench"
 - "pandoc"
versions:
 - "0.2.16--r42hdfd78af_0"
 - "0.2.16--r43hdfd78af_1"
 - "0.2.16--r44hdfd78af_2"
description: "singularity registry hpc automated addition for r-proteus-bartongroup"
config: {"url": "https://biocontainers.pro/tools/r-proteus-bartongroup", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-proteus-bartongroup", "latest": {"0.2.16--r44hdfd78af_2": "sha256:9ae049685192b3ffe70c422d8952a5a01d442701ba7cb4241bad2cbb26c6b99c"}, "tags": {"0.2.16--r42hdfd78af_0": "sha256:ccaff64ed1434cbf03a07c871d20ab0b7530801528934c260275ba39a395b471", "0.2.16--r43hdfd78af_1": "sha256:ae8682011d6cecd54f2a00078d5be7b37ba452d5d03f0e4ad74b6ea2ffb2268a", "0.2.16--r44hdfd78af_2": "sha256:9ae049685192b3ffe70c422d8952a5a01d442701ba7cb4241bad2cbb26c6b99c"}, "docker": "quay.io/biocontainers/r-proteus-bartongroup", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-proteus-bartongroup.
singularity registry hpc automated addition for r-proteus-bartongroup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-proteus-bartongroup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-proteus-bartongroup:0.2.16--r44hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-proteus-bartongroup/0.2.16--r44hdfd78af_2
$ module help quay.io/biocontainers/r-proteus-bartongroup/0.2.16--r44hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-proteus-bartongroup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-proteus-bartongroup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-proteus-bartongroup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-proteus-bartongroup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-proteus-bartongroup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-proteus-bartongroup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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