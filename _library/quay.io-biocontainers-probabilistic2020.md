---
layout: container
name:  "quay.io/biocontainers/probabilistic2020"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/probabilistic2020/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/probabilistic2020/container.yaml"
updated_at: "2023-08-10 03:36:36.265701"
latest: "1.2.3--py27h20e14e4_5"
container_url: "https://biocontainers.pro/tools/probabilistic2020"
aliases:
 - "extract_gene_seq"
 - "mut_annotate"
 - "probabilistic2020"
 - "simulate_non_silent_ratio"
 - "f2py2"
 - "f2py2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.2.3--py27h20e14e4_5"
description: "shpc-registry automated BioContainers addition for probabilistic2020"
config: {"url": "https://biocontainers.pro/tools/probabilistic2020", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for probabilistic2020", "latest": {"1.2.3--py27h20e14e4_5": "sha256:3aa8d1202e61d1395c5a150dba42cea696054521b4041e765ad3a64e73ef1f0f"}, "tags": {"1.2.3--py27h20e14e4_5": "sha256:3aa8d1202e61d1395c5a150dba42cea696054521b4041e765ad3a64e73ef1f0f"}, "docker": "quay.io/biocontainers/probabilistic2020", "aliases": {"extract_gene_seq": "/usr/local/bin/extract_gene_seq", "mut_annotate": "/usr/local/bin/mut_annotate", "probabilistic2020": "/usr/local/bin/probabilistic2020", "simulate_non_silent_ratio": "/usr/local/bin/simulate_non_silent_ratio", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/probabilistic2020.
shpc-registry automated BioContainers addition for probabilistic2020
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/probabilistic2020
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/probabilistic2020:1.2.3--py27h20e14e4_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/probabilistic2020/1.2.3--py27h20e14e4_5
$ module help quay.io/biocontainers/probabilistic2020/1.2.3--py27h20e14e4_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### probabilistic2020-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### probabilistic2020-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### probabilistic2020-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### probabilistic2020-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### probabilistic2020-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### probabilistic2020-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extract_gene_seq

```bash
$ singularity exec <container> /usr/local/bin/extract_gene_seq
$ podman run --it --rm --entrypoint /usr/local/bin/extract_gene_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_gene_seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mut_annotate

```bash
$ singularity exec <container> /usr/local/bin/mut_annotate
$ podman run --it --rm --entrypoint /usr/local/bin/mut_annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mut_annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### probabilistic2020

```bash
$ singularity exec <container> /usr/local/bin/probabilistic2020
$ podman run --it --rm --entrypoint /usr/local/bin/probabilistic2020   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probabilistic2020   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulate_non_silent_ratio

```bash
$ singularity exec <container> /usr/local/bin/simulate_non_silent_ratio
$ podman run --it --rm --entrypoint /usr/local/bin/simulate_non_silent_ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulate_non_silent_ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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