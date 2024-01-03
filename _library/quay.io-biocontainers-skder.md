---
layout: container
name:  "quay.io/biocontainers/skder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/skder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/skder/container.yaml"
updated_at: "2024-01-03 02:54:43.360452"
latest: "1.0.8--py310h0dbaff4_0"
container_url: "https://biocontainers.pro/tools/skder"
aliases:
 - "gimme_taxa.py"
 - "ncbi-genome-download"
 - "ngd"
 - "pyfastx"
 - "skDER.py"
 - "skDERcore"
 - "skani"
 - "tqdm"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.0--py310h0dbaff4_0"
 - "1.0.4--py310h0dbaff4_0"
 - "1.0.5--py310h0dbaff4_0"
 - "1.0.8--py310h0dbaff4_0"
description: "singularity registry hpc automated addition for skder"
config: {"url": "https://biocontainers.pro/tools/skder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for skder", "latest": {"1.0.8--py310h0dbaff4_0": "sha256:5d1baeba6fa7c21ebc1eb15a265c098bc9df7abc295ca61ef6d08f5ff7e510bb"}, "tags": {"1.0--py310h0dbaff4_0": "sha256:38fdcb0465610414b995547f61ef7f4cf0f04419adbb4a7dc66dc7e4d612f3ae", "1.0.4--py310h0dbaff4_0": "sha256:c1c99cdbc2ccdb0e2cc4d5678351e464c29d33c44e19608925cb2d6232a6bc1c", "1.0.5--py310h0dbaff4_0": "sha256:17128701d76d02703ad4843ae60454fe14cfbc3eac4591d655b03ecb56de6650", "1.0.8--py310h0dbaff4_0": "sha256:5d1baeba6fa7c21ebc1eb15a265c098bc9df7abc295ca61ef6d08f5ff7e510bb"}, "docker": "quay.io/biocontainers/skder", "aliases": {"gimme_taxa.py": "/usr/local/bin/gimme_taxa.py", "ncbi-genome-download": "/usr/local/bin/ncbi-genome-download", "ngd": "/usr/local/bin/ngd", "pyfastx": "/usr/local/bin/pyfastx", "skDER.py": "/usr/local/bin/skDER.py", "skDERcore": "/usr/local/bin/skDERcore", "skani": "/usr/local/bin/skani", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/skder.
singularity registry hpc automated addition for skder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/skder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/skder:1.0.8--py310h0dbaff4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/skder/1.0.8--py310h0dbaff4_0
$ module help quay.io/biocontainers/skder/1.0.8--py310h0dbaff4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### skder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### skder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### skder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### skder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### skder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### skder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gimme_taxa.py

```bash
$ singularity exec <container> /usr/local/bin/gimme_taxa.py
$ podman run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gimme_taxa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi-genome-download

```bash
$ singularity exec <container> /usr/local/bin/ncbi-genome-download
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi-genome-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngd

```bash
$ singularity exec <container> /usr/local/bin/ngd
$ podman run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfastx

```bash
$ singularity exec <container> /usr/local/bin/pyfastx
$ podman run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skDER.py

```bash
$ singularity exec <container> /usr/local/bin/skDER.py
$ podman run --it --rm --entrypoint /usr/local/bin/skDER.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skDER.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skDERcore

```bash
$ singularity exec <container> /usr/local/bin/skDERcore
$ podman run --it --rm --entrypoint /usr/local/bin/skDERcore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skDERcore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skani

```bash
$ singularity exec <container> /usr/local/bin/skani
$ podman run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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