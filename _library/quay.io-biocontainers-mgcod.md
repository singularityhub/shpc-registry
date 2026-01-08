---
layout: container
name:  "quay.io/biocontainers/mgcod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgcod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mgcod/container.yaml"
updated_at: "2026-01-08 04:09:52.307520"
latest: "1.0.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mgcod"
aliases:
 - "data.py"
 - "mgcod.py"
 - "multiprocess_mgcod.py"
 - "pipeline.py"
 - "results.py"
 - "visualizations.py"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.0.1--hdfd78af_0"
 - "1.0.2--hdfd78af_0"
description: "singularity registry hpc automated addition for mgcod"
config: {"url": "https://biocontainers.pro/tools/mgcod", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mgcod", "latest": {"1.0.2--hdfd78af_0": "sha256:fc59d1a1a0daa71bd868f5f21c233f50a7d062145a1d1d3103fd9bdc2878f5ed"}, "tags": {"1.0.0--hdfd78af_0": "sha256:6e4ea36eb702757f1891d08298aa1e1c784837c8acf2304ea0992c176d6ef444", "1.0.1--hdfd78af_0": "sha256:b0cfaec2f64684a88983c02899ada22257b48a3761c6144bbddf6068f67afebc", "1.0.2--hdfd78af_0": "sha256:fc59d1a1a0daa71bd868f5f21c233f50a7d062145a1d1d3103fd9bdc2878f5ed"}, "docker": "quay.io/biocontainers/mgcod", "aliases": {"data.py": "/usr/local/bin/data.py", "mgcod.py": "/usr/local/bin/mgcod.py", "multiprocess_mgcod.py": "/usr/local/bin/multiprocess_mgcod.py", "pipeline.py": "/usr/local/bin/pipeline.py", "results.py": "/usr/local/bin/results.py", "visualizations.py": "/usr/local/bin/visualizations.py", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgcod.
singularity registry hpc automated addition for mgcod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgcod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgcod:1.0.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgcod/1.0.2--hdfd78af_0
$ module help quay.io/biocontainers/mgcod/1.0.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgcod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgcod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgcod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgcod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgcod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgcod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### data.py

```bash
$ singularity exec <container> /usr/local/bin/data.py
$ podman run --it --rm --entrypoint /usr/local/bin/data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgcod.py

```bash
$ singularity exec <container> /usr/local/bin/mgcod.py
$ podman run --it --rm --entrypoint /usr/local/bin/mgcod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgcod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiprocess_mgcod.py

```bash
$ singularity exec <container> /usr/local/bin/multiprocess_mgcod.py
$ podman run --it --rm --entrypoint /usr/local/bin/multiprocess_mgcod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiprocess_mgcod.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pipeline.py

```bash
$ singularity exec <container> /usr/local/bin/pipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### results.py

```bash
$ singularity exec <container> /usr/local/bin/results.py
$ podman run --it --rm --entrypoint /usr/local/bin/results.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/results.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualizations.py

```bash
$ singularity exec <container> /usr/local/bin/visualizations.py
$ podman run --it --rm --entrypoint /usr/local/bin/visualizations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualizations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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