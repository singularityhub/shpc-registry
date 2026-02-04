---
layout: container
name:  "quay.io/biocontainers/dartunifrac-gpu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dartunifrac-gpu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dartunifrac-gpu/container.yaml"
updated_at: "2026-02-04 04:19:32.561967"
latest: "0.2.7--hd7384ae_0"
container_url: "https://biocontainers.pro/tools/dartunifrac-gpu"
aliases:
 - "dartunifrac-cuda"
 - "striped_unifrac"
versions:
 - "0.2.7--hd7384ae_0"
description: "singularity registry hpc automated addition for dartunifrac-gpu"
config: {"url": "https://biocontainers.pro/tools/dartunifrac-gpu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dartunifrac-gpu", "latest": {"0.2.7--hd7384ae_0": "sha256:6b61192e7260b101ecf65dc1bfd37656042ee5f91280719aee173bd68eafd3db"}, "tags": {"0.2.7--hd7384ae_0": "sha256:6b61192e7260b101ecf65dc1bfd37656042ee5f91280719aee173bd68eafd3db"}, "docker": "quay.io/biocontainers/dartunifrac-gpu", "aliases": {"dartunifrac-cuda": "/usr/local/bin/dartunifrac-cuda", "striped_unifrac": "/usr/local/bin/striped_unifrac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dartunifrac-gpu.
singularity registry hpc automated addition for dartunifrac-gpu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dartunifrac-gpu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dartunifrac-gpu:0.2.7--hd7384ae_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dartunifrac-gpu/0.2.7--hd7384ae_0
$ module help quay.io/biocontainers/dartunifrac-gpu/0.2.7--hd7384ae_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dartunifrac-gpu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dartunifrac-gpu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dartunifrac-gpu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dartunifrac-gpu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dartunifrac-gpu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dartunifrac-gpu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dartunifrac-cuda

```bash
$ singularity exec <container> /usr/local/bin/dartunifrac-cuda
$ podman run --it --rm --entrypoint /usr/local/bin/dartunifrac-cuda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dartunifrac-cuda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### striped_unifrac

```bash
$ singularity exec <container> /usr/local/bin/striped_unifrac
$ podman run --it --rm --entrypoint /usr/local/bin/striped_unifrac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/striped_unifrac   -v ${PWD} -w ${PWD} <container> -c " $@"
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