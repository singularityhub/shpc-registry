---
layout: container
name:  "quay.io/biocontainers/lollipop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lollipop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lollipop/container.yaml"
updated_at: "2025-10-26 03:54:43.946648"
latest: "0.5.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/lollipop"
aliases:
 - "tqdm"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.1.0--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_1"
 - "0.4.1--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_0"
 - "0.5.2--pyhdfd78af_0"
 - "0.5.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for lollipop"
config: {"url": "https://biocontainers.pro/tools/lollipop", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lollipop", "latest": {"0.5.3--pyhdfd78af_0": "sha256:f99c08c33e6c2a7c053ee0c53cb62a55f6094861e3f59ac2f35dc3f3c9849f3e"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:2c5a1ae184e1225709ef11f5b3828d1c55063891c69dc6798a39842fa016d9ed", "0.2.0--pyhdfd78af_0": "sha256:debb768fb6bd64ab709170c28ddb414c76c5437281e8ca0e130e6d42bb846ba1", "0.3.0--pyhdfd78af_0": "sha256:2a354e520aefe21b9a264c2333050445d0d4252efb7ec0e9d54344aab1818cd4", "0.3.0--pyhdfd78af_1": "sha256:19ad1e45048f5ec6d4dd82d6b7c4c6c113016ba9a7249a044b311b0d45f327e0", "0.4.1--pyhdfd78af_0": "sha256:9853c1302899ea3b89f97fcb85fe30368ed2fa352245a8cd76e3909b41ccff59", "0.5.0--pyhdfd78af_0": "sha256:fb6daa85b75f2d400bb664719d80bfd7079febbe43858930f3a2e2eed683be7e", "0.5.1--pyhdfd78af_0": "sha256:db2bf5f84a08fc94361095304aed7366c54e7874780816e7203e0b78188530aa", "0.5.2--pyhdfd78af_0": "sha256:09227db80f7a74c3026117e3d0015cfa415101e301c2ab08759c6be3cd3012dc", "0.5.3--pyhdfd78af_0": "sha256:f99c08c33e6c2a7c053ee0c53cb62a55f6094861e3f59ac2f35dc3f3c9849f3e"}, "docker": "quay.io/biocontainers/lollipop", "aliases": {"tqdm": "/usr/local/bin/tqdm", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lollipop.
singularity registry hpc automated addition for lollipop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lollipop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lollipop:0.5.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lollipop/0.5.3--pyhdfd78af_0
$ module help quay.io/biocontainers/lollipop/0.5.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lollipop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lollipop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lollipop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lollipop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lollipop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lollipop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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