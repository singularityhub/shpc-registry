---
layout: container
name:  "quay.io/biocontainers/pycomo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pycomo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pycomo/container.yaml"
updated_at: "2025-08-23 03:16:14.262241"
latest: "0.2.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pycomo"
aliases:
 - "depinfo"
 - "pycomo"
 - "httpx"
 - "isympy"
 - "markdown-it"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "glpsol"
 - "futurize"
 - "pasteurize"
 - "pygmentize"
versions:
 - "0.1.3--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.2.5--pyhdfd78af_0"
 - "0.2.6--pyhdfd78af_0"
 - "0.2.8--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pycomo"
config: {"url": "https://biocontainers.pro/tools/pycomo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pycomo", "latest": {"0.2.8--pyhdfd78af_0": "sha256:92afb64a59a0d3e6f4cf821a2b9871d885e4bdae0f93f9fd68631863f093e007"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:a68079badaf138cb255457842f8d2185e1aadeb8691403c405ce0e904eb365b3", "0.2.2--pyhdfd78af_0": "sha256:2f4fb0f39a781e9e3837b1e6ed5048fa334b0de72182a55d4e70989a866d9604", "0.2.5--pyhdfd78af_0": "sha256:926c9a81901d38ea9757f29d78d10cf842256bbc1b263162320f3aeaf909df63", "0.2.6--pyhdfd78af_0": "sha256:c775a30405ea2f7b14af45a04f1ea02d1c0af46a4761480beae99e767e8b6545", "0.2.8--pyhdfd78af_0": "sha256:92afb64a59a0d3e6f4cf821a2b9871d885e4bdae0f93f9fd68631863f093e007"}, "docker": "quay.io/biocontainers/pycomo", "aliases": {"depinfo": "/usr/local/bin/depinfo", "pycomo": "/usr/local/bin/pycomo", "httpx": "/usr/local/bin/httpx", "isympy": "/usr/local/bin/isympy", "markdown-it": "/usr/local/bin/markdown-it", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "glpsol": "/usr/local/bin/glpsol", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "pygmentize": "/usr/local/bin/pygmentize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pycomo.
singularity registry hpc automated addition for pycomo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pycomo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pycomo:0.2.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pycomo/0.2.8--pyhdfd78af_0
$ module help quay.io/biocontainers/pycomo/0.2.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pycomo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pycomo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pycomo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pycomo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pycomo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pycomo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### depinfo

```bash
$ singularity exec <container> /usr/local/bin/depinfo
$ podman run --it --rm --entrypoint /usr/local/bin/depinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/depinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycomo

```bash
$ singularity exec <container> /usr/local/bin/pycomo
$ podman run --it --rm --entrypoint /usr/local/bin/pycomo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycomo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
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