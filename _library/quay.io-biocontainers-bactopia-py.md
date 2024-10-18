---
layout: container
name:  "quay.io/biocontainers/bactopia-py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bactopia-py/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bactopia-py/container.yaml"
updated_at: "2024-10-18 03:41:04.896892"
latest: "1.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bactopia-py"
aliases:
 - "bactopia-citations"
 - "bactopia-download"
 - "bactopia-prepare"
 - "bactopia-search"
 - "bactopia-summary"
 - "executor"
 - "markdown-it"
 - "pysradb"
 - "rich-click"
 - "f2py3.11"
 - "coloredlogs"
 - "humanfriendly"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "pygmentize"
 - "xslt-config"
 - "xsltproc"
 - "tqdm"
 - "normalizer"
 - "python3.1"
versions:
 - "1.0.0--pyhdfd78af_0"
 - "1.0.2--pyhdfd78af_0"
 - "1.0.3--pyhdfd78af_0"
 - "1.0.4--pyhdfd78af_0"
 - "1.0.7--pyhdfd78af_0"
 - "1.0.8--pyhdfd78af_0"
 - "1.0.9--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bactopia-py"
config: {"url": "https://biocontainers.pro/tools/bactopia-py", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bactopia-py", "latest": {"1.2.0--pyhdfd78af_0": "sha256:339bb240b8ad0df1ac99e281bf2b8c5fa00ddd7fc2a33fa4fbcdca426d081410"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:9c862327762822dbb3fc8384da027bc919cf91695812e5917c62b0d95515b261", "1.0.2--pyhdfd78af_0": "sha256:8dc29581e9ac9b3e0bdc9f9c338d6f712c25d075a6626c952f183e42fe97827b", "1.0.3--pyhdfd78af_0": "sha256:ce6e11cfaa669bba5b68d4977263cab3f3f7092bd129156fd58a9b743dffddf4", "1.0.4--pyhdfd78af_0": "sha256:eb29a96ee5cfb9317ded260c8c4bafa8808d51d87a100ede4a5b3eb01fa717b8", "1.0.7--pyhdfd78af_0": "sha256:de267cbc215bd95838ea08345db3e674913ab1209dbaf0147b8a26629801ed9e", "1.0.8--pyhdfd78af_0": "sha256:a7e0d8715fbf736cf71fbebdd3bfa9acdc99bc085230e8a1bf9d0d06fd5bd3a3", "1.0.9--pyhdfd78af_0": "sha256:a2fc3a777b9f253af9a3976b76f568d68d747e3693b63fb20fd8d44312951d12", "1.1.1--pyhdfd78af_0": "sha256:87344c8c7d9966da3930309d05ad876a0ef8e81754a99290b1befb5e18f4a13f", "1.2.0--pyhdfd78af_0": "sha256:339bb240b8ad0df1ac99e281bf2b8c5fa00ddd7fc2a33fa4fbcdca426d081410"}, "docker": "quay.io/biocontainers/bactopia-py", "aliases": {"bactopia-citations": "/usr/local/bin/bactopia-citations", "bactopia-download": "/usr/local/bin/bactopia-download", "bactopia-prepare": "/usr/local/bin/bactopia-prepare", "bactopia-search": "/usr/local/bin/bactopia-search", "bactopia-summary": "/usr/local/bin/bactopia-summary", "executor": "/usr/local/bin/executor", "markdown-it": "/usr/local/bin/markdown-it", "pysradb": "/usr/local/bin/pysradb", "rich-click": "/usr/local/bin/rich-click", "f2py3.11": "/usr/local/bin/f2py3.11", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "pygmentize": "/usr/local/bin/pygmentize", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bactopia-py.
singularity registry hpc automated addition for bactopia-py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bactopia-py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bactopia-py:1.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bactopia-py/1.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/bactopia-py/1.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bactopia-py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bactopia-py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bactopia-py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bactopia-py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bactopia-py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bactopia-py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bactopia-citations

```bash
$ singularity exec <container> /usr/local/bin/bactopia-citations
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-citations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-citations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-download

```bash
$ singularity exec <container> /usr/local/bin/bactopia-download
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-prepare

```bash
$ singularity exec <container> /usr/local/bin/bactopia-prepare
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-prepare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-prepare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-search

```bash
$ singularity exec <container> /usr/local/bin/bactopia-search
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bactopia-summary

```bash
$ singularity exec <container> /usr/local/bin/bactopia-summary
$ podman run --it --rm --entrypoint /usr/local/bin/bactopia-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bactopia-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### executor

```bash
$ singularity exec <container> /usr/local/bin/executor
$ podman run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysradb

```bash
$ singularity exec <container> /usr/local/bin/pysradb
$ podman run --it --rm --entrypoint /usr/local/bin/pysradb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysradb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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