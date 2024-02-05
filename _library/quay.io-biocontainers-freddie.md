---
layout: container
name:  "quay.io/biocontainers/freddie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/freddie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/freddie/container.yaml"
updated_at: "2024-02-05 02:58:50.702476"
latest: "0.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/freddie"
aliases:
 - "Annotation_Load.py"
 - "deBGA"
 - "deSALT"
 - "freddie_cluster.py"
 - "freddie_isoforms.py"
 - "freddie_segment.py"
 - "freddie_split.py"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.4--hdfd78af_0"
description: "singularity registry hpc automated addition for freddie"
config: {"url": "https://biocontainers.pro/tools/freddie", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for freddie", "latest": {"0.4--hdfd78af_0": "sha256:ec3a09391a33021357c39ad297d298feb3edd33bfdaa279c5cb26d07779cb1cc"}, "tags": {"0.4--hdfd78af_0": "sha256:ec3a09391a33021357c39ad297d298feb3edd33bfdaa279c5cb26d07779cb1cc"}, "docker": "quay.io/biocontainers/freddie", "aliases": {"Annotation_Load.py": "/usr/local/bin/Annotation_Load.py", "deBGA": "/usr/local/bin/deBGA", "deSALT": "/usr/local/bin/deSALT", "freddie_cluster.py": "/usr/local/bin/freddie_cluster.py", "freddie_isoforms.py": "/usr/local/bin/freddie_isoforms.py", "freddie_segment.py": "/usr/local/bin/freddie_segment.py", "freddie_split.py": "/usr/local/bin/freddie_split.py", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/freddie.
singularity registry hpc automated addition for freddie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/freddie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/freddie:0.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/freddie/0.4--hdfd78af_0
$ module help quay.io/biocontainers/freddie/0.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### freddie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### freddie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### freddie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### freddie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### freddie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### freddie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Annotation_Load.py

```bash
$ singularity exec <container> /usr/local/bin/Annotation_Load.py
$ podman run --it --rm --entrypoint /usr/local/bin/Annotation_Load.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Annotation_Load.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deBGA

```bash
$ singularity exec <container> /usr/local/bin/deBGA
$ podman run --it --rm --entrypoint /usr/local/bin/deBGA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deBGA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deSALT

```bash
$ singularity exec <container> /usr/local/bin/deSALT
$ podman run --it --rm --entrypoint /usr/local/bin/deSALT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deSALT   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freddie_cluster.py

```bash
$ singularity exec <container> /usr/local/bin/freddie_cluster.py
$ podman run --it --rm --entrypoint /usr/local/bin/freddie_cluster.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freddie_cluster.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freddie_isoforms.py

```bash
$ singularity exec <container> /usr/local/bin/freddie_isoforms.py
$ podman run --it --rm --entrypoint /usr/local/bin/freddie_isoforms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freddie_isoforms.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freddie_segment.py

```bash
$ singularity exec <container> /usr/local/bin/freddie_segment.py
$ podman run --it --rm --entrypoint /usr/local/bin/freddie_segment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freddie_segment.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freddie_split.py

```bash
$ singularity exec <container> /usr/local/bin/freddie_split.py
$ podman run --it --rm --entrypoint /usr/local/bin/freddie_split.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freddie_split.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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