---
layout: container
name:  "quay.io/biocontainers/ensembl-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ensembl-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ensembl-utils/container.yaml"
updated_at: "2025-10-01 03:38:47.224831"
latest: "0.8.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ensembl-utils"
aliases:
 - "dotenv"
 - "extract_file"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "normalizer"
versions:
 - "0.2.0--pyhdfd78af_0"
 - "0.4.1--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.4.2--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.4.4--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.8.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for ensembl-utils"
config: {"url": "https://biocontainers.pro/tools/ensembl-utils", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ensembl-utils", "latest": {"0.8.0--pyhdfd78af_0": "sha256:fe69b19412fee82039edb371b356bf500fc390f0f7c645622788e932c01ac580"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:8a151186d3db4185724f3105b54765ea10438d459c9b3341ce37e4bbd8183176", "0.4.1--pyhdfd78af_0": "sha256:43df6efeb39d02cb90b496c6c46bc03fbb226a71f62bf688dbf3ea5b806e7ff8", "0.3.0--pyhdfd78af_0": "sha256:4779645e17c9b0eb55bbc8dc94bd892a6fbbb6cc191ea69d8b4ac4a0542b536e", "0.4.2--pyhdfd78af_0": "sha256:700fd5c078d5deeaf3a888a42dd0a1e800c9f39b1217994daca8e33daf8093e2", "0.5.0--pyhdfd78af_0": "sha256:178fcdb9e506bdf9850966b994d628a58ff124f51159685b1bee6f968a2e82d6", "0.4.4--pyhdfd78af_0": "sha256:3b47d4d396556078d3247c611f8c6d65a4506bb7fd68b119ac9558f6f8b60819", "0.5.1--pyhdfd78af_0": "sha256:b056534c41e3af744e09a0801f02d2f960aa7bc8f9c1602f327a564ca8b19b59", "0.6.0--pyhdfd78af_0": "sha256:2056182f0df4409c4741b2e8a655c2c469223ee7f46fb13dba8e475aeec9182e", "0.7.0--pyhdfd78af_0": "sha256:9999e5a5c0cdbfc1aceb98fdc39823e7fa4ec4f9c95664ac0951eeda5358b16f", "0.8.0--pyhdfd78af_0": "sha256:fe69b19412fee82039edb371b356bf500fc390f0f7c645622788e932c01ac580"}, "docker": "quay.io/biocontainers/ensembl-utils", "aliases": {"dotenv": "/usr/local/bin/dotenv", "extract_file": "/usr/local/bin/extract_file", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ensembl-utils.
singularity registry hpc automated addition for ensembl-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ensembl-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ensembl-utils:0.8.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ensembl-utils/0.8.0--pyhdfd78af_0
$ module help quay.io/biocontainers/ensembl-utils/0.8.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ensembl-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ensembl-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ensembl-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ensembl-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ensembl-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ensembl-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_file

```bash
$ singularity exec <container> /usr/local/bin/extract_file
$ podman run --it --rm --entrypoint /usr/local/bin/extract_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_file   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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