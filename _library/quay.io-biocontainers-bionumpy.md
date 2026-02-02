---
layout: container
name:  "quay.io/biocontainers/bionumpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bionumpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bionumpy/container.yaml"
updated_at: "2026-02-02 12:27:20.068007"
latest: "1.0.14--pyh05cac1d_0"
container_url: "https://biocontainers.pro/tools/bionumpy"
aliases:
 - "bionumpy"
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.2.17--pyha8f3691_0"
 - "0.2.20--pyha8f3691_0"
 - "0.2.22--pyha8f3691_0"
 - "0.2.23--pyha8f3691_0"
 - "0.2.25--pyha8f3691_0"
 - "0.2.26--pyha8f3691_0"
 - "0.2.31--pyha8f3691_0"
 - "1.0.1--pyha8f3691_0"
 - "1.0.2--pyha8f3691_0"
 - "1.0.8--pyha8f3691_0"
 - "1.0.9--pyha8f3691_0"
 - "1.0.10--pyha8f3691_0"
 - "1.0.11--pyha8f3691_0"
 - "1.0.12--pyha8f3691_0"
 - "1.0.13--pyh05cac1d_0"
 - "1.0.14--pyh05cac1d_0"
description: "singularity registry hpc automated addition for bionumpy"
config: {"url": "https://biocontainers.pro/tools/bionumpy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bionumpy", "latest": {"1.0.14--pyh05cac1d_0": "sha256:e91c316177b86710782b96067fba46e3995a6ff11a354454cae2ec3022567bea"}, "tags": {"0.2.17--pyha8f3691_0": "sha256:4888799ec9467a088c72b11f5ebd1da9043d6153f6c83c45cbc5925d1eb7f28b", "0.2.20--pyha8f3691_0": "sha256:2e71d23cc90a5aeafdc668ea857f119e36b5edc47c471fa551ac3f6bcd99c2dc", "0.2.22--pyha8f3691_0": "sha256:6a21c6bb7b4d2e4d60564770b3827ebaa6748d88ccfe2b7587e17afc2d57ce14", "0.2.23--pyha8f3691_0": "sha256:a930c285af69efdddf1ac27638f48d387f76c176b89845d9dab7a20ec13f23b3", "0.2.25--pyha8f3691_0": "sha256:023cb47132b5d7ed05feb2154804560f666867d6dc103c215e21dd739d0c0535", "0.2.26--pyha8f3691_0": "sha256:cb55e898d4cabde5ae4cfc65290ac423b956dc9bb5dec3183d444fce5fce5659", "0.2.31--pyha8f3691_0": "sha256:9ee4861920a0d91eb8edcfa10f5103abf5f534f4a5da38712015d2ffb2895fce", "1.0.1--pyha8f3691_0": "sha256:1b2082627a71415f2c09c19e5a314243697fc3e36c9250ce4398fdc57a298110", "1.0.2--pyha8f3691_0": "sha256:dd4e94ba95e7357a5acb82f6ea9d010abbf64800a5f77dbb8184a25bcd052ec2", "1.0.8--pyha8f3691_0": "sha256:f99cdc4ec4740a03fe1012d909bc99107f78e056c470cef932f0167c30eba09d", "1.0.9--pyha8f3691_0": "sha256:3c50e64346d8990eb69a18275392d2627efdfff26cd0f81dece449950f65b716", "1.0.10--pyha8f3691_0": "sha256:87feeedb891f73bb855939f7fe5b5ef60fd561499c0593f9177749b429d7ff2a", "1.0.11--pyha8f3691_0": "sha256:4ad8421289266bf2212aede82791664518d56f7708c7239a521e3acf52a83f6f", "1.0.12--pyha8f3691_0": "sha256:9ee2c1b7841fc708e09512544077365451b60190e0f676cefed29cb042e983e5", "1.0.13--pyh05cac1d_0": "sha256:601294dba4c31005c53814c84e7d17040f5d7d78d168eeb018b976e64d82b17f", "1.0.14--pyh05cac1d_0": "sha256:e91c316177b86710782b96067fba46e3995a6ff11a354454cae2ec3022567bea"}, "docker": "quay.io/biocontainers/bionumpy", "aliases": {"bionumpy": "/usr/local/bin/bionumpy", "f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bionumpy.
singularity registry hpc automated addition for bionumpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bionumpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bionumpy:1.0.14--pyh05cac1d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bionumpy/1.0.14--pyh05cac1d_0
$ module help quay.io/biocontainers/bionumpy/1.0.14--pyh05cac1d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bionumpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bionumpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bionumpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bionumpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bionumpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bionumpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bionumpy

```bash
$ singularity exec <container> /usr/local/bin/bionumpy
$ podman run --it --rm --entrypoint /usr/local/bin/bionumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bionumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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