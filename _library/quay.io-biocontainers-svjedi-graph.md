---
layout: container
name:  "quay.io/biocontainers/svjedi-graph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svjedi-graph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svjedi-graph/container.yaml"
updated_at: "2024-07-08 03:18:07.894481"
latest: "1.2.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/svjedi-graph"
aliases:
 - "construct-graph.py"
 - "f2py3.11"
 - "filter-alignments.py"
 - "minigraph"
 - "predict-genotype.py"
 - "svjedi-graph.py"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "1.1.0--hdfd78af_0"
 - "1.1.1--hdfd78af_0"
 - "1.2.0--hdfd78af_0"
 - "1.2.1--hdfd78af_0"
description: "singularity registry hpc automated addition for svjedi-graph"
config: {"url": "https://biocontainers.pro/tools/svjedi-graph", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for svjedi-graph", "latest": {"1.2.1--hdfd78af_0": "sha256:f4c593aa1ec4356852060993a2aceec3b7f92e868413d298d14363798608e61f"}, "tags": {"1.1.0--hdfd78af_0": "sha256:a8e1dcc074f211d4ccc99a888c7e83fa2c65493cbb576c64146b0f9c80a1d855", "1.1.1--hdfd78af_0": "sha256:cf05f24146fb2bd9b4a8b27481d4ccb8114f4f67c8300130ee348988602e76d4", "1.2.0--hdfd78af_0": "sha256:050c204e8480ab5800650630abbfd225775177481bd16c18b95a429827e95fb3", "1.2.1--hdfd78af_0": "sha256:f4c593aa1ec4356852060993a2aceec3b7f92e868413d298d14363798608e61f"}, "docker": "quay.io/biocontainers/svjedi-graph", "aliases": {"construct-graph.py": "/usr/local/bin/construct-graph.py", "f2py3.11": "/usr/local/bin/f2py3.11", "filter-alignments.py": "/usr/local/bin/filter-alignments.py", "minigraph": "/usr/local/bin/minigraph", "predict-genotype.py": "/usr/local/bin/predict-genotype.py", "svjedi-graph.py": "/usr/local/bin/svjedi-graph.py", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svjedi-graph.
singularity registry hpc automated addition for svjedi-graph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svjedi-graph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svjedi-graph:1.2.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svjedi-graph/1.2.1--hdfd78af_0
$ module help quay.io/biocontainers/svjedi-graph/1.2.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svjedi-graph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svjedi-graph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svjedi-graph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svjedi-graph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svjedi-graph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svjedi-graph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### construct-graph.py

```bash
$ singularity exec <container> /usr/local/bin/construct-graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/construct-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/construct-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-alignments.py

```bash
$ singularity exec <container> /usr/local/bin/filter-alignments.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter-alignments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-alignments.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minigraph

```bash
$ singularity exec <container> /usr/local/bin/minigraph
$ podman run --it --rm --entrypoint /usr/local/bin/minigraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minigraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### predict-genotype.py

```bash
$ singularity exec <container> /usr/local/bin/predict-genotype.py
$ podman run --it --rm --entrypoint /usr/local/bin/predict-genotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predict-genotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svjedi-graph.py

```bash
$ singularity exec <container> /usr/local/bin/svjedi-graph.py
$ podman run --it --rm --entrypoint /usr/local/bin/svjedi-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svjedi-graph.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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