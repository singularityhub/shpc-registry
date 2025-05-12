---
layout: container
name:  "quay.io/biocontainers/ms2rescore-rs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ms2rescore-rs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ms2rescore-rs/container.yaml"
updated_at: "2025-05-12 03:34:36.892585"
latest: "0.4.2--py311he252b13_0"
container_url: "https://biocontainers.pro/tools/ms2rescore-rs"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.2.0--py39h801753a_0"
 - "0.2.0--py310h28e8315_0"
 - "0.2.0--py311hff4e47f_1"
 - "0.2.0--py311h284d45d_2"
 - "0.4.1--py311he252b13_0"
 - "0.4.2--py311he252b13_0"
description: "singularity registry hpc automated addition for ms2rescore-rs"
config: {"url": "https://biocontainers.pro/tools/ms2rescore-rs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ms2rescore-rs", "latest": {"0.4.2--py311he252b13_0": "sha256:a25ad19bed126eb76442d4fcc052e4a78786bc23730486aafcd71daf67997088"}, "tags": {"0.2.0--py39h801753a_0": "sha256:9661fda435b0ca52dbe051f4fc93fae40520a1fd65df38122707a84c8655f68b", "0.2.0--py310h28e8315_0": "sha256:5adfcdbe5ac9233a1643ad6d95686f0309f5d78b32769cd2d6658fd3bfc108ad", "0.2.0--py311hff4e47f_1": "sha256:150ad35c27170c3b85a76cc98d2af0c0f6f83479f7df6b60fc7d4a3126d26478", "0.2.0--py311h284d45d_2": "sha256:e8ee34e09c3eab5f75f08e0773c76577046dd6603b41dc745a05901436c67862", "0.4.1--py311he252b13_0": "sha256:74c8b140aa62203a65e79fcb86d10cfbb837710445f7e73ea7e074be2b16deef", "0.4.2--py311he252b13_0": "sha256:a25ad19bed126eb76442d4fcc052e4a78786bc23730486aafcd71daf67997088"}, "docker": "quay.io/biocontainers/ms2rescore-rs", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ms2rescore-rs.
singularity registry hpc automated addition for ms2rescore-rs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ms2rescore-rs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ms2rescore-rs:0.4.2--py311he252b13_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ms2rescore-rs/0.4.2--py311he252b13_0
$ module help quay.io/biocontainers/ms2rescore-rs/0.4.2--py311he252b13_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ms2rescore-rs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ms2rescore-rs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ms2rescore-rs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ms2rescore-rs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ms2rescore-rs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ms2rescore-rs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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