---
layout: container
name:  "quay.io/biocontainers/micom"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/micom/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/micom/container.yaml"
updated_at: "2025-11-23 04:05:53.263259"
latest: "0.37.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/micom"
aliases:
 - "httpx"
 - "isympy"
 - "cmark"
 - "glpsol"
 - "pygmentize"
 - "futurize"
 - "pasteurize"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.32.2--pyhdfd78af_0"
 - "0.32.5--pyhdfd78af_0"
 - "0.33.0--pyhdfd78af_0"
 - "0.33.1--pyhdfd78af_0"
 - "0.33.2--pyhdfd78af_0"
 - "0.34.1--pyhdfd78af_0"
 - "0.35.0--pyhdfd78af_0"
 - "0.36.3--pyhdfd78af_0"
 - "0.37.0--pyhdfd78af_0"
 - "0.36.4--pyhdfd78af_0"
 - "0.37.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for micom"
config: {"url": "https://biocontainers.pro/tools/micom", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for micom", "latest": {"0.37.1--pyhdfd78af_0": "sha256:64195dc103e111fc83f3ec57046b572692287e7b7699d6a0746d9ee95db158f7"}, "tags": {"0.32.2--pyhdfd78af_0": "sha256:e88e4949c421da1c631562600ebdd2066b9e4d52b7caeb037ac64e6883d7c2d5", "0.32.5--pyhdfd78af_0": "sha256:8fb96ca2d0196ae736acc4a1110762499e8c9dd7b5461f49914224dcd3bbc0ad", "0.33.0--pyhdfd78af_0": "sha256:5f97f12bb8f4e8e5de9794118d901485dc09db5885fc0c66f39220236778c994", "0.33.1--pyhdfd78af_0": "sha256:53180a67df7aa32190449cba3e982d03ef60a2ee1f4599f484a0ad5261862b98", "0.33.2--pyhdfd78af_0": "sha256:c5e5374adf5e7deb743136c3c67a2ee0c7342a1b8fc7cad23888d884b5497f5b", "0.34.1--pyhdfd78af_0": "sha256:b78b48438b08852149910807d68cc996c84d7b19f7bf6159add7dae88a5550e1", "0.35.0--pyhdfd78af_0": "sha256:92a57db4027b32882993626adcd44558def0bdab406e49c91cb3f7ba9371270c", "0.36.3--pyhdfd78af_0": "sha256:9a9d2c413d660db91342c0a637ffaef46055cb1c65944faf706afc81a8e4b4a2", "0.37.0--pyhdfd78af_0": "sha256:79982bbff56affa09dd4e96d8d210be5de7f777f1d1ac6ca931113a3e80089b1", "0.36.4--pyhdfd78af_0": "sha256:c93931ce4e53617205f004145d4d862fc881be0211de50cd43bf5ca0defa37b0", "0.37.1--pyhdfd78af_0": "sha256:64195dc103e111fc83f3ec57046b572692287e7b7699d6a0746d9ee95db158f7"}, "docker": "quay.io/biocontainers/micom", "aliases": {"httpx": "/usr/local/bin/httpx", "isympy": "/usr/local/bin/isympy", "cmark": "/usr/local/bin/cmark", "glpsol": "/usr/local/bin/glpsol", "pygmentize": "/usr/local/bin/pygmentize", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/micom.
singularity registry hpc automated addition for micom
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/micom
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/micom:0.37.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/micom/0.37.1--pyhdfd78af_0
$ module help quay.io/biocontainers/micom/0.37.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### micom-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### micom-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### micom-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### micom-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### micom-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### micom-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
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