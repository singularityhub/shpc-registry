---
layout: container
name:  "quay.io/biocontainers/hsdfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hsdfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hsdfinder/container.yaml"
updated_at: "2025-09-04 03:17:59.022245"
latest: "1.1.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hsdfinder"
aliases:
 - "KO_database.keg"
 - "hsd_to_kegg"
 - "hsdfinder"
 - "operation.py"
 - "pfam.py"
 - "numpy-config"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.1.0--hdfd78af_0"
 - "1.1.1--hdfd78af_0"
description: "singularity registry hpc automated addition for hsdfinder"
config: {"url": "https://biocontainers.pro/tools/hsdfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hsdfinder", "latest": {"1.1.1--hdfd78af_0": "sha256:f5e3b69f66bcb7da1344d11979c3f14bf376eb806430c173ea2565ddd4620b1d"}, "tags": {"1.0.0--hdfd78af_0": "sha256:6af3c4284d891b246ca3430b6cdda32a8ec959a464f9aeba62da9216e05f6bb1", "1.1.0--hdfd78af_0": "sha256:71c58b2eda3d1d860405ec3bd0c6b066436e2a6104cb94fbd01ce66b1d2f2ac7", "1.1.1--hdfd78af_0": "sha256:f5e3b69f66bcb7da1344d11979c3f14bf376eb806430c173ea2565ddd4620b1d"}, "docker": "quay.io/biocontainers/hsdfinder", "aliases": {"KO_database.keg": "/usr/local/bin/KO_database.keg", "hsd_to_kegg": "/usr/local/bin/hsd_to_kegg", "hsdfinder": "/usr/local/bin/hsdfinder", "operation.py": "/usr/local/bin/operation.py", "pfam.py": "/usr/local/bin/pfam.py", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hsdfinder.
singularity registry hpc automated addition for hsdfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hsdfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hsdfinder:1.1.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hsdfinder/1.1.1--hdfd78af_0
$ module help quay.io/biocontainers/hsdfinder/1.1.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hsdfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hsdfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hsdfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hsdfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hsdfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hsdfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### KO_database.keg

```bash
$ singularity exec <container> /usr/local/bin/KO_database.keg
$ podman run --it --rm --entrypoint /usr/local/bin/KO_database.keg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KO_database.keg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsd_to_kegg

```bash
$ singularity exec <container> /usr/local/bin/hsd_to_kegg
$ podman run --it --rm --entrypoint /usr/local/bin/hsd_to_kegg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsd_to_kegg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdfinder

```bash
$ singularity exec <container> /usr/local/bin/hsdfinder
$ podman run --it --rm --entrypoint /usr/local/bin/hsdfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### operation.py

```bash
$ singularity exec <container> /usr/local/bin/operation.py
$ podman run --it --rm --entrypoint /usr/local/bin/operation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/operation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pfam.py

```bash
$ singularity exec <container> /usr/local/bin/pfam.py
$ podman run --it --rm --entrypoint /usr/local/bin/pfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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