---
layout: container
name:  "bids/broccoli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/broccoli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/broccoli/container.yaml"
updated_at: "2023-11-22 02:31:01.662117"
latest: "enh_various"
container_url: "https://hub.docker.com/r/bids/broccoli"

versions:
 - "enh_v"
 - "enh_various"
description: "BROCCOLI is a software for analysis of fMRI (functional magnetic resonance imaging) data and is written in OpenCL (Open Computing Language).  (https://github.com/BIDS-Apps/BROCCOLI)"
config: {"docker": "bids/broccoli", "latest": {"enh_various": "sha256:64050b22ef4a843a6651b3d782cdf26d7c6e6994ff7994ae9707b7e359ad3602"}, "tags": {"enh_v": "sha256:1ae7cc35e6299fbd6ee020fbe39379d65bc7103b853eae707b8f3f2581c3bee4", "enh_various": "sha256:64050b22ef4a843a6651b3d782cdf26d7c6e6994ff7994ae9707b7e359ad3602"}, "filter": ["enh_v"], "maintainer": "@vsoch", "description": "BROCCOLI is a software for analysis of fMRI (functional magnetic resonance imaging) data and is written in OpenCL (Open Computing Language).  (https://github.com/BIDS-Apps/BROCCOLI)", "url": "https://hub.docker.com/r/bids/broccoli"}
---

This module is a singularity container wrapper for bids/broccoli.
BROCCOLI is a software for analysis of fMRI (functional magnetic resonance imaging) data and is written in OpenCL (Open Computing Language).  (https://github.com/BIDS-Apps/BROCCOLI)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/broccoli
```

Or a specific version:

```bash
$ shpc install bids/broccoli:enh_various
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/broccoli/enh_various
$ module help bids/broccoli/enh_various
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### broccoli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### broccoli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### broccoli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### broccoli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### broccoli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### broccoli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### broccoli

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