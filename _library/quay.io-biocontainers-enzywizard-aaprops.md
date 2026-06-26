---
layout: container
name:  "quay.io/biocontainers/enzywizard-aaprops"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enzywizard-aaprops/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enzywizard-aaprops/container.yaml"
updated_at: "2026-06-26 02:07:59.147551"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/enzywizard-aaprops"
aliases:
 - "enzywizard-aaprops"
 - "mkdssp"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
versions:
 - "1.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for enzywizard-aaprops"
config: {"url": "https://biocontainers.pro/tools/enzywizard-aaprops", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for enzywizard-aaprops", "latest": {"1.0.2--pyhdfd78af_0": "sha256:9f9893bff273bb31b7dccb548b5d47116ccf3633438fda5e5cddfdadcd747783"}, "tags": {"1.0.2--pyhdfd78af_0": "sha256:9f9893bff273bb31b7dccb548b5d47116ccf3633438fda5e5cddfdadcd747783"}, "docker": "quay.io/biocontainers/enzywizard-aaprops", "aliases": {"enzywizard-aaprops": "/usr/local/bin/enzywizard-aaprops", "mkdssp": "/usr/local/bin/mkdssp", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enzywizard-aaprops.
singularity registry hpc automated addition for enzywizard-aaprops
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enzywizard-aaprops
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enzywizard-aaprops:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enzywizard-aaprops/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/enzywizard-aaprops/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enzywizard-aaprops-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enzywizard-aaprops-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enzywizard-aaprops-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enzywizard-aaprops-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enzywizard-aaprops-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enzywizard-aaprops-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### enzywizard-aaprops

```bash
$ singularity exec <container> /usr/local/bin/enzywizard-aaprops
$ podman run --it --rm --entrypoint /usr/local/bin/enzywizard-aaprops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enzywizard-aaprops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkdssp

```bash
$ singularity exec <container> /usr/local/bin/mkdssp
$ podman run --it --rm --entrypoint /usr/local/bin/mkdssp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkdssp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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