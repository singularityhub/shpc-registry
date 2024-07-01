---
layout: container
name:  "quay.io/biocontainers/liftover"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/liftover/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/liftover/container.yaml"
updated_at: "2024-07-01 02:49:27.348640"
latest: "1.2.2--py312ha1f7cf2_1"
container_url: "https://biocontainers.pro/tools/liftover"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.1.16--py39hd65a603_0"
 - "1.1.17--py39hd65a603_0"
 - "1.1.18--py39hd65a603_0"
 - "1.2.2--py310h2b6aa90_0"
 - "1.1.18--py310h2b6aa90_0"
 - "1.2.2--py312ha1f7cf2_1"
description: "singularity registry hpc automated addition for liftover"
config: {"url": "https://biocontainers.pro/tools/liftover", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for liftover", "latest": {"1.2.2--py312ha1f7cf2_1": "sha256:82d805d597fce7d416456ca85efa5f33a8f18d458bbac0e5176ecd3c5748ae59"}, "tags": {"1.1.16--py39hd65a603_0": "sha256:2b07045d4bc41661ab7aab7eb1aae0c004d35f73a273b76e5c8259e36ab34122", "1.1.17--py39hd65a603_0": "sha256:2c26eef3ca692c22a9a92d432305aafb9d149573b231a25e8dba302755debea8", "1.1.18--py39hd65a603_0": "sha256:417ab1d978616bfb9f6adac4e5db8898aea25331a08152971abf7fb648957a21", "1.2.2--py310h2b6aa90_0": "sha256:10ef09badb2e191164b862df5d72f8d31c9da97b9bf91054cd0a4c8a02955a56", "1.1.18--py310h2b6aa90_0": "sha256:addf893ff648c9061ec35444561c0a4bd719dc0f2df5a56e325cee3a195b5b1d", "1.2.2--py312ha1f7cf2_1": "sha256:82d805d597fce7d416456ca85efa5f33a8f18d458bbac0e5176ecd3c5748ae59"}, "docker": "quay.io/biocontainers/liftover", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/liftover.
singularity registry hpc automated addition for liftover
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/liftover
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/liftover:1.2.2--py312ha1f7cf2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/liftover/1.2.2--py312ha1f7cf2_1
$ module help quay.io/biocontainers/liftover/1.2.2--py312ha1f7cf2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### liftover-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### liftover-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### liftover-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### liftover-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### liftover-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### liftover-inspect-deffile:

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