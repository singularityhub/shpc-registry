---
layout: container
name:  "quay.io/biocontainers/naltorfs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/naltorfs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/naltorfs/container.yaml"
updated_at: "2025-09-23 04:32:05.176120"
latest: "0.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/naltorfs"
aliases:
 - "bicodon_counts_from_fasta.py"
 - "codon_freq_from_bicodons.py"
 - "find_nested_alt_orfs.py"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.1.2--pyhdfd78af_0"
 - "0.1.2"
description: "singularity registry hpc automated addition for naltorfs"
config: {"url": "https://biocontainers.pro/tools/naltorfs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for naltorfs", "latest": {"0.1.2--pyhdfd78af_0": "sha256:f21d7b3334053076d21f4c718fc73796882f68fb93d9b40b9a9a2ff33c3c171a"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:f21d7b3334053076d21f4c718fc73796882f68fb93d9b40b9a9a2ff33c3c171a", "0.1.2": "sha256:0c477b8d52711aad0ec3d95cb7a4e7ba205cc7264965a847c5c452dae7d54aec"}, "docker": "quay.io/biocontainers/naltorfs", "aliases": {"bicodon_counts_from_fasta.py": "/usr/local/bin/bicodon_counts_from_fasta.py", "codon_freq_from_bicodons.py": "/usr/local/bin/codon_freq_from_bicodons.py", "find_nested_alt_orfs.py": "/usr/local/bin/find_nested_alt_orfs.py", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/naltorfs.
singularity registry hpc automated addition for naltorfs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/naltorfs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/naltorfs:0.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/naltorfs/0.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/naltorfs/0.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### naltorfs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### naltorfs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### naltorfs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### naltorfs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### naltorfs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### naltorfs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bicodon_counts_from_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/bicodon_counts_from_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/bicodon_counts_from_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bicodon_counts_from_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codon_freq_from_bicodons.py

```bash
$ singularity exec <container> /usr/local/bin/codon_freq_from_bicodons.py
$ podman run --it --rm --entrypoint /usr/local/bin/codon_freq_from_bicodons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codon_freq_from_bicodons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find_nested_alt_orfs.py

```bash
$ singularity exec <container> /usr/local/bin/find_nested_alt_orfs.py
$ podman run --it --rm --entrypoint /usr/local/bin/find_nested_alt_orfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find_nested_alt_orfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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