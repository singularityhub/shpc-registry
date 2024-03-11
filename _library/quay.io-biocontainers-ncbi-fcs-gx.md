---
layout: container
name:  "quay.io/biocontainers/ncbi-fcs-gx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-fcs-gx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-fcs-gx/container.yaml"
updated_at: "2024-03-11 02:36:50.209888"
latest: "0.5.0--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/ncbi-fcs-gx"
aliases:
 - "action_report.py"
 - "blast_names_mapping.tsv"
 - "classify_taxonomy.py"
 - "db_exclude.locs.tsv"
 - "gx"
 - "run_gx.py"
 - "sync_files.py"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.4.0--h9f5acd7_1"
 - "0.4.0--h4ac6f70_2"
 - "0.4.1--h4ac6f70_0"
 - "0.5.0--h4ac6f70_2"
 - "0.4.1--h4ac6f70_1"
 - "0.5.0--h4ac6f70_3"
description: "singularity registry hpc automated addition for ncbi-fcs-gx"
config: {"url": "https://biocontainers.pro/tools/ncbi-fcs-gx", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ncbi-fcs-gx", "latest": {"0.5.0--h4ac6f70_3": "sha256:0870e0037d49f55fe42f018561c27eb140efef3e1467f8343937c2f7613feeac"}, "tags": {"0.4.0--h9f5acd7_1": "sha256:deb8910250c74e3d808a4515fc971be8c41f43e526ae6951963ad46f14a8ae06", "0.4.0--h4ac6f70_2": "sha256:2045eea3ce531e61629d83cadf019bc7bd1ef6f7952a83854a8780cd5e4b4f02", "0.4.1--h4ac6f70_0": "sha256:0bebb6346c31025341e6a8a6be50a1cbeb2c97c49dd348c037246c2a3fad74c1", "0.5.0--h4ac6f70_2": "sha256:5622030fd382e9e82707943ad5213f838da8d7f319baf248c820581f902078b8", "0.4.1--h4ac6f70_1": "sha256:911338cad35cf0c5ab15cec75c71f31caf954a72e8d63e3d958608f0b0e649bd", "0.5.0--h4ac6f70_3": "sha256:0870e0037d49f55fe42f018561c27eb140efef3e1467f8343937c2f7613feeac"}, "docker": "quay.io/biocontainers/ncbi-fcs-gx", "aliases": {"action_report.py": "/usr/local/bin/action_report.py", "blast_names_mapping.tsv": "/usr/local/bin/blast_names_mapping.tsv", "classify_taxonomy.py": "/usr/local/bin/classify_taxonomy.py", "db_exclude.locs.tsv": "/usr/local/bin/db_exclude.locs.tsv", "gx": "/usr/local/bin/gx", "run_gx.py": "/usr/local/bin/run_gx.py", "sync_files.py": "/usr/local/bin/sync_files.py", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-fcs-gx.
singularity registry hpc automated addition for ncbi-fcs-gx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-fcs-gx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-fcs-gx:0.5.0--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-fcs-gx/0.5.0--h4ac6f70_3
$ module help quay.io/biocontainers/ncbi-fcs-gx/0.5.0--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-fcs-gx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-fcs-gx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-fcs-gx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-fcs-gx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-fcs-gx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-fcs-gx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### action_report.py

```bash
$ singularity exec <container> /usr/local/bin/action_report.py
$ podman run --it --rm --entrypoint /usr/local/bin/action_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/action_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_names_mapping.tsv

```bash
$ singularity exec <container> /usr/local/bin/blast_names_mapping.tsv
$ podman run --it --rm --entrypoint /usr/local/bin/blast_names_mapping.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_names_mapping.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### classify_taxonomy.py

```bash
$ singularity exec <container> /usr/local/bin/classify_taxonomy.py
$ podman run --it --rm --entrypoint /usr/local/bin/classify_taxonomy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/classify_taxonomy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### db_exclude.locs.tsv

```bash
$ singularity exec <container> /usr/local/bin/db_exclude.locs.tsv
$ podman run --it --rm --entrypoint /usr/local/bin/db_exclude.locs.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/db_exclude.locs.tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gx

```bash
$ singularity exec <container> /usr/local/bin/gx
$ podman run --it --rm --entrypoint /usr/local/bin/gx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_gx.py

```bash
$ singularity exec <container> /usr/local/bin/run_gx.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_gx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_gx.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sync_files.py

```bash
$ singularity exec <container> /usr/local/bin/sync_files.py
$ podman run --it --rm --entrypoint /usr/local/bin/sync_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sync_files.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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