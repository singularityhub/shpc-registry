---
layout: container
name:  "quay.io/biocontainers/catch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/catch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/catch/container.yaml"
updated_at: "2023-09-09 02:32:27.851634"
latest: "1.5.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/catch"
aliases:
 - "analyze_probe_coverage.py"
 - "design.py"
 - "design_large.py"
 - "design_naively.py"
 - "pool.py"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.5.0--pyhdfd78af_0"
 - "1.5.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for catch"
config: {"url": "https://biocontainers.pro/tools/catch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for catch", "latest": {"1.5.1--pyhdfd78af_0": "sha256:4c063e381f1c99ef77b47a7291015e397c26add75a82b04af66e5e2adc83a743"}, "tags": {"1.5.0--pyhdfd78af_0": "sha256:9b0a8e7c650f94c2ef9618ddc8cf153e28959e57b5daba2b90a44ce66a24d9b8", "1.5.1--pyhdfd78af_0": "sha256:4c063e381f1c99ef77b47a7291015e397c26add75a82b04af66e5e2adc83a743"}, "docker": "quay.io/biocontainers/catch", "aliases": {"analyze_probe_coverage.py": "/usr/local/bin/analyze_probe_coverage.py", "design.py": "/usr/local/bin/design.py", "design_large.py": "/usr/local/bin/design_large.py", "design_naively.py": "/usr/local/bin/design_naively.py", "pool.py": "/usr/local/bin/pool.py", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/catch.
shpc-registry automated BioContainers addition for catch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/catch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/catch:1.5.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/catch/1.5.1--pyhdfd78af_0
$ module help quay.io/biocontainers/catch/1.5.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### catch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### catch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### catch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### catch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### catch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### catch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### analyze_probe_coverage.py

```bash
$ singularity exec <container> /usr/local/bin/analyze_probe_coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/analyze_probe_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze_probe_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design.py

```bash
$ singularity exec <container> /usr/local/bin/design.py
$ podman run --it --rm --entrypoint /usr/local/bin/design.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design_large.py

```bash
$ singularity exec <container> /usr/local/bin/design_large.py
$ podman run --it --rm --entrypoint /usr/local/bin/design_large.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design_large.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### design_naively.py

```bash
$ singularity exec <container> /usr/local/bin/design_naively.py
$ podman run --it --rm --entrypoint /usr/local/bin/design_naively.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/design_naively.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pool.py

```bash
$ singularity exec <container> /usr/local/bin/pool.py
$ podman run --it --rm --entrypoint /usr/local/bin/pool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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