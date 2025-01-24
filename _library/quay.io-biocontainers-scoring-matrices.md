---
layout: container
name:  "quay.io/biocontainers/scoring-matrices"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scoring-matrices/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scoring-matrices/container.yaml"
updated_at: "2025-01-24 02:52:45.684214"
latest: "0.3.0--py313h031d066_0"
container_url: "https://biocontainers.pro/tools/scoring-matrices"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.2.0--py39hf95cd2a_0"
 - "0.2.0--py310h4b81fae_0"
 - "0.2.1--py39hf95cd2a_0"
 - "0.2.2--py310h7c593f9_0"
 - "0.2.2--py310h7c593f9_1"
 - "0.3.0--py313h031d066_0"
description: "singularity registry hpc automated addition for scoring-matrices"
config: {"url": "https://biocontainers.pro/tools/scoring-matrices", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for scoring-matrices", "latest": {"0.3.0--py313h031d066_0": "sha256:3809737a4ccb17b85a4e21c2ba39be285a409729c0294ec1fb3d079f3ce52568"}, "tags": {"0.2.0--py39hf95cd2a_0": "sha256:683df7b870f58ff598cf015a4719928b3b52e06ddd820f651ee57620ebb7e24f", "0.2.0--py310h4b81fae_0": "sha256:c0439d5f21bed2b935d77393eb643112f8536dc2510abb8a93fae0fb77dc3177", "0.2.1--py39hf95cd2a_0": "sha256:a0af7a117d53e5b879c68e2a9a97d66e5c6e7f084cb0158415652baa8da83a5b", "0.2.2--py310h7c593f9_0": "sha256:1cff82a9d37e73599e7799c0bd16d3d206aff1aab4e9b42e1ba60c2a4c4503d7", "0.2.2--py310h7c593f9_1": "sha256:2250ff2eaf99ad8fb6a75b56d0383c3b4535ed02813a2d1ea203f6b42094497d", "0.3.0--py313h031d066_0": "sha256:3809737a4ccb17b85a4e21c2ba39be285a409729c0294ec1fb3d079f3ce52568"}, "docker": "quay.io/biocontainers/scoring-matrices", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scoring-matrices.
singularity registry hpc automated addition for scoring-matrices
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scoring-matrices
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scoring-matrices:0.3.0--py313h031d066_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scoring-matrices/0.3.0--py313h031d066_0
$ module help quay.io/biocontainers/scoring-matrices/0.3.0--py313h031d066_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scoring-matrices-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scoring-matrices-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scoring-matrices-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scoring-matrices-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scoring-matrices-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scoring-matrices-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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