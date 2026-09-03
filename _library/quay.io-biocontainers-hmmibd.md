---
layout: container
name:  "quay.io/biocontainers/hmmibd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmmibd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmmibd/container.yaml"
updated_at: "2026-09-03 07:02:45.666465"
latest: "2.1.3--hab16a5f_0"
container_url: "https://biocontainers.pro/tools/hmmibd"
aliases:
 - "hmmIBD"
 - "thin_sites.py"
 - "vcf2hmm.py"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "2.1.3--hab16a5f_0"
description: "singularity registry hpc automated addition for hmmibd"
config: {"url": "https://biocontainers.pro/tools/hmmibd", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hmmibd", "latest": {"2.1.3--hab16a5f_0": "sha256:eb80ccecf763f44237940601d172d52f8a56e58582b16ad0448aa54a0d25dd93"}, "tags": {"2.1.3--hab16a5f_0": "sha256:eb80ccecf763f44237940601d172d52f8a56e58582b16ad0448aa54a0d25dd93"}, "docker": "quay.io/biocontainers/hmmibd", "aliases": {"hmmIBD": "/usr/local/bin/hmmIBD", "thin_sites.py": "/usr/local/bin/thin_sites.py", "vcf2hmm.py": "/usr/local/bin/vcf2hmm.py", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmmibd.
singularity registry hpc automated addition for hmmibd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmmibd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmmibd:2.1.3--hab16a5f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmmibd/2.1.3--hab16a5f_0
$ module help quay.io/biocontainers/hmmibd/2.1.3--hab16a5f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmmibd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmmibd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmmibd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmmibd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmmibd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmmibd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hmmIBD

```bash
$ singularity exec <container> /usr/local/bin/hmmIBD
$ podman run --it --rm --entrypoint /usr/local/bin/hmmIBD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmIBD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thin_sites.py

```bash
$ singularity exec <container> /usr/local/bin/thin_sites.py
$ podman run --it --rm --entrypoint /usr/local/bin/thin_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thin_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2hmm.py

```bash
$ singularity exec <container> /usr/local/bin/vcf2hmm.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2hmm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2hmm.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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