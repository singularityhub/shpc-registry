---
layout: container
name:  "quay.io/biocontainers/atropos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/atropos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/atropos/container.yaml"
updated_at: "2024-06-27 03:28:47.769765"
latest: "1.1.32--py39hff71179_2"
container_url: "https://biocontainers.pro/tools/atropos"
aliases:
 - "atropos"
 - "tqdm"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.1.31--py39hbf8eff0_2"
 - "1.1.32--py310h4b81fae_0"
 - "1.1.32--py38he5da3d1_1"
 - "1.1.32--py39hff71179_2"
description: "shpc-registry automated BioContainers addition for atropos"
config: {"url": "https://biocontainers.pro/tools/atropos", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for atropos", "latest": {"1.1.32--py39hff71179_2": "sha256:95cc1c442be66e981c6400c106782128a9ecfce241ceb29029674f0fdd968f0c"}, "tags": {"1.1.31--py39hbf8eff0_2": "sha256:f11b1d97dd8df11f6cbda15d4b1b6e45f1c9ba8b0e4a323d352c67d2cd009e87", "1.1.32--py310h4b81fae_0": "sha256:1e9116493e4516c6ee650f2bfceab4f1371124cfeb5b83730d4b6663c27fa90f", "1.1.32--py38he5da3d1_1": "sha256:88435a0d9d53c6d21dcdd4129795cc3517a87cc8d74878d677de8ef000ed88b7", "1.1.32--py39hff71179_2": "sha256:95cc1c442be66e981c6400c106782128a9ecfce241ceb29029674f0fdd968f0c"}, "docker": "quay.io/biocontainers/atropos", "aliases": {"atropos": "/usr/local/bin/atropos", "tqdm": "/usr/local/bin/tqdm", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/atropos.
shpc-registry automated BioContainers addition for atropos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/atropos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/atropos:1.1.32--py39hff71179_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/atropos/1.1.32--py39hff71179_2
$ module help quay.io/biocontainers/atropos/1.1.32--py39hff71179_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### atropos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### atropos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### atropos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### atropos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### atropos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### atropos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### atropos

```bash
$ singularity exec <container> /usr/local/bin/atropos
$ podman run --it --rm --entrypoint /usr/local/bin/atropos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atropos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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