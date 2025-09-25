---
layout: container
name:  "quay.io/biocontainers/gtdb_to_taxdump"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gtdb_to_taxdump/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gtdb_to_taxdump/container.yaml"
updated_at: "2025-09-25 07:31:42.209831"
latest: "0.1.9--pyhcf36b3e_0"
container_url: "https://biocontainers.pro/tools/gtdb_to_taxdump"
aliases:
 - "acc2gtdb_tax.py"
 - "gtdb_to_diamond.py"
 - "gtdb_to_taxdump.py"
 - "lineage2taxid.py"
 - "ncbi-gtdb_map.py"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "tqdm"
versions:
 - "0.1.9--pyhcf36b3e_0"
description: "singularity registry hpc automated addition for gtdb_to_taxdump"
config: {"url": "https://biocontainers.pro/tools/gtdb_to_taxdump", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gtdb_to_taxdump", "latest": {"0.1.9--pyhcf36b3e_0": "sha256:9fd2151297d582ed8fdf14ed1e50f4863f835f10c7082b7af5d7fad40a122123"}, "tags": {"0.1.9--pyhcf36b3e_0": "sha256:9fd2151297d582ed8fdf14ed1e50f4863f835f10c7082b7af5d7fad40a122123"}, "docker": "quay.io/biocontainers/gtdb_to_taxdump", "aliases": {"acc2gtdb_tax.py": "/usr/local/bin/acc2gtdb_tax.py", "gtdb_to_diamond.py": "/usr/local/bin/gtdb_to_diamond.py", "gtdb_to_taxdump.py": "/usr/local/bin/gtdb_to_taxdump.py", "lineage2taxid.py": "/usr/local/bin/lineage2taxid.py", "ncbi-gtdb_map.py": "/usr/local/bin/ncbi-gtdb_map.py", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gtdb_to_taxdump.
singularity registry hpc automated addition for gtdb_to_taxdump
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gtdb_to_taxdump
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gtdb_to_taxdump:0.1.9--pyhcf36b3e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gtdb_to_taxdump/0.1.9--pyhcf36b3e_0
$ module help quay.io/biocontainers/gtdb_to_taxdump/0.1.9--pyhcf36b3e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gtdb_to_taxdump-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gtdb_to_taxdump-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gtdb_to_taxdump-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gtdb_to_taxdump-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gtdb_to_taxdump-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gtdb_to_taxdump-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### acc2gtdb_tax.py

```bash
$ singularity exec <container> /usr/local/bin/acc2gtdb_tax.py
$ podman run --it --rm --entrypoint /usr/local/bin/acc2gtdb_tax.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acc2gtdb_tax.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtdb_to_diamond.py

```bash
$ singularity exec <container> /usr/local/bin/gtdb_to_diamond.py
$ podman run --it --rm --entrypoint /usr/local/bin/gtdb_to_diamond.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtdb_to_diamond.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtdb_to_taxdump.py

```bash
$ singularity exec <container> /usr/local/bin/gtdb_to_taxdump.py
$ podman run --it --rm --entrypoint /usr/local/bin/gtdb_to_taxdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtdb_to_taxdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lineage2taxid.py

```bash
$ singularity exec <container> /usr/local/bin/lineage2taxid.py
$ podman run --it --rm --entrypoint /usr/local/bin/lineage2taxid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lineage2taxid.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-gtdb_map.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi-gtdb_map.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-gtdb_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-gtdb_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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