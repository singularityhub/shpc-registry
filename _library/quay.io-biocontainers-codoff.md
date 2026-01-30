---
layout: container
name:  "quay.io/biocontainers/codoff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/codoff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/codoff/container.yaml"
updated_at: "2026-01-30 04:13:43.426249"
latest: "1.2.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/codoff"
aliases:
 - "codoff"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.0.0--pyh7cba7a3_0"
 - "1.1.0--pyh7cba7a3_0"
 - "1.1.0--pyh7e72e81_2"
 - "1.1.8--pyh7e72e81_0"
 - "1.2.0--pyh7e72e81_0"
 - "1.2.1--pyhdfd78af_0"
 - "1.2.2--pyhdfd78af_0"
 - "1.2.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for codoff"
config: {"url": "https://biocontainers.pro/tools/codoff", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for codoff", "latest": {"1.2.3--pyhdfd78af_0": "sha256:69dea17392f6ec187bdf8d56430cf8ec4e40a59dd28bea01e4286b404dc819e6"}, "tags": {"1.0.0--pyh7cba7a3_0": "sha256:850a3867aa68f974bec3197ac0fd8df938ab39508ba981d5ca49bab256ec8d90", "1.1.0--pyh7cba7a3_0": "sha256:a76d245a0fcaed9698453461906d78f587826acb2dfa18f3e3219f08f49cfd6d", "1.1.0--pyh7e72e81_2": "sha256:bd3ee935c26e2e32f8aa2321e9762b8f9b9906f35348976acff7190b52261f7a", "1.1.8--pyh7e72e81_0": "sha256:9bc94d0b458d6a45a293b1b241e782c826b90760b58a01c1c151f500fdd2f2b3", "1.2.0--pyh7e72e81_0": "sha256:bd8125dd165ee4b8f12ec60e2c5d04fd317ffcbf47bf57f5dca3cae747708a51", "1.2.1--pyhdfd78af_0": "sha256:de0f074e7b5b59f3a82dcfab4a557acc34e9fc3c18e9ca35554a381fa5e56b45", "1.2.2--pyhdfd78af_0": "sha256:349a450aa113605d263bb932c74491c38fa45d309b93246b4ca7793c9514c02d", "1.2.3--pyhdfd78af_0": "sha256:69dea17392f6ec187bdf8d56430cf8ec4e40a59dd28bea01e4286b404dc819e6"}, "docker": "quay.io/biocontainers/codoff", "aliases": {"codoff": "/usr/local/bin/codoff", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/codoff.
singularity registry hpc automated addition for codoff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/codoff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/codoff:1.2.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/codoff/1.2.3--pyhdfd78af_0
$ module help quay.io/biocontainers/codoff/1.2.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### codoff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### codoff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### codoff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### codoff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### codoff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### codoff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### codoff

```bash
$ singularity exec <container> /usr/local/bin/codoff
$ podman run --it --rm --entrypoint /usr/local/bin/codoff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codoff   -v ${PWD} -w ${PWD} <container> -c " $@"
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