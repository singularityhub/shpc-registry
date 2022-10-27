---
layout: container
name:  "quay.io/biocontainers/abacat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abacat/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/abacat/container.yaml"
updated_at: "2022-10-27 01:03:28.523803"
latest: "0.0.4a--py_0"
container_url: "quay.io/biocontainers/abacas:1.3.1--pl5321hdfd78af_2"
aliases:
 - "annotate.py"
 - "fastANI"
 - "phenotyping.py"
 - "pip"
 - "prodigal"
 - "prodigal.py"
 - "prokka.py"
 - "python"
 - "python3"
versions:
 - "0.0.4a--py_0"
description: "abacat - A BActerial genome Curation and Annotation Toolkit"
config: {"url": "quay.io/biocontainers/abacas:1.3.1--pl5321hdfd78af_2", "maintainer": "@vsoch", "description": "abacat - A BActerial genome Curation and Annotation Toolkit", "latest": {"0.0.4a--py_0": "sha256:73d3f072a149c18942fbdfd9a0f7d3fb69e1715683b1a91c57f9f1be41d4a2f5"}, "tags": {"0.0.4a--py_0": "sha256:73d3f072a149c18942fbdfd9a0f7d3fb69e1715683b1a91c57f9f1be41d4a2f5"}, "docker": "quay.io/biocontainers/abacat", "aliases": {"annotate.py": "/usr/local/bin/annotate.py", "fastANI": "/usr/local/bin/fastANI", "phenotyping.py": "/usr/local/bin/phenotyping.py", "pip": "/usr/local/bin/pip", "prodigal": "/usr/local/bin/prodigal", "prodigal.py": "/usr/local/bin/prodigal.py", "prokka.py": "/usr/local/bin/prokka.py", "python": "/usr/local/bin/python", "python3": "/usr/local/bin/python3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abacat.
abacat - A BActerial genome Curation and Annotation Toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abacat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abacat:0.0.4a--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abacat/0.0.4a--py_0
$ module help quay.io/biocontainers/abacat/0.0.4a--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abacat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abacat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abacat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abacat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abacat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abacat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotate.py

```bash
$ singularity exec <container> /usr/local/bin/annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phenotyping.py

```bash
$ singularity exec <container> /usr/local/bin/phenotyping.py
$ podman run --it --rm --entrypoint /usr/local/bin/phenotyping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phenotyping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pip

```bash
$ singularity exec <container> /usr/local/bin/pip
$ podman run --it --rm --entrypoint /usr/local/bin/pip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal.py

```bash
$ singularity exec <container> /usr/local/bin/prodigal.py
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka.py

```bash
$ singularity exec <container> /usr/local/bin/prokka.py
$ podman run --it --rm --entrypoint /usr/local/bin/prokka.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python

```bash
$ singularity exec <container> /usr/local/bin/python
$ podman run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3

```bash
$ singularity exec <container> /usr/local/bin/python3
$ podman run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
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