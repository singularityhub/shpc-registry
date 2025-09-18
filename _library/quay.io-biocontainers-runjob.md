---
layout: container
name:  "quay.io/biocontainers/runjob"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/runjob/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/runjob/container.yaml"
updated_at: "2025-09-18 03:28:47.367975"
latest: "2.10.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/runjob"
aliases:
 - "qcs"
 - "qs"
 - "runbatch"
 - "runjob"
 - "runsge"
 - "runsge0"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "2.10.2--pyhdfd78af_0"
 - "2.10.3--pyhdfd78af_0"
 - "2.10.4--pyhdfd78af_0"
 - "2.10.5--pyhdfd78af_0"
 - "2.10.6--pyhdfd78af_0"
 - "2.10.9--pyhdfd78af_0"
description: "singularity registry hpc automated addition for runjob"
config: {"url": "https://biocontainers.pro/tools/runjob", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for runjob", "latest": {"2.10.9--pyhdfd78af_0": "sha256:cdf439d80606d9b2e3dbb6fd730232b7a80b0ad4dfc5fcd1882cddbb4626ee72"}, "tags": {"2.10.2--pyhdfd78af_0": "sha256:ca98697092fbbc8fc63c9023681f90e7c0f4b9991cc48a9ff0a1cbfa20b2241a", "2.10.3--pyhdfd78af_0": "sha256:6e2a15c74f62a676ec4dd73988133f06ad08dbf492161d02d2affcaafa9f4831", "2.10.4--pyhdfd78af_0": "sha256:3f30743ba73f42d430309b05b9c3091b323e941577818f6937866d24d01055f4", "2.10.5--pyhdfd78af_0": "sha256:7326994c66aa57e7357e5dd75f5fee66bd5cebaf0cb88bb1dc6fd9bb97ab8072", "2.10.6--pyhdfd78af_0": "sha256:5b580c79ad74dcca4e4439e469c7f34d3426c6b19883922cb856dd9c27d131e5", "2.10.9--pyhdfd78af_0": "sha256:cdf439d80606d9b2e3dbb6fd730232b7a80b0ad4dfc5fcd1882cddbb4626ee72"}, "docker": "quay.io/biocontainers/runjob", "aliases": {"qcs": "/usr/local/bin/qcs", "qs": "/usr/local/bin/qs", "runbatch": "/usr/local/bin/runbatch", "runjob": "/usr/local/bin/runjob", "runsge": "/usr/local/bin/runsge", "runsge0": "/usr/local/bin/runsge0", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/runjob.
singularity registry hpc automated addition for runjob
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/runjob
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/runjob:2.10.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/runjob/2.10.9--pyhdfd78af_0
$ module help quay.io/biocontainers/runjob/2.10.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### runjob-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### runjob-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### runjob-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### runjob-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### runjob-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### runjob-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qcs

```bash
$ singularity exec <container> /usr/local/bin/qcs
$ podman run --it --rm --entrypoint /usr/local/bin/qcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qs

```bash
$ singularity exec <container> /usr/local/bin/qs
$ podman run --it --rm --entrypoint /usr/local/bin/qs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runbatch

```bash
$ singularity exec <container> /usr/local/bin/runbatch
$ podman run --it --rm --entrypoint /usr/local/bin/runbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runjob

```bash
$ singularity exec <container> /usr/local/bin/runjob
$ podman run --it --rm --entrypoint /usr/local/bin/runjob   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runjob   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runsge

```bash
$ singularity exec <container> /usr/local/bin/runsge
$ podman run --it --rm --entrypoint /usr/local/bin/runsge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runsge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runsge0

```bash
$ singularity exec <container> /usr/local/bin/runsge0
$ podman run --it --rm --entrypoint /usr/local/bin/runsge0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runsge0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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