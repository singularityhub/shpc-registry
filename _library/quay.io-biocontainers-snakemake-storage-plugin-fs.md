---
layout: container
name:  "quay.io/biocontainers/snakemake-storage-plugin-fs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-storage-plugin-fs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-storage-plugin-fs/container.yaml"
updated_at: "2026-01-23 03:53:40.601000"
latest: "1.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-storage-plugin-fs"
aliases:
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.1.5--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
 - "1.0.3--pyhdfd78af_0"
 - "1.0.4--pyhdfd78af_0"
 - "1.0.5--pyhdfd78af_0"
 - "1.0.6--pyhdfd78af_0"
 - "1.1.0--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
 - "1.1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-storage-plugin-fs"
config: {"url": "https://biocontainers.pro/tools/snakemake-storage-plugin-fs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-storage-plugin-fs", "latest": {"1.1.3--pyhdfd78af_0": "sha256:075e6f06431771a699f41acd3dabf27f4fb6954988ba8646df3be209123f6a5e"}, "tags": {"0.1.5--pyhdfd78af_0": "sha256:7d97f360f4ecc89fbb706d35d6b848b1af9476d2f0e1cd9290aaad8687e47eb7", "0.2.0--pyhdfd78af_0": "sha256:128d850afe52b5dfef26554211a90c684708db69c2d9d33df6ee85ec31b03f46", "1.0.0--pyhdfd78af_0": "sha256:cfaf3da2645d852e62cdc02997459d35a056380d55c360738afe23ed62a6fcfb", "1.0.3--pyhdfd78af_0": "sha256:39fa2494288334b30f6ef41c627d3893d9866a8a2b259f152f763cc6c19ff443", "1.0.4--pyhdfd78af_0": "sha256:6fe69257a5939626962d07e12c471481b68e7ac876c3ca9562284326fbb592ba", "1.0.5--pyhdfd78af_0": "sha256:9221535e387df2c79583a0405394695572e4d8110631f279dfed4128ab887037", "1.0.6--pyhdfd78af_0": "sha256:b89c3c46b6ce2a5cec5d5df73f9d5aa51d18f1b39a73849426ef3eeaad98c2e1", "1.1.0--pyhdfd78af_0": "sha256:b9b592336bab9f4547e2a5f970340063d424ce5e2a6125dec4266d948d3acda8", "1.1.1--pyhdfd78af_0": "sha256:8d38ccf9105fbe281ea8c280a1c64595cc861837a2b8322380e27a36a368b654", "1.1.2--pyhdfd78af_0": "sha256:97263874f5317255fa886b560355c1d034a9a9b7091be980306cbb7bf43128d2", "1.1.3--pyhdfd78af_0": "sha256:075e6f06431771a699f41acd3dabf27f4fb6954988ba8646df3be209123f6a5e"}, "docker": "quay.io/biocontainers/snakemake-storage-plugin-fs", "aliases": {"2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-storage-plugin-fs.
singularity registry hpc automated addition for snakemake-storage-plugin-fs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-fs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-fs:1.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-storage-plugin-fs/1.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-storage-plugin-fs/1.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-storage-plugin-fs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-fs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-fs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-storage-plugin-fs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-storage-plugin-fs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-storage-plugin-fs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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