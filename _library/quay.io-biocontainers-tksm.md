---
layout: container
name:  "quay.io/biocontainers/tksm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tksm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tksm/container.yaml"
updated_at: "2024-12-11 03:37:19.264637"
latest: "0.6.1--py310ha025fb0_1"
container_url: "https://biocontainers.pro/tools/tksm"
aliases:
 - "tksm"
 - "tqdm"
 - "brotli"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.3.0--py310h2b6aa90_0"
 - "0.3.1--py39hd65a603_0"
 - "0.3.2--py310h2b6aa90_0"
 - "0.5.0--py310h2b6aa90_0"
 - "0.6.0--py38he0f268d_0"
 - "0.5.0--py39hd65a603_0"
 - "0.3.2--py38he0f268d_0"
 - "0.6.1--py310h2b6aa90_0"
 - "0.6.1--py310ha025fb0_1"
description: "singularity registry hpc automated addition for tksm"
config: {"url": "https://biocontainers.pro/tools/tksm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tksm", "latest": {"0.6.1--py310ha025fb0_1": "sha256:3765f48561d6a4a48fe6173aa7d7cf677436bb3903b5911daad1ba19a93b1259"}, "tags": {"0.3.0--py310h2b6aa90_0": "sha256:7f2302660b26d99a214b32df97538c2ce523d81d7216cd44f7143fbe51393657", "0.3.1--py39hd65a603_0": "sha256:3108642a0ff85a1539192f41e355f94414f1985c7cd624d6fe395151e1c591ba", "0.3.2--py310h2b6aa90_0": "sha256:130f3382a7dd0d4b07022d48ee227a28b6b16c93be6acfb4d18a8d30ad422cce", "0.5.0--py310h2b6aa90_0": "sha256:075ba729f805b35cce2b46c83a967dd4fefcb5d7af32d9cfa76de19ae203f675", "0.6.0--py38he0f268d_0": "sha256:3c4276868eb632459c66280146e9710283fe99fdd17cae2a6efa51407b6e2c3d", "0.5.0--py39hd65a603_0": "sha256:493c485b6341e0648d5ad2d93dae2ae76a93769eef96de6fbec1769983174c63", "0.3.2--py38he0f268d_0": "sha256:3e9e0baa86e30c5a04db01ae6a3ab987596a2b39a9a38f94d95ffac45159c905", "0.6.1--py310h2b6aa90_0": "sha256:cd072417d60f102fd45dbb46a3c392a9536155642b01755b424905dfd934c1ca", "0.6.1--py310ha025fb0_1": "sha256:3765f48561d6a4a48fe6173aa7d7cf677436bb3903b5911daad1ba19a93b1259"}, "docker": "quay.io/biocontainers/tksm", "aliases": {"tksm": "/usr/local/bin/tksm", "tqdm": "/usr/local/bin/tqdm", "brotli": "/usr/local/bin/brotli", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tksm.
singularity registry hpc automated addition for tksm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tksm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tksm:0.6.1--py310ha025fb0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tksm/0.6.1--py310ha025fb0_1
$ module help quay.io/biocontainers/tksm/0.6.1--py310ha025fb0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tksm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tksm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tksm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tksm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tksm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tksm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tksm

```bash
$ singularity exec <container> /usr/local/bin/tksm
$ podman run --it --rm --entrypoint /usr/local/bin/tksm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tksm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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