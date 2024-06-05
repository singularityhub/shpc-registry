---
layout: container
name:  "quay.io/biocontainers/ampcombi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ampcombi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ampcombi/container.yaml"
updated_at: "2024-06-05 02:53:37.098860"
latest: "0.2.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ampcombi"
aliases:
 - "amp_database.py"
 - "amp_fasta.py"
 - "ampcombi"
 - "ampcombi.py"
 - "check_input.py"
 - "diamond_alignment.sh"
 - "diamond_makedb.sh"
 - "print_header.py"
 - "reformat_tables.py"
 - "diamond"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.1.3--pyhdfd78af_0"
 - "0.1.7--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ampcombi"
config: {"url": "https://biocontainers.pro/tools/ampcombi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ampcombi", "latest": {"0.2.2--pyhdfd78af_0": "sha256:e146a1e61af09d923f2dc7bd63ea8fa43b1c1aca18e139edeaf0f2da0720647f"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:0004ccc0368f788639e51736abbb7840d703ca46499a48fb050fbcf92f47cbc1", "0.1.7--pyhdfd78af_0": "sha256:2de52e495a6fc50de9e44e3f787cd0759a67988e91c1de0e222042d25c93cafa", "0.2.0--pyhdfd78af_0": "sha256:9e41a49d0b33fdaa5a9516ea9084b557fdf1f30d8f2a50a2f813760f3c1a8bf2", "0.2.2--pyhdfd78af_0": "sha256:e146a1e61af09d923f2dc7bd63ea8fa43b1c1aca18e139edeaf0f2da0720647f"}, "docker": "quay.io/biocontainers/ampcombi", "aliases": {"amp_database.py": "/usr/local/bin/amp_database.py", "amp_fasta.py": "/usr/local/bin/amp_fasta.py", "ampcombi": "/usr/local/bin/ampcombi", "ampcombi.py": "/usr/local/bin/ampcombi.py", "check_input.py": "/usr/local/bin/check_input.py", "diamond_alignment.sh": "/usr/local/bin/diamond_alignment.sh", "diamond_makedb.sh": "/usr/local/bin/diamond_makedb.sh", "print_header.py": "/usr/local/bin/print_header.py", "reformat_tables.py": "/usr/local/bin/reformat_tables.py", "diamond": "/usr/local/bin/diamond", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ampcombi.
shpc-registry automated BioContainers addition for ampcombi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ampcombi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ampcombi:0.2.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ampcombi/0.2.2--pyhdfd78af_0
$ module help quay.io/biocontainers/ampcombi/0.2.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ampcombi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ampcombi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ampcombi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ampcombi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ampcombi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ampcombi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amp_database.py

```bash
$ singularity exec <container> /usr/local/bin/amp_database.py
$ podman run --it --rm --entrypoint /usr/local/bin/amp_database.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amp_database.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amp_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/amp_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/amp_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amp_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ampcombi

```bash
$ singularity exec <container> /usr/local/bin/ampcombi
$ podman run --it --rm --entrypoint /usr/local/bin/ampcombi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ampcombi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ampcombi.py

```bash
$ singularity exec <container> /usr/local/bin/ampcombi.py
$ podman run --it --rm --entrypoint /usr/local/bin/ampcombi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ampcombi.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_input.py

```bash
$ singularity exec <container> /usr/local/bin/check_input.py
$ podman run --it --rm --entrypoint /usr/local/bin/check_input.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_input.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond_alignment.sh

```bash
$ singularity exec <container> /usr/local/bin/diamond_alignment.sh
$ podman run --it --rm --entrypoint /usr/local/bin/diamond_alignment.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond_alignment.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond_makedb.sh

```bash
$ singularity exec <container> /usr/local/bin/diamond_makedb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/diamond_makedb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond_makedb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print_header.py

```bash
$ singularity exec <container> /usr/local/bin/print_header.py
$ podman run --it --rm --entrypoint /usr/local/bin/print_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformat_tables.py

```bash
$ singularity exec <container> /usr/local/bin/reformat_tables.py
$ podman run --it --rm --entrypoint /usr/local/bin/reformat_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformat_tables.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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