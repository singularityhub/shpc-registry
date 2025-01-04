---
layout: container
name:  "quay.io/biocontainers/genometools-genometools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genometools-genometools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genometools-genometools/container.yaml"
updated_at: "2025-01-04 03:30:11.621969"
latest: "1.6.5--py38h234d545_3"
container_url: "https://biocontainers.pro/tools/genometools-genometools"
aliases:
 - "genometools-config"
 - "gt"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.6.2--py38h5e2dfeb_3"
 - "1.6.2--py310he7ef181_4"
 - "1.6.2--py38hf7b97cc_6"
 - "1.6.3--py39h58cc16e_0"
 - "1.6.5--py310h3db02ab_0"
 - "1.6.5--py38hf7b97cc_1"
 - "1.6.5--py38h234d545_3"
description: "shpc-registry automated BioContainers addition for genometools-genometools"
config: {"url": "https://biocontainers.pro/tools/genometools-genometools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genometools-genometools", "latest": {"1.6.5--py38h234d545_3": "sha256:18bbb5910f80141d7dd7edc7111016d75cb3889355b5d16ea325d028861d1caa"}, "tags": {"1.6.2--py38h5e2dfeb_3": "sha256:0314916c25353611ab24c537be873afbcc14c7372ec55f367cb2eed4ae6fdb87", "1.6.2--py310he7ef181_4": "sha256:0e1dd9d0291cc80debd77b89d0b2b0d953eb142926864e779a2d341bbe6d95ad", "1.6.2--py38hf7b97cc_6": "sha256:76a74f69d55a9b690de5acf7e9b9dd3250ba466a591b6048ab7dc19dc3d2ac4b", "1.6.3--py39h58cc16e_0": "sha256:12bfb73e1f2aba122dccb0531094638557b685d5620cd8ec8d648041d483e293", "1.6.5--py310h3db02ab_0": "sha256:65d7359028377625e74677325e9f2383a0cbe0115d449777e18d70f0d9893fae", "1.6.5--py38hf7b97cc_1": "sha256:930cd315d7ec168d5b595210c11f10e459f6998f0929d1672f98c5723c8c073a", "1.6.5--py38h234d545_3": "sha256:18bbb5910f80141d7dd7edc7111016d75cb3889355b5d16ea325d028861d1caa"}, "docker": "quay.io/biocontainers/genometools-genometools", "aliases": {"genometools-config": "/usr/local/bin/genometools-config", "gt": "/usr/local/bin/gt", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genometools-genometools.
shpc-registry automated BioContainers addition for genometools-genometools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genometools-genometools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genometools-genometools:1.6.5--py38h234d545_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genometools-genometools/1.6.5--py38h234d545_3
$ module help quay.io/biocontainers/genometools-genometools/1.6.5--py38h234d545_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genometools-genometools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genometools-genometools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genometools-genometools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genometools-genometools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genometools-genometools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genometools-genometools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genometools-config

```bash
$ singularity exec <container> /usr/local/bin/genometools-config
$ podman run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genometools-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gt

```bash
$ singularity exec <container> /usr/local/bin/gt
$ podman run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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