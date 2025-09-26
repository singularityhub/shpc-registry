---
layout: container
name:  "quay.io/biocontainers/align_trim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/align_trim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/align_trim/container.yaml"
updated_at: "2025-09-26 03:23:36.187499"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/align_trim"
aliases:
 - "align_trim"
 - "primalbedtools"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "1.0.1--pyhdfd78af_0"
 - "1.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for align_trim"
config: {"url": "https://biocontainers.pro/tools/align_trim", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for align_trim", "latest": {"1.0.2--pyhdfd78af_0": "sha256:c11f7e8f838a521d25a162ffd55efe5c3916e828545fac82e07e7f6866badeae"}, "tags": {"1.0.1--pyhdfd78af_0": "sha256:cf7a180e474aec951580411f67c0fd5915204a40ae8a2758eede7973d37f7ab3", "1.0.2--pyhdfd78af_0": "sha256:c11f7e8f838a521d25a162ffd55efe5c3916e828545fac82e07e7f6866badeae"}, "docker": "quay.io/biocontainers/align_trim", "aliases": {"align_trim": "/usr/local/bin/align_trim", "primalbedtools": "/usr/local/bin/primalbedtools", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/align_trim.
singularity registry hpc automated addition for align_trim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/align_trim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/align_trim:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/align_trim/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/align_trim/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### align_trim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### align_trim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### align_trim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### align_trim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### align_trim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### align_trim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### align_trim

```bash
$ singularity exec <container> /usr/local/bin/align_trim
$ podman run --it --rm --entrypoint /usr/local/bin/align_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align_trim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### primalbedtools

```bash
$ singularity exec <container> /usr/local/bin/primalbedtools
$ podman run --it --rm --entrypoint /usr/local/bin/primalbedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/primalbedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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