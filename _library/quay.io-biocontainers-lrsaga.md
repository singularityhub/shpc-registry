---
layout: container
name:  "quay.io/biocontainers/lrsaga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lrsaga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lrsaga/container.yaml"
updated_at: "2026-06-24 06:47:54.457235"
latest: "0.1--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/lrsaga"
aliases:
 - "MBG"
 - "gfa_stats.py"
 - "gfa_to_fasta.py"
 - "gfapy-convert"
 - "gfapy-mergelinear"
 - "gfapy-renumber"
 - "gfapy-validate"
 - "lrSAGA.py"
 - "preprocess_mbg_gfa.py"
 - "bamtools"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "0.1--pyh106432d_0"
description: "singularity registry hpc automated addition for lrsaga"
config: {"url": "https://biocontainers.pro/tools/lrsaga", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lrsaga", "latest": {"0.1--pyh106432d_0": "sha256:edf0b8b7aa37993d7a43948df45de837ed0e5ed1fcc427189dd6bfae73358e21"}, "tags": {"0.1--pyh106432d_0": "sha256:edf0b8b7aa37993d7a43948df45de837ed0e5ed1fcc427189dd6bfae73358e21"}, "docker": "quay.io/biocontainers/lrsaga", "aliases": {"MBG": "/usr/local/bin/MBG", "gfa_stats.py": "/usr/local/bin/gfa_stats.py", "gfa_to_fasta.py": "/usr/local/bin/gfa_to_fasta.py", "gfapy-convert": "/usr/local/bin/gfapy-convert", "gfapy-mergelinear": "/usr/local/bin/gfapy-mergelinear", "gfapy-renumber": "/usr/local/bin/gfapy-renumber", "gfapy-validate": "/usr/local/bin/gfapy-validate", "lrSAGA.py": "/usr/local/bin/lrSAGA.py", "preprocess_mbg_gfa.py": "/usr/local/bin/preprocess_mbg_gfa.py", "bamtools": "/usr/local/bin/bamtools", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lrsaga.
singularity registry hpc automated addition for lrsaga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lrsaga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lrsaga:0.1--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lrsaga/0.1--pyh106432d_0
$ module help quay.io/biocontainers/lrsaga/0.1--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lrsaga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lrsaga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lrsaga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lrsaga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lrsaga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lrsaga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MBG

```bash
$ singularity exec <container> /usr/local/bin/MBG
$ podman run --it --rm --entrypoint /usr/local/bin/MBG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MBG   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa_stats.py

```bash
$ singularity exec <container> /usr/local/bin/gfa_stats.py
$ podman run --it --rm --entrypoint /usr/local/bin/gfa_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfa_to_fasta.py

```bash
$ singularity exec <container> /usr/local/bin/gfa_to_fasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/gfa_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfa_to_fasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-convert

```bash
$ singularity exec <container> /usr/local/bin/gfapy-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-mergelinear

```bash
$ singularity exec <container> /usr/local/bin/gfapy-mergelinear
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-mergelinear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-renumber

```bash
$ singularity exec <container> /usr/local/bin/gfapy-renumber
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-renumber   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfapy-validate

```bash
$ singularity exec <container> /usr/local/bin/gfapy-validate
$ podman run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfapy-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrSAGA.py

```bash
$ singularity exec <container> /usr/local/bin/lrSAGA.py
$ podman run --it --rm --entrypoint /usr/local/bin/lrSAGA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrSAGA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocess_mbg_gfa.py

```bash
$ singularity exec <container> /usr/local/bin/preprocess_mbg_gfa.py
$ podman run --it --rm --entrypoint /usr/local/bin/preprocess_mbg_gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocess_mbg_gfa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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