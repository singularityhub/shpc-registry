---
layout: container
name:  "quay.io/biocontainers/metabolights-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabolights-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metabolights-utils/container.yaml"
updated_at: "2025-01-03 03:34:43.558962"
latest: "1.3.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metabolights-utils"
aliases:
 - "dotenv"
 - "jsonpath.py"
 - "jsonpath_ng"
 - "mtbls"
 - "unidecode"
 - "httpx"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "jsonschema"
versions:
 - "1.1.2--pyhdfd78af_0"
 - "1.1.5--pyhdfd78af_0"
 - "1.1.6--pyhdfd78af_0"
 - "1.1.10--pyhdfd78af_0"
 - "1.2.2--pyhdfd78af_0"
 - "1.1.12--pyhdfd78af_0"
 - "1.3.9--pyhdfd78af_0"
description: "singularity registry hpc automated addition for metabolights-utils"
config: {"url": "https://biocontainers.pro/tools/metabolights-utils", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metabolights-utils", "latest": {"1.3.9--pyhdfd78af_0": "sha256:c9b142d41a3184df9f478b67d6d1efa4d8e9c4d1c42a60b1e39a6bd8b524ddd1"}, "tags": {"1.1.2--pyhdfd78af_0": "sha256:6917710a11466c8a328166e6c89406ec9b9bc80a90285a3f04f9dedbd8e41d88", "1.1.5--pyhdfd78af_0": "sha256:3849ce17c06a90bfc929a6249ea03c2e734a0bc2ac1ede5a1bcc4fe1da93d0a5", "1.1.6--pyhdfd78af_0": "sha256:5a69bf4f2d6dcb8db16a73ae6b6bf46a11e64189d550b97cceb7721cc0c09ddb", "1.1.10--pyhdfd78af_0": "sha256:ef4dfbafabff6aae9bf96bf4211799512a0053bc1573c187495d19ab7bd32709", "1.2.2--pyhdfd78af_0": "sha256:3913b47164c3d8a36a75e448d326a693de5081827cac78819a204292cf529334", "1.1.12--pyhdfd78af_0": "sha256:73edfbedc2343527697f8fd44ca3bc4ee78b1d98b20f619edd84abfb49d7edb9", "1.3.9--pyhdfd78af_0": "sha256:c9b142d41a3184df9f478b67d6d1efa4d8e9c4d1c42a60b1e39a6bd8b524ddd1"}, "docker": "quay.io/biocontainers/metabolights-utils", "aliases": {"dotenv": "/usr/local/bin/dotenv", "jsonpath.py": "/usr/local/bin/jsonpath.py", "jsonpath_ng": "/usr/local/bin/jsonpath_ng", "mtbls": "/usr/local/bin/mtbls", "unidecode": "/usr/local/bin/unidecode", "httpx": "/usr/local/bin/httpx", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "jsonschema": "/usr/local/bin/jsonschema"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabolights-utils.
singularity registry hpc automated addition for metabolights-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabolights-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabolights-utils:1.3.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabolights-utils/1.3.9--pyhdfd78af_0
$ module help quay.io/biocontainers/metabolights-utils/1.3.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabolights-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabolights-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabolights-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabolights-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabolights-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabolights-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpath.py

```bash
$ singularity exec <container> /usr/local/bin/jsonpath.py
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpath.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpath.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpath_ng

```bash
$ singularity exec <container> /usr/local/bin/jsonpath_ng
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpath_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpath_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtbls

```bash
$ singularity exec <container> /usr/local/bin/mtbls
$ podman run --it --rm --entrypoint /usr/local/bin/mtbls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtbls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
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