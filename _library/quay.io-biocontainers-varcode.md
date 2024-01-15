---
layout: container
name:  "quay.io/biocontainers/varcode"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/varcode/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/varcode/container.yaml"
updated_at: "2024-01-15 02:40:21.277848"
latest: "1.1.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/varcode"
aliases:
 - "epylint"
 - "f2py3.11"
 - "isort"
 - "isort-identify-imports"
 - "pyensembl"
 - "pylint"
 - "pylint-config"
 - "pyreverse"
 - "symilar"
 - "varcode"
 - "varcode-genes"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "get_objgraph"
 - "undill"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "normalizer"
 - "python3.1"
versions:
 - "1.1.0--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for varcode"
config: {"url": "https://biocontainers.pro/tools/varcode", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for varcode", "latest": {"1.1.0--pyh7cba7a3_0": "sha256:1116f471668248ae9890eb83e246ad3a5d6c92dc89e1367d8aaa7d0c8ffe56cd"}, "tags": {"1.1.0--pyh7cba7a3_0": "sha256:1116f471668248ae9890eb83e246ad3a5d6c92dc89e1367d8aaa7d0c8ffe56cd"}, "docker": "quay.io/biocontainers/varcode", "aliases": {"epylint": "/usr/local/bin/epylint", "f2py3.11": "/usr/local/bin/f2py3.11", "isort": "/usr/local/bin/isort", "isort-identify-imports": "/usr/local/bin/isort-identify-imports", "pyensembl": "/usr/local/bin/pyensembl", "pylint": "/usr/local/bin/pylint", "pylint-config": "/usr/local/bin/pylint-config", "pyreverse": "/usr/local/bin/pyreverse", "symilar": "/usr/local/bin/symilar", "varcode": "/usr/local/bin/varcode", "varcode-genes": "/usr/local/bin/varcode-genes", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "normalizer": "/usr/local/bin/normalizer", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/varcode.
singularity registry hpc automated addition for varcode
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/varcode
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/varcode:1.1.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/varcode/1.1.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/varcode/1.1.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### varcode-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### varcode-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### varcode-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### varcode-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### varcode-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### varcode-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epylint

```bash
$ singularity exec <container> /usr/local/bin/epylint
$ podman run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort

```bash
$ singularity exec <container> /usr/local/bin/isort
$ podman run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort-identify-imports

```bash
$ singularity exec <container> /usr/local/bin/isort-identify-imports
$ podman run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyensembl

```bash
$ singularity exec <container> /usr/local/bin/pyensembl
$ podman run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyensembl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint

```bash
$ singularity exec <container> /usr/local/bin/pylint
$ podman run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint-config

```bash
$ singularity exec <container> /usr/local/bin/pylint-config
$ podman run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyreverse

```bash
$ singularity exec <container> /usr/local/bin/pyreverse
$ podman run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### symilar

```bash
$ singularity exec <container> /usr/local/bin/symilar
$ podman run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varcode

```bash
$ singularity exec <container> /usr/local/bin/varcode
$ podman run --it --rm --entrypoint /usr/local/bin/varcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varcode-genes

```bash
$ singularity exec <container> /usr/local/bin/varcode-genes
$ podman run --it --rm --entrypoint /usr/local/bin/varcode-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varcode-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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