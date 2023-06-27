---
layout: container
name:  "quay.io/biocontainers/taxpasta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taxpasta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/taxpasta/container.yaml"
updated_at: "2023-06-27 03:14:13.501544"
latest: "0.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/taxpasta"
aliases:
 - "depinfo"
 - "f2py3.11"
 - "taxpasta"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "cmark"
 - "pygmentize"
 - "futurize"
 - "pasteurize"
 - "python3.1"
versions:
 - "0.1.0--pyhdfd78af_0"
 - "0.1.1--pyhdfd78af_0"
 - "0.2.3--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for taxpasta"
config: {"url": "https://biocontainers.pro/tools/taxpasta", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for taxpasta", "latest": {"0.3.0--pyhdfd78af_0": "sha256:560c3a19d2561d84d42a9da55084834315886346ea936b5824621767e9050857"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:a43b13ba645ed13e6774e98b2a3cf698c134eebeec029c4fca783defbbc0ead9", "0.1.1--pyhdfd78af_0": "sha256:a2b4becb2bb77d214aa5d797d19ba36258e9bbd8c288d0a218ca17159383385e", "0.2.3--pyhdfd78af_0": "sha256:6bc5f3c3b3b02b81481b6b677377efe45790ca5e6578c629a35ba178ccf65059", "0.3.0--pyhdfd78af_0": "sha256:560c3a19d2561d84d42a9da55084834315886346ea936b5824621767e9050857"}, "docker": "quay.io/biocontainers/taxpasta", "aliases": {"depinfo": "/usr/local/bin/depinfo", "f2py3.11": "/usr/local/bin/f2py3.11", "taxpasta": "/usr/local/bin/taxpasta", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "cmark": "/usr/local/bin/cmark", "pygmentize": "/usr/local/bin/pygmentize", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taxpasta.
singularity registry hpc automated addition for taxpasta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taxpasta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taxpasta:0.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taxpasta/0.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/taxpasta/0.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taxpasta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taxpasta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taxpasta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taxpasta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taxpasta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taxpasta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### depinfo

```bash
$ singularity exec <container> /usr/local/bin/depinfo
$ podman run --it --rm --entrypoint /usr/local/bin/depinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/depinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxpasta

```bash
$ singularity exec <container> /usr/local/bin/taxpasta
$ podman run --it --rm --entrypoint /usr/local/bin/taxpasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxpasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cmark

```bash
$ singularity exec <container> /usr/local/bin/cmark
$ podman run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmark   -v ${PWD} -w ${PWD} <container> -c " $@"
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