---
layout: container
name:  "quay.io/biocontainers/art_modern"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/art_modern/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/art_modern/container.yaml"
updated_at: "2026-01-05 05:57:17.812594"
latest: "1.3.0--h5a011d0_0"
container_url: "https://biocontainers.pro/tools/art_modern"
aliases:
 - "art_modern"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.1.4--py310h275bdba_0"
 - "1.1.8--h5a011d0_0"
 - "1.2.0--h5a011d0_0"
 - "1.1.10--h5a011d0_0"
 - "1.3.0--h5a011d0_0"
 - "1.2.1--h5a011d0_0"
description: "singularity registry hpc automated addition for art_modern"
config: {"url": "https://biocontainers.pro/tools/art_modern", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for art_modern", "latest": {"1.3.0--h5a011d0_0": "sha256:0a1dd2139798893d099738068fd5ee4a6640996d6f2a0bdbd8949532e49918f0"}, "tags": {"1.1.4--py310h275bdba_0": "sha256:c0106d301bc4a43df5c7a693eae3ad574d2e5ef13bf58955315075d796cb8386", "1.1.8--h5a011d0_0": "sha256:904f35a36c74a28d68969feff4700f99891e3dbb74dbdc5efbe7b3dff4cbb6e2", "1.2.0--h5a011d0_0": "sha256:6d8781dc24d5aa87ebcb7b29d000873dc57bc6c9e53269a1ecb7d23bdfa96e48", "1.1.10--h5a011d0_0": "sha256:4280881e598c054e860578483a4f73b202916c8134e8413eb2a80e8749996b80", "1.3.0--h5a011d0_0": "sha256:0a1dd2139798893d099738068fd5ee4a6640996d6f2a0bdbd8949532e49918f0", "1.2.1--h5a011d0_0": "sha256:a309751617d14e6cc5b5bb6d9f2a612d3f11dafa38d45ddba6f7b0444f6341bf"}, "docker": "quay.io/biocontainers/art_modern", "aliases": {"art_modern": "/usr/local/bin/art_modern", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/art_modern.
singularity registry hpc automated addition for art_modern
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/art_modern
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/art_modern:1.3.0--h5a011d0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/art_modern/1.3.0--h5a011d0_0
$ module help quay.io/biocontainers/art_modern/1.3.0--h5a011d0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### art_modern-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### art_modern-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### art_modern-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### art_modern-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### art_modern-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### art_modern-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### art_modern

```bash
$ singularity exec <container> /usr/local/bin/art_modern
$ podman run --it --rm --entrypoint /usr/local/bin/art_modern   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/art_modern   -v ${PWD} -w ${PWD} <container> -c " $@"
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