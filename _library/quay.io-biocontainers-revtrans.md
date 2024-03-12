---
layout: container
name:  "quay.io/biocontainers/revtrans"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/revtrans/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/revtrans/container.yaml"
updated_at: "2024-03-12 02:45:53.649498"
latest: "1.4--py_1"
container_url: "https://biocontainers.pro/tools/revtrans"
aliases:
 - "mod_seqfiles.py"
 - "mod_translate.py"
 - "ncbi_genetic_codes.py"
 - "revtrans.py"
 - "revtrans_jarmo.py"
 - "translate.py"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.4--py_1"
description: "shpc-registry automated BioContainers addition for revtrans"
config: {"url": "https://biocontainers.pro/tools/revtrans", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for revtrans", "latest": {"1.4--py_1": "sha256:baa7decf317a6d483a830c38349379a4c95061b73af7f7a5b0166c0ade7cf90c"}, "tags": {"1.4--py_1": "sha256:baa7decf317a6d483a830c38349379a4c95061b73af7f7a5b0166c0ade7cf90c"}, "docker": "quay.io/biocontainers/revtrans", "aliases": {"mod_seqfiles.py": "/usr/local/bin/mod_seqfiles.py", "mod_translate.py": "/usr/local/bin/mod_translate.py", "ncbi_genetic_codes.py": "/usr/local/bin/ncbi_genetic_codes.py", "revtrans.py": "/usr/local/bin/revtrans.py", "revtrans_jarmo.py": "/usr/local/bin/revtrans_jarmo.py", "translate.py": "/usr/local/bin/translate.py", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/revtrans.
shpc-registry automated BioContainers addition for revtrans
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/revtrans
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/revtrans:1.4--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/revtrans/1.4--py_1
$ module help quay.io/biocontainers/revtrans/1.4--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### revtrans-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### revtrans-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### revtrans-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### revtrans-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### revtrans-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### revtrans-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mod_seqfiles.py

```bash
$ singularity exec <container> /usr/local/bin/mod_seqfiles.py
$ podman run --it --rm --entrypoint /usr/local/bin/mod_seqfiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mod_seqfiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mod_translate.py

```bash
$ singularity exec <container> /usr/local/bin/mod_translate.py
$ podman run --it --rm --entrypoint /usr/local/bin/mod_translate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mod_translate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbi_genetic_codes.py

```bash
$ singularity exec <container> /usr/local/bin/ncbi_genetic_codes.py
$ podman run --it --rm --entrypoint /usr/local/bin/ncbi_genetic_codes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncbi_genetic_codes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### revtrans.py

```bash
$ singularity exec <container> /usr/local/bin/revtrans.py
$ podman run --it --rm --entrypoint /usr/local/bin/revtrans.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/revtrans.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### revtrans_jarmo.py

```bash
$ singularity exec <container> /usr/local/bin/revtrans_jarmo.py
$ podman run --it --rm --entrypoint /usr/local/bin/revtrans_jarmo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/revtrans_jarmo.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translate.py

```bash
$ singularity exec <container> /usr/local/bin/translate.py
$ podman run --it --rm --entrypoint /usr/local/bin/translate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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